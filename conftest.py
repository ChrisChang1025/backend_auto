import pytest
import requests
import environment

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="pre-prod", help="Test environment selection")
    parser.addoption("--vend", action="store", default="pp001", help="Test vender selection")

@pytest.fixture(scope="session")
def params(request):
    params = {}
    params['env'] = request.config.getoption("--env")
    params['vend'] = request.config.getoption("--vend")
    return params

@pytest.fixture(scope="session")
def get_url(params: dict):
    # url = environment.ENV_URL + "?password=innotech&env=" + params["env"] + "&vend=" + params["vend"]
    # r = requests.get(url)

    return environment.ENV_URL