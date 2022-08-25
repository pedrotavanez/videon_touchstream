from prometheus_client import start_http_server, Summary
from prometheus_client.openmetrics.parser import text_string_to_metric_families
import random
import time
import requests
import json
from pprint import pprint

from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY

with open(
    "/usr/src/app/code/conf/touchstream_conf.json"
) as file:
    data = json.load(file)


r = requests.get(f"http://{data['edgecaster_ip']}:9100/metrics")


from prometheus_client.parser import text_string_to_metric_families


def export_prometheus_metrics(options):

    edgecaster_data = {}

    for family in text_string_to_metric_families(r.text):
        for sample in family.samples:
            if sample[0] in data["metrics"]:
                if sample[0] == "node_thermal_zone_temp":
                    if sample[1]["type"] == "pm8994_tz":
                        temperature = sample[2]
                        print(temperature)
                        edgecaster_data["temperature"] = temperature
                elif sample[0] == "node_memory_Active_bytes":
                    print("MEMORY")
                    print(sample)
                    node_memory_Active_bytes = sample[2]
                    edgecaster_data["node_memory_Active_bytes"] = node_memory_Active_bytes
                elif sample[0] == "node_memory_MemTotal_bytes":
                    node_memory_MemTotal_bytes = sample[2]
                    edgecaster_data[
                        "node_memory_MemTotal_bytes"
                    ] = node_memory_MemTotal_bytes
                elif sample[0] == "node_cpu_seconds_total":
                    cpu_list = []
                    cpu = 0
                    node_cpu_seconds_total = sample[2]
                    if sample[1]['mode'] != "idle":
                        cpu_list.append(sample[2])
                    edgecaster_data['CPU Usage'] = node_cpu_seconds_total
    edgecaster_data['memory_usage'] = round(int(edgecaster_data['node_memory_Active_bytes']) / int(edgecaster_data['node_memory_MemTotal_bytes']) * 100,3)
    return edgecaster_data
