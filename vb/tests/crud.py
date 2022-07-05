from vb.app import create_app

async def test_verion_post(aiottp_client):
    client = await aiohttp_client(await create_app())
    resp = await client.get("/")