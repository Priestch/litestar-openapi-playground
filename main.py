from litestar import Litestar, get
from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin


@get("/")
async def hello_world() -> dict[str, str]:
    return {"hello": "world"}


openapi_config = OpenAPIConfig(title="My API", version="1.0.0", render_plugins=[ScalarRenderPlugin()])

app = Litestar(route_handlers=[hello_world],
               openapi_config=openapi_config)
