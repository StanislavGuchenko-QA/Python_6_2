import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def set_window_size():
    browser.config.window_width = 1000
    browser.config.window_height = 1000