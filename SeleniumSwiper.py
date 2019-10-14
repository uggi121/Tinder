# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:57:27 2019

@author: Rahul
"""

import pyautogui
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
'''

driver = webdriver.Firefox()
driver.get("views/index.ejs")

username = driver.find_element_by_xpath("//*[@id='user_username']")
username.clear()
username.send_keys("")

password = driver.find_element_by_xpath("//*[@id='user_password']")
password.clear()
password.send_keys("")

pyautogui.press("enter")

time.sleep(2)
classcode = driver.find_element_by_xpath("//*[@id='class_session_id']")
classcode.clear()
classcode.send_keys("hii")
pyautogui.press("enter")
time.sleep(10)
driver.close()
'''
import time

from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Swiper():
    def __init__(self):
        self.driver = webdriver.Firefox()

    def fb_login(self):
        self.driver.get('https://www.facebook.com/')
        a = self.driver.find_element_by_id('email')
        a.send_keys(input('Opened Facebook. Please enter username/email: '))
        b = self.driver.find_element_by_id('pass')
        b.send_keys(getpass(prompt='Username entered. Please enter password: '))
        print("Password entered. Logging in.")
        c = self.driver.find_element_by_id('loginbutton')
        c.click()
        try: #Check whether login was successful by finding the home button
            self.driver.find_element_by_id('u_0_c')
        except:
            return False
        return True

    def tinder_login(self):
        self.driver.get('http://tinder.com')
        time.sleep(5)
        print("Clicking on sign in with Facebook.")
        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[2]/div[1]/div/div[3]/button[1]/span").click();
        time.sleep(2)
        try: #Selenium scripts open a testing environment in chrome. Every login acts like a brand new login. Must click through tutorial
            print("Dismissing tutorial prompts")
            self.driver.find_element_by_xpath("//*[@id=\"content\"]/div/span/div/div[2]/div/div[1]/div[1]/div/button/span/span").click()
            print("Prompt 1")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@id=\"content\"]/div/span/div/div[2]/div/div/main/div/button/span/span").click()
            print("Prompt 2")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@id=\"content\"]/div/span/div/div[2]/div/div/div[1]/div/div/div[4]/button[1]/span/span").click()
            print("Prompt 3")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@id=\"content\"]/div/span/div/div[2]/div/div/div[1]/div/div/div[4]/button[1]/span/span").click()
            print ("Prompt 4")
        except:
            print('Something went wrong during login.')
            return False
        print("Ready to start swiping.")
        return True

    def swipe_tinder(self):
        actions = ActionChains(self.driver)
        time.sleep(5)
        print("Swipe until there are no more profiles.")
        try:
            #Stop swiping by catching the exception of not finding a profile. closes browser
            while self.driver.find_element_by_xpath("//*[@id=\"content\"]/div/span/div/div[1]/div/main/div/div/div/div[1]/div[1]/div/div[3]/div[1]"):
                actions.send_keys(Keys.ARROW_RIGHT).perform()
                time.sleep(2)
        except:
            print("No more profiles found. Quitting.")
            self.driver.quit()

if __name__ == "__main__":
    swiper = Swiper()
    if(swiper.fb_login()):
        if swiper.tinder_login():
            swiper.swipe_tinder()
    else:
        print("Facebook login failed, Quitting")
        swiper.driver.quit()