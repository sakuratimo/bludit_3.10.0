import requests

def login(host):
    burp0_url = "http://"+host+"/Bludit.html?tokenCSRF=fc7c3bb674fd88283670432486f4a6c2183102b5&username=admin&password=cuc123&save="
    burp0_headers = {"Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers)
    print(r.text)
if __name__ == "__main__":
   
    host =sys.argv[1]
    #host="192.168.56.101:8222"
   # path = '.'
    # ck=login(host)
    # ck1=ck[0]
    # ck2=ck[1]

    # check(ck1,ck2)
    login(host)