import os,requests
from dotenv import load_dotenv
load_dotenv()
base=os.environ["ERPNEXT_BASE_URL"].rstrip("/")
h={"Authorization":f'token {os.environ["ERPNEXT_API_KEY"]}:{os.environ["ERPNEXT_API_SECRET"]}'}
r=requests.get(f"{base}/api/resource/Item",headers=h,params={"limit_page_length":1},timeout=15); r.raise_for_status(); print(r.json())
