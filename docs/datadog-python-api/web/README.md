# Datadog Python API Client Documentation

Complete, AI-optimized documentation for the Datadog Python API client library (`datadog-api-client-python`).

**Source:** https://docs.datadoghq.com/api/latest/?tab=python
**Repository:** https://github.com/DataDog/datadog-api-client-python
**Package:** https://pypi.org/project/datadog-api-client/

---

## Documentation Contents

### 1. [GETTING_STARTED.md](GETTING_STARTED.md)
Quick start guide for new users including:
- Installation instructions
- Authentication setup
- First API calls
- Common initial tasks
- Environment configuration
- Troubleshooting common setup issues

### 2. [API_REFERENCE.md](API_REFERENCE.md)
Comprehensive API reference including:
- Installation and setup
- Authentication methods
- Core components (ApiClient, AsyncApiClient, ThreadedApiClient, Configuration)
- All configuration options
- API operations and classes
- Complete code examples
- Advanced features (pagination, retry, error handling, async operations)

### 3. [MODELS_AND_TYPES.md](MODELS_AND_TYPES.md)
Complete reference for data models and types:
- Monitor models and types
- Log models and aggregation
- APM models (Services, Spans)
- Dashboard models and widgets
- Common patterns (pagination, filtering, updates, bulk operations)
- Error models and exception handling
- Type hints and IDE support
- Enum and serialization patterns

### 4. [EXAMPLES.md](EXAMPLES.md)
Practical, working code examples:
- Monitor operations (create, list, update, delete, mute)
- Dashboard operations (create, list, get, update, delete)
- Log operations (query, aggregation, details)
- APM operations (service list, statistics)
- User management
- Incident management
- Advanced patterns (batch operations, async, retry logic)
- Error handling examples
- Full end-to-end working example

### 5. [BEST_PRACTICES.md](BEST_PRACTICES.md)
Guidelines for production-ready code:
- Authentication best practices and credential management
- Error handling strategies with retry and backoff
- Performance optimization techniques
- Rate limiting handling
- Logging and debugging approaches
- Common pitfalls and how to avoid them
- Testing patterns and mocking
- Comprehensive troubleshooting guide

---

## Quick Start

### Installation

```bash
pip install datadog-api-client
```

### Basic Usage

```python
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi

configuration = Configuration()

with ApiClient(configuration) as api_client:
    monitors_api = MonitorsApi(api_client)
    monitors = monitors_api.list_monitors()

    for monitor in monitors.data:
        print(f"Monitor: {monitor.name}")
```

### Authentication

Set environment variables:
```bash
export DD_API_KEY="your_api_key"
export DD_APP_KEY="your_application_key"
```

Or configure manually:
```python
configuration.api_key["apiKeyAuth"] = "<API_KEY>"
configuration.api_key["appKeyAuth"] = "<APP_KEY>"
```

---

## Key Features

- **Multiple API Versions:** Support for both v1 and v2 API endpoints
- **Async Support:** Full async/await support with AsyncApiClient
- **Threading:** ThreadedApiClient for concurrent operations
- **Comprehensive:** All Datadog features: monitors, dashboards, logs, APM, incidents, users, etc.
- **Robust:** Built-in error handling, retry logic, and rate limit management
- **Type Hints:** Full type annotations for IDE support and static analysis
- **Auto-Generated:** Generated from official Datadog API specification

---

## API Operations Supported

### Monitoring
- Monitor creation, listing, updating, deletion
- Monitor state management
- Alert configuration
- Monitor notifications

### Dashboards
- Dashboard CRUD operations
- Widget management
- Dashboard sharing and permissions

### Logging
- Log querying and filtering
- Log aggregation and analysis
- Log pipeline management

### APM
- Service list and metadata
- Span analysis
- Trace querying

### Incident Management
- Incident creation and updates
- Incident tracking
- Status and severity management

### User Management
- User listing and creation
- User status management
- Permission assignment

### And More...
- Cloud integrations
- Security monitoring
- Synthetic monitoring
- Case management
- Audit logs
- SLO management

---

## Python Versions Supported

- Python 3.8+
- Python 3.9, 3.10, 3.11, 3.12

---

## Common Tasks

### Create a Monitor
See [EXAMPLES.md - Create a Metric Alert Monitor](EXAMPLES.md#create-a-metric-alert-monitor)

### Query Logs
See [EXAMPLES.md - Query Logs](EXAMPLES.md#query-logs)

### List Dashboards
See [EXAMPLES.md - List Dashboards](EXAMPLES.md#list-dashboards)

### Implement Error Handling
See [BEST_PRACTICES.md - Error Handling Strategies](BEST_PRACTICES.md#error-handling-strategies)

### Handle Rate Limiting
See [BEST_PRACTICES.md - Rate Limiting](BEST_PRACTICES.md#rate-limiting)

### Use Async Operations
See [EXAMPLES.md - Async Operations](EXAMPLES.md#async-operations)

---

## Troubleshooting Quick Reference

| Issue | Solution |
|-------|----------|
| 401 Unauthorized | Verify DD_API_KEY and DD_APP_KEY credentials |
| 404 Not Found | Check correct site (datadoghq.com vs datadoghq.eu) |
| 429 Too Many Requests | Enable retries: `configuration.max_retries = 5` |
| Connection timeout | Check network, enable debug mode, use longer timeout |
| SSL certificate error | Update certifi: `pip install --upgrade certifi` |

See [BEST_PRACTICES.md - Troubleshooting](BEST_PRACTICES.md#troubleshooting) for detailed solutions.

---

## Configuration Options

```python
from datadog_api_client import Configuration

configuration = Configuration()

# Authentication
configuration.api_key["apiKeyAuth"] = "<API_KEY>"
configuration.api_key["appKeyAuth"] = "<APP_KEY>"

# Server (region)
configuration.server_variables["site"] = "datadoghq.eu"  # EU region

# Debugging
configuration.debug = True  # Enable request/response logging

# Performance
configuration.compress = False  # Disable compression

# Retry on rate limit
configuration.max_retries = 3

# Proxy
configuration.proxy = "http://proxy.example.com:8080"

# Timeout
configuration.timeout = 30  # seconds

# Unstable/Beta endpoints
configuration.unstable_operations["list_log_indexes"] = True
```

---

## Regions Supported

| Region | Site |
|--------|------|
| US | `datadoghq.com` (default) |
| EU | `datadoghq.eu` |
| US3 | `us3.datadoghq.com` |
| US1-FED | `us1-fed.datadoghq.com` |
| AP1 | `ap1.datadoghq.com` |

---

## Client Types

### ApiClient (Synchronous)
Standard blocking client for synchronous code:
```python
with ApiClient(configuration) as api_client:
    api = MonitorsApi(api_client)
    monitors = api.list_monitors()
```

### AsyncApiClient (Asynchronous)
For async/await patterns with non-blocking operations:
```python
async with AsyncApiClient(configuration) as api_client:
    api = MonitorsApi(api_client)
    monitors = await api.list_monitors()
```

Requires: `pip install datadog-api-client[async]`

### ThreadedApiClient (Threaded)
For thread-based concurrent operations:
```python
api_client = ThreadedApiClient(configuration)
# Returns AsyncResult objects for each call
```

---

## Contributing

The Datadog API client is auto-generated from the official API specification. Most code in the repository is generated and should not be modified directly.

Contributions welcome for:
- Bug fixes in generated code
- Test improvements
- Documentation enhancements
- Development tooling

See the [repository](https://github.com/DataDog/datadog-api-client-python) for contribution guidelines.

---

## License

The datadog-api-client-python library is licensed under the Apache License 2.0.

---

## Support

- **Official Documentation:** https://docs.datadoghq.com/
- **API Reference:** https://docs.datadoghq.com/api/latest/?tab=python
- **GitHub Repository:** https://github.com/DataDog/datadog-api-client-python
- **GitHub Issues:** https://github.com/DataDog/datadog-api-client-python/issues
- **Datadog Support:** https://docs.datadoghq.com/help/
- **PyPI:** https://pypi.org/project/datadog-api-client/

---

## Documentation Generated

This documentation was extracted and compiled from:
- Official Datadog API documentation
- GitHub repository README and examples
- Community best practices
- API client source code

**Last Updated:** January 2026
**Python Client Version:** 1.x+
**API Version:** v2 (with v1 support)

---

## File Structure

```
datadog-python-api/
├── README.md                    # This file
├── GETTING_STARTED.md          # Quick start guide
├── API_REFERENCE.md            # Complete API reference
├── MODELS_AND_TYPES.md         # Data models documentation
├── EXAMPLES.md                 # Practical code examples
└── BEST_PRACTICES.md           # Guidelines and troubleshooting
```

---

## How to Use This Documentation

1. **New to the API?** → Start with [GETTING_STARTED.md](GETTING_STARTED.md)
2. **Need an example?** → Check [EXAMPLES.md](EXAMPLES.md)
3. **Looking for specific endpoint?** → See [API_REFERENCE.md](API_REFERENCE.md)
4. **Working with models?** → Reference [MODELS_AND_TYPES.md](MODELS_AND_TYPES.md)
5. **Debugging or optimizing?** → Read [BEST_PRACTICES.md](BEST_PRACTICES.md)

---

