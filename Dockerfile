# start by pulling the python image
FROM python:3.10-alpine
RUN rm -rf /var/cache/apk/* && \
    apk update && \
    apk add make && \
    apk add build-base && \
    apk add gcc && \
    apk add python3-dev && \
    apk add libffi-dev && \
    apk add musl-dev && \
    apk add openssl-dev && \
    apk del build-base && \
    rm -rf /var/cache/apk/*

ENV HOME=/home/app

ENV HOME=/home/api FLASK_APP=main.py FLASK_DEBUG=True PORT=5000
RUN adduser -D app
USER app
# switch working directory
WORKDIR $HOME
COPY --chown=api:api . $HOME

RUN python -m venv venv && \
    venv/bin/pip install --upgrade pip && \
    venv/bin/pip install -r requirements.txt

# configure the container to run in an executed manner
EXPOSE 5000
CMD ["./run.sh"]