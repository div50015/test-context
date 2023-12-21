import os
import pytest
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from selene import browser
import utils.data


def pytest_addoption(parser):
    parser.addoption("--context",default="bstack",help="Specify context")


def pytest_configure(config):
    context = config.getoption("--context")
    load_dotenv(dotenv_path=f'.env.{context}')

@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def android_mobile_management(context):
    from configuration import settings
    # options = settings.to_driver_options(context=context)
    # print(f'options_conftest = {options}')
    # remote_url = settings.remote_url
    # print(f'remote_url_conftest = {remote_url}')

    options = UiAutomator2Options().load_capabilities(settings.to_driver_options(context=context))
    browser.config.driver_remote_url = settings.remote_url
    browser.config.driver_options = options


    yield

    browser.quit()