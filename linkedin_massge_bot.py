
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

# PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()
driver.get('https://www.linkedin.com')
time.sleep(2)

username = driver.find_element_by_name('session_key')
password = driver.find_element_by_name('session_password')
username.send_keys('user name....')
password.send_keys('your password...')

time.sleep(3)
submit = driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(3)


import random

n_pages = 3

for n in range(1, n_pages + 1):

    driver.get("https://put your url here" + str(n))
    time.sleep(2)

    all_buttons = driver.find_elements_by_tag_name("button")
    message_buttons = [btn for btn in all_buttons if btn.text == "Message"]

    for i in range(6, 7):
        #clicking on "Message" button
        driver.execute_script("arguments[0].click();", message_buttons[i])
        time.sleep(2)

       
        main_div = driver.find_element_by_xpath("//div[starts-with(@class, 'msg-form__msg-content-container')]")
        driver.execute_script("arguments[0].click();", main_div)

       
        paragraphs = driver.find_elements_by_tag_name("p")
        
        all_span = driver.find_elements_by_tag_name("span")
        all_span = [s for s in all_span if s.get_attribute("aria-hidden") == "true"]

        idx = [*range(3,23,2)]
        all_names = []
        for j in idx:
            name = all_span[j].text.split(" ")[0]
            all_names.append(name)
        message = "Hello " + all_names[i] + "put your massage here...."
        
        paragraphs[-5].send_keys(message)
        time.sleep(2)


        submit = driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)

        close_button = driver.find_element_by_xpath("//button[starts-with(@data-control-name, 'overlay.close_conversation_window')]")
        driver.execute_script("arguments[0].click();", close_button)
        time.sleep(2)
