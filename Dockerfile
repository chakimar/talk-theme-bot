FROM python:alpine

LABEL Name=talk-theme-bot Version=0.0.3

WORKDIR /app
ADD . /app

RUN python3 -m pip install -r requirements.txt
CMD ["python3", "run.py"]