"""
Routers Package
"""
from .auth import router as auth_router
from .tasks import router as tasks_router
from .categories import router as categories_router

__all__ = ["auth_router", "tasks_router", "categories_router"]
