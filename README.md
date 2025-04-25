# Desafio - Desenvolvedor Jr.

A API desenvolvida realiza busca da previsão do tempo atual, de acordo com a cidade informada, e guarda no bando como foi estipulado o desafio.

Para rodar o projeto será necessário instalar Python (configurar variáveis de ambiente), após isso, baixar o projeto.

Dentro da pasta raiz do projeto, rodar os seguintes comandos no terminal:

# Criação e ativação do ambiente virtual

    - python -m venv venv
    - source venv/bin/activate no Mac
    - venv\Scripts\activate se for no Windows

# Dependências necessárias

    pip install fastapi uvicorn sqlalchemy python-dotenv pydantic-settings requests

Dentro do arquivo .env, coloque sua API_KEY para validar o contato com WeatherAPI.

Rode o arquivo main.py tudo estará funcionando.

- Ambiente default utilizado: http://127.0.0.1:8000/

Os seguintes endpoints estão disponíveis:

# Inserção de previsão no banco

Método POST - http://127.0.0.1:8000/weather/{city} - Realiza a inserção de dados passados através de JSON com nome da cidade.

# Busca de previsões cadastradas

Método GET - http://127.0.0.1:8000/weather/ - Realiza a busca das previsões cadastradas no banco.
Exemplo de retorno:

[
{
"city": "Rio Pomba",
"country": "BR",
"temperature": 19.49,
"feels_like": 19.92,
"temp_min": 19.49,
"temp_max": 19.49,
"pressure": 1017,
"humidity": 93,
"wind_speed": 0.29,
"wind_deg": 139,
"clouds": 100,
"weather_description": "overcast clouds",
"weather_main": "Clouds",
"forecast_date": "2025-04-22T23:05:11",
"id": 2,
"timestamp": "2025-04-23T02:05:11"
},
{
"city": "Miguel Pereira",
"country": "BR",
"temperature": 18.83,
"feels_like": 18.81,
"temp_min": 18.83,
"temp_max": 18.83,
"pressure": 1017,
"humidity": 78,
"wind_speed": 0.34,
"wind_deg": 109,
"clouds": 100,
"weather_description": "overcast clouds",
"weather_main": "Clouds",
"forecast_date": "2025-04-22T23:03:08",
"id": 3,
"timestamp": "2025-04-23T02:05:22"
},
]

# Busca através de ID

Método GET - http://127.0.0.1:8000/weather/{weather_id} - Busca registro de acordo com o id passado

# Remoção de dados do banco através de id

Método DELETE - http://127.0.0.1:8000/weather/{weather_id} - Deleta registro de acordo com o id passado

# Busca através de filtro de cidade e data

Método GET - http://127.0.0.1:8000/weather/?city=Rio de Janeiro&date=2023-11-15' - Busca dados de acordo com a cidade e a data passadas na url
