import requests
from bs4 import BeautifulSoup
from .config import Config


class Download(Config):
    def __init__(self, url: str):
        self.url = url

    def get_list(self):
        re = requests.get(self.url)
        bs = BeautifulSoup(re.text, "lxml")
        img_list = bs.find_all("img", class_="img-tag")
        return [a["src"].replace(self.base_url, "") for a in img_list]

    def downloads(self, path, url, file_name):
        with open(path + file_name, "wb") as file:
            response = requests.get(url)
            file.write(response.content)
