from pathlib import Path

import pytest
from Resources.BrowserUtil.Browser import Browser

driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = Browser()
    browser.launch_browser()
    browser.maximize_browser()
    browser.go_to_url()
    driver = browser.get_web_driver()
    request.cls.driver = browser.get_web_driver()
    yield
    browser.close_browser()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = (report.nodeid.replace("::", "_")).replace("/", "__") + ".png"
            SS_PATH = Path(__file__).parent.parent / "Reports/Screenshots"
            _capture_screenshot(SS_PATH / file_name)
            if file_name:
                html = (
                    '<div><img src="../../Screenshots/%s" alt="screenshot" style="width:304px;height:228px;" '
                    'onclick="window.open(this.src)" align="right"/></div>' % file_name
                )
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
