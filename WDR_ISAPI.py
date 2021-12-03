import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
import time


xml_data_old = '''<?xml version="1.0" encoding="UTF-8"?>
<WDR xmlns="http://www.hikvision.com/ver20/XMLSchema" version="2.0">
<mode>open</mode>
<WDRLevel>79</WDRLevel>
</WDR>'''

xml_data_off = '''<?xml version="1.0" encoding="UTF-8"?>
<WDR xmlns="http://www.hikvision.com/ver20/XMLSchema" version="2.0">
<mode>close</mode>
<WDRLevel>79</WDRLevel>
</WDR>'''

xml_data_on = '''<?xml version="1.0" encoding="UTF-8"?>
<WDR xmlns="http://www.hikvision.com/ver20/XMLSchema" version="2.0">
<mode>open</mode>
<WDRLevel>50</WDRLevel>
</WDR>'''

#url = 'http://172.16.147.39/ISAPI/Image/channels/101/WDR'
#url = '''rtsp://admin:1q2w3e4r@172.16.147.39/ISAPI/Image/channels/101'''

def send_wdr(point, dat):
    x = requests.put(point,
                     auth=HTTPDigestAuth('admin', '1q2w3e4r'),
                     data = dat)
    print(x)
    print(x.content)
    
r = requests.get(url, auth=HTTPDigestAuth('admin', '1q2w3e4r'))
print(r.content)

send_wdr(url, xml_data_off)
time.sleep(3)
send_wdr(url, xml_data_on)
