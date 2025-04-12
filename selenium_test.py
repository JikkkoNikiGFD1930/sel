from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get("https://example.com")

# Wait for an element
wait = WebDriverWait(driver, 10)
header = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

print("Header text is:", header.text)

driver.quit()
