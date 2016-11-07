"""Module for text page element."""
from pageobjects.elements.base import BaseElement


class TextElement(BaseElement):
    """Class for text page element."""
    # pylint: disable=too-few-public-methods

    def __get__(self, obj, val):
        """Method for get element value."""
        return self.element.text
