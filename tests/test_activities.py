def test_get_activities_returns_all_activities(client):
    """Test GET /activities returns all activities with correct structure"""
    # Arrange - data is set up in conftest fixture

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    response_activities = response.json()
    assert len(response_activities) == 3
    assert "Chess Club" in response_activities
    assert "Programming Class" in response_activities
    assert "Full Activity" in response_activities


def test_get_activities_contains_correct_fields(client):
    """Test that each activity has required fields"""
    # Arrange
    # (no additional setup needed)

    # Act
    response = client.get("/activities")

    # Assert
    response_activities = response.json()
    for activity_name, activity_data in response_activities.items():
        assert "description" in activity_data
        assert "schedule" in activity_data
        assert "max_participants" in activity_data
        assert "participants" in activity_data
        assert isinstance(activity_data["participants"], list)


def test_get_activities_shows_correct_participant_count(client):
    """Test that participant lists are accurate"""
    # Arrange
    # (no additional setup needed)

    # Act
    response = client.get("/activities")

    # Assert
    response_activities = response.json()
    assert len(response_activities["Chess Club"]["participants"]) == 1
    assert "michael@mergington.edu" in response_activities["Chess Club"]["participants"]
    assert len(response_activities["Programming Class"]["participants"]) == 2
