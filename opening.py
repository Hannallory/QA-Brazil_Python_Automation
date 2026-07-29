import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
# Abra a página (lembre-se, o link é exclusivo a cada sessão)
driver.get("https://cnt-58f226c9-c4cf-45ff-bc0e-36185cc797fa.containerhub.tripleten-services.com/")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(2)

# Para encontrar um elemento, retorna um elemento único
driver.find_element(By.CSS_SELECTOR, "img.logo-image")

# Para encontrar um grupo de elementos, retorna mais de um elemento
driver.find_elements(By.CSS_SELECTOR, ".mode")

# Feche o navegador e encerre a sessão do WebDriver
driver.quit()

element = driver.find_element(By.CSS_SELECTOR, "img.logo-image")
print(element)