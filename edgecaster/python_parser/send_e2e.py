import requests
import json
from pprint import pprint

def ts_metrics(data):

    metric_list = []
    for metric in data:
        metric_dict = {}
        if metric != "node_memory_Active_bytes" and metric != "node_memory_MemTotal_bytes":
            print("METRIC00")
            print(metric)
            metric_dict['name'] = metric.replace("_", " ")
            metric_dict['type'] = "numeric"
            metric_dict['value'] = data[metric]
            metric_dict['suffix'] = " "
            metric_dict['status'] = 1
            metric_dict['visible'] = True
        if metric_dict:
            metric_list.append(metric_dict)
    return metric_list

def ts_metric_group(config, data):
    e2ePath = config["mapping"]['e2e']
    metrics_data = ts_metrics(data)
    e2eDict = {}
    e2eDict[e2ePath] = {}
    e2eDict[e2ePath][e2ePath] = []
    EdgeCaster_dict = {}
    EdgeCaster_dict["EdgeCaster"] = {}
    EdgeCaster_dict["EdgeCaster"]["status"] = 100
    EdgeCaster_dict["EdgeCaster"]["level"] = 1
    EdgeCaster_dict["EdgeCaster"]["inline"] = True
    EdgeCaster_dict["EdgeCaster"]["metrics"] = metrics_data
    EdgeCaster_dict["EdgeCaster"]["external_links"] = [
        {
            "name": "Prometheus metrics",
            "url": "http://localhost:9100/metrics",
            "launch_type": "external",
        },
        {
            "name": "Edgecaster UI",
            "url": "http://192.168.1.55",
            "launch_type": "external",
        },
    ]
    e2eDict[e2ePath][e2ePath].append(EdgeCaster_dict)
    return e2eDict


def touchstream_sender(config, data):
    e2e_data = ts_metric_group(config, data)
    pprint(e2e_data)
    headers = config['auth']
    url = f"https://{config['system']}.touchstream.global/api/rest/e2eMetrics/"
    print(url)
    r = requests.post(url, headers=headers, data=json.dumps(e2e_data))
    print(r.status_code)
    print(r.text)