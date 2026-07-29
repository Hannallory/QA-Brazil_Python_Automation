import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage  # Importar a classe POM

def test_personal_scooter_option():
    # Etapa 1: Abra o aplicativo e atualize a URL após iniciar o servidor
    driver = webdriver.Chrome()
    driver.get(' https://cnt-4fb65bc2-0e8f-4e95-af12-55e56b178faf.containerhub.tripleten-services.com?lng=pt')

    # Crie uma instância da classe de página
    urban_routes_page = UrbanRoutesPage(driver)

    # Etapa 3: use métodos POM para executar ações na página
    # Insira os locais "De" e "Para".
    urban_routes_page.enter_from_location('East 2nd Street, 601')
    urban_routes_page.enter_to_location('1300 1st St')

    # Selecione a opção "Personal".
    urban_routes_page.click_personal_option()
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Clique no ícone "Scooter".
    urban_routes_page.click_scooter_icon()
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 4: Verifique se o texto Scooter é exibido corretamente
    actual_value = urban_routes_page.get_scooter_text()
    expected_value = "Scooter"
    assert expected_value in actual_value, f"Esperado '{expected_value}', mas obtido '{actual_value}'"