from aiohttp import web
from .models import VersionModel
from .db import Version 

class VersionView(web.View):
    async def get(self):
        result = self.request.match_info.get("name", "Unknown")
        return web.Response(body="You are requesting version information for " + result)

    async def post(self):
        json_data = await self.request.json()
        version = VersionModel(**json_data)
        #Version.create(**version.dict()).save()
        return web.json_response(version.dict(), content_type='application/json')




def create_app():
    app = web.Application()
    app.add_routes([web.view("/version/{name}", VersionView)])
    return app
