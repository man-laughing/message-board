FROM python:2.7

WORKDIR /usr/local/messageboard/

COPY .  /usr/local/messageboard/

RUN \
pip install flask && pip install flask_redis && \
    ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo Asia/Shanghai > /etc/timezone 

ENTRYPOINT ["python", "app.py" ]
