import requests
import time
from zapv2 import ZAPv2
target = 'https://www.zyprotect.com:8020'
scanid = '6'
apikey = 'gosgbmpkohe5iplnieks0getmp' # Change to match the API key set in ZAP, or use None if the API key is disabled
#
# By default ZAP API client will connect to port 8080
#zap = ZAPv2(apikey=apikey)
# Use the line below if ZAP is not listening on port 8080, for example, if listening on port 8090
zap = ZAPv2(apikey=apikey, proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})

# Proxy a request to the target so that ZAP has something to deal with
print('Accessing target {}'.format(target))
zap.urlopen(target)
# Give the sites tree a chance to get updated
time.sleep(2)
#res = requests.get("http://zap/JSON/ascan/view/status", params={"url":"http://www.baidu.com"}, proxies={"http":"http://127.0.0.1:8080"})
scanid = zap.spider.stop(scanid,apikey)
scanid = zap.ascan.stop(scanid,apikey)
print(scanid)