import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage

def test_duration_personal_scooter_option():
    driver = webdriver.Chrome()
    driver.get(' https://cnt-dd24b6df-c863-463a-bd62-46f6bb77ebf4.containerhub.tripleten-services.com?lng=pt')

    urban_routes_page = UrbanRoutesPage(driver)

    urban_routes_page.enter_from_location('East 2nd Street, 601')
    urban_routes_page.enter_to_location('1300 1st St')

    urban_routes_page.click_personal_option()
    time.sleep(2)
    urban_routes_page.click_scooter_icon()
    time.sleep(2)

    # Verifique se o texto Duração está sendo exibido corretamente
    actual_value = urban_routes_page.get_duration_text()
    expected_value = "Duração"
    assert expected_value in actual_value, f"Esperado '{expected_value}', mas obtido '{actual_value}'"

    driver.quit()