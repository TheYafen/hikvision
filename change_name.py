import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
from pprint import pprint


xml_data = '''<?xml version="1.0" encoding="UTF-8"?>
<VideoInputChannel version="2.0" xmlns="http://www.hikvision.com/ver20/XMLSchema">
<id>1</id>
<inputPort>1</inputPort>
<name>kjhfkasae</name>
<videoFormat>PAL</videoFormat>
</VideoInputChannel>
'''

##name_addr += '?security=1&iv=54d3f4496c30d8e229fa6af18e7e774e'

get_url='http://192.168.195.121/ISAPI/System/Video/inputs/channels/1'
set_url='http://192.168.195.121/ISAPI/System/Video/inputs/channels/1'
r = requests.get(get_url,
                 auth=HTTPDigestAuth('admin', '1q2w3e4r'))
print(r.content.decode())
x = requests.put(set_url,
                 auth=HTTPDigestAuth('admin', '1q2w3e4r'),
                 data = xml_data)
print(x.content.decode())



##cam = Client('http://192.168.195.121', 'admin', '1q2w3e4r')
##cam.System.deviceInfo(method='put', data=name_xml_data)
##cam.System.Video.inputs.channels.1(method='put', data=name_xml_data)

