def test_encrypt_then_decrypt_roundtrip(client):
    payload = {"name": "damien", "age": 35, "other": {"alive": True, "size": 178}}

    r = client.post("/encrypt", json=payload)
    assert r.status_code == 200
    encrypted = r.json()

    for key in ("name", "age", "other"):
        assert isinstance(encrypted[key], dict)
        assert "enc" in encrypted[key]
        assert "val" in encrypted[key]

    # add a non encrypted value
    encrypted["extra"] = "non encrypted"
    payload["extra"] = "non encrypted"

    r2 = client.post("/decrypt", json=encrypted)
    assert r2.status_code == 200
    decrypted = r2.json()
    assert decrypted == payload


def test_encrypt_invalid_json(client):
    bad_json = '{"name": "damien", "age": 35, "hex": 0xab}'  # not valid

    r = client.post("/encrypt", content=bad_json, headers={"Content-Type": "application/json"})
    assert r.status_code == 422

def test_decrypt_invalid_json(client):
    bad_json = '{"name": "damien", "age": 35, "hex": 0xab}'  # not valid

    r = client.post("/decrypt", content=bad_json, headers={"Content-Type": "application/json"})
    assert r.status_code == 422