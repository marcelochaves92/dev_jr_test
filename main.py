from fastapi import FastAPI, Depends, HTTPException, Query
from typing import List, Optional
from datetime import date
from sqlalchemy import func
import crud, models, schemas, services
from database import engine, get_db
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/weather/{city}", response_model=schemas.Weather)
def fetch_and_store_weather(city: str, db=Depends(get_db)):
    weather_data = services.fetch_weather_data(city)
    return crud.create_weather_record(db, weather_data)

@app.get("/weather/", response_model=List[schemas.Weather])
def read_weather(
    city: Optional[str] = None,
    date: Optional[date] = None,
    skip: int = 0,
    limit: int = 100,
    db=Depends(get_db)
):
    if city and date:
        return crud.get_weather_by_city_and_date(db, city, str(date))
    elif city:
        return db.query(models.WeatherRecord).filter(
            models.WeatherRecord.city == city
        ).offset(skip).limit(limit).all()
    else:
        return crud.get_all_weather(db, skip=skip, limit=limit)

@app.get("/weather/{weather_id}", response_model=schemas.Weather)
def read_weather_record(weather_id: int, db=Depends(get_db)):
    db_weather = crud.get_weather(db, weather_id)
    if db_weather is None:
        raise HTTPException(status_code=404, detail="Weather record not found")
    return db_weather

@app.delete("/weather/{weather_id}", response_model=schemas.Weather)
def delete_weather_record(weather_id: int, db=Depends(get_db)):
    db_weather = crud.delete_weather_record(db, weather_id)
    if db_weather is None:
        raise HTTPException(status_code=404, detail="Weather record not found")
    return db_weather