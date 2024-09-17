FROM python:3.10-slim

WORKDIR /app

RUN useradd -m python

RUN mkdir -p /app/routes && chown -R python:python /app/routes

USER python

ENV PATH="/home/python/.local/bin:${PATH}"

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=python:python . .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
