# Correct format to send the data as JSON
def test_generate_qr():
    url = "http://example.com"
    response = client.post("/generate-qr/", json={"url": url})  # This is correct

    assert response.status_code == 200
    assert "qr_code_url" in response.json()

def test_generate_qr_invalid_url():
    url = "invalid-url"
    response = client.post("/generate-qr/", json={"url": url})

    assert response.status_code == 422  # FastAPI validation error
