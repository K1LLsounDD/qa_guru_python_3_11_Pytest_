from selene.support import by
from selene.support.conditions import have
from selene.support.shared import browser


def test_open_desktop_browser(open_desktop_window_size):
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()
    assert browser.element('#login').should(have.text('Sign in to GitHub'))


def test_open_mobile_browser(open_mobile_window_size):
    browser.open('https://github.com/')
    browser.element('.Button-content .Button-label').click()
    browser.element(by.partial_text('Sign in')).click()
    assert browser.element('#login').should(have.text('Sign in to GitHub'))
