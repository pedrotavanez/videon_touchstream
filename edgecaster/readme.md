

# Configuration
Path: conf/touchstream_conf.json
```
{
  "system":"txx",
  "context":"live",
  "edgecaster_ip": "127.0.0.1",
  "mapping": {
        "outputs": {"touchstream IVS": 20},
        "e2e": {"touchstream IVS": "channelKey"}
    },
  "auth": "<Admin menu tokens>"
  "mapping": {"edgecasterID": "064ed77c"},
  "thresholds":[
    {
      "metric1": ["valueForWarn","valueForCrit"],
      "metric2": ["valueForWarn","valueForCrit"],
      "node_thermal_zone_temp{type=\"battery\",zone=\"1\"}": [50,60]
    }
  ],
  "metrics": [
        "node_thermal_zone_temp{type=\"battery\",zone=\"1\"}",
        "node_thermal_zone_temp{type = 'pm8994_tz', zone = '23'}",
        "node_memory_Active_bytes",
        "node_memory_MemTotal_bytes",
        "node_filesystem_avail_bytes{device='/dev/block/dm-1',fstype='ext4',mountpoint='/data'}",
        "node_filesystem_size_bytes{device='/dev/block/dm-1',fstype='ext4',mountpoint='/data'}",
        "node_cpu_seconds_total"
  ]
}
```

# Edgecaster

adb shell mkdir /data/local/touchstream
adb push code

# Run docker image
Note: using --network as we are collecting metrics from prometheus exposed to localhost
* docker run -it ... --network="host"
