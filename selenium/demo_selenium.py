from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")
#to get back
driver.back()
#to forward
driver.forward()
#to refresh
driver.refresh()


#finding elements by id
#element = driver.find_element(By.ID,"content")
element= driver.find_element(By.XPATH,'//*[@id="content"]')


#wait
wait = WebDriverWait(driver,10)
element = wait.until(EC.presence_of_element_located((By.ID, "content")))


#Interactions
element.click()
element.send_keys('nothing')
element.clear()

#screenshort
driver.save_screenshot("demo.png")