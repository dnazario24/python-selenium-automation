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
driver.maximize_window()

driver.get("https://www.amazon.com")
driver.find_element(By.ID, 'nav-link-accountList-nav-line-1').click()
sleep(3)

driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
driver.find_element(By.XPATH, "//input[@type='email']")
driver.find_element(By.XPATH, "//input[@id='continue']")
sleep(3)

driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-expand']").click()
sleep(10)
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")
driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")
driver.find_element(By.XPATH, "//*[text()='Conditions of Use']")
driver.find_element(By.XPATH, "//*[text()='Privacy Notice']")
sleep(2)


