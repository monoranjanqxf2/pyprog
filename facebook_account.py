from selenium import webdriver
facebook_driver = webdriver.Chrome()
ten_minute = webdriver.Chrome()
print("Connecting facebook...!")
facebook_driver.get('https://www.facebook.com/')
ten_minute.get('https://10minutemail.net/')
if ten_minute.title=='10 Minute Mail' and facebook_driver.title=='Facebook - log in or sign up':
    print("Facebook connected")





# //div[@class='placeholder' and text()='Re-enter email address'] reenter email xpath

facebook_driver.close()
ten_minute.close()