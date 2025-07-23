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

print("Button found. Clicking it.")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(1)
print("Test completed.")

driver.quit()
