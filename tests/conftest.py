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



