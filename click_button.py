import time

from selenium.webdriver.common.by import By
from selenium import webdriver

# Abra uma nova instância do Chrome WebDriver
driver = webdriver.Chrome()

# Abra a URL especificada no navegador
driver.get(" https://cnt-b718949f-a943-4767-ab92-4f78af551bdd.containerhub.tripleten-services.com?lng=pt")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(2)

# Encontre o botão usando seu XPath e clique nele
driver.find_element(By.XPATH, "//button[@class='close-button input-close-button']").click()

# Pause a execução por 2 segundos para permitir que você veja os resultados do clique
time.sleep(2)

# Feche o navegador e encerre a sessão do WebDriver
driver.quit()