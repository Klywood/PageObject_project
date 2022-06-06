from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    add_to_basket_button = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    product_name = (By.CSS_SELECTOR, '.product_main h1')
    name_in_message = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div strong')
    product_price = (By.CSS_SELECTOR, '.product_main .price_color')
    price_in_message = (By.CSS_SELECTOR, '#messages :nth-child(3) strong')
