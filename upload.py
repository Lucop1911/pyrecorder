import requests

filepath = r"C:\Users\sCOPPELL2\Music\la\pyrecorder\record.mp4"
url = "https://file.io"

with open(filepath, "rb") as f:
    r = requests.post(url, files={"file": f})

print(r.text)
