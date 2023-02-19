import requests

def get_hashname(item, skin, wear, stat):
  item = item.replace(" ", "%20")
  skin = skin.replace(" ", "%20")
  float = {1: "%20%28Factory%20New%29",2: "%20%28Minimal%20Wear%29",3: "%20%28Field-Tested%29",4: "%20%28Well-Worn%29", 5:"%20%28Battle-Scarred%29"}
  wear = float[wear]
  if stat == 1:
    item = "StatTrak™%20"+item
  hashname = item + "%20%7C%20" + skin + wear
  return hashname

def get_nameid(hashname):
  html = requests.get(f"https://steamcommunity.com/market/listings/730/{hashname}").text
  nameid = html.split('Market_LoadOrderSpread( ')[1]
  nameid = nameid.split(' ')[0]
  return nameid

def item_data(hashname):
  nameid = get_nameid(hashname)
  out = {}
  order_data = (requests.get(f"https://steamcommunity.com/market/itemordershistogram?country=US&currency=1&language=english&two_factor=0&item_nameid={nameid}").text)

  out["buy_req"] = int((order_data.split('\"highest_buy_order":\"')[1]).split('\"')[0])/100
  out["sell_req"] = int((order_data.split('\"lowest_sell_order":\"')[1]).split('\"')[0])/100
  # out["volume"] = int(((requests.get(f"https://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name={hashname}").text).split('volume\":"')[1]).split('\"')[0])
  out["nameid"] = nameid
  return out
