from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
sys.setrecursionlimit(100000)
from selenium.webdriver.common.keys import Keys

path = "/home/timothy/Desktop/chrome driver/chromedriver"
driver = webdriver.Chrome(executable_path=path)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")



def game():
    flag = True
    prices_list = []
    while flag:
        money = int(driver.find_element(By.ID, "money").text)
        cursor_button = driver.find_element(By.CSS_SELECTOR, "#buyCursor b")
        cursor_value = int(cursor_button.text.split(" ")[2])
        prices_list.append([cursor_button, cursor_value])
        grandma = driver.find_element(By.CSS_SELECTOR, "#buyGrandma b")
        grandma_value = int(grandma.text.split(" ")[2])
        prices_list.append([grandma,grandma_value])
        factory = driver.find_element(By.CSS_SELECTOR, "#buyFactory b")
        factory_value = int(factory.text.split(" ")[2])
        prices_list.append([factory,factory_value])
        mine = driver.find_element(By.CSS_SELECTOR, "#buyMine b")
        mine_value = int(mine.text.split(" ")[2].replace(",",""))
        prices_list.append([mine,mine_value])
        shipment = driver.find_element(By.CSS_SELECTOR, "#buyShipment b")
        shipment_value = int(shipment.text.split(" ")[2].replace(",",""))
        prices_list.append([shipment,shipment_value])
        # alchemy_lab = driver.find_element(By.CSS_SELECTOR, "#buyAlchemy lab")
        # alchemy_lab_value = int(alchemy_lab.text.split(" ")[2].replace(",",""))
        # prices_list.append([alchemy_lab,alchemy_lab_value])
        portal = driver.find_element(By.CSS_SELECTOR, "#buyPortal b")
        portal_value = int(portal.text.split(" ")[2].replace(",",""))
        prices_list.append([portal,portal_value])

        prices_list.sort(key= lambda x: x[1], reverse=True)
        cookie.click()
        for i in prices_list:
            if money >= i[1]:
                i[0].click()
        game()

game()


