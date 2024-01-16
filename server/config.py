import os
from typing import Optional
from pydantic import BaseModel

# Константы по умолчанию
DEFAULT_MODEL = 'base'
DEFAULT_MODELS_PATH = './src/transcription/models/'
DEFAULT_AUDIO_PATH = './src/api/received/'
DEFAULT_TRANSCRIPTION_PATH = './src/transcription/results/'

def create_directory_if_not_exists(directory_path: str):
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(f"Folder '{directory_path}' was created")
    except FileExistsError:
        print(f"Folder '{directory_path}' already exists, skipping...")

def get_env_path(env_var: str, default_path: str) -> str:
    path = os.getenv(env_var, default_path)
    return path if path.endswith('/') else path + '/'

class AppSettings(BaseModel):
    whisper_model_type: str = os.getenv('WHISPER_MODEL_TYPE', DEFAULT_MODEL)
    whisper_models_dir: str = get_env_path('WHISPER_MODELS_DIR', DEFAULT_MODELS_PATH)
    audio_path: str = get_env_path('AUDIO_PATH', DEFAULT_AUDIO_PATH)
    transcription_path: str = get_env_path('TRANSCRIPTION_PATH', DEFAULT_TRANSCRIPTION_PATH)

app_settings = AppSettings()

create_directory_if_not_exists(app_settings.audio_path)
create_directory_if_not_exists(app_settings.transcription_path)
create_directory_if_not_exists(app_settings.whisper_models_dir)

print(f'Running with model type: {app_settings.whisper_model_type}')
print(f'Running with models path: {app_settings.whisper_models_dir}')
print(f'Running with audio path: {app_settings.audio_path}')
print(f'Running with transcription path: {app_settings.transcription_path}')
