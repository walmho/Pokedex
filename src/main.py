from scraping import getPage, findAll, screenshotAll, nameAll, loadPairs
if __name__ == "__main__":
    driver = getPage("swsh11-lost-origin")
    names = findAll(driver, "search-result__title")
    nameList = nameAll(names)
    imageList = findAll(driver, "lazy-image__wrapper")
    imageKey = screenshotAll(driver, imageList, "C:\\Users\\ryan_\\Documents\\Programming\\repos\Pokedex\\trainingPictures")

    trainingKey = loadPairs(nameList, imageKey)