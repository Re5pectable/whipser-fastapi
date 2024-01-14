from fastapi import APIRouter, File, Query, Request, UploadFile

from ..transcription import transcribe_by_filepath, get_transcription
from .utils import save_file
from .errors import *

_IS_READY = True

router = APIRouter()


def check_readiness():
    global _IS_READY
    if not _IS_READY:
        raise BusyError
    _IS_READY = False


@router.post('/recognize_new')
async def transcribe(request: Request, file: UploadFile = File(...), language: str = Query("en")):
    global _IS_READY
    check_readiness()

    try:
        saved_file_path = await save_file(file)
        data = await transcribe_by_filepath(saved_file_path)
    except Exception as e:
        raise UnknownError

    _IS_READY = True
    return data


@router.get("/status")
async def get_status():
    global _IS_READY
    print(_IS_READY)
    return {"isReadyToRecognize": _IS_READY}


@router.get("/get-recognizing")
async def get_transcript(id: str = Query('')):
    try:
        return get_transcription(id)
    except FileNotFoundError:
        raise RecognitionNotFoundError
