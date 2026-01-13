import pytest
from fastapi.testclient import TestClient


@pytest.mark.smoke
@pytest.mark.unit
def test_health_endpoint_returns_200(client):
    """
    Test que l'endpoint /api/health retourne un statut 200 et la réponse correcte.
    """
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.unit
def test_metrics_endpoint_exists(client):
    """
    Test que l'endpoint /metrics existe et retourne des métriques Prometheus.
    """
    response = client.get("/metrics")

    assert response.status_code == 200
    assert "text/plain" in response.headers.get("content-type", "")
    # Vérifie qu'il y a des métriques Prometheus dans la réponse
    assert "http_requests_total" in response.text or "http_request" in response.text


@pytest.mark.unit
def test_cors_headers_present(client):
    """
    Test que les headers CORS sont correctement configurés.
    """
    response = client.options(
        "/api/health",
        headers={
            "Origin": "http://localhost:5173",
            "Access-Control-Request-Method": "GET",
        },
    )

    # Vérifie que les headers CORS sont présents
    assert "access-control-allow-origin" in response.headers
    assert "access-control-allow-methods" in response.headers


@pytest.mark.unit
def test_openapi_docs_available(client):
    """
    Test que la documentation OpenAPI est disponible.
    """
    response = client.get("/api/docs")

    assert response.status_code == 200


@pytest.mark.unit
def test_openapi_json_available(client):
    """
    Test que le schéma OpenAPI JSON est disponible.
    """
    response = client.get("/api/openapi.json")

    assert response.status_code == 200
    data = response.json()
    assert "openapi" in data
    assert data["info"]["title"] == "CY Weather API"
