import requests
from bs4 import BeautifulSoup

# def Check(a):
#     try:
#         b = int(a)
#         return True
#     except ValueError:
#         return False

def Rice(a):
    # a 인자값 : 0 = 아침, 1 = 점심, 2 = 저녁
    BASE_URL = "http://www.gsm.hs.kr/xboard/board.php?tbnum=8"

    responses = requests.get(BASE_URL)
    dom = BeautifulSoup(responses.content, "html.parser")
    rice = dom.find("li",{"class":"today"}).findAll("span",{"class":"content"})
    data = str(rice[a])
    data = data.replace("<span class=\"content\">", "")
    data = data.replace("<br/>","")
    data = data.replace("</span>","")

    # data = list(data)
    # for i in range(len(data)):
    #     if Check(data[i]):
    #         data[i] = "$"

    # data = "".join(data)
    # data = data.replace("$","")
    return data
