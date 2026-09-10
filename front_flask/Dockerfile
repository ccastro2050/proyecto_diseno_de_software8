# Dockerfile del FRONT — Flask + Jinja2 + Bootstrap (puerto 8066)
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PUERTO=8066
EXPOSE 8066
CMD ["python", "app.py"]
