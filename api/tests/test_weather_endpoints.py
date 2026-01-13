import pytest


@pytest.mark.unit
def test_weather_current_endpoint_missing_city(client):
    """
    Test que l'endpoint /api/weather/current retourne 422 sans paramètre city.
    """
    response = client.get("/api/weather/current")
    assert response.status_code == 422


@pytest.mark.unit
def test_weather_forecast_endpoint_missing_city(client):
    """
    Test que l'endpoint /api/weather/forecast retourne 422 sans paramètre city.
    """
    response = client.get("/api/weather/forecast")
    assert response.status_code == 422


@pytest.mark.smoke
@pytest.mark.unit
def test_weather_endpoints_exist(client):
    """
    Test que les routes météo sont montées (même si elles échouent sans vraie API).
    """
    # Ces requêtes vont échouer mais pas avec 404 (route not found)
    response_current = client.get("/api/weather/current?city=Paris")
    response_forecast = client.get("/api/weather/forecast?city=Paris")

    # On accepte n'importe quel code sauf 404 (route non trouvée)
    assert response_current.status_code != 404
    assert response_forecast.status_code != 404
