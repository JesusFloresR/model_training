FROM python:3.11-slim

RUN mkdir -p /opt/ml/code

WORKDIR /opt/ml/code

COPY train.py /opt/ml/code

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "train.py"]