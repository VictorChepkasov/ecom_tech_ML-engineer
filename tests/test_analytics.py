from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_students_more_than_3_twos():

    response = client.get(
        "/students/more-than-3-twos"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    if data:
        assert "full_name" in data[0]
        assert "count_twos" in data[0]


def test_students_less_than_5_twos():

    response = client.get(
        "/students/less-than-5-twos"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    if data:
        assert "full_name" in data[0]
        assert "count_twos" in data[0]