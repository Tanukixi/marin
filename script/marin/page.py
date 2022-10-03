import requests
from bs4 import BeautifulSoup


class Page:
    def __init__(self, url):
        self.url = url

    def get(self):
        re = requests.get(self.url)
        bs = BeautifulSoup(re.text, "lxml")
        title = bs.find("h1", class_="text-left").text
        table = bs.find("table", class_="table div-table list-pc bg-white")
        tr = table.find_all("tr")
        result = []
        for i in tr[1:]:
            result.append(i.find("a")["href"])
        return result, title
