# Get Urls from HAR file, collect then sort and print out

import json

urls = []
with open("sitename.har", "r") as response_f:
    response_dict = json.load(response_f)
    logentries = response_dict["log"]["entries"]
    for entry in logentries:
        for line in logentries:
            url = line["request"]["method"] + ":" + line["request"]["url"]
            if not url in urls:
                urls.append(url)
            #print(line["request"]["method"], line["request"]["url"])

urls.sort()
for url in urls:
    print(url)
