from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from src.api.api import api_router
from src.db.session import engine, Base, SessionLocal
from sqlalchemy import text
from src.core.config import settings
from prometheus_fastapi_instrumentator import Instrumentator
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Initialize DB
Base.metadata.create_all(bind=engine)

# Auto-migration: Add account_id to entries if it doesn't exist
db = SessionLocal()
try:
    db.execute(text("ALTER TABLE entries ADD COLUMN account_id INTEGER REFERENCES accounts(id)"))
    db.commit()
    print("Migration: Added account_id to entries table.")
except Exception:
    db.rollback()
    # Column probably exists
finally:
    db.close()

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Instrument for Prometheus
Instrumentator().instrument(app).expose(app, endpoint="/actuator/prometheus")

# API Routes
app.include_router(api_router, prefix="/api")

# UI Routes
@app.get("/", response_class=HTMLResponse)
async def read_index():
    return FileResponse(os.path.join(BASE_DIR, "templates", "index.html"))

@app.get("/login", response_class=HTMLResponse)
async def login_page():
    return FileResponse(os.path.join(BASE_DIR, "templates", "login.html"))

@app.get("/register", response_class=HTMLResponse)
async def register_page():
    return FileResponse(os.path.join(BASE_DIR, "templates", "register.html"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
