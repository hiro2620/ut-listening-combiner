FROM python:3.9-slim

ENV PYTHONUNBUFFERED True

# Install ffmpeg and git
RUN apt-get update && apt-get install -y ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

# Install dependencies
COPY ./requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy local code to the container image.
COPY ./src/ ./src/
WORKDIR /app/src

CMD python3 main.py