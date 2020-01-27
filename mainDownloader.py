
from bs4 import BeautifulSoup
import requests


def downloadOdds(url):
    page_response = requests.get(
        url,
        timeout=5,
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
        }
    )

    #print(page_response.content)


    soup = BeautifulSoup(page_response.content, "html.parser")

    #print(soup)

    data = []

    odds = soup.find("tbody", {"id": "t1"})

    if (odds is not None):
        odds = odds.find_all('td')
    else:
        #print("No odds found!")
        return False


    horses = []
    horseData = []


    i = 0
    while (i < len(odds)):
        if (odds[i]["class"][0] == "sel"):
            horses.append(odds[i])
            odds.remove(odds[i])
        elif ("data-bk" in odds[i].attrs):
            currentHorseOdds = []
            while (i < len(odds) and odds[i]["class"][0] != "sel"):

                if ("data-bk" in odds[i].attrs):
                    currentHorseOdds.append({"data-bk": odds[i]["data-bk"], "odds": odds[i].string})

                i+= 1

            horseData.append(currentHorseOdds)
        else:
            i += 1




    '''for i in odds:
        if ("data-bk" in i.attrs):
            print(i)'''

    #print()

    for i in range(len(horses)):
        data.append({"name": horses[i].a["data-name"], "odds": horseData[i]})

    '''for i in data:
        print(i)'''

    return data


#print(downloadOdds("https://oddschecker.com/american-football/college-football/kai-west-at-aina-east/winner"))
