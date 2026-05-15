import csv
from datetime import datetime
from io import StringIO

from fastapi import HTTPException


REQUIRED_COLUMNS = [
    "Дата",
    "Номер группы",
    "ФИО",
    "Оценка",
]


def validate_csv(content: str):

    content = content.lstrip("\ufeff")

    reader = csv.DictReader(
        StringIO(content),
        delimiter=";"
    )

    if reader.fieldnames is None:
        raise HTTPException(
            status_code=400,
            detail="CSV file is empty"
        )

    normalized_columns = [
        column.strip()
        for column in reader.fieldnames
    ]

    if normalized_columns != REQUIRED_COLUMNS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid CSV columns: {normalized_columns}"
        )

    reader.fieldnames = normalized_columns

    fieldnames = [name.strip() for name in reader.fieldnames]

    if fieldnames != REQUIRED_COLUMNS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid CSV columns: {fieldnames}"
        )

    validated_rows = []

    for line_number, row in enumerate(reader, start=2):

        try:
            grade_date = datetime.strptime(
                row["Дата"].strip(),
                "%d.%m.%Y"
            ).date()

        except ValueError:
            raise HTTPException(
                status_code=400,
                detail=(
                    f"Invalid date '{row['Дата']}' "
                    f"at line {line_number}"
                )
            )

        group_name = row["Номер группы"].strip()

        if not group_name:
            raise HTTPException(
                status_code=400,
                detail=f"Empty group at line {line_number}"
            )

        full_name = row["ФИО"].strip()

        if not full_name:
            raise HTTPException(
                status_code=400,
                detail=f"Empty full_name at line {line_number}"
            )

        try:
            grade = int(row["Оценка"])
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid grade at line {line_number}"
            )

        if grade not in [2, 3, 4, 5]:
            raise HTTPException(
                status_code=400,
                detail=f"Grade must be between 2 and 5 at line {line_number}"
            )

        validated_rows.append(
            (
                grade_date,
                group_name,
                full_name,
                grade,
            )
        )

    return validated_rows