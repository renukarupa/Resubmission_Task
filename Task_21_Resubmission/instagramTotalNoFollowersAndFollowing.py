from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open Instagram profile
driver.get("https://www.instagram.com/guvioffical/")

# Wait for followers count to be visible
followers_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '/followers/')]/span"))
)

# Extract total number of followers
followers_count = followers_element.text

# Extract total number of following
following_element = driver.find_element(By.XPATH, "//a[contains(@href, '/following/')]/span")
following_count = following_element.text

# Print the results
print("Followers:", followers_count)
print("Following:", following_count)

# Close the WebDriver
driver.quit()
