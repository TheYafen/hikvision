import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth

ip = '192.168.195.121'

xml_data_off = '''<?xml version="1.0" encoding="UTF-8"?>
<WDR xmlns="http://www.hikvision.com/ver20/XMLSchema" version="2.0">
<mode>close</mode>
<WDRLevel>50</WDRLevel>
</WDR>'''
xml_data_on = '''<?xml version="1.0" encoding="UTF-8"?>
<WDR xmlns="http://www.hikvision.com/ver20/XMLSchema" version="2.0">
<mode>open</mode>
<WDRLevel>50</WDRLevel>
</WDR>'''
url = 'http://' + ip + '/ISAPI/Image/channels/101/WDR'
x = requests.put(url,
                 auth=HTTPDigestAuth('admin', '1q2w3e4r'),
                 data = xml_data_off)
time.sleep(3)
x = requests.put(url,
                 auth=HTTPDigestAuth('admin', '1q2w3e4r'),
                 data = xml_data_on)
print(x)
while str(x) != '<Response [200]>':
    print('WDR on: error')
    x = requests.put(url, auth=HTTPDigestAuth('admin', '1q2w3e4r'), data = xml_data_on)
    print('Retry:', x)
    if str(x) == '<Response [403]>':
        break
result = int(str(x) == '<Response [200]>')
