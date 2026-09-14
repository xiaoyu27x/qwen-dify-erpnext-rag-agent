import os,requests
from dotenv import load_dotenv
load_dotenv()
base=os.getenv("LLM_BASE_URL","http://127.0.0.1:8000/v1").rstrip("/")
r=requests.get(f"{base}/models",timeout=15); r.raise_for_status(); print(r.json())
