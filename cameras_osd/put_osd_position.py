import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
from hikvisionapi import Client


##Office Camera
ip = '192.168.195.121'

xml_data = '''<VideoOverlay><DateTimeOverlay><enabled>true</enabled><positionY>100</positionY><positionX>100</positionX><dateStyle>MM-DD-YYYY</dateStyle><timeStyle>24hour</timeStyle><displayWeek>false</displayWeek></DateTimeOverlay></VideoOverlay>'''

url = 'http://' + ip + '/ISAPI/System/Video/inputs/channels/1/overlays'


x = 'Didn\'t run'

if False:
    x = requests.put(url,
                     auth=HTTPDigestAuth('admin', '1q2w3e4r'),
                     data = xml_data)
print(x)


cam = Client('http://192.168.195.121', 'admin', '1q2w3e4r')

cam.System.Video.inputs.channels.1.overlays(method='put', data=xml_data)

                                   
##print(x)
##while str(x) != '<Response [200]>':
##    print('WDR on: error')
##    x = requests.put(url, auth=HTTPDigestAuth('admin', '1q2w3e4r'), data = xml_data_on)
##    print('Retry:', x)
##    if str(x) == '<Response [403]>':
##        break
##result = int(str(x) == '<Response [200]>')

