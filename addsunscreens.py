'''
Add Sunscreens Programs: 
Add all the sunscreens to a cart of this site https://weathershopper.pythonanywhere.com/sunscreen
----------------------------------
Python 3.7.0 and Selenium 3.141.0
----------------------------------
Author : Monoranjan Mandal
E-mail : sonu.mandal95@gmail.com  

SCOPE:
1. Read item from https://weathershopper.pythonanywhere.com/sunscreen
2. Finding web elements list
3. Iterate the list and telling the browser to click all the buttons 
4. Tell your browser to click on cart button to check the cart items

----variable used----
    driver: to load the webdriver for chrome
    button: stroring a list of all the add button
    item: to iterate through list
    button_cart: stroring selenium object for curt button of web page.
'''

from selenium import webdriver
import time
driver=webdriver.Chrome()
#maximizing web browser
driver.maximize_window()
driver.get('https://weathershopper.pythonanywhere.com/sunscreen')
# Getting a web element list of all add buttons
button=driver.find_elements_by_xpath('//button[contains(@class,"btn btn-primary")]')
# Iterating through list and clicking on each add button of the webpage to add item to cart
for item in button:
    item.click()
# Getting a webelement of cart button
time.sleep(3)
button_cart=driver.find_element_by_xpath("//button[@class='thin-text nav-link']")
#clicking cart button to view result
button_cart.click()
time.sleep(3)
driver.close()