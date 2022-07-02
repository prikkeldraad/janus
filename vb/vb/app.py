from aiohttp import web



class VersionView(web.View):
    async def get(self):
        return await get_resp(self.request)

    async def post(self):
        return await post_resp(self.request)


async def handle(request):
    name = request.match_info.get("name", "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


def create_app():
    app = web.Application()
    app.add_routes([web.get("/", handle), web.get("/{name}", handle)])
    app.add_routes([web.view("/version",VersionView)])
    return app
