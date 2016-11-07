"""Module for button page element."""
from pageobjects.elements.base import BaseElement


class ButtonElement(BaseElement):
    """Class for button page element."""
    # pylint: disable=too-few-public-methods

    def click(self):
        """Method for click element action."""
        if self.element.is_enabled():
            self.element.click()
        else:
            raise AssertionError("Element '{}' is disabled.", self.element)
