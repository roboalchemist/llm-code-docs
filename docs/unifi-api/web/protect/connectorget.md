# connectorget

Source: https://developer.ui.com/protect/v6.2.83/connectorget

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Connector - GET

GET`/v1/connector/consoles/{id}/*path`

Forward GET requests to UniFi applications using RESTful HTTP methods.

**Request Flow**: The request is proxied through `api.ui.com` cloud endpoint to the remote console at `http://127.0.0.1/proxy/[path]` with GET method.

**Requirements**:
- Console firmware version must >= 5.0.3
- For non-organization API keys: Limited to API key owner's consoles only (cannot access other admins' consoles)
- For organization API keys: Can access any console within the organization

**API Documentation**:
- Network API: [https://developer.ui.com/network](/network)
- Protect API: [https://developer.ui.com/protect](/protect)

**Examples**:
- Network: `GET /v1/connector/consoles/\{id\}/network/integration/v1/sites` retrieves network sites
- Protect: `GET /v1/connector/consoles/\{id\}/protect/integration/v1/meta/info` retrieves protect application info

**Response**: On success, the upstream API response is passed through directly. On error, a standardized error schema is returned.

path Parameters

id

required

string

Host ID to proxy the request to

path

required

string

API path to proxy

## Responses

200400401403408429500502

Response Schema: application/json