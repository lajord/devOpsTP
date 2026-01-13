import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from main import app


@pytest.fixture
def test_app():
    """
    Fixture qui retourne l'application FastAPI pour les tests.
    """
    return app


@pytest.fixture
def client(test_app):
    """
    Fixture qui crée un TestClient pour faire des requêtes HTTP simulées.
    """
    with TestClient(test_app) as client:
        yield client


@pytest.fixture
def mock_geocoding_response():
    """
    Mock de la réponse de l'API de géocodage Open-Meteo.
    """
    return {
        "results": [
            {
                "id": 2988507,
                "name": "Paris",
                "latitude": 48.85341,
                "longitude": 2.3488,
                "country": "France",
                "country_code": "FR",
            }
        ]
    }


@pytest.fixture
def mock_current_weather_response():
    """
    Mock de la réponse de l'API météo actuelle Open-Meteo.
    """
    return {
        "latitude": 48.85,
        "longitude": 2.35,
        "timezone": "Europe/Paris",
        "current": {
            "time": "2024-01-15T10:00",
            "temperature_2m": 15.5,
            "relative_humidity_2m": 75,
            "apparent_temperature": 14.2,
            "pressure_msl": 1013.5,
            "wind_speed_10m": 12.5,
            "weather_code": 2,
        },
    }


@pytest.fixture
def mock_forecast_response():
    """
    Mock de la réponse de l'API prévisions Open-Meteo.
    """
    return {
        "latitude": 48.85,
        "longitude": 2.35,
        "timezone": "Europe/Paris",
        "daily": {
            "time": [
                "2024-01-15",
                "2024-01-16",
                "2024-01-17",
                "2024-01-18",
                "2024-01-19",
                "2024-01-20",
                "2024-01-21",
            ],
            "weather_code": [2, 61, 0, 3, 95, 71, 1],
            "temperature_2m_max": [18.5, 16.2, 20.1, 15.8, 14.5, 12.3, 17.8],
            "temperature_2m_min": [8.5, 10.2, 9.1, 7.8, 6.5, 4.3, 8.8],
            "apparent_temperature_max": [17.5, 15.2, 19.1, 14.8, 13.5, 11.3, 16.8],
            "apparent_temperature_min": [7.5, 9.2, 8.1, 6.8, 5.5, 3.3, 7.8],
            "precipitation_probability_max": [0, 80, 10, 30, 95, 70, 20],
            "wind_speed_10m_max": [15.5, 22.3, 10.5, 18.7, 30.2, 25.8, 12.4],
        },
    }


@pytest.fixture
def mock_httpx_client(mock_geocoding_response, mock_current_weather_response):
    """
    Mock du client httpx pour éviter les vrais appels API.
    """
    with patch("httpx.AsyncClient") as mock_client:
        mock_instance = AsyncMock()
        mock_client.return_value.__aenter__.return_value = mock_instance

        # Par défaut, retourne la réponse de géocodage
        mock_response = AsyncMock()
        mock_response.json.return_value = mock_geocoding_response
        mock_response.raise_for_status = AsyncMock()
        mock_instance.get.return_value = mock_response

        yield mock_instance
