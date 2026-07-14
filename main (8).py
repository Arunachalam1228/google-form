"""
FastAPI backend for the Google Forms-style registration form.
Submissions are logged to the console only — no storage/database.
"""

import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, EmailStr, Field

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger("form-app")

app = FastAPI(title="Registration Form API")

BASE_DIR = Path(__file__).parent
STATIC_DIR = BASE_DIR / "static"

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


class Submission(BaseModel):
    full_name: str = Field(..., min_length=1)
    email: EmailStr
    age: Optional[int] = Field(default=None, ge=0, le=150)
    phone: str = Field(..., min_length=1)


@app.get("/")
def serve_form():
    """Serve the HTML form."""
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/submit")
def submit_form(submission: Submission):
    """Receive a form submission and log it. No persistence."""
    timestamp = datetime.now(timezone.utc).isoformat()
    logger.info(
        "New submission [%s] | name=%s | email=%s | age=%s | phone=%s",
        timestamp,
        submission.full_name,
        submission.email,
        submission.age if submission.age is not None else "N/A",
        submission.phone,
    )
    return {"status": "ok", "message": "Submission received", "timestamp": timestamp}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
