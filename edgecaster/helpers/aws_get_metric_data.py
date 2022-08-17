from aws_client import new_aws_client
from time_in_query import time_in_query
from pprint import pprint
import json
import requests

metrics = [
    "ConcurrentViews",
    "IngestAudioBitrate",
    "IngestFrameRateInterval",
    "IngestVideoBitrate",
    "LiveInputTime",
    "LiveDeliveredTime",
    "IngestFramerate",
]


def aws_metric_data(data):
    overall_data = []
    channel_name = "raD1O1Gj8bTp"
    now, ago_1m = time_in_query(60)
    client = new_aws_client(
        "cloudwatch",
        "S749HIS5RWN0AQV",
        "us-east-1",
        "arn:aws:iam::714125606834:role/touchstream-medialive-role-CrossAccountRole-DEB8UR3OTC5W",
    )
    metric_data_id = 0
    # for and append
    for metric in metrics:
        print(metric)
        metric_dict = {
            "name": metric[:20],
            "value": None,
            "status": 1,
            "type": None,
            "suffix": "",
            "visible": True,
        }
        unit_s = " seconds"
        unit_bps = " Bps"
        unit_fps = " Fps"
        if metric == "LiveDeliveredTime":
            stat = "Sum"
            metric_dict["suffix"] = unit_s
        elif metric == "IngestVideoBitrate" or metric == "IngestAudioBitrate":
            metric_dict["suffix"] = unit_bps
        elif metric == "ConcurrentViews":
            stat = "Count"
        elif metric == "IngestFramerate":
            metric_dict["suffix"] = unit_fps
        else:
            stat = "Average"
        metric_data = client.get_metric_data(
            MetricDataQueries=[
                {
                    "Id": str(metric).lower()
                    + str(metric_data_id),  # AWS Id formatting, unimportant
                    "MetricStat": {
                        "Metric": {
                            "Namespace": "AWS/IVS",
                            "MetricName": metric,
                            "Dimensions": [
                                {"Name": "Channel", "Value": "raD1O1Gj8bTp"}
                            ],
                        },
                        "Period": 60,
                        "Stat": stat,
                    },
                },
            ],
            StartTime=ago_1m,
            EndTime=now,
            ScanBy="TimestampAscending",
            MaxDatapoints=10,
        )
        n = +1
        # print(f"Cloudwatch KPIs - {metric}")
        # pprint(metric_data["MetricDataResults"])

        if len(metric_data["MetricDataResults"][0]["Values"]) >= 1:
            pprint(metric_data["MetricDataResults"][0]["Values"][-1])
            metric_dict["value"] = round(
                metric_data["MetricDataResults"][0]["Values"][-1], 3
            )
            metric_dict["type"] = "numeric"
            metric_dict["visible"] = True
        else:
            print("No data ")
            metric_value = "N/A"
            metric_dict["value"] = metric_value
            metric_dict["type"] = "text"
        overall_data.append(metric_dict)
    return overall_data


def metric_group(data):
    metric_group = [
        {
            "AWS IVS": {
                "status": 100,
                "level": 1,
                "inline": True,
                "external_links": [
                    {
                        "name": "IVS Console",
                        "url": "https://us-east-1.console.aws.amazon.com/ivs/channels/arn:aws:ivs:us-east-1:714125606834:channel:raD1O1Gj8bTp?region=us-east-1",
                        "launch_type": "external",
                    },
                    {
                        "name": "IVS CloudWatch",
                        "url": "https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#metricsV2:graph=~(view~'timeSeries~stacked~false~metrics~(~(~'AWS*2fIVS~'IngestVideoBitrate~'Channel~'raD1O1Gj8bTp)~(~'.~'IngestAudioBitrate~'.~'.)~(~'.~'IngestFramerate~'.~'.)~(~'.~'KeyframeInterval~'.~'.)~(~'.~'ConcurrentViews~'.~'.)~(~'.~'LiveInputTime~'.~'.)~(~'.~'LiveDeliveredTime~'.~'.))~region~'us-east-1);query=~'*7bAWS*2fIVS*2cChannel*7d",
                        "launch_type": "external",
                    },
                ],
                "metrics": data,
            }
        }
    ]
    return metric_group


def e2e_sender(data, system, headers, options):
    url = f"https://{system}.touchstream.global/api/rest/e2eMetrics/"
    payload = metric_group(data)
    e2e_data = {}
    e2e_data[options["channel"][0]] = {}
    e2e_data[options["channel"][0]]["064ed77c.Live.HLS.AWS_IVS"] = payload

    r = requests.post(url, headers=headers, data=json.dumps(e2e_data))
    print(r.status_code)
    print(r.text)


data = {}
metrics = aws_metric_data(data)
headers = {
    "X-TS-ID": "fef6c8f8-c79e-473d-8840-85aa62bc",
    "Authorization": "Bearer 3c972d1f0b6548508edaccc82076b09c",
    "Content-Type": "application/json",
}
options = {}
options["channel"] = ["064ed77c", "064ed77c.Live.HLS.AWS_IVS"]

e2e_sender(metrics, "tsd", headers, options)
