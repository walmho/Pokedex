from scraping.makeTraining import getPage, findAll, screenshotAll, nameAll, loadPairs
if __name__ == "__main__":
    #Note: only scrapes the lost origin set. For this model to be good, we need to scrape from multiple years of releases
    #Second note: getPage string only works for lost origin right now. Links are more unique than initially thought
    driver = getPage("swsh11-lost-origin")
    names = findAll(driver, "search-result__title")
    nameList = nameAll(names)
    imageList = findAll(driver, "lazy-image__wrapper")
    imageKey = screenshotAll(driver, imageList, "C:\\Users\\ryan_\\Documents\\Programming\\repos\Pokedex\\trainingPictures")

    trainingKey = loadPairs(nameList, imageKey)
    print(trainingKey)
