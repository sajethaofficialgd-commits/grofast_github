from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# ✅ Launch Chrome using Service (newer Selenium syntax)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 10)

# Step 1: Open SauceDemo site
driver.get("https://www.saucedemo.com/")

# Step 2: Login with valid credentials
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Step 3: Add an item to the cart
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

# Step 4: Open cart and verify the item
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
print(f"🧾 Item in cart: {cart_item}")

# Step 5: Remove the item from the cart
driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
time.sleep(1)  # Short delay to see the effect

# Step 6: Logout
driver.find_element(By.ID, "react-burger-menu-btn").click()
wait.until(EC.presence_of_element_located((By.ID, "logout_sidebar_link")))
driver.find_element(By.ID, "logout_sidebar_link").click()

print("✅ Test completed successfully.")
driver.quit()
