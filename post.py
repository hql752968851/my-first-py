import requests
import random
import time
#url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
#content="我和你"
class yaodao():
    def __init__(self,content):
        self.content=content
        self.url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        self.sign=self.get_sign()

   def get_md5(self,vslue):
      import hashlib
      m=hashlib.md5()
       m.update(value.encode("utf-8"))
      return m.hexdigest()


   def get_salt(self):
      s=str(random.randint(0,10))
      t=get_ts
      return t + s


    def get_sign(self):
      i=get_salt()
       e=get_content()
       s="fanyideskweb " + e + i + " Nw(nmmbP % A - r6U3EUn]Aj"
       return get_md5(s)


    def get_ts(self):
        t=time.time
        ts=str(int(round(t*1000)))
        return ts

     def get_content(self):

         return content




   def yield_formdate(self):
     form_data={
       'i':self.content(),
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':self.salt(),
        'sign':self.sign(),
        'ts':self.ts(),
        'bv':'fde1c7f2fa80553b128e6ed1e20e3b1b',
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTlME',
     }
         return form_data
  def get_header(self):
    headers={
        'Cookie': 'OUTFOX_SEARCH_USER_ID = -1493030219 @ 10.169.0.102;OUTFOX_SEARCH_USER_ID_NCOO = 496394606.7691763;DICT_UGC = be3af0da19b5c5e6aa4e17bd8d90b28a |;JSESSIONID = abc1nRLAQwqw1b8kbLIfx;___rl__test__cookies = 1586501179879',
        'Referer':'http://fanyi.youdao.com/',
        'User - Agent':'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 75.0.3770.100Safari / 537.36',
    }
    return headers
if __name__ == '__main__':
    print(form_date)
    print(get_headers())
    response=requests.post(url, date=form_data, headers=get_headers())
    print(response.text)