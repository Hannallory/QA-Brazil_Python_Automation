import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Abra uma nova instância do Chrome WebDriver
driver = webdriver.Chrome()

# Abra a URL especificada no navegador
driver.get(" https://cnt-1ed060d2-e8f9-4786-ad6d-591407b2f0d2.containerhub.tripleten-services.com?lng=pt")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(2)

# Encontre o campo de entrada DE e o campo de entrada PARA usando seus IDs
from_field = driver.find_element(By.ID, "from")
to_field = driver.find_element(By.ID, "to")

# Teste o atributo placeholder de cada campo de entrada para garantir que eles estejam exibindo o texto correto
assert from_field.get_attribute('placeholder') == "East 2nd Street, 601"
assert to_field.get_attribute('placeholder') == "1300 1st St"

# Feche o navegador e encerre a sessão do WebDriver
driver.quit()