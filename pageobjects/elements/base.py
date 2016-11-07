"""Module for base page element."""
from selenium.common.exceptions import NoSuchElementException
from framework.driver_manager import DriverManager


class BaseElement(object):
    """Class for base page element."""
    # pylint: disable=too-few-public-methods

    def __init__(self, locator):
        """
        :param locator: The element locator.
        """
        self.driver = DriverManager().driver
        self.locator = locator

    @property
    def element(self):
        """Property to get element.

        :returns: The instance of :class:`WebElement`.
        """
        return self.find_element()

    def find_element(self):
        """Method for find element by xpath locator.

        :returns: The instance of :class:`WebElement`.

        :raises: AssertionError if can not find element.
        """
        try:
            return self.driver.find_element_by_xpath(self.locator)
        except NoSuchElementException:
            assert 0, "No such element '{}'.".format(self.locator)
