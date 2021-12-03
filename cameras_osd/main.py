import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
from hikvisionapi import Client
from pprint import pprint

ip = '192.168.195.121'
camera_name = 'TEST_FROM_PYTHON'

overlays_xml_data = '''<VideoOverlay><DateTimeOverlay><enabled>true</enabled><positionY>100</positionY><positionX>100</positionX><dateStyle>MM-DD-YYYY</dateStyle><timeStyle>24hour</timeStyle><displayWeek>false</displayWeek></DateTimeOverlay></VideoOverlay>'''
overlays_addr = '/ISAPI/System/Video/inputs/channels/1/overlays'


name_xml_data = '''<VideoInputChannel xmlns: "http://www.hikvision.com/ver20/XMLSchema" version="2.0"><id>1</id><inputPort>1</inputPort><name>'''
name_xml_data += camera_name
name_xml_data += '</name><videoFormat>PAL</videoFormat></VideoInputChannel>'
name_addr = '/ISAPI/System/Video/inputs/channels/1'
name_addr += '?security=0'
##name_addr += '&iv=54d3f4496c30d8e229fa6af18e7e774e'


x = 'Didn\'t run'

def send():
    url = 'http://' + ip + name_addr
    print('URL:%s' % url)
    
    xml_data = name_xml_data
    print('data:%s' % xml_data)
    x = requests.put(url,
                     auth=HTTPDigestAuth('admin', '1q2w3e4r'),
                     data = xml_data)
    return x


print(send())
##cam = Client('http://192.168.195.121', 'admin', '1q2w3e4r')
##cam.System.deviceInfo(method='put', data=name_xml_data)
##cam.System.Video.inputs.channels.1(method='put', data=name_xml_data)

