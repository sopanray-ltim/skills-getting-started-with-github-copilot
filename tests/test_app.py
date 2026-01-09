from fastapi.testclient import TestClient
from src.app import app

def test_get_activities():
    client = TestClient(app)
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data

def test_signup_and_unregister():
    client = TestClient(app)
    test_email = "testuser@mergington.edu"
    activity = "Chess Club"
    # Sign up
    response = client.post(f"/activities/{activity}/signup?email={test_email}")
    assert response.status_code == 200 or response.status_code == 400
    # Unregister
    response = client.post(f"/activities/{activity}/unregister", json={"activity": activity, "email": test_email})
    assert response.status_code == 200 or response.status_code == 404
    # Confirm removal
    response = client.get("/activities")
    data = response.json()
    assert test_email not in data[activity]["participants"]
