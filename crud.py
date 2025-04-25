from sqlalchemy.orm import Session
from models import WeatherRecord
import schemas

def get_weather(db: Session, weather_id: int):
    return db.query(WeatherRecord).filter(WeatherRecord.id == weather_id).first()

def get_weather_by_city_and_date(db: Session, city: str, date: str):
    return db.query(WeatherRecord).filter(
        WeatherRecord.city == city,
        func.date(WeatherRecord.forecast_date) == date
    ).all()

def get_all_weather(db: Session, skip: int = 0, limit: int = 100):
    return db.query(WeatherRecord).offset(skip).limit(limit).all()

def create_weather_record(db: Session, weather: schemas.WeatherCreate):
    db_weather = WeatherRecord(**weather.dict())
    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)
    return db_weather

def delete_weather_record(db: Session, weather_id: int):
    db_weather = get_weather(db, weather_id)
    if db_weather:
        db.delete(db_weather)
        db.commit()
    return db_weather