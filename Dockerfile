FROM python:3.12-slim-bullseye

RUN python3 -m venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./src /code
WORKDIR /code
ENV PORT=8000

CMD ["python", "manage.py", "runserver",  "$PORT"]