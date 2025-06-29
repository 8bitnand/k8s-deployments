FROM  python:3.9
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY . .

CMD ["fastapi", "run", "app.py", "--port", "80", "--host", "0.0.0.0"]
