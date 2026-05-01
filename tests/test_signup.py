def test_signup_success_adds_participant(client):
    """Test successful signup adds student to activity"""
    # Arrange
    email = "newstudent@mergington.edu"
    activity = "Chess Club"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "Signed up" in data["message"]
    assert email in data["message"]

    # Verify participant was actually added
    activities_response = client.get("/activities")
    assert email in activities_response.json()[activity]["participants"]


def test_signup_activity_not_found(client):
    """Test signup returns 404 when activity doesn't exist"""
    # Arrange
    email = "student@mergington.edu"
    activity = "Nonexistent Activity"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_already_registered(client):
    """Test signup returns 400 when student already signed up"""
    # Arrange
    email = "michael@mergington.edu"  # Already in Chess Club
    activity = "Chess Club"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]


def test_signup_activity_full(client):
    """Test signup returns 400 when activity is at max capacity"""
    # Arrange
    email = "student@mergington.edu"
    activity = "Full Activity"  # max_participants: 1, already has 1 participant

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 400


def test_signup_increments_participant_count(client):
    """Test that signup properly increments participant count"""
    # Arrange
    email = "newstudent@mergington.edu"
    activity = "Chess Club"

    # Act - First signup
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    activities_response = client.get("/activities")
    activity_data = activities_response.json()[activity]
    assert len(activity_data["participants"]) == 2
