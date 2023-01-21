FROM python:3.11-alpine

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py .

EXPOSE 5002

CMD [ "python3", "-m" , "flask", "run", "--port=5002", "--host=0.0.0.0"]
