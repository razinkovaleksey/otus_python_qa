import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="URL"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")
