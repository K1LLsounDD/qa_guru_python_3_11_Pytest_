# 1. Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот);
# 2. Переопределите параметр с помощью indirect;

import pytest
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
        browser.element(
            '[href="/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home"]').click()
        browser.element(
            '[href="/login?return_to=https%3A%2F%2Fgithub.com%2Fsignup%3Fref_cta%3DSign%2Bup%26ref_loc%3Dheader%2Blogged%2Bout%26ref_page%3D%252F%26source%3Dheader-home"]'
        ).click()
        assert browser.element('#login').should(have.text('Sign in to GitHub'))
