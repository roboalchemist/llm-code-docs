# Datadog Python API Client - Code Examples

**Practical examples for common Datadog operations**

## Table of Contents

1. [Monitor Operations](#monitor-operations)
2. [Dashboard Operations](#dashboard-operations)
3. [Log Operations](#log-operations)
4. [APM Operations](#apm-operations)
5. [User Management](#user-management)
6. [Incident Management](#incident-management)
7. [Advanced Patterns](#advanced-patterns)
8. [Error Handling](#error-handling)

---

## Monitor Operations

### Create a Metric Alert Monitor

```python
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor import Monitor
from datadog_api_client.v2.model.monitor_type import MonitorType

configuration = Configuration()

monitor = Monitor(
    name="High CPU Usage Alert",
    type=MonitorType.METRIC_ALERT,
    query="avg(last_5m):avg:system.cpu{*} > 0.8",
    message="""
CPU usage is too high!
Value: {{value}}
Host: {{host.name}}
""",
    tags=["production", "cpu"],
    enabled=True,
    priority=1,
    no_data_timeframe=10,  # Alert if no data for 10 minutes
)

with ApiClient(configuration) as api_client:
    monitors_api = MonitorsApi(api_client)
    response = monitors_api.create_monitor(body=monitor)
    print(f"Created monitor with ID: {response.id}")
```

### Create a Log Alert Monitor

```python
from datadog_api_client.v2.model.monitor_type import MonitorType

monitor = Monitor(
    name="Critical Errors Alert",
    type=MonitorType.LOG_ALERT,
    query='status:error source:production_app',
    message="Critical errors detected in production",
    tags=["production", "logs"],
)

with ApiClient(configuration) as api_client:
    monitors_api = MonitorsApi(api_client)
    response = monitors_api.create_monitor(body=monitor)
```

### List All Monitors

```python
with ApiClient(configuration) as api_client:
    monitors_api = MonitorsApi(api_client)
    monitors = monitors_api.list_monitors()

    for monitor in monitors.data:
        print(f"Monitor: {monitor.name}")
        print(f"  ID: {monitor.id}")
        print(f"  Type: {monitor.type}")
        print(f"  State: {monitor.state}")
        print()
```

### Get a Specific Monitor

```python
monitor_id = 12345

with ApiClient(configuration) as api_client:
    monitors_api = MonitorsApi(api_client)
    monitor = monitors_api.get_monitor(monitor_id=monitor_id)

    print(f"Name: {monitor.name}")
    print(f"Query: {monitor.query}")
    print(f"Message: {monitor.message}")
```

### Update a Monitor

```python
monitor_id = 12345

with ApiClient(configuration) as api_client:
    monitors_api = MonitorsApi(api_client)

    # Get existing monitor
    monitor = monitors_api.get_monitor(monitor_id=monitor_id)

    # Update properties
    monitor.message = "Updated: " + monitor.message
    monitor.tags.append("updated")

    # Send update
    updated = monitors_api.update_monitor(
        monitor_id=monitor_id,
        body=monitor
    )
    print(f"Updated monitor: {updated.name}")
```

### Delete a Monitor

```python
monitor_id = 12345

with ApiClient(configuration) as api_client:
    monitors_api = MonitorsApi(api_client)
    monitors_api.delete_monitor(monitor_id=monitor_id)
    print(f"Deleted monitor {monitor_id}")
```

### Mute a Monitor

```python
from datadog_api_client.v2.model.monitor_update_request import MonitorUpdateRequest

monitor_id = 12345

with ApiClient(configuration) as api_client:
    monitors_api = MonitorsApi(api_client)

    # Mute all instances
    monitors_api.update_monitor_state(
        monitor_id=monitor_id,
        body=MonitorUpdateRequest(
            action="mute"
        )
    )
```

### Search Monitors by Tags

```python
with ApiClient(configuration) as api_client:
    monitors_api = MonitorsApi(api_client)

    # List monitors with specific tag
    monitors = monitors_api.list_monitors(
        tags=["production"]
    )

    print(f"Found {len(monitors.data)} production monitors")
```

---

## Dashboard Operations

### Create a Dashboard with Widgets

```python
from datadog_api_client.v2.api.dashboards_api import DashboardsApi
from datadog_api_client.v2.model.dashboard import Dashboard
from datadog_api_client.v2.model.dashboard_type import DashboardType
from datadog_api_client.v2.model.widget import Widget
from datadog_api_client.v2.model.widget_definition import WidgetDefinition
from datadog_api_client.v2.model.widget_type import WidgetType

dashboard = Dashboard(
    title="System Performance",
    description="Key system metrics dashboard",
    type=DashboardType.TIMEBOARD,
    tags=["system", "performance"],
    widgets=[
        Widget(
            definition=WidgetDefinition(
                type=WidgetType.TIMESERIES,
                requests=[{
                    "queries": [{
                        "query": "avg:system.cpu{*}"
                    }]
                }],
                title="CPU Usage"
            )
        ),
        Widget(
            definition=WidgetDefinition(
                type=WidgetType.QUERY_VALUE,
                requests=[{
                    "queries": [{
                        "query": "avg:system.mem.pct_usable{*}"
                    }]
                }],
                title="Memory Available %"
            )
        )
    ]
)

with ApiClient(configuration) as api_client:
    dashboards_api = DashboardsApi(api_client)
    response = dashboards_api.create_dashboard(body=dashboard)
    print(f"Created dashboard: {response.id}")
```

### List Dashboards

```python
with ApiClient(configuration) as api_client:
    dashboards_api = DashboardsApi(api_client)
    dashboards = dashboards_api.list_dashboards()

    for dashboard in dashboards.data:
        print(f"Dashboard: {dashboard.title}")
        print(f"  ID: {dashboard.id}")
        print(f"  Type: {dashboard.type}")
```

### Get a Dashboard

```python
dashboard_id = "abc-123-def"

with ApiClient(configuration) as api_client:
    dashboards_api = DashboardsApi(api_client)
    dashboard = dashboards_api.get_dashboard(dashboard_id=dashboard_id)

    print(f"Title: {dashboard.title}")
    print(f"Widgets: {len(dashboard.widgets)}")
```

### Update a Dashboard

```python
dashboard_id = "abc-123-def"

with ApiClient(configuration) as api_client:
    dashboards_api = DashboardsApi(api_client)

    # Get dashboard
    dashboard = dashboards_api.get_dashboard(dashboard_id=dashboard_id)

    # Modify
    dashboard.title = "Updated: " + dashboard.title

    # Update
    updated = dashboards_api.update_dashboard(
        dashboard_id=dashboard_id,
        body=dashboard
    )
```

### Delete a Dashboard

```python
dashboard_id = "abc-123-def"

with ApiClient(configuration) as api_client:
    dashboards_api = DashboardsApi(api_client)
    dashboards_api.delete_dashboard(dashboard_id=dashboard_id)
```

---

## Log Operations

### Query Logs

```python
from datadog_api_client.v2.api.logs_api import LogsApi
from datadog_api_client.v2.model.logs_list_request import LogsListRequest

request = LogsListRequest(
    filter={
        "from": "2024-01-01T00:00:00Z",
        "to": "2024-01-31T23:59:59Z",
        "query": "status:error source:api",
    },
    page={
        "limit": 100,
    },
)

with ApiClient(configuration) as api_client:
    logs_api = LogsApi(api_client)
    response = logs_api.list_logs(body=request)

    for log in response.data:
        print(f"[{log.attributes['status']}] {log.attributes['message']}")
```

### Query Logs with Aggregation

```python
from datadog_api_client.v2.model.logs_aggregate_request import LogsAggregateRequest
from datadog_api_client.v2.model.logs_metric_compute import LogsMetricCompute
from datadog_api_client.v2.model.logs_group_by import LogsGroupBy

request = LogsAggregateRequest(
    filter={
        "from": "2024-01-01T00:00:00Z",
        "to": "2024-01-31T23:59:59Z",
        "query": "source:api",
    },
    compute=[
        LogsMetricCompute(
            aggregation="count",
        )
    ],
    group_by=[
        LogsGroupBy(path="@status", limit=10)
    ],
)

with ApiClient(configuration) as api_client:
    logs_api = LogsApi(api_client)
    response = logs_api.aggregate_logs(body=request)

    for bucket in response.data.buckets:
        print(f"Status: {bucket.key}")
        print(f"  Count: {bucket.computes[0].value}")
```

### Get Log Details

```python
log_id = "abc123"

with ApiClient(configuration) as api_client:
    logs_api = LogsApi(api_client)
    log = logs_api.get_log(log_id=log_id)

    print(f"Message: {log.attributes['message']}")
    print(f"Status: {log.attributes['status']}")
    print(f"Service: {log.attributes.get('service', 'N/A')}")
```

---

## APM Operations

### Get Service List

```python
from datadog_api_client.v2.api.apm_api import APMApi

with ApiClient(configuration) as api_client:
    apm_api = APMApi(api_client)
    response = apm_api.get_service_list()

    print(response)
```

### Get Service Statistics

```python
service_name = "my-api"

with ApiClient(configuration) as api_client:
    apm_api = APMApi(api_client)
    stats = apm_api.get_service_stats(service_name=service_name)

    print(f"Service: {service_name}")
    print(f"  Requests/sec: {stats.stats.throughput}")
    print(f"  Latency (ms): {stats.stats.latency}")
    print(f"  Error rate: {stats.stats.errors}%")
```

---

## User Management

### List Users

```python
from datadog_api_client.v2.api.users_api import UsersApi

with ApiClient(configuration) as api_client:
    users_api = UsersApi(api_client)
    users = users_api.list_users()

    for user in users.data:
        print(f"User: {user.attributes['name']}")
        print(f"  Email: {user.attributes['email']}")
        print(f"  Status: {user.attributes['status']}")
```

### Create a User

```python
from datadog_api_client.v2.model.user_create_request import UserCreateRequest

user_request = UserCreateRequest(
    data={
        "type": "users",
        "attributes": {
            "name": "John Doe",
            "email": "john.doe@example.com",
        }
    }
)

with ApiClient(configuration) as api_client:
    users_api = UsersApi(api_client)
    response = users_api.create_user(body=user_request)
    print(f"Created user: {response.data.id}")
```

### Update User Status

```python
user_id = "user123"

from datadog_api_client.v2.model.user_update_request import UserUpdateRequest

update_request = UserUpdateRequest(
    data={
        "type": "users",
        "id": user_id,
        "attributes": {
            "status": "disabled"  # or "active"
        }
    }
)

with ApiClient(configuration) as api_client:
    users_api = UsersApi(api_client)
    users_api.update_user(user_id=user_id, body=update_request)
```

---

## Incident Management

### List Incidents

```python
from datadog_api_client.v2.api.incidents_api import IncidentsApi

with ApiClient(configuration) as api_client:
    incidents_api = IncidentsApi(api_client)
    incidents = incidents_api.list_incidents()

    for incident in incidents.data:
        print(f"Incident: {incident.attributes['title']}")
        print(f"  Status: {incident.attributes['status']}")
        print(f"  Severity: {incident.attributes['severity']}")
```

### Create an Incident

```python
from datadog_api_client.v2.model.incident_create_request import IncidentCreateRequest

incident_request = IncidentCreateRequest(
    data={
        "type": "incidents",
        "attributes": {
            "title": "Database connection pool exhausted",
            "status": "active",
            "severity": "critical",
        }
    }
)

with ApiClient(configuration) as api_client:
    incidents_api = IncidentsApi(api_client)
    response = incidents_api.create_incident(body=incident_request)
    print(f"Created incident: {response.data.id}")
```

### Update Incident

```python
incident_id = "incident123"

from datadog_api_client.v2.model.incident_update_request import IncidentUpdateRequest

update_request = IncidentUpdateRequest(
    data={
        "type": "incidents",
        "id": incident_id,
        "attributes": {
            "status": "resolved",
            "customer_impact_scope": "Database is now stable",
        }
    }
)

with ApiClient(configuration) as api_client:
    incidents_api = IncidentsApi(api_client)
    incidents_api.update_incident(
        incident_id=incident_id,
        body=update_request
    )
```

---

## Advanced Patterns

### Batch Create Monitors

```python
monitors_config = [
    {
        "name": "CPU Alert",
        "query": "avg(last_5m):avg:system.cpu{*} > 0.8",
    },
    {
        "name": "Memory Alert",
        "query": "avg(last_5m):avg:system.mem.pct_usable{*} < 0.1",
    },
    {
        "name": "Disk Alert",
        "query": "avg(last_5m):avg:system.disk.free{*} < 1000000000",
    },
]

with ApiClient(configuration) as api_client:
    monitors_api = MonitorsApi(api_client)

    for config in monitors_config:
        monitor = Monitor(
            name=config["name"],
            type=MonitorType.METRIC_ALERT,
            query=config["query"],
            message=f"Alert: {config['name']}",
            tags=["batch-created"],
        )
        response = monitors_api.create_monitor(body=monitor)
        print(f"Created: {response.id}")
```

### Async Operations

```python
import asyncio
from datadog_api_client import AsyncApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi

async def get_monitors():
    configuration = Configuration()

    async with AsyncApiClient(configuration) as api_client:
        monitors_api = MonitorsApi(api_client)
        monitors = await monitors_api.list_monitors()
        return monitors

# Run
monitors = asyncio.run(get_monitors())
print(f"Found {len(monitors.data)} monitors")
```

### Implement Retry Logic

```python
import time
from datadog_api_client.exceptions import ApiException

def create_monitor_with_retry(monitors_api, monitor, max_retries=3):
    """Create monitor with automatic retry on transient errors"""
    for attempt in range(max_retries):
        try:
            return monitors_api.create_monitor(body=monitor)
        except ApiException as e:
            if e.status in [429, 500, 502, 503]:  # Transient errors
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Attempt {attempt + 1} failed, retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise  # Non-transient error, fail immediately

with ApiClient(configuration) as api_client:
    monitors_api = MonitorsApi(api_client)
    response = create_monitor_with_retry(monitors_api, monitor)
```

---

## Error Handling

### Handle All Error Types

```python
from datadog_api_client.exceptions import ApiException
import json

with ApiClient(configuration) as api_client:
    monitors_api = MonitorsApi(api_client)

    try:
        response = monitors_api.create_monitor(body=monitor)
    except ApiException as e:
        print(f"HTTP Status: {e.status}")
        print(f"Reason: {e.reason}")

        # Parse error response
        try:
            error_data = json.loads(e.body)
            print(f"Error Details: {error_data}")
        except:
            print(f"Raw Response: {e.body}")

    except ConnectionError as e:
        print(f"Network error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

### Validate Input Before Sending

```python
def validate_monitor(monitor):
    """Validate monitor before sending to API"""
    errors = []

    if not monitor.name or len(monitor.name) < 3:
        errors.append("Monitor name must be at least 3 characters")

    if not monitor.query:
        errors.append("Monitor query is required")

    if not monitor.message:
        errors.append("Monitor message is required")

    if monitor.type not in MonitorType:
        errors.append(f"Invalid monitor type: {monitor.type}")

    if errors:
        raise ValueError("; ".join(errors))

    return True

# Use
try:
    validate_monitor(monitor)
    response = monitors_api.create_monitor(body=monitor)
except ValueError as e:
    print(f"Validation error: {e}")
```

---

## Full Working Example

Complete end-to-end example:

```python
#!/usr/bin/env python3
"""
Complete Datadog API example: Create monitor, list dashboards, query logs
"""

import os
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.api.dashboards_api import DashboardsApi
from datadog_api_client.v2.api.logs_api import LogsApi
from datadog_api_client.v2.model.monitor import Monitor
from datadog_api_client.v2.model.monitor_type import MonitorType

def main():
    # Configuration
    configuration = Configuration()

    # Optional: Check environment
    if not os.environ.get("DD_API_KEY"):
        print("Error: DD_API_KEY not set")
        return

    with ApiClient(configuration) as api_client:
        # Create a monitor
        print("Creating monitor...")
        monitors_api = MonitorsApi(api_client)
        monitor = Monitor(
            name="Example Monitor",
            type=MonitorType.METRIC_ALERT,
            query="avg(last_5m):avg:system.cpu{*} > 0.8",
            message="CPU is high",
        )
        monitor_response = monitors_api.create_monitor(body=monitor)
        print(f"✓ Created monitor {monitor_response.id}")

        # List dashboards
        print("\nListing dashboards...")
        dashboards_api = DashboardsApi(api_client)
        dashboards = dashboards_api.list_dashboards()
        print(f"✓ Found {len(dashboards.data)} dashboards")
        for dashboard in dashboards.data[:5]:
            print(f"  - {dashboard.title}")

        # List monitors
        print("\nListing monitors...")
        monitors = monitors_api.list_monitors()
        print(f"✓ Found {len(monitors.data)} monitors")

if __name__ == "__main__":
    main()
```

---

## Resources

- **GitHub Repository:** https://github.com/DataDog/datadog-api-client-python
- **API Documentation:** https://docs.datadoghq.com/api/latest/?tab=python
- **Python Client Docs:** https://datadoghq.dev/datadog-api-client-python/

