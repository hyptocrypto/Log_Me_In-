''' This program uses selenium to automate the login process of two cryptocurrency exchanges, Binacne and Kraken.'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json 
import os
import time

# Open Encrypted Diskimage and Prompt for password
os.system('open path/to/encrypted/diskimage')
# Wait 6 seconds for user to enter password
time.sleep(6)

# Read data from file
with open('path/to/volume/unlocked/from/encrypted/diskimage') as f:
    data = json.load(f)

# Store data as variables     
krak_user = data[0]['Username']
krak_pass = data[0]['Password']
bin_user = data[1]['Username']
bin_pass = data[1]['Password']


# Set up Chrome driver to use the Brave Browser
options = Options()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
driver_path = '/usr/local/bin/chromedriver'


def bin_login():
    

    # Navigate to Binance Login 
    driver.get('https://accounts.binance.com/en/login?return_to=aHR0cHM6Ly93d3cuYmluYW5jZS5jb20vZW4=')
    
    # Find, Click and Fill Username Space
    username_space = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[4]/form/div[1]/div[1]/div/div[1]/div/input')
    username_space.click()
    username_space.send_keys(bin_user)

    # Find, Fill and Click Password Space
    password_space = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[4]/form/div[1]/div[2]/div/div/div/input')
    password_space.click()
    password_space.send_keys(bin_pass)
    
    time.sleep(3)
    
    # Find and Click Login Button
    login_button = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div[4]/form/button')
    login_button.click()


def krak_login():
    # New driver for new window
    
    
    # Navigate to Kraken
    driver2.get('https://www.kraken.com/sign-in?')
    time.sleep(6)
    
    # Find, Click and Fill Username feild 
    username_space = driver2.find_element_by_xpath('//*[@id="react-container"]/div/div[2]/div[2]/div/div[3]/form/div/div/div[2]/div/div/input')
    username_space.click()
    username_space.send_keys(krak_user)
    
    # Find, Click and Fill Password feild
    password_space = driver2.find_element_by_xpath('//*[@id="react-container"]/div/div[2]/div[2]/div/div[3]/form/div/div/div[3]/div/div/input')
    password_space.click()
    password_space.send_keys(krak_pass)

    time.sleep(1)
    
    # Find and Click Login Button
    login_button = driver2.find_element_by_xpath('//*[@id="react-container"]/div/div[2]/div[2]/div/div[3]/form/div/div/div[4]/button')
    login_button.click()
    
    
    



    




    
if __name__ == '__main__': 

    driver = webdriver.Chrome(options = options, executable_path = driver_path)
    bin_login()

    driver2 = webdriver.Chrome(options = options, executable_path = driver_path)
    krak_login()



