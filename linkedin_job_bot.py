from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import pandas as pd
import wget

# logic of login..
# PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()
driver.get('https://www.linkedin.com')
time.sleep(2)

username = driver.find_element_by_name('session_key')
password = driver.find_element_by_name('session_password')
username.send_keys('enter your id password')
password.send_keys('password')

time.sleep(3)
submit = driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(3)
# for a bug   
# submit1 = driver.find_element_by_xpath("//button[@type='button']").click()
main_list  = []

#  data fatching with selenium
ccc = 0
for x in range(0,15):
    ccc = ccc + 25
    print(ccc)
    driver.get('https://www.linkedin.com/jobs/search/?geoId=102713980&keywords=developer&location=india&start='+str(ccc))
    time.sleep(2)

    # main_item  = driver.find_elements_by_xpath("//div[starts-with(@class,'job-card-container')]")
    try:
        main_item = driver.find_elements_by_css_selector(".base-search-card__title")
    except:
        pass
    try:
        sub_item = driver.find_elements_by_css_selector(".base-search-card__subtitle")
    except:
        pass
    try:
        location  = driver.find_elements_by_css_selector('.job-search-card__location')
    except:
        pass
    try:
        hireing = driver.find_elements_by_css_selector('.result-benefits__text')
    except:
        pass
    # print(len(main_item))
    # print(main)
    for z in range(0,len(main_item)):
        try:
            name = main_item[z].text
        except:
            name = ""
        try:
            sub_name = sub_item[z].text
        except:
            sub_name = ""
        try:
            location_name = location[z].text
        except:
            location_name = ""
        try:
            hireing_name = hireing[z].text
        except:
            hireing_name = ""
        main_dir ={
            'name':name,
            'sub_name':sub_name,
            'location':location_name,
            'hireing':hireing_name
        }
        main_list.append(main_dir)
        print(main_dir)

df = pd.DataFrame(main_list)
df.to_csv('data1.csv',index = False)

driver.quit()
