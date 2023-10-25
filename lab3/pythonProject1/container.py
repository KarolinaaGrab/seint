from dependency_injector import containers, providers

from repositories.weather_repo_db import WeatherRepo
from services.weather_service import WeatherService

import os

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    repo = providers.Singleton(
        WeatherRepo,
    )

    service = providers.Factory(
        WeatherService,
        repo=repo,

    os.environ.get("s", "def")

    )
    
    if os.getenv("weather") == '0':
        from repositories.weather_repo_db import WeatherRepo
    else:
        from repositories.weather_repo_txt import WeatherRepo
    )
