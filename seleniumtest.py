

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window() # Modo de tela cheia

driver.get('https://google.com/')