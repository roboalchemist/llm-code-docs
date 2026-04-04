# get-v1camerasidrtsps-stream

Source: https://developer.ui.com/protect/v6.2.83/get-v1camerasidrtsps-stream

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get RTSPS streams for camera

GET`/v1/cameras/{id}/rtsps-stream`

Returns existing RTSPS stream URLs for camera

path Parameters

id

required

string

The primary key of camera

## Responses

200

Response Schema: application/json

high

stringnull

medium

stringnull

low

stringnull

package

stringnull

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/protect/v6.2.83/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/protect/integration/v1/cameras/{id}/rtsps-stream" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "high": null,  "medium": null,  "low": null,  "package": null}
```