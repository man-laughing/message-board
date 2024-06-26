FROM python:2.7

WORKDIR /usr/local/messageboard/

COPY .  /usr/local/messageboard/

RUN \
pip install flask && pip install flask_redis

ENTRYPOINT ["python", "app.py" ]
