"""Module for driver manager."""
import os
from selenium import webdriver


class DriverManager(object):
    """Class for driver manager."""

    _driver = None

    def __new__(cls, *args, **kwargs):
        if not cls._driver:
            cls._driver = super(DriverManager, cls).__new__(cls, *args, **kwargs)
        return cls._driver

    @property
    def driver(self):
        """Property to get driver instance.

        :returns: Instance of :class:`webdriver.Chrome`.
        """
        if not self._driver:
            self.start()
        return self._driver

    def start(self):
        """Method for configure and start driver."""
        options = webdriver.ChromeOptions()
        options.binary_location = os.environ.get("CHROME_PATH")
        options.add_argument("--no-sandbox")
        options.add_argument("--no-default-browser-check")
        options.add_argument("--no-first-run")
        options.add_argument("--disable-default-apps")
        self._driver = webdriver.Chrome(chrome_options=options)
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()
        return self._driver

    def stop(self):
        """Method to stop driver."""
        self._driver.close()
