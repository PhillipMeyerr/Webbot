

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

#Link to the drivers for updated versions https://sites.google.com/chromium.org/driver/

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

#Wait for the page to load for language selection
time.sleep(3)

#Select the language
def select_language():
    select_lang = driver.find_element(By.ID, "langSelect-EN")
    select_lang.click()

select_language()

#Wait for the page to load for the game to start
time.sleep(2)


big_cookie = "bigCookie"
cookies_id = "cookies"
product_prefix = "product"

big_cookie = driver.find_element(By.ID, big_cookie)
    

for i in range(50):
    big_cookie.click()

class Product:
    def __init__(self, id,price,name):
        self.id = id
        self.price = price
        self.name = name
        pass
        
    def buy(self):
        print(str(self.id))
        product = driver.find_element(By.ID, product_prefix + str(self.id))
        product.click()
        pass

time.sleep(2)


# Define the products to buy
Product0 = Product(0,15,"Cursor")
Product1 = Product(1,100,"Grandma")
Product2 = Product(2,500,"Farm")
Product3 = Product(3,3000,"Mine")
Product4 = Product(4,10000,"Factory")
Product5 = Product(5,40000,"Bank")
Product6 = Product(6,200000,"Temple")
Product7 = Product(7,1666666,"Wizard Tower")
Product8 = Product(8,123456789,"Shipment")
Product9 = Product(9,3999999999,"Alchemy Lab")
Product10 = Product(10,75000000000,"Portal")
Product11 = Product(11,1000000000000,"Time Machine")
Product12 = Product(12,14000000000000,"Antimatter Condenser")

counter = 0

while counter < 5:
    counter == counter + 1
    big_cookie.click()
    nr_cookies = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    nr_cookies = int(nr_cookies.replace(",",""))
    if nr_cookies >= Product12.price:
        Product.buy(Product12)
    elif nr_cookies >= Product11.price:
        Product.buy(Product11)
    elif nr_cookies >= Product10.price:
        Product.buy(Product10)
    elif nr_cookies >= Product9.price:
        Product.buy(Product9)
    elif nr_cookies >= Product8.price:
        Product.buy(Product8)
    elif nr_cookies >= Product7.price:
        Product.buy(Product7)
    elif nr_cookies >= Product6.price:
        Product.buy(Product6)
    elif nr_cookies >= Product5.price:
        Product.buy(Product5)
    elif nr_cookies >= Product4.price:
        Product.buy(Product4)
    elif nr_cookies >= Product3.price:
        Product.buy(Product3)   
    elif nr_cookies >= Product2.price:
        Product.buy(Product2)
    elif nr_cookies >= Product1.price:
        Product.buy(Product1)
    elif nr_cookies >= Product0.price:
        Product.buy(Product0)
    else:
        continue

nr_cookies = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
nr_cookies = int(nr_cookies.replace(",",""))

#print("Number of cookies ", nr_cookies)

time.sleep(50)  

driver.quit()