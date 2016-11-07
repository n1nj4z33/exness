"""Module for base page object."""
from framework.driver_manager import DriverManager


class BasePage(object):
    """Class for base page object."""

    url = "https://www.exness.com"

    def __init__(self):
        self.driver_manager = DriverManager()
        self.driver_manager.start()

    def open(self):
        """Method for open url."""
        self.driver_manager.driver.get(self.url)

    def close(self):
        """Method for stop webdriver."""
        self.driver_manager.stop()
