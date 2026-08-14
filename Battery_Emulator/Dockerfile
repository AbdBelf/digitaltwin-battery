FROM python:3.12-slim

WORKDIR /app

COPY battery-emulator.py .

RUN pip install --no-cache-dir flask

EXPOSE 5000

CMD ["python", "battery-emulator.py"]