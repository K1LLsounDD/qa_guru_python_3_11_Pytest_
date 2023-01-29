import pytest
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
    browser.element(
        '[href="/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home"]').click()
    browser.element(
        '[href="/login?return_to=https%3A%2F%2Fgithub.com%2Fsignup%3Fref_cta%3DSign%2Bup%26ref_loc%3Dheader%2Blogged%2Bout%26ref_page%3D%252F%26source%3Dheader-home"]'
    ).click()
    assert browser.element('#login').should(have.text('Sign in to GitHub'))
