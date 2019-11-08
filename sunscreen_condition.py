'''
Finding least expensive Sunscreen based on condition Programs: 
Found all the Sunscreen item from https://weathershopper.pythonanywhere.com/sunscreen
----------------------------------
Python 3.7.0 and Selenium 3.141.0
----------------------------------
Author : Monoranjan Mandal
E-mail : sonu.mandal95@gmail.com 

Scope:
1. find products name and price through xpath
2. making two different list for item name and their price
3. making list for item containing SPF-30 item containg SPF-50 with price in a different list 
4. finding minimum price of SPF-30 and SPF-50 product and adding them to a cart
5. opening cart and verifing product and printing result

'''

from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()
item_list=[]
price_list=[]
SPF_30=[]
SPF_30_price=[]
SPF_50=[]
SPF_50_price=[]

driver.get("https://weathershopper.pythonanywhere.com/sunscreen")
#getting items and price as object
item_list_ob=driver.find_elements_by_xpath("//div[contains(@class,'text-center col-4')]/p")
#created list for item and list for price
for position,item in enumerate(item_list_ob):
    if(position%2==0):
        item_list.append(item.text)
    else:
        price_list.append(item.text[-4::])    

#making separate list for SPF-30 and SPF-50 items and their price
for position,item in enumerate(item_list):
    if "SPF-30" in item or "spf-30" in item:
        SPF_30.append(item)
        SPF_30_price.append(price_list[position])
    if "SPF-50" in item or "spf-50" in item:
        SPF_50.append(item)
        SPF_50_price.append(price_list[position])
#findind minimum priced SPF-30 and SPF-50 product and storing them in a varible
min_SPF_50_price=min(SPF_50_price)
min_SPF_30_price=min(SPF_30_price)
min_SPF_50_name=SPF_50[SPF_50_price.index(min_SPF_50_price)]
min_SPF_30_name=SPF_30[SPF_30_price.index(min_SPF_30_price)]
#finding button object and clicking appropriate button
button_list=driver.find_elements_by_xpath("//button[contains(@class,'btn btn-primary')]")
for position, item_name in enumerate(item_list):
    if(item_name==min_SPF_50_name):
        button_list[position].click()
    if(item_name==min_SPF_30_name):
        button_list[position].click()
time.sleep(5)
#getting cart button and opening cart by clicking
button_cart=driver.find_element_by_xpath("//button[contains(@class,'thin-text nav-link')]")
#clicking cart button to view result
button_cart.click()
cart_table=driver.find_element_by_xpath("//table[contains(@class,'table table-striped')]")
#getting number of rows in table
cart_rows=cart_table.find_elements_by_xpath("//tbody/descendant::tr")
#finding least moisturizer inside cart 
count=0

for cart_item in cart_rows:
    print(cart_item.text)  #for printing cart items
    if(cart_item.text[:-4:]==min_SPF_50_name):
        count+=1
    if(cart_item.text[:-4:]==min_SPF_50_name):
        count+=1
if(count==len(cart_rows)):
    print("Test Successfull")
else:
    print("Test Failed")
        
time.sleep(3)
driver.close()