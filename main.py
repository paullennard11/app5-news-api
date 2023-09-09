import requests
from send_email import send_email

api_key = "39e0ee01f466485698057710bf1e2d84"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-08-09&sortBy=publishedAt&apiKey=" \
      "39e0ee01f466485698057710bf1e2d84"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)






