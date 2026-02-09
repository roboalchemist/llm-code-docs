# getconnectedclientdetails

Source: https://developer.ui.com/network/v10.1.68/getconnectedclientdetails

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get Connected Client Details

GET`/v1/sites/{siteId}/clients/{clientId}`

Retrieve detailed information about a specific connected client, including name, IP address, MAC address, connection type and access information.

path Parameters

clientId

required

string

siteId

required

string

## Responses

200

Response Schema: application/json

type

required

string

WIREDWIRELESSVPNTELEPORT

id

required

string

name

required

string

connectedAt

string

ipAddress

string

accessExpand

required

object (Local client access details)

Represents the type of network access and/or any applicable authorization status the client is using.
- \*\*Wired clients\*\* may have direct access without additional authorization.
- \*\*Wireless clients\*\* can be connected via a protected network or an open network
that may require additional authorization (e.g., a guest portal).
- \*\*VPN clients\*\* may have different authorization mechanisms.
Currently, the only two supported access types are `GUEST` (used for wired and wireless guest clients)
and `DEFAULT` (a placeholder, which might be refined in the future releases, used for all other clients).
Filtering is possible by `access.type`, for example `access.type.eq('GUEST')` to list guest clients.

macAddress

string

uplinkDeviceId

string

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

Response Sample

200

```
{  "type": "string",  "id": "00000000-0000-0000-0000-000000000000",  "name": "string",  "connectedAt": "2024-01-01T00:00:00Z",  "ipAddress": "string",  "access": null}
```