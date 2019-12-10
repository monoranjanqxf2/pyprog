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
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://weathershopper.pythonanywhere.com/moisturizer')

#finding all item in item list as object
item_list_ob=driver.find_elements_by_xpath("//div[contains(@class,'text-center col-4')]")
duplicate_price_list=item_list_ob
main_item_list=[]
#converting item_list_ob to an 2d String list
for item in item_list_ob:
    item_list.append(item.text.split("\n"))
    main_item_list.append(item.text)
#item list found
actuall_price=[]
#finding only price list
for item in item_list:
    actuall_price.append(int(item[1][-4::]))
#finding maximum price
max_price=max(actuall_price)
#print max price
#print(f"max price :{max_price}") #for debugging purposes
#finding pos of max price item in item list
for position in range(6):
    s=item_list[position][1][-4::]
    if(int(s)==max_price):
        position_of_item=position
print("Most expensive Item sucessfully added to cart :")
print(main_item_list[position_of_item])
#getting all button object again to click the appropriate button     
button=driver.find_elements_by_xpath('//button[contains(@class,"btn btn-primary")]')
button=button[position_of_item]
#button=duplicate_price_list[pos_i]
button.click()
time.sleep(5)
#showing cart
button_cart=driver.find_element_by_xpath("//button[contains(@class,'thin-text nav-link')]")
button_cart.click()
#checking table items
cart_table=driver.find_element_by_xpath("//table[contains(@class,'table table-striped')]")
#getting number of rows in table
cart_rows=cart_table.find_elements_by_xpath("//tbody/descendant::tr")
#finding number of rows
no_of_row=len(cart_rows)
#spliting main_item_list to get item name
item_name,item_price,add_button_text=main_item_list[position_of_item].split("\n")
#print(item_name_price)
if(no_of_row==1):
    #verifying most expensive item with cart item
    if(item_name+" "+str(max_price)==cart_rows[0].text):
        print("Test Successfull")
    else:
        print("Test Failed")
else:
    print("Test Failed")
time.sleep(3)
driver.close()
