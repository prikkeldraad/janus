from vb.app import create_app

async def test_verion_get(aiohttp_client):
    client = await aiohttp_client(create_app())
    resp = await client.get("/version/jira")
    response_text = await resp.content.read()
    expected_response_text = b"You are requesting version information for jira"
    assert response_text == response_text

async def test_version_post_valid(aiohttp_client):
    client = await aiohttp_client(create_app())
    payload = {
        "software_name": "Jira",
        "major": "6",
        "minor": "2",
        "patch": "2",
        "release_name": "RC2",
        "version": "6.2"
    }
    expected_response = {"id": None, "software_name": "Jira", "release_name": "RC2", "version": "6.2", "major": "6", "minor": "2", "patch": "2"}
    resp = await client.post("/version/jira", json=payload)
    json_data = await resp.json()
    assert expected_response == json_data

async def test_version_post_valid2(aiohttp_client):
    client = await aiohttp_client(create_app())
    payload = {
        "software_name": "Jira",
        "major": None,
        "minor": None,
        "patch": None,
        "release_name": "RC2",
        "version": "6.2"
    }
    expected_response = {"id": None, "software_name": "Jira", "release_name": "RC2", "version": "6.2", "major": None, "minor": None, "patch": None}
    resp = await client.post("/version/jira", json=payload)
    json_data = await resp.json()
    assert expected_response == json_data