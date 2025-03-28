"""Elements and methods that relate to the home page upon logging in are found here"""
from pages.base_page import BasePage

class HomePage(BasePage):
    """
    This class contains elements/methods which are present on the Home Page
    """

    @property
    def get_explore_bar(self):
        """
        Gets the explore bar locator
        Returns:
            Locator: The explore bar locator
        """
        return self.page.locator(".explore-tab-bar__home.logged-in")
