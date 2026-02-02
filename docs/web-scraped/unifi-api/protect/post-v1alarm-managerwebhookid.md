# post-v1alarm-managerwebhookid

Source: https://developer.ui.com/protect/v6.2.83/post-v1alarm-managerwebhookid

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Send a webhook to the alarm manager

POST`/v1/alarm-manager/webhook/{id}`

Send a webhook to the alarm manager to trigger configured alarms

path Parameters

id

required

string

User defined string used to trigger only specific alarms. Alarm should be configured with the same ID to be triggered.

## Responses

204400

Response 204: No schema content available

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/protect/v6.2.83/connectorpost) which requires FW version >= 5.0.3

Response Sample

400

```
{  "error": "string",  "name": "string",  "cause": {}}
```