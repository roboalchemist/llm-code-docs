# executeconnectedclientaction

Source: https://developer.ui.com/network/v10.1.68/executeconnectedclientaction

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Execute Client Action

POST`/v1/sites/{siteId}/clients/{clientId}/actions`

Perform an action on a specific connected client. The request body must include the action name and any applicable input arguments.

path Parameters

clientId

required

string

siteId

required

string

request Body

action

required

string

AUTHORIZE\_GUEST\_ACCESSUNAUTHORIZE\_GUEST\_ACCESS

timeLimitMinutes

integer

(Optional) how long (in minutes) the guest will be authorized to access the network.
If not specified, the default limit is used from the site settings

dataUsageLimitMBytes

integer

(Optional) data usage limit in megabytes

rxRateLimitKbps

integer

(Optional) download rate limit in kilobits per second

txRateLimitKbps

integer

(Optional) upload rate limit in kilobits per second

## Responses

200

Response Schema: application/json

action

required

string

AUTHORIZE\_GUEST\_ACCESSUNAUTHORIZE\_GUEST\_ACCESS

revokedAuthorizationExpand

object

(Optional) Revoked authorization in case the guest was already authorized at the time of this request

grantedAuthorizationExpand

object

Granted guest authorization

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/clients/{clientId}/actions" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>" \-H "Content-Type: application/json" \-d "{  \"action\": \"string\"}"
```

Response Sample

200

```
{  "action": "string"}
```