'''
Finding most expensive Moisturizer Programs: 
Add all the moisturizer to a cart of this site https://weathershopper.pythonanywhere.com/moisturizer
----------------------------------
Python 3.7.0 and Selenium 3.141.0
----------------------------------
Author : Monoranjan Mandal
E-mail : sonu.mandal95@gmail.com 

Scope:
1. find all items as object through xpath
2. convert the item into a list
3. find price of each item from the list and store only price in an another list
4. find the maximum price from the list
5. compare the maximum price with each item of the list and store it's position
6. get all item object again and clicking only the positional object

'''

from selenium import webdriver
import time
price_list=[]
item_list=[]
pos_i=pos_j=0
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://weathershopper.pythonanywhere.com/moisturizer')

#finding all item in item list as object
item_list_ob=driver.find_elements_by_xpath("//div[contains(@class,'text-center col-4')]")

duplicate_price_list=item_list_ob
main_item_list=[]
#converting item_list_ob to an 2d String list
for i in item_list_ob:
    item_list.append(i.text.split("\n"))
    main_item_list.append(i.text)
#item list found
actuall_price=[]
#finding only price list
for j in item_list:
    actuall_price.append(int(j[1][-4::]))
#finding maximum price
max_price=max(actuall_price)
#print max price
#print(f"max price :{max_price}") #for debugging purposes
#finding pos of max price item in item list
for i in range(6):
    s=item_list[i][1][-4::]
    if(int(s)==max_price):
        pos_i=i
print("Most expensive Item sucessfully added to cart :")
print(main_item_list[pos_i])
#getting all button object again to click the appropriate button     
button=driver.find_elements_by_xpath('//button[contains(@class,"btn btn-primary")]')
button=button[pos_i]
#button=duplicate_price_list[pos_i]
button.click()
time.sleep(10)
#showing cart
button_cart=driver.find_element_by_xpath("//button[contains(@class,'thin-text nav-link')]")
button_cart.click()
time.sleep(3)
driver.close()
