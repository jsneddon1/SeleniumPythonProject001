from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument("--headless")

path = "../Drivers/geckodriver.exe"
# driver = webdriver.Firefox(executable_path=path, firefox_options=firefox_options)
driver = webdriver.Firefox(executable_path=path)
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("Automation step by step")
time.sleep(2)
# driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
driver.find_element_by_name("q").send_keys(Keys.RETURN)

time.sleep(2)
print(driver.title)

driver.close()
driver.quit()
