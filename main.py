import json

import requests

namecheapbase = "https://www.namecheap.com/market/"

with open('testbot.txt') as f:
    lines = f.readlines()


    for line in lines:
        #print(line)
        url = "https://seo-metrics1.p.rapidapi.com/search"
        headers = {
            "X-RapidAPI-Key": "142655885dmsh10c31906b923b6cp10f6b4jsnc377e82beb4b",
            "X-RapidAPI-Host": "seo-metrics1.p.rapidapi.com"
        }
        build = line.strip()
        print(build)
        querystring = {"url":build}

        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.json()["DA"])
        if int(response.json()["DA"]) >= 25:

            url = "https://seo-rank-checker.p.rapidapi.com/check"
            dnlink = namecheapbase + build

            querystring = {"metric": "semrush"}

            payload = {"url": build}
            headers = {
                "content-type": "application/json",
                "X-RapidAPI-Key": "142655885dmsh10c31906b923b6cp10f6b4jsnc377e82beb4b",
                "X-RapidAPI-Host": "seo-rank-checker.p.rapidapi.com"
            }

            responserd = requests.request("POST", url, json=payload, headers=headers, params=querystring)
            print(responserd.json()["result"]["links"]["domain"])

            if int(response.json()["DA"]) >= 65:
                resellpotential = "Mid-High $$$$"
            elif int(response.json()["DA"]) >= 55:
                resellpotential = "Low-Mid $$$$"
            elif int(response.json()["DA"]) >= 35:
                resellpotential = "Mid-High $$$"
            elif int(response.json()["DA"]) >= 25:
                resellpotential = "Low-High $$$"

            try:
                if int(responserd.json()["result"]["links"]["domain"]) > 400:

                    data = {
                        "username": "DomainSniper"
                    }

                    data["embeds"] = {
                        "username": "DomainSniper",
                        "content": None,
                        "embeds": [
                            {
                                "title": build,
                                "description": "Domain Authority: "+ response.json()["DA"]+
                                               "\nReferring Domains: " + responserd.json()["result"]["links"]["domain"]+
                                               "\nAuction: "+ "NameCheap" +
                                               "\n\nLink: " + dnlink+
                                               "\n\nResell Potential: "+ resellpotential,
                                "color": None
                            }
                        ],
                        "attachments": []
                    }

                    jsondata = json.dumps(data["embeds"])

                    webhookurl = "https://discord.com/api/webhooks/1006584345621962763/efnn_YLbLrs9bfu48vwnHlqJVwcMKpsylE0NVt6vxtr_JENSlVazAa8Jb-8cW-ahIcRF"
                    result = requests.post(webhookurl, json= data["embeds"])
                    print("Webhook posted")
            except:
                print("An exception occurred")

