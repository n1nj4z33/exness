"""Module for calculator api."""
import requests
from collections import namedtuple


FormsData = namedtuple("FormsData", ("cent_available_leverages",
                                     "cent_currencies",
                                     "cent_forex_symbols",
                                     "common_available_leverages",
                                     "common_currencies",
                                     "common_forex_symbols"))

# TODO: Refactoring to pure api manager.

def get_forms_data():
    """Method for get page forms data values.

    :returns: The instance of :class:`FormsData`.
    """
    response = requests.get("https://www.exness.com/api/calculator/forms").json()

    cent_available_leverages = (
        leverage for leverage in response["cent"]["available_leverages"])
    cent_currencies = (
        currency[0] for currency in response["cent"]["currencies"])
    cent_forex_symbols = (
        symbol[0] for symbol in response["cent"]["instruments"]["Forex_Cent"]["symbols"])

    common_available_leverages = (
        leverage for leverage in response["common"]["available_leverages"])
    common_currencies = (
        currency[0] for currency in response["common"]["currencies"])
    common_forex_symbols = (
        symbol[0] for symbol in response["common"]["instruments"]["Forex"]["symbols"])

    return FormsData(cent_available_leverages, cent_currencies, cent_forex_symbols,
                     common_available_leverages, common_currencies, common_forex_symbols)


def get_eurusd_conversion():
    """Method for get EURUSD converison value.

    :returns: The eur/usd converion value.
    """
    params = {"form_type": "common",
              "instrument": "Forex",
              "symbol": "EURUSD",
              "lot": 1,
              "leverage": 100,
              "user_currency": "USD"}
    response = requests.get("https://www.exness.com/api/calculator/calculate", params=params).json()
    return float(response["conversion_pairs"].get("EURUSD"))
