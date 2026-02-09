# deletevoucher

Source: https://developer.ui.com/network/v10.1.68/deletevoucher

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Delete Voucher

DELETE`/v1/sites/{siteId}/hotspot/vouchers/{voucherId}`

Remove a specific Hotspot voucher.

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

vouchersDeleted

integer

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g -X DELETE "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/hotspot/vouchers/{voucherId}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "vouchersDeleted": 0}
```