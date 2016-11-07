"""Module for calculator page object."""
import decimal
from Equation import Expression
from selenium.webdriver.support.ui import WebDriverWait

from exnessapi.calculator import get_eurusd_conversion

from pageobjects.base import BasePage
from pageobjects.elements.button import ButtonElement
from pageobjects.elements.dropdown import DropDownElement
from pageobjects.elements.input import InputElement
from pageobjects.elements.text import TextElement
from pageobjects.elements.table import TableElement


class CalculatorPage(BasePage):
    """Class for calculator page object."""

    __previous = None
    url = "https://www.exness.com/intl/ru/tools/calculator/"

    account = DropDownElement("//input[@name='account']")
    instruments = DropDownElement("//input[@name='Instruments']")
    symbols_forex = DropDownElement("//input[@name='SymbolsForex']")
    currency = DropDownElement("//input[@name='Currency']")
    leverage = DropDownElement("//input[@name='Leverage']")
    lot = InputElement("//input[@name='Lot']")
    calculate = ButtonElement("//button[contains(@class, 'ui-btn')]")
    margin = TextElement("//div[@id='margin']")
    profit = TextElement("//div[@id='profit']")
    swap_long = TextElement("//div[@id='swap_long']")
    swap_short = TextElement("//div[@id='swap_short']")
    volume = TextElement("//span[@id='volumemlnusd']")
    lotsmlnusd = TextElement("//span[@id='lotsmlnusd']")
    margin_formula2 = TextElement("//p[@id='margin_formula2']")
    profit_formula2 = TextElement("//p[@id='profit_formula2']")
    swap_formula2 = TextElement("//p[@id='swap_formula2']")
    swap_formula3 = TextElement("//p[@id='swap_formula3']")
    volume_formula2 = TextElement("//p[@id='volume_formula2']")
    conversion_pairs = TableElement("//div[@id='conversion_pairs']")

    @staticmethod
    def _format_formula(formula):
        """Method for format formula."""
        return Expression(formula.split("=")[0].replace("x", "*").replace("%", " / 100 "))

    @staticmethod
    def _format_swap_size(formula):
        """Method for format swap size."""
        return decimal.Decimal(formula.split("x")[2]).quantize(
            decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP)

    @staticmethod
    def _format_margin(margin):
        """Method for format margin."""
        return margin.quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP)

    @staticmethod
    def _format_profit(profit):
        """Method for format profit."""
        return profit.quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP)

    @staticmethod
    def _format_swap_long(swap_long):
        """Method for format swap long."""
        return swap_long.quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP)

    @staticmethod
    def _format_swap_short(swap_short):
        """Method for format swap short."""
        return swap_short.quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP)

    @staticmethod
    def _format_volume(volume):
        """Method for format volume."""
        return volume.quantize(decimal.Decimal('.0001'), rounding=decimal.ROUND_HALF_UP)

    @property
    def _swap_long_size(self):
        """Method for get swap long size."""
        return self._format_swap_size(self.swap_formula2)

    @property
    def _swap_short_size(self):
        """Method for get swap short size."""
        return self._format_swap_size(self.swap_formula3)

    # TODO: Refactoring this method.
    def margin_conversion(self):
        """Method for calculate margin conversion."""
        conversion = 1.0

        conversion *= self.conversion_pairs.get(self.currency + self.symbols_forex[3:], 1)
        conversion *= self.conversion_pairs.get(self.symbols_forex[3:] + self.currency, 1)

        conversion *= self.conversion_pairs.get(self.symbols_forex[:3] + self.symbols_forex[3:], 1)
        conversion *= self.conversion_pairs.get(self.symbols_forex[3:] + self.symbols_forex[:3], 1)

        if self.currency in ["AUD", "CAD", "CHF", "CZK", "DKK", "GBP", "HKD",
                             "HUF", "JPY", "LTL", "MXN", "NOK", "NZD", "PLN",
                             "RUR", "SEK", "SGD", "TRY", "ZAR"]:

            conversion *= self.conversion_pairs.get(self.currency + self.symbols_forex[:3], 1)
            conversion *= self.conversion_pairs.get(self.symbols_forex[:3] + self.currency, 1)

            conversion /= self.conversion_pairs.get(self.currency + self.symbols_forex[3:], 1)
            conversion /= self.conversion_pairs.get(self.symbols_forex[3:] + self.currency, 1)

        if self.currency in ["EUR", "USD", "MAU", "MAG", "MPT", "MPD", "MBA",
                             "MBB", "MBC", "MBD"]:
            conversion /= self.conversion_pairs.get(self.currency + self.symbols_forex[3:], 1)
            conversion /= self.conversion_pairs.get(self.symbols_forex[3:] + self.currency, 1)

            conversion /= self.conversion_pairs.get(self.currency + self.symbols_forex[3:], 1)
            conversion /= self.conversion_pairs.get(self.symbols_forex[3:] + self.currency, 1)

        return conversion

    # TODO: Refactoring this method.
    def profit_conversion(self):
        """Method for calculate profit conversion."""
        conversion = 1.0
        conversion *= self.conversion_pairs.get(self.currency + self.symbols_forex[:3], 1)
        conversion *= self.conversion_pairs.get(self.symbols_forex[3:] + self.currency, 1)

        conversion *= self.conversion_pairs.get(self.symbols_forex[:3] + self.currency, 1)

        conversion /= self.conversion_pairs.get(self.currency + self.symbols_forex[:3], 1)
        conversion /= self.conversion_pairs.get(self.symbols_forex[3:] + self.currency, 1)

        conversion /= self.conversion_pairs.get(self.currency + self.symbols_forex[3:], 1)

        return conversion

    # TODO: Refactoring this method.
    def swap_long_conversion(self):
        """Method for calculate swap long conversion."""
        conversion = 1.0
        conversion *= self.conversion_pairs.get(self.currency + self.symbols_forex[:3], 1)
        conversion *= self.conversion_pairs.get(self.symbols_forex[3:] + self.currency, 1)
        conversion /= self.conversion_pairs.get(self.currency + self.symbols_forex[:3], 1)
        conversion /= self.conversion_pairs.get(self.symbols_forex[3:] + self.currency, 1)

        return conversion

    # TODO: Refactoring this method.
    def swap_short_conversion(self):
        """Method for calculate swap short conversion."""
        conversion = 1.0
        conversion *= self.conversion_pairs.get(self.currency + self.symbols_forex[:3], 1)
        conversion *= self.conversion_pairs.get(self.symbols_forex[3:] + self.currency, 1)
        conversion /= self.conversion_pairs.get(self.currency + self.symbols_forex[:3], 1)
        conversion /= self.conversion_pairs.get(self.symbols_forex[3:] + self.currency, 1)

        return conversion

    def calculate_margin(self):
        """Method for calculate margin."""
        formula = self._format_formula(self.margin_formula2)
        conversion = self.margin_conversion()
        return self._format_margin(decimal.Decimal(formula()) * decimal.Decimal(conversion))

    def calculate_profit(self):
        """Method for calculate profit."""
        formula = self._format_formula(self.profit_formula2)
        conversion = self.profit_conversion()
        return self._format_profit(decimal.Decimal(formula()) * decimal.Decimal(conversion))

    def calculate_swap_long(self):
        """Method for calculate swap long."""
        formula = self._format_formula(self.swap_formula2)
        conversion = self.swap_long_conversion()
        return self._format_swap_long(decimal.Decimal(formula()) * decimal.Decimal(conversion))

    def calculate_swap_short(self):
        """Method for calculate swap short."""
        formula = self._format_formula(self.swap_formula3)
        conversion = self.swap_short_conversion()
        return self._format_swap_short(decimal.Decimal(formula()) * decimal.Decimal(conversion))

    def calculate_volume(self):
        """Method for calculate volume."""
        formula = self._format_formula(self.volume_formula2)
        conversion = get_eurusd_conversion()
        return self._format_volume(
            (decimal.Decimal(formula()) * decimal.Decimal(conversion) / decimal.Decimal(1000000)))

    def __check_margin_text(self):
        """Method for check margin results text."""
        if self.margin:
            if self.__previous != self.margin_formula2:
                self.__previous = self.margin_formula2
                return self.margin.split()[1] == self.currency
            else:
                return self.margin.split()[1] == self.currency
        return False

    def wait_for_results(self):
        """Method for waiting results is visiable."""
        return WebDriverWait(self.driver_manager.driver, 10).until(
            lambda x: self.__check_margin_text(),
            message="Results are not availiable.")

    def calculate_results(self):
        """Method for calculate results."""
        self.calculate.click()
        self.wait_for_results()

    @property
    def expected_results(self):
        """Property to get expected results."""
        return ("{} {}".format(self.calculate_margin(), self.currency))
        # TODO: Not implemented.
        # "{} {}".format(self.calculate_profit(), self.currency),
        # "{} pt. = {} {}".format(self._swap_long_size,
        #                         self.calculate_swap_long(),
        #                         self.currency),
        # "{} pt. = {} {}".format(self._swap_short_size,
        #                         self.calculate_swap_short(),
        #                         self.currency),
        # "{}".format(self.calculate_volume()))

    @property
    def results(self):
        """Property to get results."""
        return (self.margin)
        # TODO: Not implemented.
        # self.profit,
        # self.swap_long,
        # self.swap_short,
        # self.volume)
