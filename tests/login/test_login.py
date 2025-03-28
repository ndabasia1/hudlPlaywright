"""Tests here focus on the login screen"""
import pytest
from playwright.sync_api import expect
from config.config import config
from config.constants import ErrorMessages, Labels, AttributeValues, TestData, Messages

@pytest.fixture
def logo_visible(login_page):
    """
    Ensure the logo is visible before executing a test
    Args:
        login_page: An instance of the login page
    """
    if not login_page.is_logo_visible():
        pytest.fail(ErrorMessages.LOGO_NOT_VISIBLE)

def test_login_logout(page, logo_visible, login_page, home_page):
    """
    Test able to login and logout successfully
    Args:
        page (Page): The page object of the browser
        logo_visible: Fixture to be run before this test
        login_page: An instance of the login page
        home_page: An instance of the home page
    """
    login_page.enter_into_field(AttributeValues.USERNAME, config.email)
    login_page.click_button(Labels.CONTINUE)
    login_page.enter_into_field(AttributeValues.PASSWORD, config.password)
    login_page.click_button(Labels.CONTINUE)
    expect(home_page.get_explore_bar).to_be_visible()
    home_page.hover_over_display_name()
    home_page.log_out()
    assert page.url == config.environment

def test_invalid_email_format(logo_visible, login_page):
    """
    Test unable to login with an invalid email format
    Args:
        logo_visible: Fixture to be run before this test
        login_page: An instance of the login page
    """
    login_page.enter_into_field(AttributeValues.USERNAME, TestData.TEST_STRING)
    login_page.click_button(Labels.CONTINUE)
    expect(login_page.get_error_message()).to_contain_text(Messages.ENTER_VALID_EMAIL)

def test_incorrect_email(logo_visible, login_page):
    """
    Test unable to login with an incorrect email
    Args:
        logo_visible: Fixture to be run before this test
        login_page: An instance of the login page
    """
    login_page.enter_into_field(AttributeValues.USERNAME, TestData.INVALID_EMAIL)
    login_page.click_button(Labels.CONTINUE)
    login_page.enter_into_field(AttributeValues.PASSWORD, TestData.TEST_STRING)
    login_page.click_button(Labels.CONTINUE)
    expect(login_page.get_error_message()).to_contain_text(Messages.INVALID_CREDENTIALS)

def test_incorrect_password(logo_visible, login_page):
    """
    Test unable to login with an incorrect password
    Args:
        logo_visible: Fixture to be run before this test
        login_page: An instance of the login page
    """
    login_page.enter_into_field(AttributeValues.USERNAME, config.email)
    login_page.click_button(Labels.CONTINUE)
    login_page.enter_into_field(AttributeValues.PASSWORD, TestData.TEST_STRING)
    login_page.click_button(Labels.CONTINUE)
    expect(login_page.get_error_message()).to_contain_text(Messages.INCORRECT_CREDENTIALS)

def test_edit_email(logo_visible, login_page):
    """
    Test able to edit your email once on the password screen
    Args:
        logo_visible: Fixture to be run before this test
        login_page: An instance of the login page
    """
    login_page.enter_into_field(AttributeValues.USERNAME, config.email)
    login_page.click_button(Labels.CONTINUE)
    expect(login_page.get_input_field(AttributeValues.USERNAME)).not_to_be_visible()
    login_page.click_link(Labels.EDIT)
    expect(login_page.get_input_field(AttributeValues.USERNAME)).to_be_visible()

def test_create_account_link(logo_visible, login_page):
    """
    Test able to navigate to the registration screen
    Args:
        logo_visible: Fixture to be run before this test
        login_page: An instance of the login page
    """
    login_page.click_link(Labels.CREATE_ACCOUNT)
    expect(login_page.get_header).to_have_text(Labels.CREATE_ACCOUNT)

def test_alternative_login_options(logo_visible, login_page):
    """
    Test the alternative login options are present
    Args:
        logo_visible: Fixture to be run before this test
        login_page: An instance of the login page
    """
    expect(login_page.get_button_span(Labels.CONTINUE_WITH_GOOGLE)).to_be_visible()
    expect(login_page.get_button_span(Labels.CONTINUE_WITH_FACEBOOK)).to_be_visible()
    expect(login_page.get_button_span(Labels.CONTINUE_WITH_APPLE)).to_be_visible()

def test_reset_password(logo_visible, login_page):
    """
    Test able to trigger the password reset screen
    Args:
        logo_visible: Fixture to be run before this test
        login_page: An instance of the login page
    """
    login_page.enter_into_field(AttributeValues.USERNAME, config.email)
    login_page.click_button(Labels.CONTINUE)
    login_page.click_link(Labels.FORGOT_PASSWORD)
    login_page.click_button(Labels.CONTINUE)
    expect(login_page.get_header).to_have_text(Labels.CHECK_YOUR_EMAIL)
