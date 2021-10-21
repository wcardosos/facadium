from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Selenium:
    @staticmethod
    def init() -> webdriver.Chrome:
        options_chrome = Options()
        options_chrome.add_argument('--headless')
        options_chrome.add_argument('--no-sandbox')
        options_chrome.add_argument('--single-process')
        options_chrome.add_argument('--disable-dev-shm-usage')

        return webdriver.Chrome(options=options_chrome)