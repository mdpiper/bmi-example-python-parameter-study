FROM python:3.12

COPY requirements.txt /tmp/

RUN --mount=type=cache,target=/root/.cache/pip,sharing=locked \
    pip3 install -r /tmp/requirements.txt


WORKDIR /code
COPY . /code

RUN --mount=type=cache,target=/root/.cache/pip,sharing=locked \
    pip3 install -e /code \
    && bmiheat-parameter-study setup study/study-config.yaml
