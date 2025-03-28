"""Fixtures to be used by all tests are found here"""
import pytest
from playwright.sync_api import sync_playwright
from config.config import config
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.fixture
def browser():
    """
    Fixture to set-up and launch a playwright browser instance
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)         # Change to True to run headless
        p.selectors.set_test_id_attribute("data-qa-id")
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    """
    Fixture to set-up and launch a playwright page instance
    Args:
        browser (Browser): The browser instance used to create the page
    """
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture
def login_page(page):
    """
    Fixture to set-up the login page instance
    Args:
        page (Page): The page instance used to set-up the login page object
    """
    page.goto(config.environment + "login")
    login_page = LoginPage(page)
    return login_page

@pytest.fixture
def home_page(page):
    """
    Fixture to set-up the home page instance
    Args:
        page (Page): The page instance used to set-up the home page object
    """
    home_page = HomePage(page)
    return home_page
