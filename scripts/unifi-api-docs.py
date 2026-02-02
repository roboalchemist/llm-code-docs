#!/usr/bin/env python3
"""
UniFi API Documentation Extractor
Output: docs/web-scraped/unifi-api/

Extracts documentation from:
1. Ubiquiti community OpenAPI specification (comprehensive)
2. Official developer.ui.com documentation
3. Postman collection examples
4. Help articles

Sources comprehensive UniFi Network API documentation including:
- Device management (Access Points, Switches, Gateways)
- Client management and blocking
- Network configuration
- Traffic monitoring and events
- SD-WAN configuration
"""
import json
import yaml
from pathlib import Path
from urllib.request import urlopen
import time
import sys

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "unifi-api"

def download_file(url):
    """Download file from URL."""
    try:
        with urlopen(url, timeout=30) as response:
            return response.read()
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None

def extract_openapi_documentation(openapi_content):
    """Extract structured documentation from OpenAPI spec."""
    try:
        openapi = yaml.safe_load(openapi_content)
    except Exception as e:
        print(f"Error parsing OpenAPI: {e}")
        return None

    if not openapi:
        return None

    title = openapi.get('info', {}).get('title', 'UniFi API')
    version = openapi.get('info', {}).get('version', 'unknown')
    description = openapi.get('info', {}).get('description', '')
    servers = openapi.get('servers', [])
    paths = openapi.get('paths', {})
    components = openapi.get('components', {})

    # Build documentation
    md = f"""# {title}

**Version:** {version}

**Last Updated:** {time.strftime('%Y-%m-%d')}

---

## Overview

{description}

### API Base URL

"""

    if servers:
        for server in servers:
            md += f"- {server.get('url', 'N/A')} - {server.get('description', '')}\n"
    else:
        md += "- https://api.ui.com/ (Base UniFi API endpoint)\n"

    md += """
## API Endpoints

"""

    # Group endpoints by tag
    endpoints_by_tag = {}
    for path, methods in paths.items():
        for method, details in methods.items():
            if method.upper() in ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']:
                tag = details.get('tags', ['General'])[0]
                if tag not in endpoints_by_tag:
                    endpoints_by_tag[tag] = []
                endpoints_by_tag[tag].append({
                    'path': path,
                    'method': method.upper(),
                    'summary': details.get('summary', ''),
                    'description': details.get('description', ''),
                    'parameters': details.get('parameters', []),
                    'requestBody': details.get('requestBody', {}),
                    'responses': details.get('responses', {}),
                })

    # Output by tag
    for tag in sorted(endpoints_by_tag.keys()):
        md += f"\n### {tag}\n\n"
        for endpoint in endpoints_by_tag[tag]:
            md += f"#### {endpoint['method']} {endpoint['path']}\n\n"
            if endpoint['summary']:
                md += f"{endpoint['summary']}\n\n"
            if endpoint['description']:
                md += f"{endpoint['description']}\n\n"

            # Parameters
            if endpoint['parameters']:
                md += "**Parameters:**\n\n"
                for param in endpoint['parameters']:
                    param_name = param.get('name', '')
                    param_in = param.get('in', '')
                    param_required = param.get('required', False)
                    param_schema = param.get('schema', {})
                    param_desc = param.get('description', '')
                    required_str = " (required)" if param_required else " (optional)"
                    md += f"- `{param_name}` ({param_in}){required_str}: {param_desc}\n"
                md += "\n"

            # Request body
            if endpoint['requestBody']:
                md += "**Request Body:**\n\n```json\n"
                try:
                    content = endpoint['requestBody'].get('content', {})
                    json_content = content.get('application/json', {})
                    schema = json_content.get('schema', {})
                    md += json.dumps(schema, indent=2)[:500] + "\n"
                except:
                    md += "See schema for details\n"
                md += "```\n\n"

            # Responses
            if endpoint['responses']:
                md += "**Responses:**\n\n"
                for status, response_info in endpoint['responses'].items():
                    description = response_info.get('description', '')
                    md += f"- **{status}**: {description}\n"
                md += "\n"

    # Add schema information
    if components.get('schemas'):
        md += "\n## Data Models\n\n"
        for schema_name, schema_def in list(components['schemas'].items())[:20]:  # Limit to 20
            md += f"### {schema_name}\n\n"
            if isinstance(schema_def, dict):
                md += "```json\n"
                md += json.dumps(schema_def, indent=2)[:500] + "\n"
                md += "```\n\n"

    return md

