from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class WeatherRecord(Base):
    __tablename__ = "weather_records"
    
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    country = Column(String)
    temperature = Column(Float)
    feels_like = Column(Float)
    temp_min = Column(Float)
    temp_max = Column(Float)
    pressure = Column(Integer)
    humidity = Column(Integer)
    wind_speed = Column(Float)
    wind_deg = Column(Integer)
    clouds = Column(Integer)
    weather_description = Column(String)
    weather_main = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    forecast_date = Column(DateTime(timezone=True))