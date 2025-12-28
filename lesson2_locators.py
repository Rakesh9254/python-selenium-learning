from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

print("Page Loaded")

wait = WebDriverWait(driver, 10)

# 1️⃣ Wait for username field
username = wait.until(
    EC.presence_of_element_located((By.NAME, "username"))
)
username.send_keys("Admin")

# 2️⃣ Wait for password field
password = wait.until(
    EC.presence_of_element_located((By.NAME, "password"))
)
password.send_keys("admin123")

# 3️⃣ Wait for login button
login_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
login_btn.click()

print("Login button clicked successfully")
wait()

driver.quit()
