from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IMDbSearchPage:
    URL = "https://www.imdb.com/search/names/"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def set_name(self, name):
        name_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'name'))
        )
        name_field.send_keys(name)

    def set_birth_month(self, month):
        month_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'birth_month'))
        )
        for option in month_dropdown.find_elements(By.TAG_NAME, 'option'):
            if option.text == month:
                option.click()
                break

    def set_birth_day(self, day):
        day_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'birth_day'))
        )
        for option in day_dropdown.find_elements(By.TAG_NAME, 'option'):
            if option.text == str(day):
                option.click()
                break

    def set_birth_year(self, year):
        year_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'birth_year'))
        )
        year_field.send_keys(year)

    def click_search(self):
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Search")]'))
        )
        search_button.click()
