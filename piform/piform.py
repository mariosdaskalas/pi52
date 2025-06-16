from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException, \
    NoAlertPresentException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print('piform.py')

service = Service('/usr/local/bin/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')
#options.add_argument('--headless')
#options.add_argument('--disable-notifications')
#options.add_argument('--disable-popup-blocking')
#options.add_argument("--no-sandbox")
#options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service=service, options=options)

driver.get(f'http://root.local/?p=1')
#wait = WebDriverWait(driver, 10)

mail = driver.find_element(By.XPATH, '//input[@type="email"]')
mail.send_keys("root@root.com")

textarea = driver.find_element(By.XPATH, '//textarea')
textarea.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

time.sleep(5)