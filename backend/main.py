"""
News Analytics Platform - Main API Entry Point
"""
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

from api.routes import articles, analytics, scraper, health
from utils.config import settings
from utils.database import init_db

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events"""
    logger.info("Starting News Analytics Platform API...")
    
    # Initialize database
    await init_db()
    logger.info("Database initialized")
    
    yield
    
    logger.info("Shutting down News Analytics Platform API...")


# Create FastAPI app
app = FastAPI(
    title="News Analytics Platform API",
    description="API for news scraping, processing, and analytics",
    version="1.0.0",
    lifespan=lifespan
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
app.include_router(health.router, prefix="/api/v1", tags=["health"])
app.include_router(articles.router, prefix="/api/v1", tags=["articles"])
app.include_router(analytics.router, prefix="/api/v1", tags=["analytics"])
app.include_router(scraper.router, prefix="/api/v1", tags=["scraper"])


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "News Analytics Platform API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/api/v1/health"
    }


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.ENVIRONMENT == "development"
    )
