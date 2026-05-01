def test_root_redirects_to_index(client):
    """Test GET / redirects to static index.html"""
    # Arrange
    # (no setup needed)

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert "/static/index.html" in response.headers["location"]
