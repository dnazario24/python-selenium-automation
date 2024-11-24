from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://amazon.com")

# Find element
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'nav-search-submit-button')

# Find XPATH
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
driver.find_element(By.XPATH, "//input[@role='searchbox']")

# by XPATH, any tag, but with attribute=value
driver.find_element(By.XPATH, "//*[@role='searchbox']")

#by XPATH, by multiple attributes:
driver.find_element(By.XPATH, "//input[@tabindex='0' and @name='field-keywords']")
driver.find_element(By.XPATH, "//input[@tabindex='0' and @name='field-keywords' and @dir='auto']")

# by XPATH, text()
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")

# by XPATH, text() + attr:
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

# by XPATH, partial match
driver.find_element(By.XPATH, "//select[contains(@aria-describedby, 'search')]")