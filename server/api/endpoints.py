from fastapi import APIRouter, File, Query, Request, UploadFile

from ..config import app_settings
from ..transcription import get_transcription, transcribe_by_filepath
from .errors import *
from .utils import convert_to_mp3, save_file

_IS_READY = True

router = APIRouter()


def verify_readiness():
    global _IS_READY
    if not _IS_READY:
        raise BusyError
    _IS_READY = False


@router.post('/recognize_new')
async def transcribe(request: Request, file: UploadFile = File(...), language: str = Query("en")):
    global _IS_READY
    verify_readiness()

    try:
        path_to_target_file = await save_file(file)
        
        if not path_to_target_file.endswith('.mp3'):
            convert_to_mp3(path_to_target_file, path_to_target_file + '.mp3')
            path_to_target_file += '.mp3'
        
        transcription_path = app_settings.transcription_path + file.filename + '.json'    
        data = transcribe_by_filepath(language, path_to_target_file, transcription_path)
        
    except Exception as e:
        _IS_READY = True
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
