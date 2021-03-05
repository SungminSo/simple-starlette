from starlette.routing import Route

from .views import Hello


rest_routes = [
    Route('/hello', Hello),
]
