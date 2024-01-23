import os
import requests
import subprocess
from datetime import datetime

# フォルダを作成
folder_name = f"rss_dj_EN_{datetime.now().strftime('%Y%m')}"
os.makedirs(folder_name, exist_ok=True)

# RSSフィードのURLリスト
urls = [
    "https://feeds.a.dj.com/rss/RSSOpinion.xml",
    "https://feeds.a.dj.com/rss/RSSWorldNews.xml",
    "https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml",
    "https://feeds.a.dj.com/rss/RSSMarketsMain.xml",
    "https://feeds.a.dj.com/rss/RSSWSJD.xml",
    "https://feeds.a.dj.com/rss/RSSLifestyle.xml"
]

# RSSフィードをダウンロードして保存
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        file_name = f"{folder_name}/rss_dj_{datetime.now().strftime('%Y%m%d_%H%M')}_{os.path.basename(url).replace('.xml', '')}.xml"
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {url}")
    else:
        print(f"Failed to download {url}")

# ファイルをコミットとプッシュ
subprocess.run(["git", "config", "--local", "user.email", "action@github.com"])
subprocess.run(["git", "config", "--local", "user.name", "GitHub Action"])
subprocess.run(["git", "add", f"{folder_name}/*"])
subprocess.run(["git", "commit", "-m", f"Add RSS XML files for {datetime.now().strftime('%Y%m%d')}"])
subprocess.run(["git", "push", "origin", "main"])
