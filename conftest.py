import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='language for the browser interface')

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {"intl.accept_languages": language})

    # Инициализация драйвера
    
    driver = webdriver.Chrome( options=chrome_options)

    yield driver  # Передаем драйвер в тест
    driver.quit()  # Закрытие драйвера после теста