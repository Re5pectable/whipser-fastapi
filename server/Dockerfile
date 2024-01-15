FROM python:3.9

WORKDIR /src

COPY requirements.txt .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache-dir -r requirements.txt
RUN apt update && apt install -y ffmpeg

COPY . .

WORKDIR /

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
