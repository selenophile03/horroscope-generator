from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

# Crucial modification: Correcting folder tracking paths
from api.calculator import get_zodiac_sign, generate_horoscope_report

app = FastAPI(title="Horoscope Generator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/horoscope")
def calculate_horoscope(month: int, day: int):
    if month < 1 or month > 12 or day < 1 or day > 31:
        raise HTTPException(status_code=400, detail="Invalid date parameters.")
    
    sign = get_zodiac_sign(month, day)
    report = generate_horoscope_report(sign)
    return report

# Pointing explicitly to the static asset folder relative to execution
static_path = os.path.join(os.path.dirname(__file__), "..", "static")

@app.get("/")
def read_root():
    return FileResponse(os.path.join(static_path, "index.html"))
