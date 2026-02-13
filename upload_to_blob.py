import requests
from datetime import datetime

# Direct URL to the new Azurite port
base_url = "http://127.0.0.1:10010/devstoreaccount1"
container_url = f"{base_url}/datasets"
blob_url = f"{container_url}/All_Diets.csv"

# Standard headers for Azure REST API (Simplified)
headers = {
    'x-ms-version': '2019-12-12',
    'x-ms-date': datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT'),
    'x-ms-blob-type': 'BlockBlob'
}

print("🚀 Attempting Direct HTTP Upload (Bypassing SDK Signature)...")

try:
    # 1. Create Container (Ignore if it already exists)
    requests.put(f"{container_url}?restype=container", headers={'x-ms-version': '2019-12-12'})
    
    # 2. Upload File
    with open("All_Diets.csv", 'rb') as f:
        response = requests.put(blob_url, data=f, headers=headers)
    
    if response.status_code == 201:
        print("✅ SUCCESS! File uploaded via Direct HTTP.")
    else:
        print(f"❌ Failed: {response.status_code}")
        print(f"Response: {response.text}")

except Exception as e:
    print(f"❌ Connection Error: {e}")