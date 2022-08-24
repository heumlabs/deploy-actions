# Container image that runs your code
FROM python:3.10

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY . /code

RUN pip install -r /code/requirement.txt

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/code/entrypoint.sh"]
