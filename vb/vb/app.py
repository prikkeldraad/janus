from aiohttp import web
from .models import VersionModel

async def handle(request):
    name = request.match_info.get("name", "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


class VersionView(web.View):
    async def get(self):
        result = self.request.match_info.get("name", "Unknown")
        return web.Response(body="You are requesting version information for " + result)





def create_app():
    app = web.Application()
    app.add_routes([web.view("/version/{name}", VersionView)])
    app.add_routes([web.get("/", handle), web.get("/{name}", handle)])
    return app
