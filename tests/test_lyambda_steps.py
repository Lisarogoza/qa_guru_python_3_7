import allure
from allure_commons.types import Severity
from allure_commons.types import AttachmentType
from selene.support.shared import browser
from selene.support import by
from selene.support.conditions import be
from selene.support.shared.jquery_style import s

@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "rogozinskaya")
@allure.feature("Проверка наличия задачи в репозитории")
@allure.story("Пример теста с лямбда шагами через with allure.step")
@allure.link("https://github.com", name="Testing")
def test_lyambda_steps():
    with allure.step("Открыть главную страницу"):
        browser.open("https://github.com")
        browser.driver.maximize_window()
    with allure.step("Найти репозиторий"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("eroshenkoam/allure-example")
        s(".header-search-input").submit()
    with allure.step("Перейти по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()
    with allure.step("Открыть таб Issues"):
        s("#issues-tab").click()
    with allure.step("Проверить наличие Issue с номером 69"):
        s(by.partial_text("69")).should(be.visible)
    with allure.step("Сделать скриншот"):
        allure.attach(browser.driver.get_screenshot_as_png(), name="repo_screenshot",
                      attachment_type=AttachmentType.PNG)


browser.quit()
