"""Elements and methods that relate to the login page are found here"""
from pages.base_page import BasePage

class LoginPage(BasePage):
    """
    This class contains elements/methods which are present on the Login Page
    """

    @property
    def get_logo(self):
        """
        Gets the logo element
        Returns:
            Locator: The logo element
        """
        return self.page.locator("#custom-prompt-logo")

    @property
    def get_header(self):
        """
        Gets the header h1 element
        Returns:
            Locator: The header h1 element
        """
        return self.page.locator("h1")

    def get_input_field(self, field_name):
        """
        Gets an input field element
        Args:
            field_name (str): The name of the field to get
        Returns:
            Locator: The input field element with name field_name
        """
        return self.page.locator(f"input[id={field_name}]")

    def get_button(self, button_name):
        """
        Gets a button element
        Args:
            button_name (str): The name of the button to get
        Returns:
            Locator: The button element with name button_name
        """
        return self.page.locator(f"//button[text()= '{button_name}']")

    def get_link(self, link_name):
        """
        Gets a link element
        Args:
            link_name (str): The name of the link to get
        Returns:
            Locator: The link element with name link_name
        """
        return self.page.locator(f"//a[text()= '{link_name}']")

    def get_error_message(self):
        """
        Gets an error message element
        Returns:
            Locator: The error message element
        """
        return self.page.locator(".ulp-input-error-message")

    def get_button_span(self, span_text):
        """
        Gets a button span element
        Args:
            span_text (str): The name of the button span to get
        Returns:
            Locator: The button span element with name span_text
        """
        return self.page.locator(f"//button/span[text()= '{span_text}']")

    def is_logo_visible(self):
        """
        Gets the visibility status of the logo element
        Returns:
            Boolean: The visibility status
        """
        return self.get_logo.is_visible()

    def enter_into_field(self, field_name, field_value):
        """
        Enters text into a field
        Args:
            field_name (str): The name of the field to enter text into
            field_value (str): The value of the field to enter
        """
        self.get_input_field(field_name).fill(field_value)

    def click_button(self, button_name):
        """
        Click a button
        Args:
            button_name (str): The name of the button to click
        """
        self.get_button(button_name).click()

    def click_link(self, link_name):
        """
        Click a link
        Args:
            link_name (str): The name of the link to click
        """
        self.get_link(link_name).click()
