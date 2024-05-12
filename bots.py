import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"./chromedriver-win64/chromedriver.exe"
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# Configure Chrome options to disable notifications
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

# Initialize Chrome WebDriver with configured options
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.facebook.com")
driver.implicitly_wait(10)

email_element = driver.find_element(By.ID, 'email')
email_element.send_keys(email)

password_element = driver.find_element(By.ID, 'pass')
password_element.send_keys(password)

login_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='royal_login_button']")
login_button.click()

messenger_btn = driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Messenger')]")
messenger_btn.click()

name_element = driver.find_element(By.XPATH, "//span[text()='Mark Jairah Madera']")
name_element.click()

input_name = driver.find_element(By.CLASS_NAME, "x78zum5.x1iyjqo2.xq8finb.x16n37ib.x1xmf6yo.x1e56ztr.xeuugli.x1n2onr6")
input_name.click()

driver.switch_to.active_element.send_keys("This is a real test!")
driver.switch_to.active_element.send_keys(Keys.ENTER)

# input("Press Enter to exit...")

try:
    sent_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Sent')]"))
    )
    print("Message sent successfully!")
except:
    print("Failed to send message or 'Sent' message not found.")

driver.quit()
