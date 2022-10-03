from marin.page import Page
from marin.download import Download
from marin.config import Config
import os
import time

base_url = Config().base_url

url = input("\033[94m다운로드 할 만화의 링크 : ")

page, title = Page("https://marumaru303.com/bbs/cmoic/20012").get()

title = title.replace(" ", "")
print("검색된 만화 : " + title)
os.mkdir(f"./{title}")
print("5초후 다운로드가 시작됩니다.")
time.sleep(5)

x = 1
for i in page[::-1]:
    os.system("cls")
    os.mkdir(f"./{title}/{x}")
    print(f"{x}화 다운로드 시작")
    da = Download(base_url + i)
    list = da.get_list()
    page = 1
    for j in list:
        path = f"./{title}/{x}/"
        url = f"{base_url}{j}"
        name = f"{page}.jpg"
        da.downloads(path, url, name)
        print(f"{page}페이지 다운로드 성공!")
        page += 1
        time.sleep(1.0)

    x += 1
