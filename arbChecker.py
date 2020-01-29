import json

with open('odds.json') as json_file:
    data = json.load(json_file)



def parseFrac(frac):
    breaker = frac.find('/')
    if(breaker != -1):
        return int(frac[:breaker]) / int(frac[breaker + 1:]) + 1
    return int(frac) + 1


for sportNames in data:
    print("checking", sportNames)
    for sport in data[sportNames]:

        events = list(sport.keys())
        for eventName in events:
            best = {}
            if(type(sport[eventName]) is list):
                for option in sport[eventName]:
                    if(len(option["odds"]) > 0):
                        max = 0
                        for odds in option["odds"]:
                            if( not odds["odds"] == None):
                                decOdds = parseFrac(odds["odds"])
                                if decOdds > max:
                                    max = decOdds
                        print("Max odds", max)
