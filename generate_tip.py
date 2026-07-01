import os
import json
import urllib.request
from datetime import date

API_KEY = os.environ["API_NINJAS_KEY"]

req = urllib.request.Request(
    "https://api.api-ninjas.com/v2/quoteoftheday",
    headers={"X-Api-Key": API_KEY}
)

with urllib.request.urlopen(req) as res:
    data = json.loads(res.read().decode())

quote = data["quote"]
author = data["author"]
today = date.today().strftime("%Y-%m-%d")

entry = f"\n\n## {today}\n\n> {quote}\n>\n> — {author}\n"

with open("quotes.md", "a") as f:
    f.write(entry)

print(f"Wrote quote for {today}")
