# from selenium import webdriver
from selenium import webdriver
import time
import os

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service




# Tunnukset
username = os.environ["user"]
current_pass = os.environ['loginpassword']

# Must be over 8 chars
wifipass = os.environ["new_pass"]

# Muuta
URL = os.environ["url"]

# Muuta
# chrome_driver_path =os.environ["driver_path"]
# driver = webdriver.Chrome(chrome_driver_path)

s=Service(os.environ["driver_path"])
driver = webdriver.Chrome(service=s)

driver.get(URL)

# Login
try:
    user_input = driver.find_element_by_name("username_login")
    user_input.send_keys(username)
    password_input = driver.find_element_by_name("password_login")
    submit = driver.find_element_by_name("login")
    password_input.send_keys(current_pass)
    submit.click()
except Exception as e:
    print(e.message)
time.sleep(1)

# Set new passwords
try:
    # 2.4 ghz
    new_pass = driver.find_element_by_name("wpa_psk_key")
    new_pass.clear()
    new_pass.send_keys(wifipass)
    # 5 ghz
    new_pass_5ghz = driver.find_element_by_name("wl5g_wpa_psk_key")
    new_pass_5ghz.clear()
    new_pass_5ghz.send_keys(wifipass)
    save = driver.find_element_by_name("save")
    save.click()
except Exception as e:
    print(e.message)

driver.refresh()
time.sleep(5)