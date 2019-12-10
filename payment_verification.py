'''
Finding least expensive Moisturizer based on condition Programs: 
Found all the moisturizer item from https://weathershopper.pythonanywhere.com/moisturizer
----------------------------------
Python 3.7.0 and Selenium 3.141.0
----------------------------------
Author : Monoranjan Mandal
E-mail : sonu.mandal95@gmail.com 

Scope:
1. find products name and price through xpath
2. making two different list for item name and their price
3. making list for item containing aloe item containg almond with price in a different list 
4. finding minimum price of aloe and almond product and adding them to a cart
5. opening cart and verifing product and printing result

'''
import selenium
from selenium import webdriver
#from selenium.webdriver.common.by import By
import time
import random
import random_emailid
card_driver=webdriver.Chrome()
driver=webdriver.Chrome()
driver.maximize_window()
item_list=[]
price_list=[]
aloe=[]
aloe_price=[]
almond=[]
almond_price=[]
card_numbers=[]
card_driver.get('https://stripe.com/docs/testing#cards')
driver.get("https://weathershopper.pythonanywhere.com/moisturizer")
#getting items and price as object
item_list_ob=driver.find_elements_by_xpath("//div[contains(@class,'text-center col-4')]/p")
#created list for item and list for price
time.sleep(3)
for position,item in enumerate(item_list_ob):
    if(position%2==0):
        item_list.append(item.text)
    else:
        price_list.append(item.text[-4::])    

#making separate list for aloe and almond items and their price
for position,item in enumerate(item_list):
    if "Aloe" in item:
        aloe.append(item)
        aloe_price.append(price_list[position])
    if "Almond" in item:
        almond.append(item)
        almond_price.append(price_list[position])
#findind minimum priced aloe and almond product and storing them in a varible
min_almond_price=min(almond_price)
min_aloe_price=min(aloe_price)
min_almond_name=almond[almond_price.index(min_almond_price)]
min_aloe_name=aloe[aloe_price.index(min_aloe_price)]
#finding button object and clicking appropriate button
button_list=driver.find_elements_by_xpath("//button[contains(@class,'btn btn-primary')]")
for position, item_name in enumerate(item_list):
    if(item_name==min_almond_name):
        button_list[position].click()
    if(item_name==min_aloe_name):
        button_list[position].click()
time.sleep(3)
#getting cart button and opening cart by clicking
button_cart=driver.find_element_by_xpath("//button[contains(@class,'thin-text nav-link')]")
time.sleep(3)
#clicking cart button to view result
button_cart.click()
cart_table=driver.find_element_by_xpath("//table[contains(@class,'table table-striped')]")
#getting number of rows in table
time.sleep(3)
cart_rows=cart_table.find_elements_by_xpath("//tbody/descendant::tr")
#finding least moisturizer inside cart 
count=0

for cart_item in cart_rows:
    print(cart_item.text)  #for printing cart items
    if(cart_item.text[:-4:]==min_almond_name):
        count+=1
    if(cart_item.text[:-4:]==min_almond_name):
        count+=1
if(count==len(cart_rows)):
    print("Test Successfull")
else:
    print("Test Failed")
        

'''
Payment verification code starts here

'''
payment_button=driver.find_element_by_xpath("//button[contains(@type,'submit')]")
payment_button.click()

#Opening test mode to get all the card numbers
card_driver.get('https://stripe.com/docs/testing#cards')
#getting all card numbers
card_list=card_driver.find_elements_by_xpath("//td[contains(@class,'card-number')]")
#closing the web page
#time.sleep(5)
for card_num in card_list:
    card_numbers.append(card_num.text)

#print(card_numbers)

random_card_num=random.randint(1,10)
print(f'card number : {card_numbers[random_card_num]}')

#switching to frame
iframe=driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(iframe)

#filling mail id, card details, clicking on remeber me buttons and filling phone number
driver.find_element_by_xpath("//input[contains(@type,'email')]").send_keys(random_emailid.generate_random_emails())
driver.find_element_by_xpath("//input[contains(@type,'tel')]").send_keys(card_numbers[random_card_num])
driver.find_element_by_xpath("//input[contains(@placeholder,'MM / YY')]").send_keys('02/22')
driver.find_element_by_xpath("//input[contains(@placeholder,'CVC')]").send_keys('123')
#checking wether zip code is needed or not
try:
    zip_code=driver.find_element_by_xpath("//input[contains(@placeholder,'ZIP Code')]")
    zip_code.send_keys('123456')
except selenium.common.exceptions.NoSuchElementException as e:
    print('No zip code needed')
driver.find_element_by_xpath("//div[contains(@class,'Checkbox-tick')]").click()
driver.find_element_by_xpath("//input[contains(@autocomplete,'mobile tel')]").send_keys('9211420420')
driver.find_element_by_xpath("//button[contains(@type,'submit')]").click()
#refreshing the page
time.sleep(10)
result=driver.find_element_by_xpath("//h2")
print(f'test result : {result.text}')
card_driver.close()
driver.close()