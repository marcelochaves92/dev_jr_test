from datetime import datetime
from pydantic import BaseModel

class WeatherBase(BaseModel):
    city: str
    country: str
    temperature: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    wind_speed: float
    wind_deg: int
    clouds: int
    weather_description: str
    weather_main: str
    forecast_date: datetime

class WeatherCreate(WeatherBase):
    pass

class Weather(WeatherBase):
    id: int
    timestamp: datetime
    
    class Config:
        from_attributes = True