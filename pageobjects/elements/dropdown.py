"""Module for dropdown page element."""
from pageobjects.elements.base import BaseElement


class DropDownElement(BaseElement):
    """Class for dropdown page element."""
    # pylint: disable=too-few-public-methods

    def __get__(self, obj, cls=None):
        """Method for get element value."""
        return self.get_selected_value()

    def __set__(self, obj, value):
        """Method for set element value."""
        self.element.find_element_by_xpath(
            self.locator + "/..//div[contains(@class, 'ui-selectBtnChoose')]").click()
        self.element.find_element_by_xpath(
            self.locator + "/..//div[@data-value='{}']".format(value)).click()

    @property
    def selected_element(self):
        """Property for get selected element.

        :returns: The instance of :class:`WebElement`.
        """
        return self.element.find_element_by_xpath(
            self.locator + "/..//div[contains(@class, 'ui-selectItem__selected')]")

    def get_selected_value(self):
        """Method for get selected element value.

        :returns: The selected element value.
        """
        return self.selected_element.get_attribute("data-value")
