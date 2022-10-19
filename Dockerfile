FROM python:3.10
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./ /code
#uvicorn main:app --reload
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8005"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8005"]
