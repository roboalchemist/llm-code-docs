# Datadog Python API Client - Complete Reference

**Source:** https://docs.datadoghq.com/api/latest/?tab=python
**Repository:** https://github.com/DataDog/datadog-api-client-python
**Official Docs:** https://datadoghq.dev/datadog-api-client-python/

## Table of Contents

1. [Installation](#installation)
2. [Authentication](#authentication)
3. [Core Components](#core-components)
4. [Configuration](#configuration)
5. [API Operations](#api-operations)
6. [Examples](#examples)
7. [Advanced Features](#advanced-features)

---

## Installation

### Basic Installation

Install the Python client library using pip:

```bash
pip install datadog-api-client
```

### With Async Support

For asynchronous operations, include the async extra:

```bash
pip install datadog-api-client[async]
```

### Requirements

- Python 3.8 or higher
- Required dependencies are automatically installed with pip

---

## Authentication

### Environment Variables (Default)

The client reads credentials from environment variables by default:

```bash
export DD_API_KEY="<YOUR_API_KEY>"
export DD_APP_KEY="<YOUR_APPLICATION_KEY>"
```

### Manual Configuration

Configure credentials directly in your code:

```python
from datadog_api_client import ApiClient, Configuration

configuration = Configuration()
configuration.api_key["apiKeyAuth"] = "<YOUR_API_KEY>"
configuration.api_key["appKeyAuth"] = "<YOUR_APPLICATION_KEY>"
```

### Server Configuration

Switch between Datadog instances (e.g., EU):

```python
configuration.server_variables["site"] = "datadoghq.eu"
```

Available sites:
- `datadoghq.com` (US, default)
- `datadoghq.eu` (EU)

---

## Core Components

### ApiClient (Synchronous)

The standard synchronous client for API operations:

```python
from datadog_api_client import ApiClient, Configuration

configuration = Configuration()
with ApiClient(configuration) as api_client:
    # Use api_client with various API classes
    pass
```

### AsyncApiClient (Asynchronous)

For async/await patterns with non-blocking operations:

```python
from datadog_api_client import AsyncApiClient, Configuration
import asyncio

configuration = Configuration()

async def main():
    async with AsyncApiClient(configuration) as api_client:
        # Use async API operations
        pass

asyncio.run(main())
```

Requires: `pip install datadog-api-client[async]`

### ThreadedApiClient

For thread-based concurrent operations:

```python
from datadog_api_client import ThreadedApiClient, Configuration

configuration = Configuration()
api_client = ThreadedApiClient(configuration)
# Returns AsyncResult objects for each API call
```

### Configuration Object

Central configuration management for the API client:

```python
from datadog_api_client import Configuration

configuration = Configuration()
configuration.api_key["apiKeyAuth"] = "<API_KEY>"
configuration.api_key["appKeyAuth"] = "<APP_KEY>"
configuration.debug = True  # Enable request/response logging
configuration.compress = False  # Disable GZIP compression
configuration.server_variables["site"] = "datadoghq.eu"
configuration.proxy = "http://proxy.example.com:8080"
```

---

## Configuration

### Request/Response Compression

Control GZIP compression (enabled by default):

```python
configuration.compress = False
```

### Debug Logging

Enable detailed request and response logging:

```python
configuration.debug = True
```

### Proxy Configuration

Route API requests through a proxy:

```python
configuration.proxy = "http://user:password@proxy.example.com:8080"
```

### Retry Configuration

Enable automatic retries for rate-limit errors (429 status):

```python
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

# Simple retry with custom count
configuration.max_retries = 5

# Advanced retry policy
retry_policy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504]
)
```

### Unstable/Beta Endpoints

Enable experimental API endpoints:

```python
configuration.unstable_operations["list_log_indexes"] = True
configuration.unstable_operations["create_scenario"] = True
```

---

## API Operations

### Supported API Versions

The library provides access to both v1 and v2 API endpoints:

- **v1 API:** Legacy endpoints in `datadog_api_client.v1`
- **v2 API:** Current endpoints in `datadog_api_client.v2`

### API Classes (v2)

Common API classes available in `datadog_api_client.v2.api`:

```python
from datadog_api_client.v2.api import (
    APMApi,                          # Application Performance Monitoring
    AuditApi,                        # Audit logs and trails
    CaseManagementApi,               # Case management
    CloudCostManagementApi,          # Cloud cost analysis
    DashboardsApi,                   # Dashboard management
    IncidentsApi,                    # Incident management
    LogsApi,                         # Log ingestion and querying
    MetricsApi,                      # Metrics and timeseries
    MonitorsApi,                     # Monitor and alerting
    OpsgenieIntegrationApi,          # Opsgenie integration
    SecurityMonitoringApi,           # Security monitoring rules
    SyntheticsApi,                   # Synthetic monitoring
    UsersApi,                        # User management
)
```

### Example: Create a Monitor

```python
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor import Monitor
from datadog_api_client.v2.model.monitor_type import MonitorType

body = Monitor(
    name="Test Monitor",
    type=MonitorType.METRIC_ALERT,
    query="avg(last_5m):avg:system.cpu{*} > 0.5",
)

with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)
    print(response)
```

---

## Examples

### Example 1: Get Service List (APM)

```python
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apm_api import APMApi

configuration = Configuration()

with ApiClient(configuration) as api_client:
    api_instance = APMApi(api_client)
    response = api_instance.get_service_list()
    print(response)
```

### Example 2: Create a Monitor

```python
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor import Monitor
from datadog_api_client.v2.model.monitor_type import MonitorType

configuration = Configuration()

body = Monitor(
    name="My Test Monitor",
    type=MonitorType.METRIC_ALERT,
    query="avg(last_5m):avg:system.memory.free{*} > 100000000",
    message="Test message",
)

with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)
    print(response)
```

### Example 3: Query Logs

```python
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi
from datadog_api_client.v2.model.logs_list_request import LogsListRequest

configuration = Configuration()

body = LogsListRequest(
    filter={
        "from": "2024-01-01",
        "to": "2024-01-31",
        "query": "status:error",
    },
    page={"limit": 10},
)

with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.list_logs(body=body)
    print(response)
```

### Example 4: List Dashboards

```python
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboards_api import DashboardsApi

configuration = Configuration()

with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.list_dashboards()
    print(response)
```

### Example 5: Async Operations

```python
from datadog_api_client import AsyncApiClient, Configuration
from datadog_api_client.v2.api.apm_api import APMApi
import asyncio

async def main():
    configuration = Configuration()

    async with AsyncApiClient(configuration) as api_client:
        api_instance = APMApi(api_client)
        response = await api_instance.get_service_list()
        print(response)

asyncio.run(main())
```

---

## Advanced Features

### Pagination

List operations include built-in pagination methods:

```python
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboards_api import DashboardsApi

configuration = Configuration()

with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)

    # Retrieve paginated results
    response = api_instance.list_dashboards(page_size=10)

    # Iterate through pages
    for dashboard in response.data:
        print(dashboard)
```

### Rate Limit Handling

The library automatically handles rate limits (429 responses) when retry is configured:

```python
configuration.max_retries = 5  # Automatically retry on 429
```

The Retry-After header is respected, and backoff is applied automatically.

### Error Handling

Handle API errors gracefully:

```python
from datadog_api_client.exceptions import ApiException

try:
    response = api_instance.create_monitor(body=body)
except ApiException as e:
    print(f"Error: {e.status} - {e.reason}")
    print(f"Response body: {e.body}")
```

### Context Manager Pattern

Use context managers for proper resource cleanup:

```python
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.list_monitors()
    # Client automatically closed after the with block
```

### Custom Headers

Add custom headers to API requests:

```python
configuration.api_key_prefix = {"X-Custom-Header": "value"}
```

### Timeouts

Configure request timeouts:

```python
import requests

configuration.timeout = 10  # seconds
```

---

## Common Use Cases

### User Management

```python
from datadog_api_client.v2.api.users_api import UsersApi

with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    users = api_instance.list_users()
    for user in users.data:
        print(f"{user.attributes['name']} ({user.attributes['email']})")
```

### Incident Management

```python
from datadog_api_client.v2.api.incidents_api import IncidentsApi

with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    incidents = api_instance.list_incidents()
    for incident in incidents.data:
        print(f"Incident: {incident.attributes['title']}")
```

### Security Monitoring

```python
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    rules = api_instance.list_rules()
    for rule in rules.data:
        print(f"Rule: {rule.attributes['name']}")
```

---

## Troubleshooting

### Debug Mode

Enable debug logging to see full request/response details:

```python
configuration.debug = True
```

### Common Issues

**Issue:** "Unauthorized" error (401)
- **Solution:** Verify DD_API_KEY and DD_APP_KEY are set correctly
- Check that API key has appropriate permissions

**Issue:** "Not Found" error (404)
- **Solution:** Verify the correct site is configured (EU vs US)
- Check that the resource exists

**Issue:** "Too Many Requests" error (429)
- **Solution:** Enable retry mechanism with `configuration.max_retries`
- Implement exponential backoff

### Environment Variables

Verify environment variables are set:

```bash
echo $DD_API_KEY
echo $DD_APP_KEY
```

---

## Resources

- **Official Repository:** https://github.com/DataDog/datadog-api-client-python
- **API Documentation:** https://datadoghq.dev/datadog-api-client-python/
- **Datadog Docs:** https://docs.datadoghq.com/
- **API Reference:** https://docs.datadoghq.com/api/latest/?tab=python
- **Issue Tracker:** https://github.com/DataDog/datadog-api-client-python/issues

---

## Support

- **Datadog Support:** https://docs.datadoghq.com/help
- **Community:** Slack, GitHub Discussions
- **Contributing:** See CONTRIBUTING.md in the repository

