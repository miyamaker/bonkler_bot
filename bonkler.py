from requests import get
from web3 import Web3
import json, time

ETH1 = 1000000000000000000
ADDRESS = "0x5167D014a056E43883e1BBEa5530c3c0dC993281"
BONK_ADDRESS = "0xF421391011Dc77c0C2489d384C26e915Efd9e2C5"

def bonkle():
    # while 1:
    data = get("https://bonkler.remilia.org/bonkler?c=1")
    _data = data.json()
    now = time.time()
    endTime = _data["auctionData"]["endTime"]
    bonklerID = _data["auctionData"]["bonklerId"]
    nextBonkler = _data["auctionData"]["nextBonklerId"]
    genHash = _data["generationHash"]
    amount = _data["auctionData"]["amount"]
    nextgenhash = _data["nextGenerationHash"]
    t = endTime - now
    # if t:
    web3 = Web3(Web3.HTTPProvider("https://eth.llamarpc.com"))
    bal = web3.eth.get_balance(ADDRESS)
    nonce = web3.eth.get_transaction_count(ADDRESS)
    print(f'miyagod has {bal} eth and {nonce} txns!')
    txn = {
        "to": BONK_ADDRESS,
        "nonce": nonce,
        "value": ETH1,
        "data": "0x",
        "gas": 200000,
        "maxFeePerGas": 2000000000,
        "maxPriorityFeePerGas": 10000000000,
    }
        # print(bal)
        # print(f'current bonkler is {bonklerID}, genhash is {genHash}, auction ending in {endTime-now}')
        # else:
        #     time.sleep(t)


if __name__ == "__main__":
    bonkle()