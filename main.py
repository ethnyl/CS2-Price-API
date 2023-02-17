from backend/marketdata import item_data, get_hashname
import os
import time

csmb = """                   __ 
 ____ ___  __ _   / / 
/ __/(_-< /  ' \ / _ \ 
\__//___//_/_/_//_.__/ 
      \n══════════════════════"""

print(csmb)

mode = int(input("[1] Weapons\n[2] Cases\n[?] "))
os.system('clear')

if mode == 1:
  print(csmb)
  gun = input("[-] Gun\n[?] ")
  os.system('clear');print(csmb)
  skin = input("[-] Skin\n[?] ")
  os.system('clear');print(csmb)
  wear = int(input("[-] Wear\n┈┈┈┈┈┈┈┈┈┈┈┈┈\n[1] Factory New\n[2] Minimal Wear\n[3] Field Tested\n[4] Well Worn\n┈┈┈┈┈┈┈┈┈┈┈┈┈\n[?] "))
  os.system('clear');print(csmb)
  stat = 0
  if input("[1] StatTrak\n[?] ") == '1':
    stat = 1
  start_time = time.time()
  os.system('clear');print(csmb,"\nFetching data...")
  hashname = get_hashname(gun, skin, wear, stat)
  
elif mode == 2:
  print(csmb)
  case = input("[-] Case\n[?] ")
  start_time = time.time()
  os.system('clear');print(csmb,"\nFetching data...")
  hashname = case.replace(' ', '%20')
  
try:
  print(item_data(hashname))
except:
  exit("[!] Item data not avaliable")
  
print(f"Executed in {round(time.time() - start_time, 3)} seconds.")
