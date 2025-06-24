import requests
import zipfile
import os

json_url = "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json"
response = requests.get(json_url)
data = response.json()

# Lọc đúng bản Windows x64
for item in data['channels']['Stable']['downloads']['chromedriver']:
    if 'win64' in item['url']:
        download_url = item['url']
        break

# Tải về
zip_path = "chromedriver_win64.zip"
with requests.get(download_url, stream=True) as r:
    with open(zip_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

# Giải nén
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall("chromedriver_win64")

os.remove(zip_path)
print("✅ Đã tải và giải nén ChromeDriver cho Windows x64.")
