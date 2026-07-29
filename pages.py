import time
import helpers
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class UrbanRoutesPage:
    # --- LOCALIZADORES ---
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")

    call_taxi_button = (By.XPATH,
                        '//button[contains(@class, "button") and (contains(., "Pedir um táxi") or contains(@class, "round"))]')
    comfort_tariff_card = (By.XPATH, '//div[text()="Comfort"]/..')

    phone_button = (By.CLASS_NAME, "np-text")
    phone_input = (By.ID, "phone")
    next_phone_button = (By.XPATH, '//button[contains(., "Próximo")]')
    code_input = (By.ID, "code")
    confirm_phone_button = (By.XPATH, '//button[contains(., "Confirmar")]')

    payment_method_button = (By.CLASS_NAME, "pp-text")
    add_card_button = (By.CLASS_NAME, "pp-plus-container")
    card_number_input = (By.ID, "number")
    card_code_input = (By.XPATH, "//div[@class='card-code-input']//input[@id='code']")
    save_card_button = (By.XPATH, "//div[contains(@class, 'pp-buttons')]//button[@type='submit']")
    close_payment_modal = (By.CSS_SELECTOR, ".payment-picker.open .close-button")

    comment_input = (By.ID, "comment")

    blanket_switch = (By.XPATH, '(//span[contains(@class, "slider")])[1]')
    blanket_checkbox = (By.XPATH, '(//input[contains(@class, "r-type-checkbox") or @type="checkbox"])[1]')

    ice_cream_plus = (By.XPATH, '(//div[@class="counter-plus"])[1]')
    ice_cream_value = (By.XPATH, '(//div[@class="counter-value"])[1]')

    smart_button = (By.CLASS_NAME, "smart-button")
    car_search_modal = (By.CLASS_NAME, "order-body")

    def __init__(self, driver):
        self.driver = driver

    # --- MÉTODOS DE AÇÃO ---
    def set_route(self, from_address, to_address):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)
        to_elem = self.driver.find_element(*self.to_field)
        to_elem.send_keys(to_address)
        to_elem.send_keys(Keys.TAB)

    def click_call_taxi(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.call_taxi_button)).click()

    def select_comfort_plan(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.comfort_tariff_card))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(lambda d: "active" in element.get_attribute("class"))

    def set_phone_number(self, phone_number):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.phone_button)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.phone_input)).send_keys(phone_number)
        self.driver.find_element(*self.next_phone_button).click()

        sms_code = helpers.retrieve_phone_code(self.driver)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.code_input)).send_keys(sms_code)
        self.driver.find_element(*self.confirm_phone_button).click()

    def add_credit_card(self, card_number, card_code):
        # Removemos as travas do WebDriverWait. Agora é fluxo direto com pausas fixas.
        time.sleep(1)
        self.driver.find_element(*self.payment_method_button).click()

        time.sleep(1)
        self.driver.find_element(*self.add_card_button).click()

        time.sleep(1)
        self.driver.find_element(*self.card_number_input).send_keys(card_number)

        time.sleep(1)
        cvv_input = self.driver.find_element(*self.card_code_input)
        cvv_input.send_keys(card_code)

        time.sleep(1)
        cvv_input.send_keys(Keys.TAB)

        time.sleep(1)
        self.driver.find_element(*self.save_card_button).click()

        # Pausa longa para garantir o salvamento no servidor
        time.sleep(3)

        self.driver.find_element(*self.close_payment_modal).click()

        # Pausa para a janela fechar e o main.py poder ler o texto em paz
        time.sleep(2)

    def set_comment(self, message):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.comment_input)).send_keys(message)

    def order_blanket_and_handkerchiefs(self):
        checkbox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.blanket_checkbox))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
        if not checkbox.is_selected():
            self.driver.execute_script("arguments[0].click();", checkbox)

    def is_blanket_selected(self):
        return self.driver.find_element(*self.blanket_checkbox).is_selected()

    def add_ice_creams(self, count=2):
        plus_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ice_cream_plus))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", plus_btn)
        for _ in range(count):
            plus_btn.click()

    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ice_cream_value).text

    def click_order_taxi(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.smart_button)).click()

    def is_car_search_modal_visible(self):
        modal = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.car_search_modal))
        return modal.is_displayed()