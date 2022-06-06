r"""
To RUN test:
    pytest -s test_product_page.py
"""

from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()

    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page.product_name_should_match_the_message()
    page.product_price_should_match_the_message()
