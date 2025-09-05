# Getting Started

## Option 1 – **Nix + uv**
**Setup**
```bash
nix develop
uv sync
```

**Run**
```bash
uv run python -m uvicorn --app-dir src app:app
```

---

## Option 2 – **uv only**
**Setup**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh   # skip if already installed
uv sync
```

**Run**
```bash
uv run python -m uvicorn --app-dir src app:app
```

---

## Option 3 – **Plain Python (no uv)**
**Setup**
```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

**Run**
```bash
python -m uvicorn --app-dir src app:app
```

---

## Option 4 – **Docker**
**Setup & Run**
```bash
docker build -t riot_take_home .
docker run --rm -it -p 8000:8000 riot_take_home
```

# Comments on the project
## Tests

The project includes unit tests for the encryption and signing API routes, covering:
- successful round-trips (encrypt → decrypt, sign → verify),
- invalid JSON inputs,
- tampered payloads and malformed requests.

I chose to test this at the route level only, one could want to test lower level components such as
the independent implementations of Cipher and Signer in a larger project.

To run the tests:
```
# with uv :
uv run pytest -v

# with pip
pytest -v
```

## `/encrypt` response format
I chose to wrap each encrypted property values in an object to manage the identification of encrypted content in my service layer and 
not in the implementation of the Cipher. 

#### Example:
Input:
```
{
  "name": "John Doe",
  "age": 30,
  "contact": {
    "email": "john@example.com",
    "phone": "123-456-7890"
  }
}
```

Output:
```
{
    "name": {
        "enc": "B64Cipher",
        "val": "IkpvaG4gRG9lIg=="
    },
    "age": {
        "enc": "B64Cipher",
        "val": "MzA="
    },
    "contact": {
        "enc": "B64Cipher",
        "val": "eyJlbWFpbCI6ImpvaG5AZXhhbXBsZS5jb20iLCJwaG9uZSI6IjEyMy00NTYtNzg5MCJ9"
    }
}
```

Doing so allows us to reliably identify encrypted properties in the `/decrypt` endpoint.

## Pydantic models
For the sake of simplicity in this exercise, I chose to use a rather loose definition of a JSON object in my input validation :

```
class AnyDict(RootModel[dict[str, Any]]):
    pass
```
In a production setting we would enforce a stricter definition of a Json that would for instance refuse values like NaN or Infinity.
These can sometimes be sent through permissive tools like curl,
but are not valid JSON according to the specification and won’t be accepted by most clients (Postman...).

## Logging

I didn’t add a lot of custom logs in this project. The endpoints are pretty small,
and FastAPI/Uvicorn already print useful info about requests and errors by default.

What I did add is a simple exception handler to catch and log unexpected crashes.
In a real production system you’d normally want more detailed logs (things like
request context, payloads...) and more specific exception handling instead of one generic catch-all.

