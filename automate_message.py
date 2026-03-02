from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com")

print("Scan QR Code...")

# Wait for WhatsApp login
WebDriverWait(driver, 120).until(
    EC.presence_of_element_located((By.ID, "pane-side"))
)

print("Logged in!")

name = "Harsh Sogra"
msg = "Sorry"

# Search box
search = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
)

search.click()
search.send_keys(name)
time.sleep(2)
search.send_keys(Keys.ENTER)

while True:
    box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    box.send_keys(msg)
    box.send_keys(Keys.ENTER)

    print("Message sent")
    time.sleep(60)

input("Press ENTER to exit...")