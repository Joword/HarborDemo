FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
LABEL author="Joword"
WORKDIR /app
COPY requirements.txt .
COPY app.py .
COPY pip.conf .
RUN pip install --no-cache-dir -r requirements.txt 

EXPOSE 8093
RUN python3 app.py