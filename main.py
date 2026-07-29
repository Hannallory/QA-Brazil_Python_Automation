import data
from pages import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
        cls.driver = webdriver.Chrome()
        # Tempo de espera implícita para evitar falhas de carregamento da página
        cls.driver.implicitly_wait(10)

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        from_value = self.driver.find_element(
            *routes_page.from_field
        ).get_attribute("value")
        assert from_value == data.ADDRESS_FROM

    def test_select_plan(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_call_taxi()
        routes_page.select_comfort_plan()

        comfort_card = self.driver.find_element(
            *routes_page.comfort_tariff_card
        )
        assert "active" in comfort_card.get_attribute("class")

    def test_fill_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_phone_number(data.PHONE_NUMBER)

        phone_button_text = self.driver.find_element(
            *routes_page.phone_button
        ).text
        assert phone_button_text == data.PHONE_NUMBER

    def test_fill_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_credit_card(data.CARD_NUMBER, data.CARD_CODE)

        payment_text = self.driver.find_element(
            *routes_page.payment_method_button
        ).text
        assert "Cartão" in payment_text or "Card" in payment_text

    def test_comment_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_comment(data.MESSAGE_FOR_DRIVER)

        comment_value = self.driver.find_element(
            *routes_page.comment_input
        ).get_attribute("value")
        assert comment_value == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_blanket_and_handkerchiefs()
        assert routes_page.is_blanket_selected() is True

    def test_order_2_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_ice_creams(2)
        assert routes_page.get_ice_cream_count() == "2"

    def test_car_search_modal_appears(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_order_taxi()
        assert routes_page.is_car_search_modal_visible() is True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()