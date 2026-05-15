from fastapi import APIRouter, File, UploadFile, HTTPException

from app.schemas import (
    UploadResponse,
    StudentTwosResponse,
)

from app.validators import validate_csv

from app.services.grades_service import (
    load_grades,
    get_students_more_than_3_twos,
    get_students_less_than_5_twos,
)

router = APIRouter()


@router.post(
    "/upload-grades",
    response_model=UploadResponse
)
def upload_grades(
    file: UploadFile = File(...)
):

    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are allowed"
        )

    content = file.file.read().decode("utf-8")

    validated_rows = validate_csv(content)

    result = load_grades(validated_rows)

    return result


@router.get(
    "/students/more-than-3-twos",
    response_model=list[StudentTwosResponse]
)
def students_more_than_3_twos():

    return get_students_more_than_3_twos()


@router.get(
    "/students/less-than-5-twos",
    response_model=list[StudentTwosResponse]
)
def students_less_than_5_twos():

    return get_students_less_than_5_twos()