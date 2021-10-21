from lib.selenium import Selenium

browser = Selenium.init()

browser.get('https://www.google.com.br/')

print(f"Título da página: {browser.title}")