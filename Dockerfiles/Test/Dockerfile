FROM python:2.7.15

RUN apt-get update && apt-get install -yq curl && apt-get clean
RUN pip install pytest requests

WORKDIR /app

ADD tests /app/tests

ENTRYPOINT ["pytest", "tests/", "-v", "-s"]
