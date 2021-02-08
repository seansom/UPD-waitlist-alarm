# please execute 'pip install selenium' first in terminal to get dependency
# also download webdriver and unzip it to your chosen webdriver_directory
# webdriver download link: https://chromedriver.storage.googleapis.com/index.html?path=88.0.4324.96/

from selenium import webdriver
from getpass import getpass
import sys, os, winsound, time

# set webdriver directory
webdriver_directory = 'C:\\Users\\seansom\\Downloads\\chromedriver'

# set course url
course_url = 'https://crs.upd.edu.ph/student_registration/class_search/1872'


# get user credentials
username = input('Username:\n>')
password = getpass('Password:\n>')


try:
    browser = webdriver.Chrome(webdriver_directory)

except:
    print('Webdriver not found in specified directory. Exiting...')
    sys.exit()


# log-in sequence
browser.get('https://crs.upd.edu.ph/')

while True:
    username_input = browser.find_element_by_id('txt_login')
    password_input = browser.find_element_by_id('pwd_password')

    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.submit()

    if 'Login Error' not in browser.page_source:
        print('Login Successful. Starting search...\n')
        break

    else:
        print('Invalid username or password. Please try again.')
        username = input('Username:\n>')
        password = getpass('Password:\n>')

        time.sleep(2)
        browser.get('https://crs.upd.edu.ph/')


browser.get(course_url)


# initialize counter for checking
check_counter = 0
print(f'check_counter = {check_counter}')


while True:
    if 'OPEN' in browser.page_source:
        browser.quit()
        print('OPEN waitlist detected. Starting alarm...')
        break

    else:
        browser.refresh()
        check_counter += 1
        print(f'check_counter = {check_counter}')
        time.sleep(2)

while True:
    winsound.Beep(2500, 1000)
    time.sleep(2)