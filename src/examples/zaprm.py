import requests
import time
from zapv2 import ZAPv2
target = 'http://www.baidu.com'
scanid = '4'
apikey = 'gosgbmpkohe5iplnieks0getmp' # Change to match the API key set in ZAP, or use None if the API key is disabled
#
# By default ZAP API client will connect to port 8080
#zap = ZAPv2(apikey=apikey)
# Use the line below if ZAP is not listening on port 8080, for example, if listening on port 8090
zap = ZAPv2(apikey=apikey, proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})

# Proxy a request to the target so that ZAP has something to deal with
print ('Alerts: ')
pprint (zap.core.alerts())