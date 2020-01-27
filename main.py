from mainDownloader import downloadOdds
from dirSearch import findSports
import json

data = findSports()
odds = {}


print("Events have finnished downloading!")

for i in data:
    key = list(i.keys())[0]
    print("Downloading odds for", key)
    links = i[list(i.keys())[0]]
    downloadedOdds = []
    done = []
    for link in links:
        if link not in done:
            try:
                downloadedOdds += [{link: downloadOdds("https://oddschecker.com/" + link)}]
            except:
                print("Error downloading ", "https://oddschecker.com/" + link)
            done.append(link)
    odds[key] = downloadedOdds

print("All odds have been downloaded")

#print(odds)

with open('odds.json', 'w') as json_file:
  json.dump(odds, json_file, sort_keys=True, indent=4)

print("All odds have been downloaded and can be found in the 'odds.json' file!")
