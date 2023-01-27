import allure
from allure_commons.types import Severity
from selene.support.shared import browser
from selene.support import by
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "rogozinskaya")
@allure.feature("Проверка наличия задачи в репозитории")
@allure.story("Пример теста с декоратором @allure.step")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps():
    open_main_page()
    find_repo("eroshenkoam/allure-example")
    open_repo("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#45")


@allure.step("Открыть главную страницу")
def open_main_page():
    browser.open("https://github.com")
    browser.driver.maximize_window()


@allure.step("Найти репозиторий")
def find_repo(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def open_repo(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()


browser.quit()
