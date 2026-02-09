# getadopteddevicelateststatistics

Source: https://developer.ui.com/network/v10.1.68/getadopteddevicelateststatistics

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get Latest Adopted Device Statistics

GET`/v1/sites/{siteId}/devices/{deviceId}/statistics/latest`

Retrieve the latest real-time statistics of a specific adopted device, such as uptime, data transmission rates, CPU and memory utilization.

path Parameters

siteId

required

string

deviceId

required

string

## Responses

200

Response Schema: application/json

uptimeSec

integer

lastHeartbeatAt

string

nextHeartbeatAt

string

loadAverage1Min

number

loadAverage5Min

number

loadAverage15Min

number

cpuUtilizationPct

number

memoryUtilizationPct

number

uplinkExpand

object

interfacesExpand

required

object

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/devices/{deviceId}/statistics/latest" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "uptimeSec": 0,  "lastHeartbeatAt": "2024-01-01T00:00:00Z",  "nextHeartbeatAt": "2024-01-01T00:00:00Z",  "loadAverage1Min": 0,  "loadAverage5Min": 0,  "loadAverage15Min": 0,  "cpuUtilizationPct": 0,  "memoryUtilizationPct": 0,  "uplink": {    "txRateBps": 0,    "rxRateBps": 0  },  "interfaces": {    "radios": [      {        "frequencyGHz": 0,        "txRetriesPct": 0      }    ]  }}
```