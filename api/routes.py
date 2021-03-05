from starlette.routing import Route

from .views import rest_example


rest_routes = [
    Route('/hello', rest_example),
]
