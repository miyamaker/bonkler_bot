from requests import get
import json, time

data = get("https://bonkler.remilia.org/bonkler?c=1")
_data = data.json()
now = time.time()
bonklerID = _data["auctionData"]["bonklerId"]
nextBonkler = _data["auctionData"]["nextBonklerId"]
genHash = _data["generationHash"]
nextgenhash = _data["nextGenerationHash"]
endTime = _data["auctionData"]["endTime"]
print(f'current bonkler is {bonklerID}, genhash is {genHash}, auction ending in {endTime-now}')