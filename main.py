import time

from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.zoho.com/in/inventory/inventory-software-demo/#/home/inventory-dashboard")
driver.maximize_window()
# driver.find_element(By.XPATH, "//div/a[@class='zgh-login']").click()
# driver.find_element(By.XPATH, "//input[@id='login_id']").send_keys("lokeshm.bly@gmail.com")
# driver.find_element(By.ID, "nextbtn").click()
# time.sleep(5)
# # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys(
# # "Loki@9606")
# driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Loki@9606")
# driver.find_element(By.ID, "nextbtn").click()
# time.sleep(10)
# driver.find_element(By.XPATH, "//div[contains(text(),'Skip for now')]").click()
time.sleep(10)
driver.find_element(By.ID, "ember89").click()
driver.find_element(By.ID, "ember93").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
time.sleep(3)
driver.find_element(By.ID, "ember407").send_keys("Curtain")
# Select(driver.find_element(By.ID, "ember411")).select_by_visible_text("UNITS")
driver.find_element(By.ID, "ember411").send_keys("UNITS")
driver.find_element(By.ID, "ember411").click()
time.sleep(3)
# driver.find_element(By.XPATH, "//div[@class='col-lg-8']/div[@class='input-group']/input[
# @id='ember971']").send_keys("125")
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[2]/form[1]/div[3]/div[2]/div["
                              "1]/div[2]/div[1]/div[1]/input[1]").send_keys("125")
driver.find_element(By.XPATH,
                    "/html[1]/body[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[2]/form[1]/div[3]/div[2]/div[2]/div["
                    "2]/div[1]/div[1]/input[1]").send_keys(
"100")
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[2]/form[1]/div[4]/div["
                              "1]/button[1]").click()
# action = ActionChains(driver)
# action.scroll_to_element(driver.find_element(By.ID, "ember566")).perform()
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# action.scroll_by_amount(1, 100)
# driver.find_element(By.ID, "ember566").send_keys("125")
# action = ActionChains(driver)
# action.scroll_to_element(driver.find_element(By.ID, "ember407")).perform()
# action.scroll_to_element(driver.find_element(By.XPATH, "//input[@id='ember570']")).perform()
# driver.find_element(By.XPATH, "//input[@id='ember570']").send_keys("125")
# action = ActionChains(driver)
# action.move_to_element(element).send_keys("125")
# driver.find_element(By.ID, "ember566").
# driver.find_element(By.ID, "ember570").send_keys("100")
time.sleep(10)
# driver.find_element(By.XPATH, "//div[@class='auto-select ac-selected']/input").send_keys("UNITS")
# driver.find_element(By.XPATH, "//div[@class='auto-select ac-selected']/input").click()
# # driver.find_element(By.XPATH, "//input[@id='ember645']").send_keys("125")
# # driver.find_element(By.XPATH, "//input[@id='ember649']").send_keys("100")
# Select(driver.find_element(By.XPATH, "//span[.='Inventory Asset']")).select_by_value("Inventory Asset")
# time.sleep(10)
# driver.get("https://www.zoho.com/in/inventory/inventory-software-demo/#/inventory/items")
# driver.maximize_window()
# driver.find_element(By.ID, "ember94").click()
# time.sleep(1)
# driver.find_element(By.XPATH, "//div[@class='form-group']/input").send_keys("Curtain")
# driver.find_element(By.XPATH, "//div[@class='auto-select ac-selected']/input").send_keys("UNITS")
# driver.find_element(By.XPATH, "//div[@class='auto-select ac-selected']/input").click()
# time.sleep(10)
# driver.find_element(By.XPATH, "//div[@class='input-group']/input[@id='ember242']").send_keys("125")
# time.sleep(15)
# driver.find_element(By.XPATH, "//div/input[@id='ember242']").send_keys("125")
# driver.find_element(By.XPATH, "//div[@class='dimension-fields']/span/input[@id = 'ember6756']").send_keys(1)
# driver.find_element(By.XPATH, "//div/span[@class='dimension-input'][1]").send_keys("1")
# time.sleep(10)
# driver.find_element(By.XPATH, "//div/span[@class='dimension-input'][2]").send_keys("1")
# driver.find_element(By.XPATH, "//div/span[@class='dimension-input'][3]").send_keys("1")
# driver.find_element(By.XPATH, "//div/span[@class='dimension-input']/input[@id='ember6758']").send_keys(1)
# time.sleep(10)
##################
# items = driver.find_elements(By.XPATH, "//div[@class='table-responsive overflow-initial  ']/table[1]/tbody[1]/tr")
# for i in items:
#     try:
#         j = i.find_element(By.XPATH, "td/div[2]/a")
#         if j.text == "Area Rug":
#             j.click()
#             break
#     except NoSuchElementException:
#         print("Element not found in this row")
# time.sleep(1)
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[3]/ul[1]/li[2]/a[1]")))
# driver.find_element(By.XPATH, "//div[3]/ul[1]/li[2]/a[1]").click()
# a = driver.find_elements(By.XPATH, "//div[@class='fill-container']/table/tbody/tr")
# print(a)
# for k in a:
#     print(k.text)
# # WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.c))
# driver.find_element(By.XPATH, "//div/button[@class='btn btn-secondary']").click()
# driver.find_element(By.ID, "ember3699").send_keys(1020.00)
# time.sleep(20)

#  @forgot_password
#  Scenario Outline: Reset Password Functionality
#    When the user clicks on the "Forgot Password" link
#    Then the system should successfully navigate to the password reset page and display a "<message>"
#    Examples:
#      |message                                                                    |
#      |Please enter your email address or mobile number to search for your account|
#
#  @signup
#  Scenario Outline: Sign Up Functionality
#    When the user clicks on the "Sign Up" link
#    Then the system should successfully navigate to the sign-up page and verify a "<message>"
#    Examples:
#      |message         |
#      |Sign Up         |
#
#