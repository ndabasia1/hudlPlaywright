"""Elements and methods which are present across multiple pages are stored here"""
class BasePage:
    """
    This class contains elements/methods which are present across more than one page
    """
    def __init__(self, page):
        self.page = page

    def hover_over_display_name(self):
        """
        Hover over your display name in the header
        """
        self.page.locator(".hui-globaluseritem__display-name").hover()

    def log_out(self):
        """
        Click the logout action found in the header
        """
        self.page.locator(".hui-globalusermenu").get_by_test_id("webnav-usermenu-logout").click()
