FROM python:3.11.6

WORKDIR /backend_auto

COPY . /backend_auto

RUN pip install -r requirement.txt

CMD ["pytest", "-s", "-m", "regression", "--env=pre-prod", "--vend=pp001"]