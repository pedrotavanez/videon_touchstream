import requests
import json
from pprint import pprint


headers = {
    "X-TS-ID": "fef6c8f8-c79e-473d-8840-85aa62bc",
    "Authorization": "Bearer 3c972d1f0b6548508edaccc82076b09c",
    "Content-Type": "application/json",
}
# AWS Data


def rtmp_kpis(data):
    rtmp_data = data
    if rtmp_data["status"] == "STREAM_RUNNING":
        rtmp_status = 1
    else:
        rtmp_status = 0
    json_data = json.loads(rtmp_data["service"]["data"])
    rtmp_status = {
        "name": "RTMP Status",
        "value": rtmp_data["status"],
        "type": "text",
        "visible": True,
        "status": rtmp_status,
    }
    ivs_arn = {
        "name": "IVS ARN",
        "value": json_data["selected_channel_arn"],
        "type": "text",
        "visible": False,
        "status": 1,
    }
    metric_list = []
    metric_list.append(rtmp_status)
    metric_list.append(ivs_arn)
    return metric_list, rtmp_status


def rtmp_metric_group(data, rtmp_status):
    if rtmp_status["value"] != "STREAM_RUNNING":
        metric_group_status = 0
    else:
        metric_group_status = 100
    metric_group = [
        {
            "RTMP Edgecaster": {
                "status": metric_group_status,
                "level": 1,
                "inline": True,
                "update_threshold": 5,
                "external_links": [],
                "metrics": data,
            }
        }
    ]
    return metric_group


def send_e2e(data, options):
    channel_key = options["mapping"]["e2e"]
    payload = {}
    payload[channel_key] = {}
    payload[channel_key][channel_key] = data
    r = requests.post(
        f"https://{options['system']}.touchstream.global/api/rest/e2eMetrics/",
        headers=options["auth"],
        data=json.dumps(payload),
    )
    if r.status_code != 200:
        print("Error")
        print(r.status_code)
        print(r.text)
    else:
        print("Request Sent")
        pprint(r.text)


def output_streams(ts_dict, edgecaster_ip, options):
    # Connection to Edgecaster API
    proto = "http://"
    # host = "172.18.184.17"
    host = edgecaster_ip
    port = ":2020"
    output_streams_endpoint = "/v2/out_streams/"
    outputs_list = []
    for output_channels in ts_dict["outputs"]:
        # print(ts_dict["outputs"][output_channels])
        edgecaster_output = ts_dict["outputs"][output_channels]
        outputs_list.append(edgecaster_output)
    full_url = proto + host + port + output_streams_endpoint
    r = requests.get(full_url)
    data = json.loads(r.text)
    for out_stream in data["out_streams"]:
        if out_stream["out_stream_id"] in outputs_list:
            # print("Found")
            streamID = out_stream["out_stream_id"]
            r_detail = requests.get(full_url + str(streamID))
            detailed_data = json.loads(r_detail.text)
            # print(f'output type: {detailed_data["output_type"]["value"]}')
            output_type = detailed_data["output_type"]["value"]
            if output_type == "rtmp":
                rtmp_data, rtmp_status = rtmp_kpis(
                    detailed_data["output_type"][output_type]
                )
                rtmp_group = rtmp_metric_group(rtmp_data, rtmp_status)
            stream_status = detailed_data["output_type"][output_type]["status"]
            # print(detailed_data['output_type'][output_type]['service'])
            if (
                detailed_data["output_type"][output_type]["service"]["value"]
                == "aws_ivs"
            ):
                print("IVS destination")
                print(detailed_data["output_type"][output_type]["service"])
    # pprint(rtmp_group)
    send_rtmp = send_e2e(rtmp_group, options)


if __name__ == "__main__":
    integration_dict = {
        "outputs": {"touchstream IVS": 20},  # "demoChannel":17
        "e2e": {"touchstream IVS": "channelKey"},
    }

    pprint(output_streams(integration_dict))
