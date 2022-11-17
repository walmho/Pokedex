from scraping.makeTraining import getPage, findAll, screenshotAll, nameAll, loadPairs
import os
if __name__ == "__main__":
    localPath = "C:\\Users\\ryan_\\Documents\\Programming\\repos\Pokedex\\trainingPictures"
    #using direct links for now
    links = [
        "https://www.tcgplayer.com/search/pokemon/swsh11-lost-origin?=grid&productLineName=pokemon&setName=swsh11-lost-origin",
        "https://www.tcgplayer.com/search/pokemon/swsh12-silver-tempest?productLineName=pokemon&setName=swsh12-silver-tempest&page=1&view=grid"
        
        ]
    #Finding if any images already exist in directory
    count = 0
    dirPath = localPath
    for path in os.listdir(dirPath):
        if os.path.isfile(os.path.join(dirPath, path)):
            count += 1

    for l in range(len(links)):
        print(links)
        print(links[l])
        driver = getPage(links[l])
        names = findAll(driver, "search-result__title")
        nameList = nameAll(names)
        #Screenshots every listing, even non-card items. Work-around is to find the dimensions of a normal card
        #and trim out anything that isn't those dimensions
        imageList = findAll(driver, "lazy-image__wrapper")
        imageKey = screenshotAll(driver, imageList, localPath, count)

        trainingKey = loadPairs(nameList, imageKey)
        print(trainingKey)
