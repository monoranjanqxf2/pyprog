from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.find_element_by_xpath("//a[contains(@class,'_3ko_Ud')]").click()