import requests
from requests.auth import HTTPDigestAuth
import xml.dom.minidom

url = 'http://172.16.144.40/ISAPI/Image/channels/'
#url = 'http://172.16.147.39/ISAPI/Image/channels/101/WDR'
#url = '''rtsp://admin:1q2w3e4r@172.16.147.39/ISAPI/Image/channels/101'''
    
r = requests.get(url, auth=HTTPDigestAuth('admin', '1q2w3e4r'))
print(r.content.decode('utf-8'))

#doc = xml.dom.minidom.parse(x)
