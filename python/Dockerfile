FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
LABEL author="Joword"
WORKDIR /app
EXPOSE 8093
COPY . /app
RUN pip install gunicorn && pip install --no-cache-dir -r requirements.txt