import requests
url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    return '15846868788059'


def git_sign():
    return 'f72f881076baa0bd359c8ed705df4000'


def git_ts():
    return '1584686878805'


form_data={
'i':'我和你都是中国人',
'from':'AUTO',
'to':'AUTO',
'smartresult':'dict',
'client':'fanyideskweb',
'salt': get_salt(),
'sign': git_sign(),
'ts': git_ts(),
'bv':'fde1c7f2fa80553b128e6ed1e20e3b1b',
'doctype':'json',
'version':'2.1',
'keyfrom':'fanyi.web',
'action':'FY_BY_REALTlME',
}
response=requests.post(url,form_data)
print(response.text)