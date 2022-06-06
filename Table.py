import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/html/html_tables.asp")

print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[1]/th[1]').text)

print("Number of row : ", len(driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr')))

print("Number of col : ", len(driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr[1]/th')))
print("Number of col : ", len(driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr[2]/td')))


print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[2]/td[1]').text, end="  ")
print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[2]/td[2]').text, end="  ")
print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[2]/td[3]').text)

print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[3]/td[1]').text, end="  ")
print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[3]/td[2]').text, end="  ")
print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[3]/td[3]').text)


## Assignment  : print all table values with the loop

