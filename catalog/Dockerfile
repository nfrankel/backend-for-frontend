FROM python:3.11-alpine

COPY requirements.txt requirements.txt
RUN --mount=type=cache,target=/root/.cache pip3 install -r requirements.txt

COPY app.py .

EXPOSE 5001

CMD [ "python3", "-m" , "flask", "run", "--port=5001", "--host=0.0.0.0"]
