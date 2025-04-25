import requests
from datetime import datetime
from fastapi import HTTPException
from schemas import WeatherCreate
import config

def fetch_weather_data(city: str) -> WeatherCreate:
    params = {
        'q': city,
        'appid': config.settings.OPENWEATHER_API_KEY,
        'units': 'metric'
    }
    
    try:
        response = requests.get(config.settings.OPENWEATHER_BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        return WeatherCreate(
            city=data['name'],
            country=data['sys']['country'],
            temperature=data['main']['temp'],
            feels_like=data['main']['feels_like'],
            temp_min=data['main']['temp_min'],
            temp_max=data['main']['temp_max'],
            pressure=data['main']['pressure'],
            humidity=data['main']['humidity'],
            wind_speed=data['wind']['speed'],
            wind_deg=data['wind'].get('deg', 0),
            clouds=data['clouds']['all'],
            weather_description=data['weather'][0]['description'],
            weather_main=data['weather'][0]['main'],
            forecast_date=datetime.fromtimestamp(data['dt'])
        )
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Error fetching weather data: {str(e)}")