import allure
from allure_commons.types import Severity
from selene import browser, have


@allure.tag("Web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Valera")
@allure.feature("Issue")
@allure.story("Неавторизованный пользователь")
@allure.link("https://github.com/Deus1986/HW3", name="Testing")
def test_hw_10():
    browser.open("/")
    browser.element("#issues-tab").click()
    browser.element("#issue_1_link").should(have.text("home_work_10"))
