r"""
To RUN test:
    pytest -s test_product_page.py
"""
import pytest

from .pages.product_page import ProductPage


# @pytest.mark.parametrize('promo_offer',
#                          ["0", "1", "2", "3", "4", "5", "6",
#                           pytest.param("7", marks=pytest.mark.xfail(reason='wrong book name after adding to basket')),
#                           "8", "9"])
# def test_guest_can_add_product_to_basket(browser, promo_offer):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
#     page = ProductPage(browser, link)
#     page.open()
#
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#
#     page.product_name_should_match_the_message()
#     page.product_price_should_match_the_message()

@pytest.mark.xfail(reason='Success message will always appear after adding product to basket')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()

    page.add_to_basket()

    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()

    page.should_not_be_success_message()


@pytest.mark.xfail(reason='Success message will not disappear')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()

    page.add_to_basket()

    page.should_success_message_disappear()
