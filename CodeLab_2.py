import requests


url = "http://www.baidu.com"

headers = {
            "User_Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0"
        }


requ = requests.get(url=url, headers=headers)

print(requ.text)