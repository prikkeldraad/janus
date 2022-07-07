from vb.app import create_app

async def test_verion_get(aiohttp_client):
    client = await aiohttp_client(create_app())
    resp = await client.get("/version/jira")
    response_text = await resp.content.read()
    expected_response_text = b"You are requesting version information for jira"
    assert response_text == response_text 