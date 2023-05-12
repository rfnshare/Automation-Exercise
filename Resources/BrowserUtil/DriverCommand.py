from Resources.BrowserUtil.Browser import Browser


class DriverCommand:
    """
    This class is used to execute the driver commands.
    """

    webdriver = Browser().get_web_driver()

    def implicitly_wait(self, time):
        """
        This method is used to set the implicit wait time.
        :param time:
        :return:
        """
        self.webdriver.implicitly_wait(time)

    def maximize_windows(self):
        """
        This method is used to maximize the windows.
        :return:
        """
        self.webdriver.maximize_window()

    def close_focused_screen(self):
        """
        This method is used to close the focused screen.
        :return:
        """
        self.webdriver.close()

    def get_current_page_title(self):
        """
        This method is used to get the current page title.
        :return:
        """
        return self.webdriver.title
