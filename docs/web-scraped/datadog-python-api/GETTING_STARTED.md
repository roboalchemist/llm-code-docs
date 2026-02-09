# Datadog Python API Client - Getting Started Guide

**Quick Start Guide for the datadog-api-client-python library**

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Datadog account with API and Application keys

## Step 1: Install the Library

```bash
# Basic installation
pip install datadog-api-client

# With async support
pip install datadog-api-client[async]
```

Verify the installation:

```bash
python -c "from datadog_api_client import ApiClient; print('Installation successful')"
```

## Step 2: Get Your API Keys

1. Navigate to **Organization Settings** in your Datadog account
2. Select **API Keys** from the left sidebar
3. Click **New Key** to generate an API key
4. Copy the key value
5. Select **Application Keys**
6. Click **New Key** to generate an application key
7. Copy the application key value

**Security Note:** Never commit API keys to version control. Use environment variables instead.

## Step 3: Set Environment Variables

```bash
# Linux/macOS
export DD_API_KEY="your_api_key_here"
export DD_APP_KEY="your_application_key_here"

# Windows (PowerShell)
$env:DD_API_KEY="your_api_key_here"
$env:DD_APP_KEY="your_application_key_here"

# Windows (Command Prompt)
set DD_API_KEY=your_api_key_here
set DD_APP_KEY=your_application_key_here
```

Or add to your `.bashrc`, `.zshrc`, or Windows environment variables for persistence.

## Step 4: Verify Authentication

Create a test script `test_auth.py`:

```python
from datadog_api_client import ApiClient, Configuration

configuration = Configuration()

with ApiClient(configuration) as api_client:
    print("Connection successful!")
    print(f"Using configuration: {configuration}")
```

Run the script:

```bash
python test_auth.py
```

## Step 5: Your First API Call

Create a script to list monitors:

```python
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi

configuration = Configuration()

with ApiClient(configuration) as api_client:
    monitors_api = MonitorsApi(api_client)
    monitors = monitors_api.list_monitors()

    print(f"Total monitors: {len(monitors.data)}")
    for monitor in monitors.data:
        print(f"- {monitor.name} (ID: {monitor.id})")
```

## Common First-Time Tasks

### Task 1: Create a Simple Monitor

```python
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor import Monitor
from datadog_api_client.v2.model.monitor_type import MonitorType

configuration = Configuration()

monitor_body = Monitor(
    name="My First Monitor",
    type=MonitorType.METRIC_ALERT,
    query="avg(last_5m):avg:system.cpu{*} > 0.8",
    message="CPU usage is high: {{value}}",
)

with ApiClient(configuration) as api_client:
    monitors_api = MonitorsApi(api_client)
    response = monitors_api.create_monitor(body=monitor_body)
    print(f"Created monitor: {response.id}")
```

### Task 2: List Dashboards

```python
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboards_api import DashboardsApi

configuration = Configuration()

with ApiClient(configuration) as api_client:
    dashboards_api = DashboardsApi(api_client)
    dashboards = dashboards_api.list_dashboards()

    for dashboard in dashboards.data:
        print(f"Dashboard: {dashboard.title}")
```

### Task 3: Get APM Service Data

```python
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apm_api import APMApi

configuration = Configuration()

with ApiClient(configuration) as api_client:
    apm_api = APMApi(api_client)
    services = apm_api.get_service_list()

    print(response)
```

### Task 4: Query Logs

```python
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi
from datadog_api_client.v2.model.logs_list_request import LogsListRequest

configuration = Configuration()

body = LogsListRequest(
    filter={
        "from": "2024-01-01T00:00:00Z",
        "to": "2024-01-31T23:59:59Z",
        "query": "status:error source:my_app",
    },
    page={"limit": 100},
)

with ApiClient(configuration) as api_client:
    logs_api = LogsApi(api_client)
    response = logs_api.list_logs(body=body)

    print(f"Found {len(response.data)} logs")
```

## Configuration Options

The `Configuration` object allows you to customize behavior:

