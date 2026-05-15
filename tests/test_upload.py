from pathlib import Path

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_upload_grades():

    csv_path = Path("students_grades.csv")

    with open(csv_path, "rb") as file:

        response = client.post(
            "/upload-grades",
            files={
                "file": (
                    "students_grades.csv",
                    file,
                    "text/csv",
                )
            },
        )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ok"
    assert data["records_loaded"] == 2000
    assert data["students"] == 40


def test_upload_invalid_csv():

    invalid_csv = (
        "Дата;Номер группы;ФИО;Оценка\n"
        "01.09.2024;101;Иванов Иван;10"
    )

    response = client.post(
        "/upload-grades",
        files={
            "file": (
                "invalid.csv",
                invalid_csv,
                "text/csv",
            )
        },
    )

    assert response.status_code == 400