import data
import helpers
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver
        self.locators = Locators

    def set_from(self, from_address):
        WebDriverWait(self.driver, timeout=10). until(EC.presence_of_element_located(self.locators.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver,timeout=10).until(EC.presence_of_element_located(self.locators.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.locators.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.locators.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_request_taxi_button(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable(self.locators.request_taxi_button))

    def click_on_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_rate(self):
        return self.driver.find_element(*self.locators.comfort_rate)

    def click_on_comfort_rate(self):
        self.get_comfort_rate().click()

    def get_smart_button_shown(self):
        smart_button = WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(self.locators.smart_button))
        return smart_button.is_displayed()

    def set_phone_number(self, phone_number):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.element_to_be_clickable(Locators.phone_number_field)).click()
        wait.until(EC.element_to_be_clickable(Locators.phone_number_field_input)).send_keys(phone_number)
        value = self.driver.find_element(*self.locators.phone_number_field_input).get_property('value')
        wait.until(EC.element_to_be_clickable(Locators.phone_number_field_button)).click()
        phone_code = helpers.retrieve_phone_code(self.driver)
        wait.until(EC.element_to_be_clickable(Locators.code_sms_field)).send_keys(phone_code)
        wait.until(EC.element_to_be_clickable(Locators.confirm_button)).click()
        return value

    def open_payment_method_popup(self):
        WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable(Locators.payment_method_field)).click()

    def click_add_card(self):
        WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable(Locators.add_card)).click()

    def get_card_field(self):
        return WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located(Locators.card_number))

    def set_card_number(self, card_number):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(Locators.card_number)).send_keys(card_number)

    def get_card_code(self):
        return WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located(Locators.card_code))

    def set_code_number(self, code_number):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(Locators.card_code)).send_keys(code_number)

    def click_add_button(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable(Locators.add_button)).click()

    def close_popup_payment_method(self):
        WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable(Locators.close_button)).click()

    def is_card_selected(self):
        return WebDriverWait(self.driver, timeout= 10).until(EC.visibility_of_element_located(Locators.payment_method_confirmation)).is_displayed()

    def set_message_for_driver(self, message):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(Locators.message_for_driver_field)).send_keys(message)

    def get_message_to_the_driver(self):
        return WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located(Locators.message_for_driver_field)).get_attribute("value")

    def click_order_requirements(self):
        WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable(Locators.order_requirements)).click()

    def set_blanket_and_scarves(self):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(Locators.blanket_and_scarves_slider)).click()

    def get_blanket_and_scarves(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(Locators.blanket_and_scarves_slider))

    def blanket_and_scarves_selected(self):
        slider = self.driver.find_elements(*Locators.blanket_and_scarves_slider_checked)
        return slider[0].get_property('checked')

    def set_icecream(self):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(Locators.plus_icecream)).click()
        WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located(Locators.plus_icecream)).click()

    def get_numero_ice_cream(self):
        return int(WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(Locators.number_of_ice_creams)).text.strip())

    def click_order_taxi(self):
        WebDriverWait(self.driver, timeout=20).until(EC.visibility_of_element_located(Locators.order_taxi_button)).click()

    def get_taxi_order_title(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(Locators.confirmation_message)).text.strip()
