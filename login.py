from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#for using in chrome. Here I am not writing executable path because i have copied and pasted the exe file inside python folder in C drive
#driver = webdriver.Chrome()


#this line of code is written so that browser doesnot open up and everything is done under the hood
chrome_options = Options()
chrome_options.add_argument("--headless")

#for using in chrome
driver = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options)

#driver variable is responsible for establishing a connection between selenium and chrome
driver.get('https://quotes.toscrape.com/')

time.sleep(2)

driver.find_element_by_css_selector('.header-box .col-md-4 p a').click()
username = driver.find_element_by_css_selector('#username')
password = driver.find_element_by_css_selector('#password')
time.sleep(3)
username.send_keys('abc')
time.sleep(3)
password.send_keys('123456')
time.sleep(3)
driver.find_element_by_css_selector('[value="Login"]').click()
time.sleep(3)

div = driver.find_elements_by_css_selector('.quote')
for info in div:
    quote = info.find_element_by_css_selector('.text').text
    author = info.find_element_by_css_selector('.author').text
    print(quote,author)
    for tag in info.find_elements_by_css_selector('.tag'):
        print(tag.text)
    
    print('-------------------------------')

driver.find_element_by_css_selector('.header-box p a').click()
time.sleep(3)

driver.quit()

