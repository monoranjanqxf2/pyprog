'''
Add Moisturizer Programs: 
Add all the moisturizer to a cart of this site https://weathershopper.pythonanywhere.com/moisturizer
----------------------------------
Python 3.7.0 and Selenium 3.141.0
----------------------------------
Author : Monoranjan Mandal
E-mail : sonu.mandal95@gmail.com  

SCOPE:
1. Read item from https://weathershopper.pythonanywhere.com/moisturizer
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
driver.get('https://weathershopper.pythonanywhere.com/moisturizer')
# Getting a web element list of all add buttons
button=driver.find_elements_by_xpath('//button[contains(@class,"btn btn-primary")]')
# Iterating through list and clicking on each add button of the webpage to add item to cart
for item in button:
    item.click()
# Getting a webelement of cart button
time.sleep(3)
button_cart=driver.find_element_by_xpath("//button[contains(@class,'thin-text nav-link')]")
#clicking cart button to view result
button_cart.click()
table=driver.find_element_by_xpath("//table[contains(@class,'table table-striped')]")
#getting number of rows in table
rows=table.find_elements_by_xpath("//tbody/descendant::tr")
#finding number of rows
no_of_row=len(rows)
#check if number of row is 6 or not
if(no_of_row==6):
    print("Test successfull")
else:
    print("Test Failed")
time.sleep(3)
driver.close()