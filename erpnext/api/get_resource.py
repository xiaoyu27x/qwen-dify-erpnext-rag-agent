import os, requests
from dotenv import load_dotenv
load_dotenv()
base=os.environ["ERPNEXT_BASE_URL"].rstrip("/")
headers={"Authorization":f'token {os.environ["ERPNEXT_API_KEY"]}:{os.environ["ERPNEXT_API_SECRET"]}'}
r=requests.get(f"{base}/api/resource/Item",headers=headers,params={"limit_page_length":20},timeout=30)
r.raise_for_status()
print(r.json())
