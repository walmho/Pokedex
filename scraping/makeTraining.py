#Take screenshots of n cards from the tcgplayer website, as well as their corresponding name, and save to file
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PIL import Image
from io import BytesIO

def getPage(setName):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    link =f"""
    https://www.tcgplayer.com/search/pokemon/{setName}?
    =grid&productLineName=pokemon&setName={setName}
    """
    driver.get(link)
    driver.fullscreen_window()
    time.sleep(5)
    return driver

def findImages(driver, imageClass):
    element = driver.find_elements(By.CLASS_NAME, imageClass)
    return element

def screenshot(driver, images, fileLocation):
    for i in range(len(images)):
        driver.execute_script('arguments[0].scrollIntoView({block: "center"});', images[i])
        images[i].screenshot(f"{fileLocation}\\training_{i+1}.png")

    driver.quit()

driver = getPage("swsh11-lost-origin")
imageList = findImages(driver, "lazy-image__wrapper")
screenshot(driver, imageList, "C:\\Users\\ryan_\\Documents\\Programming\\repos\Pokedex\\trainingPictures")
