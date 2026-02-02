# post-v1camerasidrtsps-stream

Source: https://developer.ui.com/protect/v6.2.83/post-v1camerasidrtsps-stream

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Create RTSPS streams for camera

POST`/v1/cameras/{id}/rtsps-stream`

Returns RTSPS stream URLs for specified quality levels

path Parameters

id

required

string

The primary key of camera

request Body

qualitiesExpand

required

Array of string

Array of quality levels of RTSPS streams

## Responses

200

Response Schema: application/json

high

string

medium

string

low

string

package

string

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/protect/v6.2.83/connectorpost) which requires FW version >= 5.0.3

Response Sample

200

```
{  "high": "https://example.com",  "medium": "https://example.com",  "low": "https://example.com",  "package": "https://example.com"}
```