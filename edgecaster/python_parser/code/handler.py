from python_parser.code.node_exporter_metrics import get_metrics
from python_parser.code.node_data_transform import data_cleanup
from python_parser.code.metrics_filter import metrics_filtering
from python_parser.code.thresholds import match_thresholds
from python_parser.code.touchstream_sender import touchstream_sender
from python_parser.code.config import config


def handler(metrics, options):
    req_status, exporter_data = get_metrics(options["edgecaster_ip"])
    data = data_cleanup(exporter_data)
    filtered_data = metrics_filtering(data, options["metrics"])
    print("Filtered Data")

    data_validated = match_thresholds(
        filtered_data, {"metric1": "v1", "go_goroutines": 2}, options
    )
    # pprint(data_validated)
    touchstream_sender(config, data_validated)


if __name__ == "__main__":
    handler(
        "",
        options={
            "metrics": [
                'node_thermal_zone_temp{type="battery",zone="1"}',
                "node_memory_Active_bytes",
                "node_memory_MemTotal_bytes",
                'node_cpu_frequency_hertz{cpu="0"}',
                'node_cpu_frequency_hertz{cpu="1"}',
                'node_cpu_frequency_hertz{cpu="2"}',
                'node_cpu_frequency_hertz{cpu="3"}',
                "node_thermal_zone_temp{type = 'pm8994_tz', zone = '23'}",
                "node_filesystem_avail_bytes{device='/dev/block/dm-1',fstype='ext4',mountpoint='/data'}",
                "node_filesystem_size_bytes{device='/dev/block/dm-1',fstype='ext4',mountpoint='/data'}",
                "node_cpu_seconds_total{cpu='0',mode='iowait'}",
                "node_cpu_seconds_total{cpu='0',mode='irq'}",
                "node_cpu_seconds_total{cpu='0',mode='nice'}",
                "node_cpu_seconds_total{cpu='0',mode='softirq'}",
                "node_cpu_seconds_total{cpu='0',mode='steal'}",
                "node_cpu_seconds_total{cpu='0',mode='system'}",
                "node_cpu_seconds_total{cpu='0',mode='user'}",
                "node_cpu_seconds_total{cpu='1',mode='iowait'}",
                "node_cpu_seconds_total{cpu='1',mode='irq'}",
                "node_cpu_seconds_total{cpu='1',mode='nice'}",
                "node_cpu_seconds_total{cpu='1',mode='softirq'}",
                "node_cpu_seconds_total{cpu='1',mode='steal'}",
                "node_cpu_seconds_total{cpu='1',mode='system'}",
                "node_cpu_seconds_total{cpu='1',mode='user'}",
                "node_cpu_seconds_total{cpu='2',mode='iowait'}",
                "node_cpu_seconds_total{cpu='2',mode='irq'}",
                "node_cpu_seconds_total{cpu='2',mode='nice'}",
                "node_cpu_seconds_total{cpu='2',mode='softirq'}",
                "node_cpu_seconds_total{cpu='2',mode='steal'}",
                "node_cpu_seconds_total{cpu='2',mode='system'}",
                "node_cpu_seconds_total{cpu='2',mode='user'}",
                "node_cpu_seconds_total{cpu='3',mode='iowait'}",
                "node_cpu_seconds_total{cpu='3',mode='irq'}",
                "node_cpu_seconds_total{cpu='3',mode='nice'}",
                "node_cpu_seconds_total{cpu='3',mode='softirq'}",
                "node_cpu_seconds_total{cpu='3',mode='steal'}",
                "node_cpu_seconds_total{cpu='3',mode='system'}",
                "node_cpu_seconds_total{cpu='3',mode='user'}",
            ]
        },
    )
