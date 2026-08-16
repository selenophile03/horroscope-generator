from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.calculator import get_zodiac_sign, generate_horoscope_report

app = FastAPI(title="Horoscope Generator API")

# API Endpoint to compute and fetch the daily horoscope profile
@app.get("/api/horoscope")
def calculate_horoscope(month: int, day: int):
    if month < 1 or month > 12 or day < 1 or day > 31:
        raise HTTPException(status_code=400, detail="Invalid date parameters provided.")
    
    sign = get_zodiac_sign(month, day)
    report = generate_horoscope_report(sign)
    return report

# Serve UI frontend assets
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return FileResponse("static/index.html")
