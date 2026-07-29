import time
from selenium import webdriver
from pages import UrbanRoutesPage


def test_duration_personal_scooter_option():
    driver = webdriver.Chrome()
    driver.get(' https://cnt-5b9d0530-e5e1-4029-bd28-2a5d7539ac5b.containerhub.tripleten-services.com?lng=pt'
               '')

    urban_routes_page = UrbanRoutesPage(driver)

    # Use a etapa "enter_locations" para inserir ambos os locais
    urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')

    urban_routes_page.click_personal_option()
    time.sleep(2)
    urban_routes_page.click_scooter_icon()
    time.sleep(2)

    actual_value = urban_routes_page.get_duration_text()
    expected_value = "Duração"
    assert expected_value in actual_value, f"Esperado '{expected_value}', mas obtido '{actual_value}'"

    driver.quit()