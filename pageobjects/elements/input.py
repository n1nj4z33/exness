"""Module for input page element."""
from pageobjects.elements.base import BaseElement


class InputElement(BaseElement):
    """Class for input page element."""
    # pylint: disable=too-few-public-methods

    def __set__(self, obj, val):
        """Method for set element value."""
        if self.element.is_enabled():
            self.element.clear()
            self.element.send_keys(str(val).replace(".", ","))
        else:
            raise AssertionError("Element '{}' is disabled.", self.element)
