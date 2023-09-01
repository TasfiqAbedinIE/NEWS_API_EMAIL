import requests
from send_email import send_mail

api_key = "f6d3e98c13834d14a1d4e8a8c91582a2"
country = "us"
category = "business"
url = f"https://newsapi.org/v2/top-headlines?country={country}&" \
      f"category={category}&" \
      "apiKey=f6d3e98c13834d14a1d4e8a8c91582a2&" \
      "language=en"

request = requests.get(url)
content = request.json()

list_of_articles = content["articles"]
# print(list_of_articles)
# print(len(list_of_articles))

body = ""
for article in list_of_articles[:5]:
    if article["title"] and article["description"] and article["url"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

body = "Subject: Today's news" + "\n" + body
# print(body)

body = body.encode("utf-8")
send_mail(user_message=body)
