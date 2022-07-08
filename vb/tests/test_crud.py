from vb.app import create_app

async def test_verion_get(aiohttp_client):
    client = await aiohttp_client(create_app())
    resp = await client.get("/version/jira")
    response_text = await resp.content.read()
    expected_response_text = b"You are requesting version information for jira"
    assert response_text == response_text

async def test_version_post(aiohttp_client):
    client = await aiohttp_client(create_app())
    resp = await client.post("/version/jira", json={
        "major": "10000"
    })
    json_data = await resp.json()
    expected_response_text = b"You are requesting version information for jira"
    assert expected_response_text == json_data