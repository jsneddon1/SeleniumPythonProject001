import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("../Drivers/chromedriver.exe")

driver.set_page_load_timeout(10)

driver.get("https://www.google.com")

driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_name("q").send_keys(Keys.RETURN)
#driver.find_element_by_name("btnK").click()

time.sleep(10)

driver.close()
driver.quit()

print("Test Completed")