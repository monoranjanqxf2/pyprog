"""
Weather Shopper Program
Author : Monoranjan Mandal
E-mail : sonu.mandal95@gmail.com 
Getting temperature from https://weathershopper.pythonanywhere.com/ 

SCOPE:
1. Read temperature from https://weathershopper.pythonanywhere.com/
2. Check If temperature is less than 19 follow step 3 or follow step 4
3. Tell your browser to click on buy moisturizer button 
4. Tell your browser to click on buy sunscreens button

----variable used----
    driver: to load the webdriver for chrome
    temp_from_api: to get the temperature
    button: stroring pselenium object for buy button


"""

from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('https://weathershopper.pythonanywhere.com/')

#getting the selenium object by xpath
temp_from_api=driver.find_element_by_xpath("//span[contains(@id,'temperature')]") 

#Converting slicing the string to remove degree celciousand converting temperature into int 
temp_from_api=int(temp_from_api.text[0:2])

#print(f"Temperature is :{temp_from_api}") #use this print statement only for debuggin purpose
time.sleep(2)
#Checking temperature value is less than 19 or not
if temp_from_api<19:
    #getting the selenium object by xpath
    button=driver.find_element_by_xpath("//button[text()='Buy moisturizers']")
    #Checking whether the page is opened or not and displaying result.
    if(button!=None):
        print(f"Result : {button.text} page Successfully opened")
        button.click()
    else:
        print(f"Result : {button.text} page failed to epen")
else:
    #getting the selenium object by xpath
    button=driver.find_element_by_xpath("//button[text()='Buy sunscreens']")
    #Checking whether the page is opened or not and displaying result.
    if(button!=None):
        print(f"Result : {button.text} page Successfully opened")
        button.click()
    else:
        print(f"Result : {button.text} page failed to epen")

time.sleep(2)
driver.close()