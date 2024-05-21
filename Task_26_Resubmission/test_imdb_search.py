import pytest
from selenium import webdriver
from imdb.imdb_page import IMDbSearchPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Make sure you have the correct WebDriver installed and accessible
    yield driver
    driver.quit()


def test_imdb_search(driver):
    search_page = IMDbSearchPage(driver)
    search_page.load()

    search_page.set_name("Tom")
    search_page.set_birth_month("July")
    search_page.set_birth_day(3)
    search_page.set_birth_year("1980")
    search_page.click_search()

    # Wait for and verify results
    search_page.wait_for_results()
    assert "Name Search Results" in driver.title