def test_sign_and_verify_match(client):
    payload = {"name": "damien", "age": 35, "other": {"alive": True, "size": 178}}

    # /sign returns a signature string
    r = client.post("/sign", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert "signature" in body
    assert isinstance(body["signature"], str)
    assert body["signature"]  # non-empty

    sig = body["signature"]

    # /verify succeeds (204) with the same payload
    r2 = client.post("/verify", json={"signature": sig, "data": payload})
    assert r2.status_code == 204  # No Content


def test_verify_fails_on_tampered_payload(client):
    payload = {"name": "damien", "age": 35, "other": {"alive": True, "size": 178}}
    sig = client.post("/sign", json=payload).json()["signature"]

    tampered_payload = {"name": "damien", "age": 35, "other": {"alive": False, "size": 178}}
    r = client.post("/verify", json={"signature": sig, "data": tampered_payload})
    assert r.status_code == 400

def test_sign_invalid_json(client):
    bad_json = '{"name": "damien", "age": 35, "hex": 0xab}'  # not valid

    r = client.post("/sign", content=bad_json, headers={"Content-Type": "application/json"})
    assert r.status_code == 422

def test_verify_invalid_json(client):
    bad_json = '{"name": "damien", "age": 35, "hex": 0xab}'  # not valid

    r = client.post("/verify", content=bad_json, headers={"Content-Type": "application/json"})
    assert r.status_code == 422

def test_verify_malformed_json(client):
    malformed_json = '{"sig":"abcde", "content":"arbitrary"}'

    r = client.post("/verify", content=malformed_json, headers={"Content-Type": "application/json"})
    assert r.status_code == 422