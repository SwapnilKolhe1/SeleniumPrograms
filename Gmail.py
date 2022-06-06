from selenium import webdriver

Driver = webdriver.Chrome()
# Driver.get("https://accounts.google.com/")
#
# inputEmail = Driver.find_element_by_id("identifierId")
# inputEmail.send_keys("snilkolhe27@gmail.com")
#
# inputNext = Driver.find_element_by_id("identifierNext").click()


##-------------------------------------------------------

Driver.get("https://mail.rediff.com/")

rediffmailButton = Driver.find_elements_by_class_name("mailicon")
rediffmailButton.click()

