"""Module for calculator tests."""
import time
import pytest

from exnessapi.calculator import get_forms_data
from pageobjects.calculator import CalculatorPage


class TestExnessCalculator(object):
    """Class for exness calculator tests."""

    def setup_class(self):
        """Method for setup test session."""
        self.calculator_page = CalculatorPage() # pylint: disable=attribute-defined-outside-init
        self.calculator_page.open()

    def teardown_class(self):
        """Method for teardown test session."""
        self.calculator_page.close()

    @staticmethod
    def teardown_method():
        """Method for teardown test."""
        time.sleep(3) # ddos protection

    # TODO: Use get_forms_data().common_forex_symbols
    # TODO: Use get_forms_data().common_available_leverages
    @pytest.mark.parametrize("symbols_forex", ["EURUSD"])
    @pytest.mark.parametrize("currency", get_forms_data().common_currencies)
    @pytest.mark.parametrize("leverage", [100])
    @pytest.mark.parametrize("lot", [0.01])
    def test_common_forex(self, symbols_forex, currency, leverage, lot):
        """Test for exness calculator common forex tests."""
        self.calculator_page.account = "common"
        self.calculator_page.instruments = "Forex"
        self.calculator_page.symbols_forex = symbols_forex
        self.calculator_page.currency = currency
        self.calculator_page.leverage = leverage
        self.calculator_page.lot = lot
        self.calculator_page.calculate_results()
        assert self.calculator_page.results == self.calculator_page.expected_results

    # TODO: Use parametrize
    @pytest.mark.skip(reason="Not implemented.")
    def test_common_nymex(self, symbols_forex, currency, leverage, lot):
        """Test for exness calculator common nymex tests."""
        self.calculator_page.account = "common"
        self.calculator_page.instruments = "NYMEX"
        self.calculator_page.symbols_forex = symbols_forex
        self.calculator_page.currency = currency
        self.calculator_page.leverage = leverage
        self.calculator_page.lot = lot
        self.calculator_page.calculate.click()
        assert self.calculator_page.results == self.calculator_page.expected_results

    # TODO: Use parametrize
    @pytest.mark.skip(reason="Not implemented.")
    def test_cent_forex(self, symbols_forex, currency, leverage, lot):
        """Test for exness calculator cent forex tests."""
        self.calculator_page.account = "cent"
        self.calculator_page.instruments = "Forex"
        self.calculator_page.symbols_forex = symbols_forex
        self.calculator_page.currency = currency
        self.calculator_page.leverage = leverage
        self.calculator_page.lot = lot
        self.calculator_page.calculate.click()
        assert self.calculator_page.results == self.calculator_page.expected_results
