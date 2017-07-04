#Project Sagiri - A Personal Exercise on Web Automation using Pyautogui and Selenium
#Coded by Mark Nolledo
#Credits to Marvin Bruno Jr. and John Michael Dharma for their repos, tips, and inspiration.

import pyautogui, sys
import xml.etree.ElementTree
from selenium import webdriver

#Open browser and navigate to specified website
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.facebook.com")

#Read the XML key file where the credentials are stored.
readFile = xml.etree.ElementTree.parse('fb_key.xml').getroot()
username = readFile.findtext('username')
password = readFile.findtext('password')

#Find the specific elements required for the login.
usernameTextBox = browser.find_element_by_id('email')
passwordTextBox = browser.find_element_by_id('pass')

#Send the credentials to the specified input elements.
usernameTextBox.send_keys(username)
passwordTextBox.send_keys(password)

#Simulate click on the login button
browser.find_element_by_id('u_0_r').click()

#FOR 2-STEP LOGIN MODE
if browser.current_url == 'https://web.facebook.com/checkpoint/?next':
    browser.find_element_by_id('u_0_3').click()
    browser.find_element_by_id('u_0_7').click()

#Click Never on Save Password
pyautogui.click(x=1239, y=204)

#Find Update Status Textbox and post a status
browser.implicitly_wait(5)
statusBox = browser.find_element_by_tag_name('textarea')
status = 'HELLO WORLD! This is a status posted using selenium-python! #Awesomeness #WebAutomation #TrialAndError'
statusBox.send_keys(status)
statusBox.submit()

sys.exit()
