# Bakend Auto

## Installation and Environment Setup

Install Python packages with pip and requirements.txt

```
pip install -r requirement.txt
```

## Execute your test

Pytest will execute all the tests which file name start from test_

```
pytest
```

Pytest will execute the tests with report in html format

```
pytest --html=report.html
```

Pytest will execute the tests with params Pre-Prod environment and vend name pp01

```
pytest --env=pre-prod --vend=pp01
```

## Test data file structure

test data ---- test service name ---- sub service name ---- test method name

> For example:
> 
> We have test_user.py in tests/user folder to verify all APIs related to user service. There is a test_checkToken method in TestUser class. If you want to verify the API checkToken, please add your cases in the checkToken.json
>
>The path will be as below: 
> testdata/user/checkToken.json