#USES PYTHON3

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

driver1 = webdriver.PhantomJS()
driver2 = webdriver.PhantomJS()

driver1.get("http://www.cleverbot.com/")
element1 = driver1.find_element_by_name("stimulus")

driver2.get("http://www.cleverbot.com/")
element2 = driver2.find_element_by_name("stimulus")

print(" ")
print("CTRL+C to exit the app")
print(" ")

nb = input('Verge the conversation on: ')

while True:
    print(" ")
    element1.send_keys(nb, Keys.ENTER)

    time.sleep(5)
    
    response1 = driver1.find_element_by_xpath("//*[@id='line1']/span[1]")
    print('1-> '+response1.text)
    print(" ")

    element2.send_keys(response1.text, Keys.ENTER)

    time.sleep(5)
    
    response2 = driver2.find_element_by_xpath("//*[@id='line1']/span[1]")
    print('2-> '+response2.text)
    print(" ")
    
    nb = response2.text


driver1.close()
driver2.close()
