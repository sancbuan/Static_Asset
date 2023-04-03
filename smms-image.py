#FileName: smms-image.py
import requests
import os
import json
import pathlib
import sys

def getUploadedImages(token) -> str:
    url = "https://sm.ms/api/v2/upload_history"
    headers = {"Authorization": token}
    return requests.get(url, headers=headers).text

data = json.loads(getUploadedImages(sys.argv[1]))

for img in data["data"]:
    path = "./data/" + img["storename"]
    if not pathlib.Path(path).is_file():
        pic = requests.get(img["url"]).content
        f = open(path, "wb")
        f.write(pic)
        f.close()
        del pic
        print("Successfully get "+img["storename"]+" .")
    else:
        print(""+img["storename"]+" is already exists.")