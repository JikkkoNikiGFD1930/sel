from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

# Load the website
driver.get("https://1fichier.com/")

# Wait a little if needed (optional)
driver.implicitly_wait(10)

# Save screenshot
driver.save_screenshot("screenshot.png")

driver.quit()
