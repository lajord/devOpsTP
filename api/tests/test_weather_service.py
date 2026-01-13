import pytest
from src.services.weather_service import WeatherService


@pytest.fixture
def weather_service():
    """Fixture pour créer une instance du service météo."""
    return WeatherService()


@pytest.mark.unit
def test_wmo_to_description(weather_service):
    """
    Test la conversion des codes WMO en descriptions françaises.
    """
    assert weather_service._get_weather_description(0) == "Ciel dégagé"
    assert weather_service._get_weather_description(61) == "Pluie légère"
    assert weather_service._get_weather_description(95) == "Orage"
    assert weather_service._get_weather_description(71) == "Neige légère"
    assert weather_service._get_weather_description(999) == "Conditions inconnues"


@pytest.mark.unit
def test_wmo_to_icon(weather_service):
    """
    Test la conversion des codes WMO en codes d'icône.
    """
    assert weather_service._wmo_to_icon(0) == "01d"  # Ciel dégagé
    assert weather_service._wmo_to_icon(61) == "10d"  # Pluie
    assert weather_service._wmo_to_icon(95) == "11d"  # Orage
    assert weather_service._wmo_to_icon(71) == "13d"  # Neige
    assert weather_service._wmo_to_icon(999) == "01d"  # Code inconnu -> défaut


@pytest.mark.unit
def test_weather_service_urls_configured(weather_service):
    """
    Test que les URLs de l'API sont bien configurées.
    """
    assert weather_service.geocoding_url == "https://geocoding-api.open-meteo.com/v1/search"
    assert weather_service.weather_url == "https://api.open-meteo.com/v1/forecast"
