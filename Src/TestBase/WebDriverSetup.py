import inspect
from pathlib import Path
import pytest
import logging.config


@pytest.mark.usefixtures("setup")
class WebDriverSetup:
    def get_logger(self):
        file = logging.FileHandler(
            Path(__file__).parent.parent.parent / "Reports/Logs/logfile.log"
        )  # File for log
        formatter = logging.Formatter(
            "%(levelname)s :%(name)s :%(message)s :%(asctime)s",
            datefmt="%Y-%m-%d %I:%M:%S %p",
        )  # Format of log
        file.setFormatter(formatter)  # set formatter into file

        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.addHandler(file)  # adding log into file
        logger.setLevel(logging.INFO)
        return logger

    def take_ss(self, name):
        SS_PATH = Path(__file__).parent / "../../Reports/Screenshots"
        self.driver.get_screenshot_as_file(SS_PATH / name)
