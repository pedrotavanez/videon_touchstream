import re
from pprint import pprint


def data_cleanup(data):
    line_delete_rx = []
    data_in_transformation = data.split("\n")
    clean_list = []
    for i, batch in enumerate(data_in_transformation):
        if re.match(r"^#", str(batch)):
            n = 0
            line_delete_rx.append(batch)
            n += 1
        else:
            clean_list.append(batch)
    structured_data = t2j(clean_list)
    return structured_data


def calculate_kpis(data):
    ts_dict = {}
    ts_dict["ts_cpu_usage"] = None
    ts_dict["ts_filesystem_usage"] = None
    ts_dict["ts_mem_usage"] = None
    """
    sum by (cpu)(node_cpu_seconds_total{mode!="idle"})
    """
    data['node_cpu_seconds_total{cpu="0",mode="iowait"}']
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    data[""]
    """
     : '210.99',
     'node_cpu_seconds_total{cpu="0",mode="irq"}': '3440.84',
     'node_cpu_seconds_total{cpu="0",mode="nice"}': '79.7',
     'node_cpu_seconds_total{cpu="0",mode="softirq"}': '725.22',
     'node_cpu_seconds_total{cpu="0",mode="steal"}': '0',
     'node_cpu_seconds_total{cpu="0",mode="system"}': '10345.6',
     'node_cpu_seconds_total{cpu="0",mode="user"}': '12153.25',
     'node_cpu_seconds_total{cpu="1",mode="iowait"}': '310.82',
     'node_cpu_seconds_total{cpu="1",mode="irq"}': '2921.33',
     'node_cpu_seconds_total{cpu="1",mode="nice"}': '0.46',
     'node_cpu_seconds_total{cpu="1",mode="softirq"}': '265.09',
     'node_cpu_seconds_total{cpu="1",mode="steal"}': '0',
     'node_cpu_seconds_total{cpu="1",mode="system"}': '10131.23',
     'node_cpu_seconds_total{cpu="1",mode="user"}': '11475.97',
     'node_cpu_seconds_total{cpu="2",mode="iowait"}': '6.58',
     'node_cpu_seconds_total{cpu="2",mode="irq"}': '143.04',
     'node_cpu_seconds_total{cpu="2",mode="nice"}': '0.58',
     'node_cpu_seconds_total{cpu="2",mode="softirq"}': '112.62',
     'node_cpu_seconds_total{cpu="2",mode="steal"}': '0',
     'node_cpu_seconds_total{cpu="2",mode="system"}': '3659.7',
     'node_cpu_seconds_total{cpu="2",mode="user"}': '2615.49',
     'node_cpu_seconds_total{cpu="3",mode="iowait"}': '4.98',
     'node_cpu_seconds_total{cpu="3",mode="irq"}': '221.08',
     'node_cpu_seconds_total{cpu="3",mode="nice"}': '0.24',
     'node_cpu_seconds_total{cpu="3",mode="softirq"}': '155.53',
     'node_cpu_seconds_total{cpu="3",mode="steal"}': '0',
     'node_cpu_seconds_total{cpu="3",mode="system"}': '2545.83',
     'node_cpu_seconds_total{cpu="3",mode="user"}': '1887.99',
     """
    return data


def t2j(data):
    metric_dictionary = {}
    for metric_set in data:
        if len(metric_set) >= 1:
            metric_name = metric_set.split(" ")[0]
            metric_value = metric_set.split(" ")[1]
            metric_dictionary[metric_name] = metric_value
    calculate_kpis(metric_dictionary)
    return metric_dictionary
