import os, json, requests
from dotenv import load_dotenv
load_dotenv()
base=os.environ["ERPNEXT_BASE_URL"].rstrip("/")
headers={"Authorization":f'token {os.environ["ERPNEXT_API_KEY"]}:{os.environ["ERPNEXT_API_SECRET"]}'}
params={"fields":json.dumps(["item_code","warehouse","actual_qty","valuation_rate","stock_value"]),"limit_page_length":1000}
r=requests.get(f"{base}/api/resource/Bin",headers=headers,params=params,timeout=30)
r.raise_for_status()
print(r.json())
