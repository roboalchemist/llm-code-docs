# getnetworkreferences

Source: https://developer.ui.com/network/v10.1.68/getnetworkreferences

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get Network References

GET`/v1/sites/{siteId}/networks/{networkId}/references`

Retrieve references to a specific network.

path Parameters

networkId

required

string

siteId

required

string

## Responses

200

Response Schema: application/json

referenceResourcesExpand

required

Array of object (Network reference resource)

List of network reference resources

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/network/v10.1.68/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/network/integration/v1/sites/{siteId}/networks/{networkId}/references" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "referenceResources": [    {      "resourceType": "CLIENT",      "referenceCount": 0,      "references": [        {          "referenceId": "00000000-0000-0000-0000-000000000000"        }      ]    }  ]}
```