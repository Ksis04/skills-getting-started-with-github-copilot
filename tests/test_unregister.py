def test_unregister_success_removes_participant(client):
    """Test successful unregister removes student from activity"""
    # Arrange
    email = "michael@mergington.edu"
    activity = "Chess Club"

    # Act
    response = client.delete(f"/activities/{activity}/unregister?email={email}")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "Unregistered" in data["message"]

    # Verify participant was actually removed
    activities_response = client.get("/activities")
    assert email not in activities_response.json()[activity]["participants"]


def test_unregister_activity_not_found(client):
    """Test unregister returns 404 when activity doesn't exist"""
    # Arrange
    email = "student@mergington.edu"
    activity = "Nonexistent Activity"

    # Act
    response = client.delete(f"/activities/{activity}/unregister?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_student_not_registered(client):
    """Test unregister returns 400 when student isn't registered"""
    # Arrange
    email = "notregistered@mergington.edu"
    activity = "Chess Club"

    # Act
    response = client.delete(f"/activities/{activity}/unregister?email={email}")

    # Assert
    assert response.status_code == 400
    assert "not signed up" in response.json()["detail"]


def test_unregister_decrements_participant_count(client):
    """Test that unregister properly decrements participant count"""
    # Arrange
    email = "emma@mergington.edu"
    activity = "Programming Class"
    initial_count = len(client.get("/activities").json()[activity]["participants"])

    # Act
    response = client.delete(f"/activities/{activity}/unregister?email={email}")

    # Assert
    assert response.status_code == 200
    activities_response = client.get("/activities")
    new_count = len(activities_response.json()[activity]["participants"])
    assert new_count == initial_count - 1
