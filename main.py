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

select_lang = driver.find_element(By.ID, "langSelect-EN")
select_lang.click()

#Wait for the page to load for the game to start
time.sleep(2)


big_cookie = "bigCookie"
cookies_id = "cookies"
product_prefix = "product"
can_buy = True


big_cookie = driver.find_element(By.ID, big_cookie)
double_click = ActionChains(driver)
double_click_cookie = double_click.double_click(big_cookie).perform()


for i in range(250):
    big_cookie.click()

cursor_product = driver.find_element(By.ID, product_prefix + "0")
#cursor_product.click()
grandma_product = driver.find_element(By.ID, product_prefix + "1")
#grandma_product.click()
grandma_product = driver.find_element(By.ID, product_prefix + "1")
#grandma_product.click()

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

time.sleep(5)
grandma = Product(1,100,"Grandma")
#Product.buy(grandma)

avaible_products = driver.find_elements(By.CLASS_NAME, "product unlocked enabled")
print(avaible_products)

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


while True:
    big_cookie.click()
    time.sleep(1)
    Product.buy(Product3)
    Product.buy(Product2)
    Product.buy(Product1)
    Product.buy(Product0)
    
    #Product.buy(Product +str(0))
    #cookies = driver.find_element(By.ID, cookies_id).text
    #for i in range(0,13,1):
     #   Product.buy("Product"+str(i))
      # time.sleep(1)
  #  select_product = driver.find_elements(By.CLASS_NAME, "product unlocked enabled")
    
avaible_products = driver.find_elements(By.CLASS_NAME, "product unlocked enabled")
print(avaible_products)

time.sleep(50)  

driver.quit()