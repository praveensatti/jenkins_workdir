import logging
import requests
import json
elasticsearch_url = "http://elk.imiconnect.local:9200/_cluster/health?pretty"
from logging.handlers import RotatingFileHandler
logging.basicConfig(level=logging.DEBUG, filename="out.log",filemode="a+",format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",datefmt='%Y-%m-%dT%H:%M:%S')
logger = logging.getLogger('logger_method')
handler = RotatingFileHandler('out.log',maxBytes=10000000, backupCount=5)
logger.addHandler(handler)
payload = {}
headers= {}
response = requests.request("GET", elasticsearch_url, headers=headers, data = payload)
log = json.loads(response.text.encode('utf8'))
if log['active_shards_percent_as_number'] == 100.0:
    logging.info(log)
