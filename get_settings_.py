import requests
from requests.auth import HTTPDigestAuth
import xml.dom.minidom

url = 'http://192.168.195.121/ISAPI/Image/channels/'
#url = 'http://172.16.147.39/ISAPI/Image/channels/101/WDR'
#url = 'http://192.168.195.121/ISAPI/System/time'
#url = '''rtsp://admin:1q2w3e4r@172.16.147.39/ISAPI/Image/channels/101'''
    
##r = requests.get(url, auth=HTTPDigestAuth('admin', '1q2w3e4r'))
##print(r.content.decode('utf-8'))

url_Artem = 'http://192.168.195.121/ISAPI/System/Video/inputs/channels/1'
r = requests.get(url_Artem, auth=HTTPDigestAuth('admin', '1q2w3e4r'))
print(r.content.decode('utf-8'))

#doc = xml.dom.minidom.parse(x)
