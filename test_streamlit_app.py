from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

print("Starting test...")

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the running Streamlit app
driver.get("http://localhost:8501")  # Make sure your app is running

# Wait for a button to appear
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "button"))
)

print("Find Create new item link and click.")
create_pg_link = driver.find_element(By.XPATH, "//*[contains(text(),'Create New Item')]")
create_pg_link.click()

time.sleep(2)
print("Find Home link and click.")
home_pg_link = driver.find_element(By.XPATH, "//*[contains(text(),'Home')]")
home_pg_link.click()

time.sleep(2)

print("Find display inventory link and click.")
display_pg_link = driver.find_element(By.XPATH, "//*[contains(text(),'View Full Inventory')]")
display_pg_link.click()

time.sleep(2)
print("Find Home link and click.")
home_pg_link = driver.find_element(By.XPATH, "//*[contains(text(),'Home')]")
home_pg_link.click()

print("Test completed.")

driver.quit()
