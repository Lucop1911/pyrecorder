import requests

filepath = r"C:\Users\sCOPPELL2\Music\la\pyrecorder\record.mp4"
url = "https://file.io"

with open(filepath, "rb") as f:
    r = requests.post(url, files={"file": f})

# Print using UTF-8 encoding safely
print(r.text.encode("utf-8", errors="ignore").decode("utf-8"))
