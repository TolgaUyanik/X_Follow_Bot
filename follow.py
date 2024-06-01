from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random 


URL = "https://x.com/i/flow/login"
#Enter here your account information.
UserName = "Your User Name"
Password = "Your Password"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
time.sleep(random.uniform(3.0, 6.0))
username = driver.find_element(by=By.NAME, value="text")

username.send_keys(UserName)
next_button = driver.find_element(by=By.XPATH, value = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span")
time.sleep(random.uniform(3.0, 6.0))
next_button.click()
time.sleep(random.uniform(3.0, 6.0))
password = driver.find_element(by=By.NAME, value="password")
password.send_keys(Password)
time.sleep(random.uniform(3.0, 6.0))
log_in_button = driver.find_element(by=By.XPATH, value= "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/button/div/span/span")
log_in_button.click()
time.sleep(random.uniform(6.0, 9.0))
#enter here the account following address
driver.get("https://x.com/thedankoe/following")
time.sleep(random.uniform(3.0, 6.0))

#Check the follower count and update it. 
for i in range(1,20):
    print(i)
    selector = f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[{i}]/div/div/button/div/div[2]/div[1]/div[2]/button/div/span/span"
    follow_button = driver.find_element(by=By.XPATH,  value = selector)
    follow_button.click()
    time.sleep(random.uniform(3.0, 6.0))
