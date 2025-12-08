FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PORT=3000

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 3000

# Use sh -c so ${PORT} is expanded from ENV when container starts
CMD ["sh", "-c", "gunicorn -b 0.0.0.0:${PORT} main:app"]
