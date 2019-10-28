import requests
from bs4 import BeautifulSoup

result = requests.get("https://improv.com/sanjose/calendar/")

# print(result.status_code)
# print(result.headers)
src = result.content
# print(src)


soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("h3")
# print(links)
# print("\n")

artist = list(links)
# print(artist)
# print(type(artist))

strip_list = [item.text.strip() for item in artist]
# print(strip_list)

for item in strip_list:
    if item == "Ari Shaffir":
        print("Hey! Ari is performing here!")
    else:
        pass


# links = soup.find_all("img")
# print(links)
# print("\n")
# # for link in links:
# #     if "id" in link.text:
# #         print(link)
# #         print(link.attrs['href'])
# print(type(links))
