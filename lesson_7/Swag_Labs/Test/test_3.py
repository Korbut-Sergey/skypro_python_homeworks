from lesson_7.Swag_Labs.Pages.Shopmainpage import Shopmainpage
from lesson_7.Swag_Labs.Pages.Shopcontainer import Shopcontainer


def test_shop(chrome_browser):
    expected_total = "58.29"

    shopmain = Shopmainpage(chrome_browser)
    shopmain.registration_fields()
    shopmain.buy_issue()
    shopmain.click_issue()
    shopmain.into_container()

    container = Shopcontainer(chrome_browser)
    container.checkout()
    container.info()
    container.price()
    assert expected_total in container.price()
    print(f"Итог равен ${container.price()}")