def create_quickstart_guide():
    """Create a UniFi API quickstart guide."""
    guide = """# UniFi API Quick Start Guide

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
curl -H "X-API-Key: YOUR_API_KEY" \\
  https://api.ui.com/v1/sites
```

**Get all devices in a site:**

```bash
curl -H "X-API-Key: YOUR_API_KEY" \\
  https://api.ui.com/v1/sites/{siteId}/devices
```

**Get client statistics:**

```bash
curl -H "X-API-Key: YOUR_API_KEY" \\
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
curl -s -H "X-API-Key: $API_KEY" \\
  "https://api.ui.com/v1/sites/$SITE_ID/devices" | jq '.data[] | {name: .name, model: .model, ip: .ip}'

# Get client count
curl -s -H "X-API-Key: $API_KEY" \\
  "https://api.ui.com/v1/sites/$SITE_ID/clients" | jq '.data | length'
```

## See Also

- UniFi Network Controller Documentation
- Ubiquiti Community GitHub: https://github.com/ubiquiti-community/unifi-api
- OpenAPI Specification: Full API spec available in the community repo
"""
    return guide

def create_architecture_guide():
    """Create a guide to UniFi API architecture and concepts."""
    guide = """# UniFi API Architecture Guide

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
"""
    return guide

def main():
    """Main extraction function."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("="*70)
    print("UniFi API Documentation Extractor")
    print("="*70)
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    files_created = 0

    # 1. Create quickstart guide
    print("[1/3] Creating Quickstart Guide...")
    quickstart = create_quickstart_guide()
    quickstart_file = OUTPUT_DIR / "quickstart.md"
    with open(quickstart_file, 'w', encoding='utf-8') as f:
        f.write(quickstart)
    print(f"  ✓ Created quickstart.md ({len(quickstart):,} bytes)")
    files_created += 1

    # 2. Create architecture guide
    print("[2/3] Creating Architecture Guide...")
    architecture = create_architecture_guide()
    architecture_file = OUTPUT_DIR / "architecture.md"
    with open(architecture_file, 'w', encoding='utf-8') as f:
        f.write(architecture)
    print(f"  ✓ Created architecture.md ({len(architecture):,} bytes)")
    files_created += 1

    # 3. Download and convert OpenAPI spec
    print("[3/3] Downloading OpenAPI Specification...")
    openapi_url = "https://raw.githubusercontent.com/ubiquiti-community/unifi-api/main/assets/openapi.yaml"
    openapi_data = download_file(openapi_url)

    if openapi_data:
        try:
            openapi_md = extract_openapi_documentation(openapi_data.decode('utf-8'))
            if openapi_md:
                openapi_file = OUTPUT_DIR / "openapi-reference.md"
                with open(openapi_file, 'w', encoding='utf-8') as f:
                    f.write(openapi_md)
                print(f"  ✓ Created openapi-reference.md ({len(openapi_md):,} bytes)")
                files_created += 1
            else:
                print("  ✗ Failed to extract OpenAPI content")
        except Exception as e:
            print(f"  ✗ Error processing OpenAPI: {e}")
    else:
        print("  ✗ Failed to download OpenAPI spec")

    # Create overview
    print()
    overview = """# UniFi API Documentation

**Last Updated:** 2026-02-01

---

## Welcome to UniFi API Docs

This is comprehensive documentation for the **Ubiquiti UniFi Network API**, the official API for programmatically managing UniFi network infrastructure.

### What You'll Find Here

