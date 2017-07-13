#!/Users/david/anaconda/bin/python3
# -*- coding: utf-8 -*-

__appname__ = "Gym Class Booking"
__author__ = "David Brough"
__version__ = "0.1.0"
__license__ = "GNU GPL 3.0"

from selenium import webdriver
import credentials

email = credentials.login['email']
password = credentials.login['password']

''' Open browser and navigate to login page '''
browser = webdriver.Chrome()
browser.get('https://www.thegymgroup.com/login/')


''' Input email and password into fields and submit '''
emailElem = browser.find_element_by_id('tx_gym_auth_pi_email_3362')
emailElem.send_keys(str(email))
passwordElem = browser.find_element_by_id('tx_gym_auth_pi_password_3362')
passwordElem.send_keys(str(password))
passwordElem.submit()

''' Navigate to the classes page for Sheffield '''
browser.get('https://www.thegymgroup.com/classes/')
cityElem = browser.find_element_by_partial_link_text('Sheffield')
cityElem.click()

# if __name__ == "__main__":
#     # execute only if run as a script
#     main()
