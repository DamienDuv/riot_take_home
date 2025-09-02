### Setup
If you're using nix:
```
nix develop
uv sync
```

Otherwise
```
curl -LsSf https://astral.sh/uv/install.sh | sh # skip if installed
uv sync
```

Or if you don't use uv:
```
python -m venv .venv
. .venv/bin/activate     # Windows: .\.venv\Scripts\activate
pip install -r requirements.txt || pip install fastapi "uvicorn[standard]"
```

### Run
To run the project use with uv :

```
uv run python -m uvicorn --app-dir src app:app
```

Without uv (with venv activated):
```
python -m uvicorn --app-dir src app:app
```

### Docker

To run with docker:
```
 docker build -t riot_take_home .
 docker run --rm -it -p 8000:8000 riot_take_home
```