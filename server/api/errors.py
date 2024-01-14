from fastapi import HTTPException

BusyError = HTTPException(
    status_code=401,
    detail={"error": "Server is busy. Please try again later."}
)

EmptyIDError = HTTPException(
    status_code=400,
    detail="ID cannot be empty"
)

RecognitionNotFoundError = HTTPException(
    status_code=404,
    detail="Recognition not found"
)

UnknownError = HTTPException(
    status_code=500,
    detail="An error occurred while processing the request"
)