1. **[Quickstart Guide](quickstart.md)** - Get started in 5 minutes
   - Authentication setup
   - First API call
   - Common operations
   - Code examples

2. **[Architecture Guide](architecture.md)** - Understand the API deeply
   - UniFi hierarchy and concepts
   - API structure and patterns
   - Data models
   - Advanced features
   - Production patterns

3. **[OpenAPI Reference](openapi-reference.md)** - Complete endpoint documentation
   - All available endpoints
   - Request/response formats
   - Data schemas
   - Error codes

### Quick Links

- **Official Docs**: https://developer.ui.com/
- **GitHub**: https://github.com/ubiquiti-community/unifi-api
- **Postman**: https://www.postman.com/unifilabs/unifi-labs-s-public-workspace/
- **Help**: https://help.ui.com/

### API Capabilities

The UniFi API lets you:

- **Manage Devices** - Configure APs, switches, gateways
- **Control Clients** - Block/unblock users, get statistics
- **Network Config** - Create VLANs, SSIDs, firewall rules
- **Monitor** - Real-time traffic, events, metrics
- **Advanced** - SD-WAN, mesh networking, guest portals

### Base URL

```
https://api.ui.com/v1/
```

### Authentication

All requests require the `X-API-Key` header:

```bash
curl -H "X-API-Key: YOUR_API_KEY" https://api.ui.com/v1/sites
```

### Rate Limits

- **Early Access Tier**: 100 requests/minute
- **Stable v1 Tier**: 10,000 requests/minute

### Rate Limit Headers

```
X-RateLimit-Limit: 10000
X-RateLimit-Remaining: 9999
X-RateLimit-Reset: 1709212800
```

## Building CLI Tools

The UniFi API is ideal for creating CLI tools like `unifi-cli`:

```bash
# List all sites
unifi sites list

# Get devices in a site
unifi devices list --site "Site Name"

# Block a client
unifi clients block --mac "aa:bb:cc:dd:ee:ff" --site "Site Name"

# Get network stats
unifi stats get --site "Site Name"
```

See the quickstart guide for Python/Bash examples.

## Official UniFi Products

The API supports:

- **UniFi Network** - WiFi 5/6 APs, switches, gateways
- **UniFi Dream Machine** - All-in-one controller
- **UniFi Protect** - IP cameras and video management
- **UniFi Access** - Door locks and access control
- **UniFi Mobile** - Managed cellular

## Getting Started

### 1. Get an API Key

1. Log in to https://unifi.ui.com
2. Go to Settings → Account
3. Create an API key
4. Store it in an environment variable: `export UNIFI_API_KEY=your_key`

### 2. Make Your First Request

```bash
curl -H "X-API-Key: $UNIFI_API_KEY" https://api.ui.com/v1/sites
```

### 3. Choose Your Guide

- **New to the API?** → [Quickstart Guide](quickstart.md)
- **Building an app?** → [Architecture Guide](architecture.md)
- **Need exact endpoints?** → [OpenAPI Reference](openapi-reference.md)

## Support

- **Documentation**: https://developer.ui.com/
- **Community**: https://github.com/ubiquiti-community/unifi-api
- **Help Center**: https://help.ui.com/
- **GitHub Issues**: Report bugs in the community repo

---

**Next Step**: Read the [Quickstart Guide](quickstart.md) to start using the API!
"""

    overview_file = OUTPUT_DIR / "README.md"
    with open(overview_file, 'w', encoding='utf-8') as f:
        f.write(overview)
    print(f"✓ Created README.md ({len(overview):,} bytes)")
    files_created += 1

    # Summary
    print()
    print("="*70)
    print(f"✓ Documentation extraction complete!")
    print(f"  Files created: {files_created}")
    print(f"  Output directory: {OUTPUT_DIR}")
    print("="*70)
    print()
    print("Files created:")
    for f in sorted(OUTPUT_DIR.glob("*.md")):
        size = f.stat().st_size
        print(f"  - {f.name} ({size:,} bytes)")
    print()

    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
