import requests


def get_metrics(edgecaster_ip):
    url = f"http://{edgecaster_ip}:9100/metrics"
    r = requests.get(url, stream=True)
    return r.status_code, r.text
