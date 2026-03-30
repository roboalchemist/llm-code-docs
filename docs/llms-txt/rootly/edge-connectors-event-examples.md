# Source: https://docs.rootly.com/edge-connectors-event-examples.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Event Examples

> Real-world examples of event payloads from Rootly Edge Connectors

## Overview

This page provides real-world examples of event payloads that Edge Connectors receive when polling the Rootly API. These examples show the structure and data available for templating in your action configurations.

## Event Types

Edge Connector events are divided into two categories based on how actions are triggered:

<Info>
  **Understanding Action Types:** Automatic events trigger actions automatically (configured in `on:` section), while manual trigger events are user-initiated actions (configured in `callable:` section). See the [Automatic vs Callable Actions](/edge-connectors-actions#automatic-vs-callable-actions) guide for detailed comparison.
</Info>

### Automatic Event Types

These events are triggered automatically by system events and can be subscribed to by connectors for monitoring and notifications:

**Alert Events:**

* `alert.created` - New alert from monitoring system
* `alert.updated` - Alert properties changed
* `alert.acknowledged` - Alert acknowledged by a user
* `alert.resolved` - Alert marked as resolved
* `alert.deleted` - Alert removed

**Incident Events:**

* `incident.created` - New incident started
* `incident.updated` - Incident properties changed
* `incident.in_triage` - Incident moved to triage status
* `incident.mitigated` - Incident mitigated
* `incident.resolved` - Incident marked resolved
* `incident.cancelled` - Incident cancelled
* `incident.deleted` - Incident deleted

### Manual Trigger Event Types

These events are triggered by user actions and are managed by actions' `event_types_trigger` field, not connector subscriptions:

* `action.triggered` - Standalone action triggered by a user
* `alert.action_triggered` - Action triggered from an alert context
* `incident.action_triggered` - Action triggered from an incident context

<Info>
  Automatic events can be subscribed to when configuring your Edge Connector. Manual trigger events are configured per action and execute when users trigger them from the UI.
</Info>

## Event Payload Examples

Below are detailed examples of event payloads for each event type.

### alert.created - Production Database Alert

```json  theme={null}
{
  "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "event_id": "a3bb189e-8bf9-3888-9912-ace4e6543002",
  "event_type": "alert.created",
  "timestamp": "2025-10-26T21:30:00Z",
  "data": {
    "id": "6aeb35ae-ca31-4bcf-91bd-c4ecce44dedc",
    "source": "datadog",
    "summary": "High database latency detected",
    "status": "open",
    "labels": {
      "severity": "critical",
      "component": "database",
      "region": "us-west-2"
    },
    "data": {
      "host": "prod-db-01.example.com",
      "latency_ms": 1500,
      "threshold_ms": 500,
      "query_count": 342
    },
    "started_at": "2025-10-26T21:29:45Z",
    "ended_at": null,
    "created_at": "2025-10-26T21:29:50Z",
    "updated_at": "2025-10-26T21:29:50Z",
    "services": [
      {
        "id": "8e3f9c2a-1d5b-4e8f-9a3c-7b2d4e6f8a1c",
        "name": "DB - Production Database",
        "slug": "db-production"
      }
    ],
    "environments": [
      {
        "id": "2c4e6a8b-3f5d-4a7c-8b9e-1f3a5c7d9e2b",
        "name": "Production",
        "slug": "production",
        "color": "#E74C3C"
      }
    ]
  }
}
```

### Template Usage

```yaml  theme={null}
parameters:
  alert_id: "{{ id }}"
  alert_summary: "{{ summary }}"
  severity: "{{ labels.severity }}"
  host: "{{ data.host }}"
  latency: "{{ data.latency_ms }}"
  service_name: "{{ services.0.name }}"      # First service
  environment: "{{ environments.0.slug }}"   # First environment
```

## alert.created - PagerDuty Integration

```json  theme={null}
{
  "id": "9d4e2f1c-7a8b-4c3d-9e5f-6a7b8c9d0e1f",
  "event_id": "5c6d7e8f-9a0b-4c5d-8e9f-0a1b2c3d4e5f",
  "event_type": "alert.created",
  "timestamp": "2025-10-26T21:35:00Z",
  "data": {
    "id": "b8c9d0e1-f2a3-4b5c-6d7e-8f9a0b1c2d3e",
    "source": "pagerduty",
    "summary": "API service is down",
    "status": "open",
    "labels": {
      "severity": "high",
      "urgency": "high",
      "impact": "critical"
    },
    "data": {
      "incident_key": "PD-12345",
      "incident_url": "https://example.pagerduty.com/incidents/12345",
      "triggered_by": "monitoring_service",
      "escalation_policy": "Engineering On-Call"
    },
    "started_at": "2025-10-26T21:34:30Z",
    "ended_at": null,
    "created_at": "2025-10-26T21:34:35Z",
    "updated_at": "2025-10-26T21:34:35Z",
    "services": [
      {
        "id": "3f4e5d6c-7b8a-4c9d-0e1f-2a3b4c5d6e7f",
        "name": "API Gateway",
        "slug": "api-gateway"
      },
      {
        "id": "8a9b0c1d-2e3f-4a5b-6c7d-8e9f0a1b2c3d",
        "name": "Authentication Service",
        "slug": "auth-service"
      }
    ],
    "environments": [
      {
        "id": "1e2f3a4b-5c6d-7e8f-9a0b-1c2d3e4f5a6b",
        "name": "Production",
        "slug": "production",
        "color": "#E74C3C"
      }
    ]
  }
}
```

### Template Usage

```yaml  theme={null}
parameters:
  pagerduty_key: "{{ data.incident_key }}"
  pagerduty_url: "{{ data.incident_url }}"
  urgency: "{{ labels.urgency }}"
  all_services: "{{ services | join:', ' }}"  # "API Gateway, Authentication Service"
```

## alert.updated - Status Change

```json  theme={null}
{
  "id": "4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a",
  "event_id": "7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b",
  "event_type": "alert.updated",
  "timestamp": "2025-10-26T22:00:00Z",
  "data": {
    "id": "6aeb35ae-ca31-4bcf-91bd-c4ecce44dedc",
    "source": "datadog",
    "summary": "High database latency detected",
    "status": "resolved",
    "labels": {
      "severity": "critical",
      "component": "database"
    },
    "data": {
      "host": "prod-db-01.example.com",
      "latency_ms": 150,
      "resolution": "auto-scaled database pool"
    },
    "started_at": "2025-10-26T21:29:45Z",
    "ended_at": "2025-10-26T21:59:30Z",
    "created_at": "2025-10-26T21:29:50Z",
    "updated_at": "2025-10-26T22:00:00Z",
    "services": [
      {
        "id": "8e3f9c2a-1d5b-4e8f-9a3c-7b2d4e6f8a1c",
        "name": "DB - Production Database",
        "slug": "db-production"
      }
    ],
    "environments": [
      {
        "id": "2c4e6a8b-3f5d-4a7c-8b9e-1f3a5c7d9e2b",
        "name": "Production",
        "slug": "production",
        "color": "#E74C3C"
      }
    ]
  }
}
```

## incident.created - Full Example

Based on `EdgeConnectors::IncidentSerializer`:

```json  theme={null}
{
  "id": "c1d2e3f4-a5b6-7c8d-9e0f-1a2b3c4d5e6f",
  "event_id": "2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e",
  "event_type": "incident.created",
  "timestamp": "2025-10-26T23:00:00Z",
  "data": {
    "id": "9f8e7d6c-5b4a-3210-fedc-ba9876543210",
    "sequential_id": 42,
    "title": "Production API Gateway Outage",
    "slug": "production-api-gateway-outage",
    "summary": "Complete outage affecting all customers",
    "status": "started",
    "kind": "normal",
    "private": false,
    "detected_at": "2025-10-26T22:58:00Z",
    "acknowledged_at": null,
    "started_at": "2025-10-26T22:58:00Z",
    "mitigated_at": null,
    "resolved_at": null,
    "cancelled_at": null,
    "created_at": "2025-10-26T22:59:00Z",
    "updated_at": "2025-10-26T23:00:00Z",
    "services": [
      {
        "id": "3f4e5d6c-7b8a-4c9d-0e1f-2a3b4c5d6e7f",
        "name": "API Gateway",
        "slug": "api-gateway"
      }
    ],
    "environments": [
      {
        "id": "1e2f3a4b-5c6d-7e8f-9a0b-1c2d3e4f5a6b",
        "name": "Production",
        "slug": "production",
        "color": "#E74C3C"
      }
    ],
    "functionalities": [
      {
        "id": "a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d",
        "name": "API Requests",
        "slug": "api-requests"
      }
    ],
    "severity": {
      "id": "5e4d3c2b-1a09-8f7e-6d5c-4b3a2910fedc",
      "name": "SEV1",
      "slug": "sev1",
      "color": "#FF0000"
    }
  }
}
```

## alert.action\_triggered - User-Initiated Restart on Alert

```json  theme={null}
{
  "id": "e6f7a8b9-c0d1-2e3f-4a5b-6c7d8e9f0a1b",
  "event_id": "d5e6f7a8-b9c0-1d2e-3f4a-5b6c7d8e9f0a",
  "event_type": "alert.action_triggered",
  "timestamp": "2025-10-26T23:15:00Z",
  "action": {
    "id": "7a8b9c0d-1e2f-3a4b-5c6d-7e8f9a0b1c2d",
    "name": "Restart Test Service",
    "slug": "restart_test_service"
  },
  "data": {
    "entity_id": "f0a1b2c3-d4e5-6f7a-8b9c-0d1e2f3a4b5c",
    "parameters": {
      "service_name": "api-gateway",
      "environment": "production",
      "force_restart": true,
      "drain_timeout": 30
    },
    "triggered_by": {
      "id": 50,
      "name": "Quentin Rousseau",
      "email": "quentin@rootly.com"
    }
  }
}
```

### Template Usage in Actions

```yaml  theme={null}
# Script action for alert actions
- name: restart_test_service
  type: script
  script: /opt/scripts/restart-service.sh
  trigger:
    event_type: "alert.action_triggered"

  parameters:
    # Action metadata (from top-level action object)
    action_display_name: "{{ action.name }}"  # "Restart Test Service"
    action_slug: "{{ action.slug }}"          # "restart_test_service"

    # User inputs (from UI)
    service_name: "{{ parameters.service_name }}"
    environment: "{{ parameters.environment }}"
    force: "{{ parameters.force_restart }}"

    # Context data
    entity_id: "{{ entity_id }}"
    triggered_by_email: "{{ triggered_by.email }}"

    # Hardcoded
    region: "us-west-2"
    timeout: "60"
```

## incident.action\_triggered - Escalation on Incident

```json  theme={null}
{
  "id": "b9c0d1e2-f3a4-5b6c-7d8e-9f0a1b2c3d4e",
  "event_id": "a8b9c0d1-e2f3-4a5b-6c7d-8e9f0a1b2c3d",
  "event_type": "incident.action_triggered",
  "timestamp": "2025-10-26T23:20:00Z",
  "action": {
    "id": "6c7d8e9f-0a1b-2c3d-4e5f-6a7b8c9d0e1f",
    "name": "Scale Infrastructure",
    "slug": "scale_infrastructure"
  },
  "data": {
    "entity_id": "d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a",
    "parameters": {
      "target_capacity": 200,
      "scaling_policy": "aggressive"
    },
    "triggered_by": {
      "id": 42,
      "name": "Sarah Johnson",
      "email": "sarah@example.com"
    }
  }
}
```

## action.triggered - Standalone Action

```json  theme={null}
{
  "id": "c3d4e5f6-a7b8-9c0d-1e2f-3a4b5c6d7e8f",
  "event_id": "b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e",
  "event_type": "action.triggered",
  "timestamp": "2025-10-26T23:25:00Z",
  "action": {
    "id": "5f6a7b8c-9d0e-1f2a-3b4c-5d6e7f8a9b0c",
    "name": "Clear Global Cache",
    "slug": "clear_global_cache"
  },
  "data": {
    "parameters": {
      "cache_type": "redis",
      "scope": "global"
    },
    "triggered_by": {
      "id": 50,
      "name": "Quentin Rousseau",
      "email": "quentin@rootly.com"
    }
    // No entity_id - this is a standalone action
  }
}
```

## Edge Cases

### Alert with No Services

```json  theme={null}
{
  "event_type": "alert.created",
  "data": {
    "id": "e9f0a1b2-c3d4-5e6f-7a8b-9c0d1e2f3a4b",
    "summary": "Orphaned alert",
    "status": "open",
    "services": [],        // ← Empty array
    "environments": []     // ← Empty array
  }
}
```

### Alert with Custom Data (Datadog)

```json  theme={null}
{
  "event_type": "alert.created",
  "data": {
    "id": "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a",
    "source": "datadog",
    "summary": "CPU usage above 90%",
    "status": "open",
    "data": {
      "tags": ["env:production", "service:api", "host:prod-01"],
      "metric": "system.cpu.usage",
      "value": 94.2,
      "threshold": 90.0,
      "monitor_id": "12345678",
      "monitor_name": "High CPU Usage"
    }
  }
}
```

### Standalone Action with No Parameters

```json  theme={null}
{
  "event_type": "action.triggered",
  "action": {
    "id": "c7d8e9f0-a1b2-3c4d-5e6f-7a8b9c0d1e2f",
    "name": "Clear Cache",
    "slug": "clear_cache"
  },
  "data": {
    "parameters": {},      // ← No user inputs required
    "triggered_by": {
      "id": 50,
      "name": "Quentin Rousseau",
      "email": "quentin@rootly.com"
    }
    // No entity_id - standalone action
  }
}
```

## HTTP Action Examples

### alert.created → Slack Notification

```yaml  theme={null}
- name: notify_slack_alert
  type: http
  trigger:
    event_type: "alert.created"
  http:
    url: "{{ env.SLACK_WEBHOOK_URL }}"
    method: POST
    headers:
      Content-Type: "application/json"
    body: |
      {
        "text": ":warning: New Alert",
        "attachments": [{
          "color": "danger",
          "fields": [
            {"title": "Summary", "value": "{{ summary }}", "short": false},
            {"title": "Source", "value": "{{ source }}", "short": true},
            {"title": "Severity", "value": "{{ labels.severity }}", "short": true},
            {"title": "Host", "value": "{{ data.host }}", "short": true},
            {"title": "Environment", "value": "{{ environments.0.name }}", "short": true}
          ]
        }]
      }
  timeout: 10
```

### incident.created → PagerDuty Integration

```yaml  theme={null}
- name: create_pagerduty_incident
  type: http
  trigger:
    event_type: "incident.created"
  http:
    url: "https://api.pagerduty.com/incidents"
    method: POST
    headers:
      Authorization: "Token token={{ env.PAGERDUTY_TOKEN }}"
      Content-Type: "application/json"
      From: "{{ env.PAGERDUTY_FROM_EMAIL }}"
    body: |
      {
        "incident": {
          "type": "incident",
          "title": "[{{ severity.name }}] {{ title }}",
          "service": {
            "id": "{{ env.PAGERDUTY_SERVICE_ID }}",
            "type": "service_reference"
          },
          "urgency": "high",
          "body": {
            "type": "incident_body",
            "details": "{{ summary }}\n\nAffected services: {{ services.0.name }}"
          }
        }
      }
  timeout: 15
```

### alert.action\_triggered → Restart Service API

```yaml  theme={null}
- name: restart_service_api
  type: http
  trigger:
    event_type: "alert.action_triggered"
    action_name: "restart_service_api"
  parameter_definitions:
    - name: service_name
      type: string
      required: true
    - name: force_restart
      type: boolean
      default: false
  http:
    url: "https://api.example.com/v1/services/{{ parameters.service_name }}/restart"
    method: POST
    headers:
      Authorization: "Bearer {{ env.API_TOKEN }}"
      Content-Type: "application/json"
      X-Triggered-By: "{{ triggered_by.email }}"
    body: |
      {
        "force": {{ parameters.force_restart }},
        "reason": "Manual restart via Rootly",
        "alert_id": "{{ entity_id }}"
      }
  timeout: 60
```

### action.triggered → Clear Global Cache

```yaml  theme={null}
- name: clear_cache_http
  type: http
  trigger:
    event_type: "action.triggered"
    action_name: "clear_cache_http"
  parameter_definitions:
    - name: cache_type
      type: string
      options: ["redis", "memcached", "all"]
      required: true
  http:
    url: "https://cache-api.example.com/v1/clear"
    method: POST
    headers:
      X-API-Key: "{{ env.CACHE_API_KEY }}"
    params:
      type: "{{ parameters.cache_type }}"
    body: |
      {
        "triggered_by": "{{ triggered_by.email }}",
        "scope": "global"
      }
  timeout: 30
```

**HTTP Action Behavior:**

* Exit code = HTTP status code (200, 404, 500, etc.)
* Stdout = Response body + status message
* Stderr = Error message (if request fails)
* Success = 2xx status codes
* Failure = 4xx, 5xx status codes

## Template Access Patterns

### Simple Fields

```yaml  theme={null}
alert_id: "{{ id }}"
status: "{{ status }}"
summary: "{{ summary }}"
```

### Nested Objects

```yaml  theme={null}
severity: "{{ labels.severity }}"
host: "{{ data.host }}"
metric_value: "{{ data.value }}"
```

### Arrays (First Element)

```yaml  theme={null}
service_name: "{{ services.0.name }}"
service_slug: "{{ services.0.slug }}"
environment: "{{ environments.0.slug }}"
```

### Environment Variables

```yaml  theme={null}
api_key: "{{ env.DATADOG_API_KEY }}"
region: "{{ env.AWS_REGION }}"
```

### Mixed

```yaml  theme={null}
message: "[{{ labels.severity }}] {{ summary }} on {{ data.host }} in {{ environments.0.name }}"
# Result: "[critical] High database latency detected on prod-db-01.example.com in Production"
```

## Testing Locally

Create a test event payload file:

```bash  theme={null}
# test-alert.json
{
  "events": [{
    "id": "b6c7d8e9-f0a1-2b3c-4d5e-6f7a8b9c0d1e",
    "event_id": "a5b6c7d8-e9f0-1a2b-3c4d-5e6f7a8b9c0d",
    "event_type": "alert.created",
    "timestamp": "2025-10-26T23:00:00Z",
    "data": {
      "id": "9e0f1a2b-3c4d-5e6f-7a8b-9c0d1e2f3a4b",
      "source": "test",
      "summary": "Test alert for local development",
      "status": "open",
      "labels": {"severity": "critical"},
      "data": {"host": "localhost"},
      "services": [{"id": "8d9e0f1a-2b3c-4d5e-6f7a-8b9c0d1e2f3a", "name": "Test Service", "slug": "test"}],
      "environments": [{"id": "7c8d9e0f-1a2b-3c4d-5e6f-7a8b9c0d1e2f", "name": "Development", "slug": "dev"}]
    }
  }]
}
```

Then post to your local mock server to trigger actions.


Built with [Mintlify](https://mintlify.com).