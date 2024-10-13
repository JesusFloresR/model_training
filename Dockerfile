FROM python:3.11-slim

COPY . /opt/ml/code

WORKDIR /opt/ml/code

RUN pip install -r requirements.txt
RUN pip install sagemaker-training

CMD [ "python", "train.py" ]