"""Module for table page element."""
from pageobjects.elements.base import BaseElement


class TableElement(BaseElement):
    """Class for table page element."""
    # pylint: disable=too-few-public-methods

    def __get__(self, obj, val):
        """Method for get element value."""
        names = self.element.find_elements_by_xpath("//span[@class='calc-pairName']")
        values = {}

        for name in names:
            value = name.find_element_by_xpath(
                "//span[contains(text(), '{}')]/../span[@class='calc-pairValue']".format(name.text))
            values.update({name.text: float(value.text)})
        return values
