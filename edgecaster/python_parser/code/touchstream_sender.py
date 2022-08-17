import requests
import json
from pprint import pprint


def ts_metric_group(config, data):
    e2ePath = config["e2e_path"]
    e2eDict = {}
    e2eDict[e2ePath] = {}
    e2eDict[e2ePath][e2ePath] = []
    # e2eDict[e2ePath][e2ePath]["EdgeCaster"] = {}
    # e2eDict[e2ePath][e2ePath]["EdgeCaster"]["status"] = 100
    # e2eDict[e2ePath][e2ePath]["EdgeCaster"]["level"] = 1
    # e2eDict[e2ePath][e2ePath]["EdgeCaster"]["inline"] = True
    # e2eDict[e2ePath][e2ePath]["EdgeCaster"]["metrics"] = data
    other_dict = {}
    other_dict["EdgeCaster"] = {}
    other_dict["EdgeCaster"]["status"] = 100
    other_dict["EdgeCaster"]["level"] = 1
    other_dict["EdgeCaster"]["inline"] = True
    other_dict["EdgeCaster"]["metrics"] = data
    other_dict["EdgeCaster"]["external_links"] = [
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
    e2eDict[e2ePath][e2ePath].append(other_dict)
    return e2eDict


def touchstream_sender(config, data):
    pprint(config)
    e2e_data = ts_metric_group(config, data)
    pprint(e2e_data)
    headers = {
        "Authorization": config["Authorization"],
        "X-TS-ID": config["X-TS-ID"],
        "Content-Type": "application/json",
    }
    url = f"https://{config['system']}.touchstream.global/api/rest/e2eMetrics/"
    print(url)
    r = requests.post(url, headers=headers, data=json.dumps(e2e_data))
    print(r.status_code)
    print(r.text)
