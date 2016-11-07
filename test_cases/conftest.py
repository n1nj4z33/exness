"""Module for test configuration."""
import pytest
from framework.driver_manager import DriverManager


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):  # pylint: disable=unused-argument
    """Method for prepare html report."""
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    driver = DriverManager()
    xfail = hasattr(report, "wasxfail")

    if report.when == "call":
        extra.append(pytest_html.extras.url(driver.instance.current_url))
        if (report.skipped and xfail) or (report.failed and not xfail):
            extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
            screenshot = driver.instance.get_screenshot_as_base64()
            extra.append(pytest_html.extras.image(screenshot, "Screenshot"))
        report.extra = extra
