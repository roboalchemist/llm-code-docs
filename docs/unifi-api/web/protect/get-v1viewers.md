# get-v1viewers

Source: https://developer.ui.com/protect/v6.2.83/get-v1viewers

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get all viewers

GET`/v1/viewers`

Get detailed information about all viewers

## Responses

200

Response Schema: application/json

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/protect/v6.2.83/connectorpost) which requires FW version >= 5.0.3

Response Sample

200

```
[  {    "id": "string",    "modelKey": "string",    "state": "CONNECTED",    "name": "string",    "mac": "string",    "liveview": "string",    "streamLimit": 0  }]
```