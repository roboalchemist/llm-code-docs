# createvouchers

Source: https://developer.ui.com/network/v10.1.68/createvouchers

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Generate Vouchers

POST`/v1/sites/{siteId}/hotspot/vouchers`

Create one or more Hotspot vouchers.

path Parameters

siteId

required

string

request Body

count

integer

Number of vouchers to generate

name

required

string

Voucher note, duplicated across all generated vouchers

authorizedGuestLimit

integer

(Optional) limit for how many different guests can use the same voucher to authorize network access

timeLimitMinutes

required

integer

How long (in minutes) the voucher will provide access to the network since authorization of the first guest.
Subsequently connected guests, if allowed, will share the same expiration time.

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

201

Response Schema: application/json

vouchersExpand

Array of object (Hotspot voucher details)

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/hotspot/vouchers" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>" \-H "Content-Type: application/json" \-d "{  \"count\": 0,  \"name\": \"string\",  \"authorizedGuestLimit\": 1,  \"timeLimitMinutes\": 0,  \"dataUsageLimitMBytes\": 0,  \"rxRateLimitKbps\": 0,  \"txRateLimitKbps\": 0}"
```

Response Sample

201

```
{  "vouchers": [    {      "id": "00000000-0000-0000-0000-000000000000",      "createdAt": "2024-01-01T00:00:00Z",      "name": "string",      "code": "string",      "authorizedGuestLimit": 0,      "authorizedGuestCount": 0,      "activatedAt": "2024-01-01T00:00:00Z",      "expiresAt": "2024-01-01T00:00:00Z",      "expired": true,      "timeLimitMinutes": 0,      "dataUsageLimitMBytes": 0,      "rxRateLimitKbps": 0,      "txRateLimitKbps": 0    }  ]}
```