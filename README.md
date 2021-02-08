# UP Diliman CRS Waitlist Alarm Script

A simple Python and Selenium-based program to constantly look for any open waitlists.

- Dependencies: selenium
- Webdriver Download: https://chromedriver.storage.googleapis.com/index.html?path=88.0.4324.96/

- Works by logging in to CRS and constantly refreshing a waitlist URL while checking for an OPEN keyword.
- If an open waitlist is detected, a constant beeping alarm is triggered until program termination.