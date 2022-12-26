FROM python:3.10

COPY . /code

RUN pip install -r /code/requirement.txt

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/code/entrypoint.sh"]
