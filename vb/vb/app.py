from aiohttp import web
from .models import SoftwareModel, VersionModel
from .db import Version, Software 

from pydantic import ValidationError 


class SoftwareView(web.View):
    async def get(self):
        name = self.request.match_info.get("name", "Unknown")
        software = Software.get(Software.name==name)

    async def post(self):
        json_data = await self.request.json()
        try:
            software = SoftwareModel(**json_data)
        except ValidationError as ex:
            return web.Response(body=ex.json(), content_type="application/json")
        
        Software.create(**software.dict()).save()
        return web.json_response(software.dict(), content_type="application/json")



class VersionView(web.View):
    async def get(self):
        result = self.request.match_info.get("name", "Unknown")
        return web.Response(body="You are requesting version information for " + result)

    async def post(self):
        json_data = await self.request.json()
        try:
            version = VersionModel(**json_data)
        except ValidationError as ex:
            return web.Response(body=ex.json(), content_type='application/json')
            

        Version.create(**version.dict()).save()
        return web.json_response(version.dict(), content_type='application/json')




def create_app():
    app = web.Application()
    app.add_routes([web.view("/version/{name}", VersionView)])
    app.add_routes([web.view("/software/", SoftwareView)])
    return app
