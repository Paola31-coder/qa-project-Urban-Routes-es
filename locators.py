from selenium.webdriver.common.by import By

class Locators:

    # Seleccionar la ruta de destino
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Seleccionar la tarifa comfort
    request_taxi_button = (By.CSS_SELECTOR, ".button.round")
    smart_button = (By.CLASS_NAME, "smart-button")
    comfort_rate = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")

    # Rellenar el campo número de teléfono
    phone_number_field = (By.XPATH, "//div[contains(@class, 'np-button')]//div[text()='Número de teléfono']")
    phone_number_field_input = (By.ID, "phone")
    phone_number_field_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    next_button = (By.XPATH, "//button[text()='Siguiente']")
    code_sms_field = (By.XPATH, "//*[@id='code']")
    confirm_button = (By.XPATH, "//button[text()='Confirmar']")

    #Agregar una tarjeta de credito
    payment_method_field = (By.CSS_SELECTOR, ".pp-button")
    add_card = (By.CSS_SELECTOR, '.pp-plus-container')
    card_number =(By.ID, 'number')
    card_code =(By.NAME, "code")
    add_button =(By.XPATH, "//div[@class='pp-buttons']/button[text()='Agregar']")
    close_button = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")
    payment_method_confirmation = (By.XPATH, "//div[contains(@class, 'pp-value-text') and text()='Tarjeta']")

    # Mensaje para el conductor
    message_for_driver_field = (By.ID, 'comment')

    # Requisito del pedido
    order_requirements = (By.CLASS_NAME, 'reqs-head')
    blanket_and_scarves_slider_checked = (By.XPATH, "//div[contains(@class, 'r-sw-container') and .//div[text()='Manta y pañuelos']]//input[@type='checkbox']")
    blanket_and_scarves_slider = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")
    plus_icecream = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]")
    number_of_ice_creams = (By.XPATH, "//div[text()='Helado']/following::div[contains(@class, 'counter-value')][1]")

    # Pedir un taxi
    order_taxi_button = (By.CLASS_NAME, "smart-button")
    confirmation_message = (By.CSS_SELECTOR, 'div.order-header-title')