```python
from datadog_api_client import Configuration

configuration = Configuration()

# Authentication
configuration.api_key["apiKeyAuth"] = "your_api_key"
configuration.api_key["appKeyAuth"] = "your_app_key"

# Server (region)
configuration.server_variables["site"] = "datadoghq.eu"  # For EU

# Logging & Debug
configuration.debug = True  # Print request/response details

# Performance
configuration.compress = False  # Disable GZIP compression

# Retries
configuration.max_retries = 3  # Retry on 429 (rate limit)

# Proxy
configuration.proxy = "http://proxy.example.com:8080"
```

## Regions

The client supports multiple Datadog regions:

```python
# US (default)
configuration.server_variables["site"] = "datadoghq.com"

# EU
configuration.server_variables["site"] = "datadoghq.eu"

# US3
configuration.server_variables["site"] = "us3.datadoghq.com"

# US1-FED
configuration.server_variables["site"] = "us1-fed.datadoghq.com"

# AP1
configuration.server_variables["site"] = "ap1.datadoghq.com"
```

## Error Handling

Handle API errors gracefully:

```python
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.exceptions import ApiException

configuration = Configuration()

try:
    with ApiClient(configuration) as api_client:
        monitors_api = MonitorsApi(api_client)
        monitors = monitors_api.list_monitors()
        print(f"Found {len(monitors.data)} monitors")

except ApiException as e:
    print(f"API Error: {e.status} - {e.reason}")
    print(f"Details: {e.body}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Using with Virtual Environments

Recommended for Python projects:

```bash
# Create virtual environment
python3 -m venv datadog_env

# Activate
source datadog_env/bin/activate  # macOS/Linux
datadog_env\Scripts\activate     # Windows

# Install package
pip install datadog-api-client

# Set environment variables in .env file
echo "DD_API_KEY=your_key" > .env
echo "DD_APP_KEY=your_app_key" >> .env

# Load before running scripts
export $(cat .env | xargs)
python your_script.py
```

## Async Operations

For asynchronous code (requires `pip install datadog-api-client[async]`):

```python
from datadog_api_client import AsyncApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
import asyncio

async def get_monitors():
    configuration = Configuration()

    async with AsyncApiClient(configuration) as api_client:
        monitors_api = MonitorsApi(api_client)
        monitors = await monitors_api.list_monitors()
        return monitors

# Run the async function
monitors = asyncio.run(get_monitors())
print(monitors)
```

## Troubleshooting

### Issue: "Unauthorized" (401 Error)

```
Datadog API error: 401
UNAUTHORIZED
```

**Solutions:**
- Verify `DD_API_KEY` is set correctly: `echo $DD_API_KEY`
- Verify `DD_APP_KEY` is set correctly: `echo $DD_APP_KEY`
- Keys haven't rotated or been revoked
- API key has sufficient permissions

### Issue: "Not Found" (404 Error)

```
Datadog API error: 404
NOT_FOUND
```

**Solutions:**
- Check the correct site/region: `datadoghq.com` vs `datadoghq.eu`
- Verify the resource ID exists
- Ensure you're using the correct API endpoint

### Issue: "Too Many Requests" (429 Error)

```
Datadog API error: 429
TOO_MANY_REQUESTS
```

**Solutions:**
```python
configuration.max_retries = 5  # Enable automatic retries
```

### Issue: Import Errors

```
ModuleNotFoundError: No module named 'datadog_api_client'
```

**Solutions:**
- Install the package: `pip install datadog-api-client`
- Verify correct virtual environment: `which python`
- Check installation: `pip show datadog-api-client`

## Next Steps

1. **Read the full API reference:** See `API_REFERENCE.md`
2. **Explore examples:** Check the GitHub repository for v1/v2 examples
3. **Review Datadog docs:** https://docs.datadoghq.com/
4. **Join the community:** Slack, GitHub Discussions

## Resources

- **GitHub:** https://github.com/DataDog/datadog-api-client-python
- **PyPI:** https://pypi.org/project/datadog-api-client/
- **Official API Docs:** https://docs.datadoghq.com/api/latest/?tab=python
- **API Client Docs:** https://datadoghq.dev/datadog-api-client-python/

