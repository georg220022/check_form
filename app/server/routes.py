from fastapi.routing import APIRoute
from .app import search_form, add_test_data

routes = [
    APIRoute(path="/get_form", endpoint=search_form, methods=["POST"]),
    APIRoute(path="/add_test_data", endpoint=add_test_data, methods=["GET"]),
]
