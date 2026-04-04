# post-v1camerasidtalkback-session

Source: https://developer.ui.com/protect/v6.2.83/post-v1camerasidtalkback-session

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Create talkback session for camera

POST`/v1/cameras/{id}/talkback-session`

Returns the talkback stream URL and audio configuration for a specific camera

path Parameters

id

required

string

The primary key of camera

## Responses

200

Response Schema: application/json

url

required

string

Talkback stream URL

codec

required

string

Audio format to use.

samplingRate

required

integer

Sampling Rate.

bitsPerSample

required

integer

Bits per sample.

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/protect/v6.2.83/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g -X POST "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/protect/integration/v1/cameras/{id}/talkback-session" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "url": "https://example.com",  "codec": "string",  "samplingRate": 0,  "bitsPerSample": 0}
```