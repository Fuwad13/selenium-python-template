from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from config import Config

class BrowserFactory:
    """Factory class to initialize different Browser WebDriver instances."""

    @staticmethod
    def get_driver(browser: str):
        browser = browser.lower()
        if browser == "chrome":
            service = ChromeService(executable_path=Config.CHROMEDRIVER_PATH_LINUX)
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Chrome(service=service, options=options)
        elif browser == "firefox":
            service = FirefoxService(executable_path=Path(__file__).parent / "drivers" / "geckodriver") # TODO : Update the path
            options = FirefoxOptions()
            options.add_argument("--start-maximized")
            return webdriver.Firefox(service=service, options=options)
        elif browser == "edge":
            service = EdgeService(executable_path=Path(__file__).parent / "drivers" / "msedgedriver") # TODO : Update the path
            options = EdgeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Edge(service=service, options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")