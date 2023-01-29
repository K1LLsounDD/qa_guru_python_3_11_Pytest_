# 1. ���������� ��������� ����, ���� ����������� ������ ���������� (� ��������);
# 2. �������������� �������� � ������� indirect;

import pytest
from selene.support import by
from selene.support.shared import browser
from selene.support.conditions import have


@pytest.mark.parametrize('browser_window_size', ['Desktop', 'Mobile'], indirect=True)
def test_only_desktop_browser_size(browser_window_size):
    if browser.config.window_width == 414:
        pytest.skip(reason='Test only in desktop browser screen resolution.')
    elif browser.config.window_width == 1920:
        browser.open('https://github.com/')
        browser.element('[href="/login"]').click()
        assert browser.element('#login').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize('browser_window_size', ['Desktop', 'Mobile'], indirect=True)
def test_only_mobile_browser_size(browser_window_size):
    if browser.config.window_width == 1920:
        pytest.skip(reason='Test only in mobile browser screen resolution.')
    elif browser.config.window_width == 414:
        browser.open('https://github.com/')
        browser.element('.Button-content .Button-label').click()
        browser.element(by.partial_text('Sign in')).click()
        assert browser.element('#login').should(have.text('Sign in to GitHub'))
