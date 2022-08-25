from pprint import pprint
from hurry.filesize import size, alternative

"""
FS / Netstat have multiple values
'node_filesystem_device_error{device="tmpfs",fstype="tmpfs",mountpoint="/containers/services/kmsg/tmp"}
'node_filesystem_avail_bytes{device="rootfs",fstype="tmpfs",mountpoint="/"}
"""


def match_thresholds(data, thresholds, options):
    overall_list = []
    print(f"Thresholds: {thresholds}")
    ts_format = ts_metrics(data, options)
    # for threshold in thresholds:
    #    for metric in ts_format:
    #        if threshold == metric:
    #            metric_name = metric
    #            metric_value  = data[metric]
    #            if int(metric_value) > int(thresholds[metric_name]):
    #                print("Bad status")
    return ts_format


def ts_metrics(data, options):
    overall_list = []
    for kpi in data:

        if kpi in options["metrics"]:
            print("Match")
            print(kpi)
            metric_template = {
                "name": None,
                "type": None,
                "value": None,
                "status": None,
            }
            print(f"KPI: {kpi}")
            name = kpi
            value = data[kpi]
            print(float(data[kpi]))
            metric_template["name"] = name[:20]
            value_converted = size(float(value), system=alternative)
            value = float(value_converted.split(" ")[0])
            value_unit = str(value_converted.split(" ")[1])
            metric_template["value"] = float(value)
            metric_template["suffix"] = " " + str(value_unit)
            metric_template["type"] = "numeric"
            metric_template["status"] = 1
            overall_list.append(metric_template)
    exit()
    return overall_list
