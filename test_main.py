import data
from selenium import webdriver
from selenium.webdriver import Keys
from methods import UrbanRoutesPage


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    # Prueba configurar la dirección
    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    # Pedir un taxi
    def test_click_order_a_taxi(self):
        self.routes_page.click_on_request_taxi_button()
        assert self.routes_page.get_smart_button_shown()

    # Prueba seleccionar tarifa comfort
    def test_select_comfort_rate(self):
        self.routes_page.get_comfort_rate()
        self.routes_page.click_on_comfort_rate()
        comfort_text = "Comfort"
        comfort_icon = self.routes_page.get_comfort_rate().text
        assert comfort_text in comfort_icon

    # Prueba rellenar el número de teléfono
    def test_set_phone_number(self):
        value = self.routes_page.set_phone_number(data.phone_number)
        assert data.phone_number == value

    # Prueba agregar una tarjeta de credito
    def test_set_payment_method(self):
        self.routes_page.open_payment_method_popup()
        self.routes_page.click_add_card()
        self.routes_page.set_card_number(data.card_number)
        self.routes_page.set_code_number(data.card_code)
        self.routes_page.get_card_code().send_keys(Keys.TAB)
        self.routes_page.click_add_button()
        self.routes_page.close_popup_payment_method()
        assert self.routes_page.is_card_selected()

    # Prueba escribir un mensaje para el controlador
    def test_set_message_for_driver(self):
        self.routes_page.set_message_for_driver(data.message_for_driver)
        assert self.routes_page.get_message_to_the_driver() == data.message_for_driver

    # Prueba pedir una manta y pañuelos
    def test_order_blanket_and_scarves(self):
        self.routes_page.set_blanket_and_scarves()
        assert self.routes_page.blanket_and_scarves_selected()

    # Prueba pedir 2 helados
    def test_order_two_icecreams(self):
        self.routes_page.set_icecream()
        assert self.routes_page.get_numero_ice_cream() == 2

    # Prueba aparece el modal para buscar un taxi.
    def test_click_order_taxi(self):
        self.routes_page.click_order_taxi()
        assert "Buscar automóvil" in self.routes_page.get_taxi_order_title()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()