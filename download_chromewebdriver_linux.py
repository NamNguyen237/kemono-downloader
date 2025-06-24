import requests
import zipfile
import os

# URL JSON endpoint
json_url = "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json"

# Tải JSON
response = requests.get(json_url)
data = response.json()

# Lấy link tải ChromeDriver cho Windows x64
download_url = data['channels']['Stable']['downloads']['chromedriver'][0]['url']

# Tải file zip
zip_file_path = "chromedriver_win64.zip"
with requests.get(download_url, stream=True) as r:
    with open(zip_file_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

# Giải nén
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall("chromedriver_win64")

# Xóa file zip
os.remove(zip_file_path)

print("✅ ChromeDriver đã được tải và giải nén thành công.")
