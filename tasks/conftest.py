import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose browser language: en, ru, fr, etc."
    )


@pytest.fixture(scope="function")
def browser(request):
    # Получаем язык из командной строки
    user_language = request.config.getoption("--language")

    # Настраиваем опции Chrome
    options = Options()
    options.add_experimental_option('prefs', {
        'intl.accept_languages': user_language
    })

    print(f"\nstart browser for test with language: {user_language}..")
    browser = webdriver.Chrome(options=options)

    yield browser

    print("\nquit browser..")
    browser.quit()