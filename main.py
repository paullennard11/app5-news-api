import requests

api_key = "39e0ee01f466485698057710bf1e2d84"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-08-09&sortBy=publishedAt&apiKey=" \
      "39e0ee01f466485698057710bf1e2d84"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])






