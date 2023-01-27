import allure
from allure_commons.types import Severity
from selene.support.shared import browser
from selene.support import by
from selene.support.conditions import be


@allure.tag("web")
@allure.label("owner", "rogozinskaya")
@allure.severity(Severity.NORMAL)
@allure.feature("Проверка наличия задачи в репозитории")
@allure.story("Пример теста Selene, без шагов")
@allure.link("https://github.com", name="Testing")
def test_github_selene():
    browser.open("https://github.com")
    browser.driver.maximize_window()
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys('eroshenkoam/allure-example')
    browser.element('.header-search-input').submit()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text('69')).should(be.visible)


browser.quit()
