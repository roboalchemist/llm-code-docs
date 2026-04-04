# UniFi API Architecture Guide

**Last Updated:** 2026-02-01

---

## UniFi Hierarchy

Understanding the UniFi API requires understanding the hierarchy:

```
Organization (unifi.ui.com account)
├── Site (Network deployment)
│   ├── Devices (APs, Switches, Gateways)
│   ├── Clients (Connected users/devices)
│   ├── Networks (VLANs)
│   ├── SSIDs (WiFi networks)
│   └── Firewall Rules
```

### Organization Level

An organization contains one or more sites. Each site is a separate network deployment.

```bash
GET /v1/organizations
```

### Site Level

A site is a specific network deployment (e.g., "Head Office", "Warehouse").

```bash
GET /v1/sites
GET /v1/sites/{siteId}
```

### Device Level

Devices are physical UniFi equipment (APs, switches, gateways).

```bash
GET /v1/sites/{siteId}/devices
GET /v1/sites/{siteId}/devices/{deviceId}
```

## Key Concepts

### Devices

Physical network equipment managed through UniFi:

- **Access Points (APs)** - WiFi radios (U6, U7, etc.)
- **Switches** - Network switches (USW-8, USW-48, etc.)
- **Gateways** - UDM, UDR, UDM-SE, etc.
- **Cameras** - UniFi Protect cameras (managed separately)

### Clients

Connected users and devices to the UniFi network:

- Associated via WiFi SSIDs
- Can be blocked/unblocked
- Provide statistics (throughput, signal strength)

### Networks (VLANs)

Logical network segments:

- Require a VLAN ID (1-4094)
- Have IPv4/IPv6 subnets
- Can have DHCP servers
- Support various purposes (General, Guest, IoT, etc.)

### SSIDs (WiFi Networks)

Wireless networks broadcasted by Access Points:

- Multiple SSIDs per site
- Each SSID connects to one or more networks
- Can be secured (WPA2/WPA3) or open
- Support band steering and airtime fairness

### Firewall Rules

Control traffic within and between networks:

- Ingress/Egress rules
- Based on protocols, ports, addresses
- Can allow, deny, or rate-limit traffic

## API Structure

### Base URL

```
https://api.ui.com/v1/
```

### Common Patterns

Most endpoints follow these patterns:

**List resources:**
```bash
GET /v1/sites/{siteId}/{resource}
```

**Get single resource:**
```bash
GET /v1/sites/{siteId}/{resource}/{id}
```

**Create resource:**
```bash
POST /v1/sites/{siteId}/{resource}
Content-Type: application/json

{ ... object definition ... }
```

**Update resource:**
```bash
PATCH /v1/sites/{siteId}/{resource}/{id}
Content-Type: application/json

{ ... updated fields ... }
```

**Delete resource:**
```bash
DELETE /v1/sites/{siteId}/{resource}/{id}
```

**Perform action:**
```bash
POST /v1/sites/{siteId}/{resource}/{id}/{action}
```

## Pagination

For endpoints returning lists, use pagination:

```bash
GET /v1/sites/{siteId}/devices?limit=50&offset=0
```

Response includes:

```json
{
  "data": [...],
  "meta": {
    "count": 100,
    "limit": 50,
    "offset": 0
  }
}
```

## Filtering & Sorting

Some endpoints support filtering and sorting:

```bash
GET /v1/sites/{siteId}/clients?filter=connected:true
GET /v1/sites/{siteId}/devices?sort=name
```

## Webhooks & Events

Real-time notifications via webhooks:

```bash
POST /v1/sites/{siteId}/events/subscribe
```

Events include:
- Device state changes
- Client connect/disconnect
- Firewall rule matches
- Network changes

## Data Models

### Device Model

```json
{
  "id": "device-id",
  "name": "AP-Living-Room",
  "model": "U6-LR",
  "mac": "a1:b2:c3:d4:e5:f6",
  "ip": "192.168.1.100",
  "uptime": 86400,
  "status": "connected",
  "signal_strength": -35,
  "clients": {
    "connected": 15,
    "authorized": 20
  }
}
```

