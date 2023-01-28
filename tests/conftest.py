import pytest
from selene.support.shared import browser


@pytest.fixture(params=['Desktop', 'Mobile'])
def browser_window_size(request):
    if request.param == 'Desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif request.param == 'Mobile':
        browser.config.window_width = 414
        browser.config.window_height = 896
    return request


@pytest.fixture
def open_desktop_window_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()


@pytest.fixture
def open_mobile_window_size():
    browser.config.window_width = 414
    browser.config.window_height = 896
    yield
    browser.quit()
