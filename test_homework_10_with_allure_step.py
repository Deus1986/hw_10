import allure
from allure_commons.types import Severity
from selene import browser, have


@allure.tag("Web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "Volodya", "Semen")
@allure.feature("killer feature")
@allure.story("Неавторизованный пользователь")
@allure.link("https://github.com/Deus1986/HW3", name="Testing")
def test_hw_10_with_allure_step():
    with allure.step("Открыть браузер"):
        browser.open("/")

    with allure.step("Нажать на Issue"):
        browser.element("#issues-tab").click()

    with allure.step("Проверить, что значение issue содержит текст 'home_work_10'"):
        browser.element("#issue_1_link").should(have.text("home_work_10"))
