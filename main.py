import requests
from send_email import send_email

topic = "tesla"

api_key = "39e0ee01f466485698057710bf1e2d84"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-08-09&" \
      "sortBy=publishedAt&" \
      "apiKey=39e0ee01f466485698057710bf1e2d84" \
      "&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles, description, and URLs
body = "Subject: Today's news\n"  # Set the subject here

for article in content["articles"][:20]:
    if article["title"] is not None:
        body += article["title"] + "\n" \
                + article["description"] \
                + "\n" + article["url"] + "\n\n"

body = body.encode("utf-8")
send_email(message=body)