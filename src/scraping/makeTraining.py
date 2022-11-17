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

def findAll(driver, className):
    element = driver.find_elements(By.CLASS_NAME, className)
    return element

def screenshotAll(driver, images, fileLocation):
    imageKey = []
    for i in range(len(images)):
        driver.execute_script('arguments[0].scrollIntoView({block: "center"});', images[i])
        images[i].screenshot(f"{fileLocation}\\training_{i+1}.png")
        imageKey.append(f"training_{i+1}.png")

    driver.quit()
    return imageKey

def nameAll(names):
    nameList = []
    for i in range(len(names)):
        nameList.append(names[i].text)

    print(nameList)
    return nameList

def loadPairs(names, imageKey):
    answers = dict(zip(names, imageKey))
    return answers

driver = getPage("swsh11-lost-origin")
names = findAll(driver, "search-result__title")
nameList = nameAll(names)
imageList = findAll(driver, "lazy-image__wrapper")
imageKey = screenshotAll(driver, imageList, "C:\\Users\\ryan_\\Documents\\Programming\\repos\Pokedex\\trainingPictures")

trainingKey = loadPairs(nameList, imageKey)
