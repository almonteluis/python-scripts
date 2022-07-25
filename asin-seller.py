from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook, load_workbook
wb = Workbook()
dest_filename = '/sheets/comp.xlsx'
ws1 = wb.active
ws1.title = "seller's names"


# initialize the chrome driver
driver = webdriver.Chrome(executable_path='/Users/imedia/Documents/projects/python-scripts/env/bin/chromedriver')

# head to Sellercentral login page
driver.get("https://www.amazon.com/dp/B07FWMYFXS")

driver.implicitly_wait(10) # seconds

# get all sellers
driver.find_element(By.XPATH, '//*[@id="olpLinkWidget_feature_div"]/div[2]/span/a').click()
driver.implicitly_wait(20) # seconds
sellers = driver.find_elements(By.XPATH, '//*[@id="aod-offer"]')
print("Sellers are: ")
for seller in sellers:
    name = seller.find_element(By.XPATH, './/*[@id="aod-offer-soldBy"]/div/div/div[2]/a')
    print(name.text)
    ws1.append(name.text)

ws1.save(dest_filename)
driver.quit()
