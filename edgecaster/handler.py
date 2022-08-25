from python_parser.send_e2e import touchstream_sender
from python_parser.prometheus_parser import export_prometheus_metrics
from api.get_api_status import output_streams, send_e2e
from helpers.aws_get_metric_data import run_me
import json
import time

with open("/usr/src/app/code/conf/touchstream_conf.json") as file:
    data = json.load(file)


while True:
    # Post Edgecaster data
    output_streams(data["mapping"], data["edgecaster_ip"], data)
    # Post prometheus data
    prom_metrics = export_prometheus_metrics(data)
    touchstream_sender(data, prom_metrics)
    # Post IVS data - Should be run through our scheduler, needs crossaccount!!
    # run_me(data)
    time.sleep(60)  # E2E API has a 1m rate limit
