from urllib.parse import quote

from src.app import activities


def test_unregister_removes_student_from_activity(client):
    # Arrange
    activity_name = "Chess Club"
    email = "departing.student@mergington.edu"
    activities[activity_name]["participants"].append(email)
    endpoint = f"/activities/{quote(activity_name, safe='')}/participants"

    # Act
    response = client.delete(endpoint, params={"email": email})

    # Assert
    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]
