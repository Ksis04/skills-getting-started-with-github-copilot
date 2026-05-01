import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Provide a TestClient for the FastAPI app"""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities to known state before each test"""
    # Arrange: Set up clean test data
    activities.clear()
    activities.update({
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 2,
            "participants": ["michael@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 3,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Full Activity": {
            "description": "Activity at capacity",
            "schedule": "Mondays, 2:00 PM - 3:00 PM",
            "max_participants": 1,
            "participants": ["john@mergington.edu"]
        }
    })
    yield
