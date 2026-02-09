# Datadog Python API Client - Best Practices & Troubleshooting

**Guidelines for reliable and efficient Datadog API usage**

## Table of Contents

1. [Authentication Best Practices](#authentication-best-practices)
2. [Error Handling Strategies](#error-handling-strategies)
3. [Performance Optimization](#performance-optimization)
4. [Rate Limiting](#rate-limiting)
5. [Logging and Debugging](#logging-and-debugging)
6. [Common Pitfalls](#common-pitfalls)
7. [Testing](#testing)
8. [Troubleshooting](#troubleshooting)

---

## Authentication Best Practices

### 1. Use Environment Variables

Never hardcode credentials in your application:

```python
# Bad - DO NOT DO THIS
configuration.api_key["apiKeyAuth"] = "your_api_key_here"

# Good - Use environment variables
import os
from datadog_api_client import Configuration

configuration = Configuration()
# Automatically reads from DD_API_KEY and DD_APP_KEY
```

### 2. Secure Credential Storage

For production applications, use secure credential management:

```python
# Using python-dotenv for local development
from dotenv import load_dotenv
import os

load_dotenv()  # Load from .env file

# Using AWS Secrets Manager for AWS deployments
import boto3
import json

def get_datadog_credentials():
    """Retrieve Datadog credentials from AWS Secrets Manager"""
    secrets_client = boto3.client('secretsmanager')
    secret = secrets_client.get_secret_value(SecretId='datadog/api-keys')
    credentials = json.loads(secret['SecretString'])
    return credentials['api_key'], credentials['app_key']

# For Azure
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

credential = DefaultAzureCredential()
client = SecretClient(vault_url="https://your-keyvault.vault.azure.net", credential=credential)
api_key = client.get_secret("datadog-api-key").value
```

### 3. Validate Credentials on Startup

```python
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi
import sys

def validate_credentials():
    """Validate Datadog credentials"""
    configuration = Configuration()

    try:
        with ApiClient(configuration) as api_client:
            users_api = UsersApi(api_client)
            # Simple API call to verify authentication
            users_api.list_users(page_size=1)
            print("✓ Credentials validated successfully")
            return True
    except Exception as e:
        print(f"✗ Authentication failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    validate_credentials()
    # Continue with main application
```

### 4. Rotate API Keys Regularly

```python
# Implement key rotation strategy
"""
1. Generate new API key in Datadog UI
2. Update application to use new key
3. Wait for key propagation (usually immediate)
4. Revoke old key in UI
5. Monitor for any authentication errors
"""
```

---

## Error Handling Strategies

### 1. Comprehensive Error Handling

```python
from datadog_api_client.exceptions import ApiException
import json
import logging

logger = logging.getLogger(__name__)

def safe_api_call(api_func, *args, **kwargs):
    """Wrapper for safe API calls with comprehensive error handling"""
    try:
        return api_func(*args, **kwargs)

    except ApiException as e:
        logger.error(f"Datadog API Error: {e.status} {e.reason}")

        # Parse error body if available
        try:
            error_data = json.loads(e.body)
            logger.error(f"Error details: {error_data}")
        except:
            logger.error(f"Error body: {e.body}")

        # Handle specific status codes
        if e.status == 401:
            logger.error("Authentication failed - check credentials")
        elif e.status == 403:
            logger.error("Insufficient permissions")
        elif e.status == 404:
            logger.error("Resource not found")
        elif e.status == 429:
            logger.error("Rate limit exceeded")
        elif e.status >= 500:
            logger.error("Server error - retry later")

        raise

    except ConnectionError as e:
        logger.error(f"Connection error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected error: {type(e).__name__}: {e}")
        raise
```

### 2. Retry with Exponential Backoff

```python
import time
from functools import wraps
from datadog_api_client.exceptions import ApiException

def retry_with_backoff(max_retries=3, base_delay=1, max_delay=60):
    """Decorator for retry with exponential backoff"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except ApiException as e:
                    # Only retry on transient errors
                    if e.status not in [429, 500, 502, 503, 504]:
                        raise

                    if attempt == max_retries - 1:
                        raise

                    # Calculate backoff with jitter
                    delay = min(base_delay * (2 ** attempt), max_delay)
                    import random
                    delay += random.uniform(0, delay * 0.1)

                    print(f"Attempt {attempt + 1} failed, retrying in {delay:.1f}s...")
                    time.sleep(delay)
        return wrapper
    return decorator

# Usage
@retry_with_backoff(max_retries=3)
def create_monitor_with_retry(api, monitor):
    return api.create_monitor(body=monitor)
```

---

## Performance Optimization

### 1. Use Connection Pooling

```python
from datadog_api_client import ApiClient, Configuration

# Reuse a single ApiClient instance for multiple operations
configuration = Configuration()

with ApiClient(configuration) as api_client:
    # All API operations use the same connection
    monitors_api = MonitorsApi(api_client)
    dashboards_api = DashboardsApi(api_client)

    monitors = monitors_api.list_monitors()
    dashboards = dashboards_api.list_dashboards()
    # Single connection, multiple API calls
```

### 2. Disable Unnecessary Compression

For local testing or low-bandwidth scenarios:

```python
configuration = Configuration()
configuration.compress = False  # Faster for small payloads
```

### 3. Batch Operations

```python
def batch_create_monitors(monitors_data, batch_size=10):
    """Create multiple monitors efficiently"""
    from datadog_api_client.v2.api.monitors_api import MonitorsApi
    from datadog_api_client.v2.model.monitor import Monitor
    from datadog_api_client.v2.model.monitor_type import MonitorType

    results = []

    with ApiClient(configuration) as api_client:
        api = MonitorsApi(api_client)

        for i, data in enumerate(monitors_data):
            monitor = Monitor(
                name=data["name"],
                type=MonitorType.METRIC_ALERT,
                query=data["query"],
                message=data["message"],
            )

            try:
                result = api.create_monitor(body=monitor)
                results.append({"success": True, "id": result.id})
            except Exception as e:
                results.append({"success": False, "error": str(e)})

            # Log progress
            if (i + 1) % batch_size == 0:
                print(f"Processed {i + 1}/{len(monitors_data)}")

    return results
```

### 4. Lazy Load Data

```python
from datadog_api_client.v2.api.monitors_api import MonitorsApi

def get_monitors_lazy(api):
    """Generator for memory-efficient pagination"""
    page = 1
    while True:
        monitors = api.list_monitors(page_number=page, page_size=100)

        if not monitors.data:
            break

        for monitor in monitors.data:
            yield monitor

        page += 1

# Usage
with ApiClient(configuration) as api_client:
    api = MonitorsApi(api_client)
    for monitor in get_monitors_lazy(api):
        print(monitor.name)
```

---

## Rate Limiting

### 1. Built-in Rate Limit Handling

```python
from datadog_api_client import Configuration

configuration = Configuration()

# Enable automatic retry on rate limit (429)
configuration.max_retries = 5

# With custom retry policy
from urllib3.util.retry import Retry

retry_policy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET", "POST", "PUT", "DELETE"]
)
```

### 2. Monitor Rate Limit Headers

```python
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi

configuration = Configuration()

with ApiClient(configuration) as api_client:
    api = MonitorsApi(api_client)
    response = api.list_monitors()

    # Check rate limit headers if available
    if hasattr(api_client, 'last_response'):
        headers = api_client.last_response.headers
        remaining = headers.get('X-RateLimit-Remaining')
        reset = headers.get('X-RateLimit-Reset')
        print(f"Rate limit remaining: {remaining}")
        print(f"Rate limit reset: {reset}")
```

### 3. Implement Request Throttling

```python
import time
from threading import Lock

class ThrottledApiClient:
    """API client with request throttling"""
    def __init__(self, requests_per_second=10):
        self.requests_per_second = requests_per_second
        self.min_request_interval = 1.0 / requests_per_second
        self.last_request_time = 0
        self.lock = Lock()

    def wait_if_needed(self):
        """Wait if necessary to maintain rate limit"""
        with self.lock:
            elapsed = time.time() - self.last_request_time
            if elapsed < self.min_request_interval:
                time.sleep(self.min_request_interval - elapsed)
            self.last_request_time = time.time()

    def call(self, api_func, *args, **kwargs):
        """Call API function with throttling"""
        self.wait_if_needed()
        return api_func(*args, **kwargs)

# Usage
throttler = ThrottledApiClient(requests_per_second=5)

with ApiClient(configuration) as api_client:
    api = MonitorsApi(api_client)
    monitors = throttler.call(api.list_monitors)
```

---

## Logging and Debugging

### 1. Enable Debug Mode

```python
import logging

# Enable HTTP logging
logging.basicConfig()
logging.getLogger("urllib3").setLevel(logging.DEBUG)

# Enable Datadog API client logging
configuration = Configuration()
configuration.debug = True
```

### 2. Structured Logging

```python
import logging
import json
from datetime import datetime

class DatadogApiLogger:
    """Structured logging for Datadog API operations"""
    def __init__(self, logger_name="datadog_api"):
        self.logger = logging.getLogger(logger_name)

    def log_api_call(self, method, endpoint, status, duration, error=None):
        """Log API call details"""
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "method": method,
            "endpoint": endpoint,
            "status": status,
            "duration_ms": duration,
        }

        if error:
            log_data["error"] = str(error)
            self.logger.error(json.dumps(log_data))
        else:
            self.logger.info(json.dumps(log_data))

# Usage
logger = DatadogApiLogger()

import time
start = time.time()
try:
    monitors = api.list_monitors()
    duration = (time.time() - start) * 1000
    logger.log_api_call("GET", "/api/v2/monitors", 200, duration)
except Exception as e:
    duration = (time.time() - start) * 1000
    logger.log_api_call("GET", "/api/v2/monitors", None, duration, error=e)
```

---

## Common Pitfalls

### 1. Not Closing Connections

Bad:
```python
# BAD: Connection left open
api_client = ApiClient(configuration)
monitors = api_client.monitors_api.list_monitors()
# api_client never closed!
```

Good:
```python
# GOOD: Automatic cleanup with context manager
with ApiClient(configuration) as api_client:
    monitors_api = MonitorsApi(api_client)
    monitors = monitors_api.list_monitors()
    # Connection closed automatically
```

### 2. Reusing Stale Configuration

```python
# BAD: Creating new ApiClient each time
for i in range(100):
    with ApiClient(configuration) as api_client:
        # Creates 100 connections
        pass

# GOOD: Reuse connection
with ApiClient(configuration) as api_client:
    for i in range(100):
        # Single connection for 100 operations
        pass
```

### 3. Missing Error Details

```python
# BAD: Swallowing error details
try:
    monitors = api.list_monitors()
except:
    print("Failed")

# GOOD: Preserve error information
import traceback
try:
    monitors = api.list_monitors()
except Exception as e:
    logger.error(f"Failed to list monitors: {e}", exc_info=True)
    raise
```

### 4. Hardcoding IDs

```python
# BAD: Hardcoded IDs
monitor_id = 123456
api.delete_monitor(monitor_id=monitor_id)

# GOOD: Look up IDs dynamically
monitors = api.list_monitors(name="My Monitor")
if monitors.data:
    for monitor in monitors.data:
        api.delete_monitor(monitor_id=monitor.id)
```

---

## Testing

### 1. Mock API Calls

```python
from unittest.mock import Mock, patch
from datadog_api_client.v2.api.monitors_api import MonitorsApi

def test_create_monitor():
    """Test monitor creation with mocking"""
    mock_response = Mock()
    mock_response.id = 123
    mock_response.name = "Test Monitor"

    with patch.object(MonitorsApi, 'create_monitor', return_value=mock_response):
        api = MonitorsApi(Mock())
        result = api.create_monitor(body=Mock())

        assert result.id == 123
        assert result.name == "Test Monitor"
```

### 2. Test with Fixtures

```python
import pytest
from datadog_api_client import ApiClient, Configuration

@pytest.fixture
def api_client():
    """Fixture for API client"""
    configuration = Configuration()
    with ApiClient(configuration) as client:
        yield client

def test_list_monitors(api_client):
    """Test listing monitors"""
    from datadog_api_client.v2.api.monitors_api import MonitorsApi

    api = MonitorsApi(api_client)
    monitors = api.list_monitors()

    assert len(monitors.data) >= 0
```

---

## Troubleshooting

### Problem: "Unauthorized" (401)

```
Datadog API error: 401
UNAUTHORIZED
```

**Solutions:**
1. Verify credentials are set:
   ```bash
   echo $DD_API_KEY
   echo $DD_APP_KEY
   ```

2. Verify credentials in configuration:
   ```python
   print(configuration.api_key)
   ```

3. Check API key permissions in Datadog UI

4. Regenerate API key if suspected compromise

### Problem: "Rate Limited" (429)

```
Datadog API error: 429
TOO_MANY_REQUESTS
```

**Solutions:**
```python
# Enable automatic retry
configuration.max_retries = 5

# Or implement manual backoff
import time
time.sleep(30)  # Wait 30 seconds
```

### Problem: "Not Found" (404)

```
Datadog API error: 404
NOT_FOUND
```

**Solutions:**
1. Verify resource exists
2. Check correct site:
   ```python
   configuration.server_variables["site"] = "datadoghq.com"  # or datadoghq.eu
   ```

3. Verify ID format:
   ```python
   print(f"Monitor ID: {monitor.id} (type: {type(monitor.id)})")
   ```

### Problem: SSL Certificate Error

```
ssl.SSLError: certificate verify failed
```

**Solutions (dev only, never in production):**
```python
import ssl
import urllib3

# Disable certificate verification (INSECURE!)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Via environment variable
import os
os.environ['CURL_CA_BUNDLE'] = ''
```

**Proper solution:**
```bash
# Update certificate bundle
pip install --upgrade certifi

# Or use specific CA bundle
export REQUESTS_CA_BUNDLE=/path/to/ca-bundle.crt
```

---

## Resources

- **Official Docs:** https://docs.datadoghq.com/
- **API Reference:** https://docs.datadoghq.com/api/latest/?tab=python
- **GitHub Issues:** https://github.com/DataDog/datadog-api-client-python/issues
- **Datadog Support:** https://docs.datadoghq.com/help/

