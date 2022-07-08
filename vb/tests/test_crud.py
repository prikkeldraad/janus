from vb.app import create_app

async def test_verion_get(aiohttp_client):
    client = await aiohttp_client(create_app())
    resp = await client.get("/version/jira")
    response_text = await resp.content.read()
    expected_response_text = b"You are requesting version information for jira"
    assert response_text == response_text

async def test_version_post(aiohttp_client):
    client = await aiohttp_client(create_app())
    payload = {   "software_name": "Jira",
        "major": "6",
        "minor": "2",
        "release_name": "RC2"}
    resp = await client.post("/version/jira", json=payload)
    json_data = await resp.json()
    assert payload == json_data