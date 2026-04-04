# UniFi API Quick Start Guide

**Last Updated:** 2026-02-01

---

## What is the UniFi API?

The UniFi API allows you to programmatically control and monitor Ubiquiti UniFi network infrastructure. This includes:

- **Access Points (APs)** - Manage WiFi 5/6 APs
- **Switches** - Control network switches and port configurations
- **Gateways** - UDM, UDR, and other gateway devices
- **Clients** - List, block/unblock, and monitor connected devices
- **Networks** - Create and configure VLANs and SSIDs
- **Monitoring** - Real-time traffic, events, and statistics
- **Advanced Features** - Port forwarding, firewall rules, DNS, SD-WAN

## Getting Started

### 1. Authentication

The UniFi API uses API key authentication via the `X-API-Key` header.

```bash
curl -H "X-API-Key: YOUR_API_KEY" https://api.ui.com/v1/sites
```

**Obtaining an API Key:**
1. Log in to UniFi Site Manager at unifi.ui.com
2. Go to Settings → Account
3. Create an API key with appropriate permissions
4. Store the key securely (use environment variables in production)

### 2. Rate Limiting

Different API tiers have different rate limits:

- **Early Access**: 100 requests/minute
- **Stable v1**: 10,000 requests/minute

Check rate limit headers in responses:
```
X-RateLimit-Limit: 10000
X-RateLimit-Remaining: 9999
X-RateLimit-Reset: 1709212800
```

### 3. Making Your First API Call

**List all sites:**

```bash
curl -H "X-API-Key: YOUR_API_KEY" \
  https://api.ui.com/v1/sites
```

**Get all devices in a site:**

```bash
curl -H "X-API-Key: YOUR_API_KEY" \
  https://api.ui.com/v1/sites/{siteId}/devices
```

**Get client statistics:**

```bash
curl -H "X-API-Key: YOUR_API_KEY" \
  https://api.ui.com/v1/sites/{siteId}/clients
```

## Common Use Cases

### Device Management

**List all devices in a site:**
```bash
GET /v1/sites/{siteId}/devices
```

**Get device details:**
```bash
GET /v1/sites/{siteId}/devices/{deviceId}
```

**Reboot a device:**
```bash
POST /v1/sites/{siteId}/devices/{deviceId}/reboot
```

### Client Management

**List all clients:**
```bash
GET /v1/sites/{siteId}/clients
```

**Get client details:**
```bash
GET /v1/sites/{siteId}/clients/{clientId}
```

**Block a client:**
```bash
POST /v1/sites/{siteId}/clients/{clientId}/block
```

**Unblock a client:**
```bash
POST /v1/sites/{siteId}/clients/{clientId}/unblock
```

### Network Configuration

**List networks/VLANs:**
```bash
GET /v1/sites/{siteId}/networks
```

**Create a new network:**
```bash
POST /v1/sites/{siteId}/networks
Content-Type: application/json

{
  "name": "Guest Network",
  "vlan_id": 100,
  "subnet": "192.168.100.0/24"
}
```

**List SSIDs:**
```bash
GET /v1/sites/{siteId}/ssids
```

### Monitoring & Events

**Get site statistics:**
```bash
GET /v1/sites/{siteId}/stats
```

**Get events:**
```bash
GET /v1/sites/{siteId}/events
```

**Get traffic metrics:**
```bash
GET /v1/sites/{siteId}/traffic
```

## Response Format

All API responses are JSON. Success responses include the data directly or wrapped in a `data` field.

**Successful response (200):**
```json
{
  "data": {
    "id": "site-id",
    "name": "My Site",
    "role": "admin"
  }
}
```

**Error response (4xx/5xx):**
```json
{
  "meta": {
    "rc": "error",
    "msg": "Invalid API key"
  }
}
```

## Best Practices

1. **Store API keys securely** - Use environment variables, not hardcoded strings
2. **Implement retry logic** - Handle rate limiting with exponential backoff
3. **Use specific sites** - Always specify siteId in requests
4. **Monitor rate limits** - Check X-RateLimit headers
5. **Error handling** - Check response status and error messages
6. **Pagination** - Use limit/offset for large result sets
7. **Caching** - Cache data locally to reduce API calls

## Error Codes

Common HTTP status codes:

- **200** - Success
- **400** - Bad request (invalid parameters)
- **401** - Unauthorized (invalid/missing API key)
- **403** - Forbidden (insufficient permissions)
- **404** - Not found (resource doesn't exist)
- **429** - Too many requests (rate limited)
- **500** - Server error

## Useful Links

- **Official Docs**: https://developer.ui.com/
- **API Portal**: https://unifi.ui.com/api
- **Help & Support**: https://help.ui.com/
- **Getting Started**: https://help.ui.com/hc/en-us/articles/30076656117655
- **Postman Collection**: https://www.postman.com/unifilabs/unifi-labs-s-public-workspace/

## Building CLI Tools

The UniFi API is perfect for building CLI tools to manage your network:

### Python Example

```python
import requests
import os

class UniFiClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.ui.com/v1"
        self.session = requests.Session()
        self.session.headers.update({"X-API-Key": api_key})

    def get_sites(self):
        return self.session.get(f"{self.base_url}/sites").json()

    def get_devices(self, site_id):
        return self.session.get(
            f"{self.base_url}/sites/{site_id}/devices"
        ).json()

    def block_client(self, site_id, client_id):
        return self.session.post(
            f"{self.base_url}/sites/{site_id}/clients/{client_id}/block"
        ).json()

# Usage
api_key = os.environ.get("UNIFI_API_KEY")
client = UniFiClient(api_key)
sites = client.get_sites()
print(f"Sites: {sites}")
```

### Bash Example

```bash
#!/bin/bash

API_KEY="${UNIFI_API_KEY}"
SITE_ID="${1}"

# Get all devices
curl -s -H "X-API-Key: $API_KEY" \
  "https://api.ui.com/v1/sites/$SITE_ID/devices" | jq '.data[] | {name: .name, model: .model, ip: .ip}'

# Get client count
curl -s -H "X-API-Key: $API_KEY" \
  "https://api.ui.com/v1/sites/$SITE_ID/clients" | jq '.data | length'
```

## See Also

- UniFi Network Controller Documentation
- Ubiquiti Community GitHub: https://github.com/ubiquiti-community/unifi-api
- OpenAPI Specification: Full API spec available in the community repo
