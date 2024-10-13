FROM python:3.11-slim

COPY . /opt/ml/code

WORKDIR /opt/ml/code

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "train.py"]