import re
import requests
from bs4 import BeautifulSoup

result = requests.get("http://www.punchlinecomedyclub.com/?awtrc=true&C=blue_hob&&https://ad.atdmt.com/s/go;adv=11212213594029;ec=11212214381600;c.a=71700000023599255;s.a=GOOGLE;p.a=71700000023599255;as.a=58700002499585776;c.n=Punch+Line+Comedy+Club+-+San+Francisco+(Brand);p.n=Punch+Line+Comedy+Club+-+San+Francisco+(Brand);as.n=Punch+Line+San+Francisco+(gen);qpb=1;?bidkw=punchline+sf&dvc=c&h=http%3A%2F%2Fwww.punchlinecomedyclub.com%2F%3Fawtrc%3Dtrue%26C%3Dblue_hob%26gclsrc%3Daw.ds%26&gclid=Cj0KCQjwrrXtBRCKARIsAMbU6bHN2yNUQ_wOZtcTydkqFDE4R9qU-JtT8twNhX0XepId9Xfgxvv4oVIaAqEyEALw_wcB&gclsrc=aw.ds")

# print(result.status_code)
# print(result.headers)
src = result.content
# print(src)


soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("img")
# print(links)
# print("\n")
#
artist = list(links)
# print(artist)
# print(type(artist))

result = re.findall('[A-Z]{5,}', str(artist))
print(result)
