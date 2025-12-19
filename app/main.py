import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.templating import Jinja2Templates
from fastapi import Request
from app.users.router import router as router_users
from app.movies.router import router as router_movies
from app.reviews.router import router as router_reviews
from app.favorites.router import router as router_favorites
from app import db
from app.admin import setup_admin
import os

# Initialize database if not exists
if not Path(__file__).parent.parent.joinpath('kinovzor.db').exists():
    print("\n📁 Database not found. Creating...")
    from init_db import init_db
    init_db()
    print("\n🍋 Loading seed data...")
    from seed_db import seed_movies_and_reviews
    seed_movies_and_reviews()
    print("\n✅ All ready!\n")

app = FastAPI(
    title="KinoVzor API",
    description="Movie review and rating platform",
    version="1.0.0"
)

# Add session middleware for admin authentication
app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv('SECRET_KEY', 'your-secret-key-change-in-production'),
    session_cookie='admin_session',
    max_age=86400  # 24 hours
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers FIRST (before static files)
app.include_router(router_users)
app.include_router(router_movies)
app.include_router(router_reviews)
app.include_router(router_favorites)

# Setup SQLAdmin
setup_admin(app)

# Get the correct paths for static files and templates
STATIC_DIR = Path(__file__).parent / "static"
TEMPLATES_DIR = Path(__file__).parent / "templates"

# Setup Jinja2 templates
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

# Mount static files
if STATIC_DIR.exists():
    app.mount('/static', StaticFiles(directory=str(STATIC_DIR)), 'static')
else:
    print(f"\n⚠️ Warning: Static directory not found at {STATIC_DIR}")

# Root route - serve index.html from templates
@app.get('/')
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    
    print("\n" + "="*50)
    print("🌟 KinoVzor - Movie Review Platform")
    print("="*50)
    print("\n🚀 Starting server...")
    print("📱 API: http://127.0.0.1:8000")
    print("📊 Admin Panel: http://127.0.0.1:8000/admin")
    print("📝 Docs: http://127.0.0.1:8000/docs\n")
    
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )