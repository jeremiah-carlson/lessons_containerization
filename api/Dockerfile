FROM docker.io/library/python:3.11-slim-bookworm AS base
CMD /bin/bash
WORKDIR /root

COPY ./app/ /root/

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

FROM base
WORKDIR /root
CMD [ "python3", "main.py" ]