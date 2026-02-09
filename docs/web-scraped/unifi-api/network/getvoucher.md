# getvoucher

Source: https://developer.ui.com/network/v10.1.68/getvoucher

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get Voucher Details

GET`/v1/sites/{siteId}/hotspot/vouchers/{voucherId}`

Retrieve details of a specific Hotspot voucher.

path Parameters

voucherId

required

string

siteId

required

string

## Responses

200

Response Schema: application/json

id

required

string

createdAt

required

string

name

required

string

Voucher note, may contain duplicate values across multiple vouchers

code

required

string

Secret code to active the voucher using the Hotspot portal

authorizedGuestLimit

integer

(Optional) limit for how many different guests can use the same voucher to authorize network access

authorizedGuestCount

required

integer

For how many guests the voucher has been used to authorize network access

activatedAt

string

(Optional) timestamp when the voucher has been activated (authorization time of the first guest)

expiresAt

string

(Optional) timestamp when the voucher will become expired. All guests using the voucher will be unauthorized from network access

expired

required

boolean

Whether the voucher has been expired and can no longer be used to authorize network access

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

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/hotspot/vouchers/{voucherId}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "id": "00000000-0000-0000-0000-000000000000",  "createdAt": "2024-01-01T00:00:00Z",  "name": "string",  "code": "string",  "authorizedGuestLimit": 0,  "authorizedGuestCount": 0,  "activatedAt": "2024-01-01T00:00:00Z",  "expiresAt": "2024-01-01T00:00:00Z",  "expired": true,  "timeLimitMinutes": 0,  "dataUsageLimitMBytes": 0,  "rxRateLimitKbps": 0,  "txRateLimitKbps": 0}
```