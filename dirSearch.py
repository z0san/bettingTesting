from bs4 import BeautifulSoup
import requests
from mainDownloader import downloadOdds

debug = True

def findLinks():
    sports = ["american-footbal", "athletics/tokyo-2020", "austrailian-rules", "awards", "badminton", "baseball", "basketball", "bowls", "boxing", "cheltenham-festival", "chess", "cricket", "cycling", "darts", "football", "gaelic-games", "golf", "greyhounds", "handball", "harness-racing", "horse-racing", "ice-hockey", "novelty", "politics", "pool", "rugby-league", "rugby-union", "snooker", "tv", "table-tennis", "tennis", "ufc-mma", "vollyball", "winter-sports"]

    data = []

    for i in sports:
        url = "https://oddschecker.com/" + i
        print(url)
        page_response = requests.get(
            url,
            timeout=10,
            headers={
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
            }
        )

        soup = BeautifulSoup(page_response.content, "html.parser")

        data = []

        odds = soup.find("tbody", {"id": "t1"})

        if (odds is None):
            foundLinks = []
            if(soup.find("tr", {"class": "match-on"}) is None):
                links = soup.findAll("a")
                for link in links:
                    if (i in link["href"] and "oddschecker" not in link["href"] and "winner" in link["href"] and "2020" not in link["href"] and "?" not in link["href"]):
                        if ("results" not in link["class"]):
                            if debug: print("good link: " + link["href"])
                            foundLinks.append(link["href"])
            else:
                matches = soup.findAll("tr", {"class": "match-on"})
                matches += soup.findAll("tr", {"class": "match-on no-top-border"})
                for looking in matches:
                    if (looking.find("td", {"class": "time all-odds-click"}).div.span.string != "In Play"):
                        if debug: print("good link: " + looking.a["href"])
                        foundLinks.append(looking.a["href"])
            data.append({i: foundLinks})
        else:
            pass
            print("TODO")

    return data

print(findLinks())
