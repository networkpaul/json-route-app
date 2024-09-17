FROM python:3.10-slim

WORKDIR /code

RUN useradd -m python

USER python

ENV PATH="/home/python/.local/bin:${PATH}"

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=python:python . .

RUN mkdir -p routes

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