### Client Model

```json
{
  "id": "client-id",
  "mac": "aa:bb:cc:dd:ee:ff",
  "hostname": "laptop",
  "ip": "192.168.1.50",
  "ssid": "Home Network",
  "signal_strength": -45,
  "tx_rate": 150000000,
  "rx_rate": 200000000,
  "bytes_sent": 1000000000,
  "bytes_received": 2000000000,
  "connected_at": 1609459200,
  "blocked": false
}
```

### Network Model

```json
{
  "id": "network-id",
  "name": "Guest Network",
  "vlan_id": 100,
  "subnet": "192.168.100.0/24",
  "gateway": "192.168.100.1",
  "dhcp_enabled": true,
  "dhcp_start": "192.168.100.100",
  "dhcp_end": "192.168.100.200",
  "dns_servers": ["192.168.100.1"]
}
```

## Error Handling

### Common Errors

| Status | Error | Cause |
|--------|-------|-------|
| 401 | Unauthorized | Invalid or missing API key |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource doesn't exist |
| 429 | Too Many Requests | Rate limited |
| 400 | Bad Request | Invalid parameters |

### Retry Strategy

```python
import time
import requests

def call_unifi_api(url, headers, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 429:  # Rate limited
                wait_time = int(response.headers.get('X-RateLimit-Reset', 60))
                time.sleep(wait_time)
                continue
            return response
        except requests.ConnectionError:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
    return None
```

## Performance Considerations

1. **Batch operations** - Get multiple resources in one call when possible
2. **Caching** - Cache device/network data locally
3. **Webhooks** - Use webhooks instead of polling for events
4. **Rate limits** - Respect rate limit headers
5. **Parallel requests** - Use async/threading for multiple API calls

## Security Best Practices

1. **API Key Rotation** - Regularly rotate API keys
2. **Scope Limiting** - Use least-privilege API keys when possible
3. **Network ACLs** - Restrict API access by IP when possible
4. **HTTPS Only** - Always use HTTPS (never HTTP)
5. **Secret Management** - Use secure secret storage (vaults, environment variables)
6. **Audit Logging** - Log all API operations
7. **Rate Limiting** - Implement client-side rate limiting

## Advanced Features

### Site Meshes

Connect multiple sites with mesh networking:

```bash
GET /v1/sites/{siteId}/meshes
```

### SD-WAN Configuration

Manage SD-WAN settings for advanced routing:

```bash
GET /v1/sites/{siteId}/sdwan
```

### Guest Portal

Configure guest network portal:

```bash
POST /v1/sites/{siteId}/guest-portal/configure
```

### Traffic Analysis

Deep packet inspection and QoS:

```bash
GET /v1/sites/{siteId}/traffic-analysis
```

## Building Production Applications

### Python SDK Pattern

```python
from typing import Optional, List
import requests
import os

class UniFiAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.ui.com/v1"

    def _request(self, method: str, endpoint: str, **kwargs):
        headers = kwargs.pop('headers', {})
        headers['X-API-Key'] = self.api_key
        headers['Content-Type'] = 'application/json'

        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, headers=headers, **kwargs)
        response.raise_for_status()
        return response.json()

    def get_sites(self) -> List[dict]:
        return self._request('GET', '/sites')['data']

    def get_devices(self, site_id: str) -> List[dict]:
        return self._request('GET', f'/sites/{site_id}/devices')['data']

    def get_clients(self, site_id: str) -> List[dict]:
        return self._request('GET', f'/sites/{site_id}/clients')['data']

    def block_client(self, site_id: str, client_id: str) -> dict:
        return self._request('POST', f'/sites/{site_id}/clients/{client_id}/block')

# Usage
api = UniFiAPI(os.environ['UNIFI_API_KEY'])
devices = api.get_devices('site-123')
```

---

**See Also:**
- Quick Start Guide
- API Reference
- Common Use Cases
