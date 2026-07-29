from selenium import webdriver
import time
from urban_routes_main_page import UrbanRoutesPage

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_personal_scooter_option(self):
        self.driver.get('https://cnt-8f25f166-edc1-4f8d-b177-7e4079036890.containerhub.tripleten-services.com')
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')
        urban_routes_page.click_personal_option()
        time.sleep(2)
        urban_routes_page.click_scooter_icon()
        time.sleep(2)
        actual_value = urban_routes_page.get_scooter_text()
        expected_value = "Scooter"
        assert expected_value in actual_value, f"Esperado '{expected_value}', mas obtido '{actual_value}'"

    def test_duration_personal_scooter_option(self):
        self.driver.get('https://cnt-dbeabe19-3865-47cd-8da9-085001a9f5ed.containerhub.tripleten-services.com')
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')
        urban_routes_page.click_personal_option()
        time.sleep(2)
        urban_routes_page.click_scooter_icon()
        time.sleep(2)
        actual_value = urban_routes_page.get_duration_text()
        expected_value = "Duração"
        assert expected_value in actual_value, f"Esperado '{expected_value}', mas obtido '{actual_value}'"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()