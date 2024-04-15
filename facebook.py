import time

from selenium import webdriver
from selenium.common import NoAlertPresentException
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()

driver.find_element(By.ID, "email").send_keys("johncena92424@gmail.com")
driver.find_element(By.ID, "pass").send_keys("Loki@9606")

driver.find_element(By.XPATH, "//button[.='Log in']").click()
time.sleep(50)

# driver.switch_to.alert.dismiss()
# popup_window = driver.switch_to.window(driver.window_handles[-1])
# # Close the popup window
# popup_window.close()
# # Switch back to the main window
# driver.switch_to.window(driver.window_handles[0])
# try:
#     alert = driver.switch_to.alert
#     # Dismiss the alert
#     alert.dismiss()
#     print("Alert dismissed successfully.")
# except NoAlertPresentException:
#     print("No alert found.")
# driver.switch_to.alert.dismiss()
time.sleep(10)

# time.sleep(20)
a = driver.find_element(By.XPATH, "//div[@class='xg87l8a x1iymm2a']").text
time.sleep(20)
print(a)
# driver.find_element(By.XPATH, "//a[.='Create new account']").click()
# try:
#
#     a = driver.find_element(By.XPATH, "//span[@class='_akzt']").text
# except NoSuchElementException:
#     a = driver.find_element(By.CLASS_NAME, "_9axz").text
# print(a)
# time.sleep(10)
