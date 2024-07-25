FROM python:2.7-slim
WORKDIR /usr/local/messageboard/
COPY .  /usr/local/messageboard/
RUN pip install flask \
    && pip install flask_redis \
    && ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo Asia/Shanghai > /etc/timezone
EXPOSE 5000
ENTRYPOINT ["python", "app.py" ]
