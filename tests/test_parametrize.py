# 2. Переопределите параметр с помощью indirect;

import pytest
from selene.support import by
from selene.support.conditions import have
from selene.support.shared import browser


@pytest.mark.parametrize('browser_window_size', ['Desktop'], indirect=True)
def test_github_desktop(browser_window_size):
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()
    assert browser.element('#login').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize('browser_window_size', ['Mobile'], indirect=True)
def test_github_mobile(browser_window_size):
    browser.open('https://github.com/')
    browser.element('.Button-content .Button-label').click()
    browser.element(by.partial_text('Sign in')).click()
    assert browser.element('#login').should(have.text('Sign in to GitHub'))
