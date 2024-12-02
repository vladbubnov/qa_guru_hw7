import pytest
from selene import browser


@pytest.fixture(scope='function')
def browser_management():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = 'https://github.com/vladbubnov/test_data/blob/main'

    yield

    browser.quit()