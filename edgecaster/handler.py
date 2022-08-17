# from python_parser.code.handler import handler as prometheus_handler
from python_parser.send_e2e import touchstream_sender
from python_parser.prometheus_parser import export_prometheus_metrics
from api.get_api_status import output_streams, send_e2e
import json
from pprint import pprint

with open(
    "/usr/src/app/code/conf/touchstream_conf.json"
) as file:
    data = json.load(file)

print(data)


prom_metrics = export_prometheus_metrics(data)
touchstream_sender(data,prom_metrics)
output_streams(data["mapping"], data["edgecaster_ip"], data)
