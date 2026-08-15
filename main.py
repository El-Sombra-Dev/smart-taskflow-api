"""
Smart TaskFlow API - Main Application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routers.auth import router as auth_router
from routers.tasks import router as tasks_router
from routers.categories import router as categories_router
from config import settings

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
description="""
## Smart TaskFlow API

A professional, production-ready Task Management API.

### Features

- JWT Authentication - Secure user authentication
- Task Management - Full CRUD operations for tasks
- Categories - Organize tasks with categories
- Pagination and Filtering - Efficient data retrieval
- Input Validation - Pydantic models for data validation

### Authentication

All endpoints except /api/auth/register and /api/auth/login
require authentication.

Use the JWT token in the Authorization header:

Authorization: Bearer YOUR_JWT_TOKEN
""",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router)
app.include_router(tasks_router)
app.include_router(categories_router)


@app.get("/", tags=["Root"])
def root():
    """
    Root endpoint - API information
    """
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "description": "A professional Task Management API",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health", tags=["Health"])
def health_check():
    """
    Health check endpoint
    """
    return {
        "status": "healthy",
        "version": settings.APP_VERSION
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )
