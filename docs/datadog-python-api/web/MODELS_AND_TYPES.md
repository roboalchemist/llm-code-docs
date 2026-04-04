# Datadog Python API Client - Models and Types Reference

**Comprehensive guide to common model classes and data types**

## Table of Contents

1. [Monitor Models](#monitor-models)
2. [Log Models](#log-models)
3. [APM Models](#apm-models)
4. [Dashboard Models](#dashboard-models)
5. [Common Patterns](#common-patterns)
6. [Error Models](#error-models)

---

## Monitor Models

### Monitor Type

Enum representing monitor types:

```python
from datadog_api_client.v2.model.monitor_type import MonitorType

MonitorType.COMPOSITE_MONITOR  # Composite monitor
MonitorType.LOG_ALERT          # Log alert
MonitorType.METRIC_ALERT       # Metric alert
MonitorType.SERVICE_CHECK      # Service check
MonitorType.SYNTHETICS_ALERT   # Synthetics alert
MonitorType.EVENT_ALERT        # Event alert
MonitorType.PROCESS_ALERT      # Process alert
MonitorType.SLO_ALERT          # SLO alert
```

### Monitor Class

The main monitor object:

```python
from datadog_api_client.v2.model.monitor import Monitor

monitor = Monitor(
    name="CPU Alert",                              # Display name
    type=MonitorType.METRIC_ALERT,                # Monitor type
    query="avg(last_5m):avg:system.cpu{*} > 0.8", # Alert condition
    message="CPU is high: {{value}}%",            # Notification message
    tags=["production", "critical"],              # Tags
    enabled=True,                                 # Enable/disable
    priority=1,                                   # Priority (1-5)
    no_data_timeframe=10,                        # Minutes without data before alert
    evaluation_delay=300,                         # Evaluation delay in seconds
    keep_alive_interval=600,                      # Alert persistence interval
)
```

### Monitor Attributes

Key properties:

```python
# After creating/retrieving a monitor
monitor.id              # Integer, unique identifier
monitor.name            # String, display name
monitor.type            # MonitorType enum
monitor.query           # String, alert condition
monitor.message         # String, notification message
monitor.tags            # List[String], associated tags
monitor.enabled         # Boolean, enable status
monitor.created_at      # Integer, Unix timestamp
monitor.modified_at     # Integer, Unix timestamp
monitor.created_by      # Monitor creator info
monitor.modified_by     # Last modifier info
monitor.state           # MonitorState (alert, no_alert, ok)
```

### Monitor State

The state of a monitor:

```python
from datadog_api_client.v2.model.monitor_state import MonitorState

MonitorState.ALERT      # Monitor is in alert state
MonitorState.NO_ALERT   # Monitor is not alerting
MonitorState.UNKNOWN    # State unknown
```

---

## Log Models

### LogsListRequest

Request object for querying logs:

```python
from datadog_api_client.v2.model.logs_list_request import LogsListRequest

request = LogsListRequest(
    filter={
        "from": "2024-01-01T00:00:00Z",        # Start date (ISO 8601)
        "to": "2024-01-31T23:59:59Z",          # End date (ISO 8601)
        "query": "status:error source:api",    # Query string
    },
    page={
        "limit": 100,                          # Results per page (max 1000)
        "cursor": None,                        # Pagination cursor
    },
    sort=Sort.TIMESTAMP_DESCENDING,            # Sort order
)
```

### Log Attributes

Properties of a log entry:

```python
log.id                  # Unique log ID
log.attributes.host     # Hostname
log.attributes.service  # Service name
log.attributes.status   # Log level (debug, info, warn, error)
log.attributes.message  # Log message
log.attributes.tags     # Associated tags
log.attributes.timestamp  # Log timestamp (Unix milliseconds)
log.attributes.source   # Log source (application, language)
```

### Log Aggregation

Group logs by attributes:

```python
from datadog_api_client.v2.model.logs_aggregate_request import LogsAggregateRequest

request = LogsAggregateRequest(
    filter={
        "from": "2024-01-01T00:00:00Z",
        "to": "2024-01-31T23:59:59Z",
        "query": "status:error",
    },
    compute=[
        LogsMetricCompute(
            aggregation="count",               # count, cardinality, percentile, etc.
            metric="",                         # Leave empty for count
            type=AggregationMetricType.COUNT,
        )
    ],
    group_by=[
        LogsGroupBy(path="@status", limit=10)  # Group by status
    ],
)
```

---

## APM Models

### Service

Represents an APM service:

```python
service.name              # Service name
service.type              # Service type (web, db, cache, etc.)
service.version           # Service version
service.environment       # Environment (prod, staging, dev)
service.stats.throughput  # Requests per second
service.stats.latency     # Response time in milliseconds
service.stats.errors      # Error rate percentage
service.stats.apdex       # Apdex score (0-1)
```

### Span

Represents a distributed trace span:

```python
span.id                   # Unique span ID
span.trace_id             # Associated trace ID
span.parent_id            # Parent span ID
span.service              # Service name
span.operation_name       # Operation being traced
span.resource_name        # Resource identifier
span.start_time           # Start timestamp (nanoseconds)
span.duration             # Duration in nanoseconds
span.tags                 # Associated tags and metadata
span.metrics              # Span metrics
```

---

## Dashboard Models

### Dashboard

Main dashboard object:

```python
from datadog_api_client.v2.model.dashboard import Dashboard
from datadog_api_client.v2.model.dashboard_type import DashboardType

dashboard = Dashboard(
    title="System Overview",                    # Dashboard title
    description="Key system metrics",          # Description
    type=DashboardType.TIMEBOARD,              # Dashboard type
    tags=["system", "monitoring"],             # Tags
    is_read_only=False,                        # Read-only flag
    layout_type=LayoutType.ORDERED,            # Layout type
    widgets=[],                                # Dashboard widgets
)
```

### Dashboard Widget

Individual dashboard widget:

```python
from datadog_api_client.v2.model.widget import Widget
from datadog_api_client.v2.model.widget_definition import WidgetDefinition

widget = Widget(
    definition=WidgetDefinition(
        type=WidgetType.TIMESERIES,            # Widget type
        requests=[
            WidgetRequest(
                response_format="timeseries",
                on_right_yaxis=False,
                queries=[
                    MetricsQueryOptions(
                        query="avg:system.cpu{*}",  # Metric query
                    )
                ],
            )
        ],
        title="CPU Usage",                     # Widget title
        yaxis=YAxis(
            min=0,                             # Y-axis minimum
            max=100,                           # Y-axis maximum
        ),
    )
)
```

### Widget Types

Common widget types:

```python
from datadog_api_client.v2.model.widget_type import WidgetType

WidgetType.TIMESERIES      # Time series graph
WidgetType.QUERY_VALUE     # Single value display
WidgetType.GAUGE           # Gauge visualization
WidgetType.DISTRIBUTION    # Distribution chart
WidgetType.HEATMAP         # Heatmap visualization
WidgetType.TOPLIST         # Top list
WidgetType.TABLE           # Data table
WidgetType.NUMBER          # Number display
WidgetType.ALERT_GRAPH     # Alert status graph
```

---

## Common Patterns

### Pagination with Response

```python
from datadog_api_client.v2.api.monitors_api import MonitorsApi

with ApiClient(configuration) as api_client:
    api = MonitorsApi(api_client)

    # First page
    response = api.list_monitors(page_size=10)

    # Access data
    for monitor in response.data:
        print(monitor.name)

    # Check for more pages
    if hasattr(response, 'links') and 'next' in response.links:
        # Fetch next page using cursor/offset
        next_response = api.list_monitors(
            page_size=10,
            page_number=2
        )
```

### Filtering and Sorting

```python
# Monitors with filter
monitors = api.list_monitors(
    name="CPU",              # Filter by name
    tags=["production"],      # Filter by tags
    status="alert",          # Filter by status
)

# Sort ascending/descending
monitors = api.list_monitors(
    sort="name",             # Sort by field
    # Use "-name" for descending
)
```

### Optional Parameters

```python
# Include optional fields
response = api.list_dashboards(
    filter_shared=False,     # Exclude shared dashboards
    sort_field="name",       # Sort by field
    sort_direction="asc",    # Sort direction
)
```

### Bulk Operations

```python
# Create multiple monitors
monitors = []
for i in range(3):
    monitor = Monitor(
        name=f"Monitor {i}",
        type=MonitorType.METRIC_ALERT,
        query=f"avg(last_5m):avg:system.load{{host:{i}}} > 0.5",
        message="Load is high",
    )
    response = api.create_monitor(body=monitor)
    monitors.append(response)
```

### Update Operations

```python
# Update an existing monitor
monitor.message = "Updated message"
monitor.tags = ["updated-tag"]

updated = api.update_monitor(
    monitor_id=monitor.id,
    body=monitor
)
```

### Delete Operations

```python
# Delete a monitor
api.delete_monitor(monitor_id=123)

# Delete with force flag (for composite monitors)
api.delete_monitor(
    monitor_id=123,
    force=True
)
```

---

## Error Models

### API Exception

Handle API errors:

```python
from datadog_api_client.exceptions import ApiException

try:
    response = api.create_monitor(body=monitor)
except ApiException as e:
    print(f"Status: {e.status}")      # HTTP status code
    print(f"Reason: {e.reason}")      # HTTP reason
    print(f"Body: {e.body}")          # Response body
    print(f"Headers: {e.headers}")    # Response headers
```

### Common HTTP Status Codes

```python
400  # Bad Request - Invalid parameters
401  # Unauthorized - Invalid credentials
403  # Forbidden - Insufficient permissions
404  # Not Found - Resource doesn't exist
409  # Conflict - Resource already exists
429  # Too Many Requests - Rate limit exceeded
500  # Internal Server Error
503  # Service Unavailable
```

### Error Response Body

Typical error response:

```python
{
    "errors": [
        "Invalid parameter: query must not be empty"
    ]
}
```

### Validation Errors

Validate input before sending:

```python
# Ensure required fields
if not monitor.name or not monitor.query:
    raise ValueError("Monitor name and query are required")

# Validate types
if not isinstance(monitor.type, MonitorType):
    raise ValueError("Invalid monitor type")
```

---

## Type Hints and IDE Support

The library uses Python type hints for better IDE support:

```python
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor import Monitor
from datadog_api_client.v2.model.monitors_list_response import MonitorsListResponse

def create_cpu_monitor(api: MonitorsApi, threshold: float) -> Monitor:
    """Create a CPU usage monitor"""
    monitor = Monitor(
        name="CPU Alert",
        type=MonitorType.METRIC_ALERT,
        query=f"avg(last_5m):avg:system.cpu{{*}} > {threshold}",
        message="CPU is high",
    )
    return api.create_monitor(body=monitor)

def list_all_monitors(api: MonitorsApi) -> list[Monitor]:
    """Get all monitors"""
    response: MonitorsListResponse = api.list_monitors()
    return response.data
```

---

## Working with Enums

Safe enum usage:

```python
from datadog_api_client.v2.model.monitor_type import MonitorType
from datadog_api_client.v2.model.monitor_state import MonitorState

# Direct enum comparison
if monitor.state == MonitorState.ALERT:
    print("Monitor is alerting")

# Get enum value string
monitor_type_str = monitor.type.value  # "metric_alert"

# Create from string
monitor_type = MonitorType(user_input)
```

---

## Serialization

Convert models to/from JSON:

```python
import json

# Model to dictionary
monitor_dict = monitor.to_dict()

# Model to JSON string
monitor_json = json.dumps(monitor_dict, default=str)

# Dictionary to model
from datadog_api_client.v2.model.monitor import Monitor
monitor = Monitor.from_dict(monitor_dict)
```

---

## References

- **API Spec:** https://docs.datadoghq.com/api/latest/?tab=python
- **GitHub:** https://github.com/DataDog/datadog-api-client-python
- **Model Documentation:** https://datadoghq.dev/datadog-api-client-python/

