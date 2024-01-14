import os
from typing import Literal, Optional

from pydantic import BaseModel, FileUrl

available_models = Literal['tiny', 'base', 'small', 'medium', 'large']

DEFAULT_MODEL = 'base'
DEFAULT_MODELS_PATH = './src/transcription/models/'
DEFAULT_AUDIO_PATH = './src/api/received/'
DEFAULT_TRANSCRIPTION_PATH = './src/transcription/results/'


def get_model_type():
    in_env = os.environ.get('WHISPER_MODEL_TYPE')
    if in_env:
        print('Running with user model:', in_env)
        return in_env
    print('Running with default model:', DEFAULT_MODEL)
    return DEFAULT_MODEL


def get_models_path():
    in_env = os.environ.get('WHISPER_MODELS_DIR')
    if in_env:
        print('Running with user models path:', in_env)
        return in_env
    print('Running with default models path:', DEFAULT_MODELS_PATH)
    return DEFAULT_MODELS_PATH


def get_audio_path():
    in_env = os.environ.get('AUDIO_PATH')
    if in_env:
        print('Running with user audio path:', in_env)
        return in_env
    print('Running with default audio path:', DEFAULT_AUDIO_PATH)
    return DEFAULT_AUDIO_PATH

def get_transcription_path():
    in_env = os.environ.get('TRANSCRIPTION_PATH')
    if in_env:
        print('Running with user transcription path:', in_env)
        return in_env
    print('Running with default transcription path:', DEFAULT_TRANSCRIPTION_PATH)
    return DEFAULT_TRANSCRIPTION_PATH


class AppSettings(BaseModel):
    whisper_model_type: Optional[available_models] = get_model_type()
    whisper_models_dir: Optional[FileUrl] = get_models_path()
    audio_path: Optional[FileUrl] = get_audio_path()
    transcription_path: Optional[FileUrl] = get_transcription_path()


app_settings = AppSettings()
