# Source: https://docs.rootly.com/edge-connectors-actions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Action Configuration

> Configure script and HTTP actions for Edge Connectors to automate responses to events

## Overview

Actions define what your Edge Connector executes in response to events. Each action specifies:

* **Type**: Script or HTTP request
* **Source Type**: Local scripts or Git-based scripts
* **Trigger**: Which events activate this action
* **Parameters**: User-configurable inputs (for manual triggers)
* **Execution details**: Scripts to run or HTTP requests to make

## Automatic vs Callable Actions

Edge Connector actions fall into two categories with different behaviors:

### Automatic Actions (`on:` section)

**What they are:**

* Execute automatically in response to Rootly system events
* Run without user interaction
* Configured in the `on:` section where the event type is the key

**When to use:**

* Auto-remediation (restart services when alerts fire)
* Notifications (send webhooks when incidents are created)
* Data collection (gather logs when alerts trigger)
* Monitoring integration (sync status to external systems)

**Configuration:**

```yaml  theme={null}
on:
  alert.created:                    # Event type is the key
    script: /opt/scripts/handle-alert.sh
    parameters:
      alert_id: "{{ id }}"
      severity: "{{ labels.severity }}"
    timeout: 60
```

**Characteristics:**

* ✅ No `parameter_definitions` needed (no user input)
* ✅ Execute immediately when events occur
* ✅ Registered with backend for visibility/audit
* ✅ Appear in Rootly UI as read-only badges (visible but not clickable)
* ✅ Users can see what automations are configured

**How they appear in Rootly UI:**

* Badge: "🔄 Script: alert.created" or "🌐 HTTP: incident.created"
* Read-only display showing what's automated
* No interaction possible (run automatically only)

### Callable Actions (`callable:` section)

**What they are:**

* Triggered manually by users from the Rootly UI
* Require user input via parameter forms
* Configured in the `callable:` section where the action slug is the key

**When to use:**

* Manual remediation (restart specific services on demand)
* User-initiated operations (deploy hotfixes, scale infrastructure)
* Diagnostic tools (collect logs, run health checks)
* Administrative tasks (clear caches, trigger backups)

**Configuration:**

```yaml  theme={null}
callable:
  restart_service:                  # Action slug is the key
    name: "Restart Service"         # Display name in UI (required)
    description: "Restart a production service with graceful shutdown"
    trigger: alert.action_triggered # Shows on alerts
    script: /opt/scripts/restart.sh
    parameter_definitions:          # Creates UI form
      - name: service_name
        type: string
        required: true
        description: "Service to restart"
    timeout: 120
```

**Characteristics:**

* ✅ Require `parameter_definitions` to create UI forms
* ✅ Users provide input values before execution
* ✅ Registered with backend to generate UI buttons
* ✅ Appear in Rootly UI as interactive buttons
* ✅ Can be triggered from alerts, incidents, or standalone

**How they appear in Rootly UI:**

* Button: "Restart Service" with form dialog
* Users click → fill out form → submit → action executes
* Real-time execution status and results shown

### Comparison Table

| Feature                    | Automatic Actions (`on:`)                             | Callable Actions (`callable:`)              |
| -------------------------- | ----------------------------------------------------- | ------------------------------------------- |
| **Trigger**                | System events (alert.created, incident.created, etc.) | User clicks button in Rootly UI             |
| **User Input**             | None - uses event data only                           | Yes - users fill out parameter forms        |
| **Config Section**         | `on:` (event type is key)                             | `callable:` (action slug is key)            |
| **parameter\_definitions** | Not needed                                            | Required to create UI forms                 |
| **name**                   | Optional                                              | Required for UI display                     |
| **UI Appearance**          | Read-only badge (visible, not clickable)              | Interactive button (clickable with form)    |
| **Registration**           | Registered for visibility                             | Registered to generate UI                   |
| **Execution**              | Immediate when event occurs                           | On-demand when user triggers                |
| **Use Cases**              | Auto-remediation, notifications, monitoring           | Manual operations, diagnostics, admin tasks |

### Registration Behavior

**Both automatic and callable actions are registered with the Rootly backend on connector startup:**

1. **Connector Startup:**
   * Reads `actions.yml` configuration
   * Sends all actions to `POST /rec/v1/actions` endpoint
   * Backend syncs actions for this connector

2. **Backend Processing:**
   * **Automatic actions** (no `parameter_definitions`):
     * Stored for visibility and audit
     * Displayed as read-only badges in UI
     * Users can see what automations exist
   * **Callable actions** (with `parameter_definitions`):
     * UI forms generated from parameter definitions
     * Displayed as interactive buttons
     * Users can click and provide inputs

3. **Sync Behavior:**
   * Backend matches actions by slug
   * Creates new actions not seen before
   * Updates existing actions with new configuration
   * Removes actions no longer in config

**What gets sent to backend:**

* Action slug, name, description (for UI display)
* Action type (script or HTTP) and timeout
* Trigger event types
* Parameter definitions (for callable actions only)

**What stays on connector:**

* Script paths and execution details
* HTTP URLs, headers, and body templates
* Security settings and environment variables

<Info>
  The presence of `parameter_definitions` is what tells the backend whether an action is automatic (read-only) or callable (interactive).
</Info>

## Action File Structure

Actions are defined in an `actions.yml` file with three main sections:

```yaml  theme={null}
# Global defaults (optional)
defaults:
  timeout: 30
  source_type: local
  env:
    ENVIRONMENT: production

# Automatic actions - triggered by system events
on:
  alert.created:
    script: /path/to/script.sh
    # ...

# Manual actions - triggered by users from UI
callable:
  restart_service:
    name: "Restart Service"
    # ...
```

## Action Types

### Script Actions

Execute scripts from local filesystem or Git repositories.

#### Local Scripts

Execute scripts stored on the Edge Connector host:

```yaml  theme={null}
callable:
  restart_service:
    name: "Restart Production Service"
    description: |
      Restarts the specified service with graceful shutdown.
      Use when service becomes unresponsive.
    trigger: alert.action_triggered
    script: /opt/scripts/restart-service.sh
    parameter_definitions:
      - name: service_name
        type: string
        required: true
        description: "Service to restart"
      - name: environment
        type: string
        required: false
        default: "production"
        options: ["development", "staging", "production"]
    timeout: 300
```

**Key Fields:**

* `script`: Absolute path to the script to execute
* `timeout`: Maximum execution time in seconds
* `parameter_definitions`: User inputs when triggered manually
* `trigger`: Specifies the event type (`alert.action_triggered`, `incident.action_triggered`, or defaults to `action.triggered`)
* `source_type`: `local` (default) or `git`

#### Git-Based Scripts

Execute scripts from a Git repository that the Edge Connector syncs automatically:

```yaml  theme={null}
callable:
  run_playbook:
    name: "Run Incident Playbook"
    description: "Execute Ansible playbook from Git repository"
    trigger: incident.action_triggered
    source_type: git
    script: playbooks/incident-response.yml
    git_options:
      url: "https://github.com/your-org/runbooks.git"
      branch: main
      poll_interval_sec: 300
    parameter_definitions:
      - name: playbook
        type: list
        options: [database, network, application]
        required: true
        description: "Which playbook to run"
    parameters:
      incident_id: "{{ entity_id }}"
      severity: "{{ severity.slug }}"
    timeout: 600
```

**Git Options:**

* `url`: Git repository URL (HTTPS or SSH)
* `branch`: Branch to checkout (default: `main`)
* `poll_interval_sec`: How often to pull updates (default: 300)

<Info>
  Git-based scripts allow you to version control your automation scripts and update them without redeploying the Edge Connector.
</Info>

### HTTP Actions

Make HTTP/HTTPS requests to external APIs or webhooks.

```yaml  theme={null}
on:
  alert.created:
    http:
      url: "https://example.com/webhook"
      method: POST
      headers:
        Content-Type: "application/json"
        Authorization: "Bearer {{ env.API_TOKEN }}"
      params:
        source: "rootly"
      body: |
        {
          "alert_id": "{{ id }}",
          "summary": "{{ summary }}",
          "severity": "{{ labels.severity }}",
          "services": "{{ services | map: 'name' | join: ', ' }}"
        }
    timeout: 30
```

**HTTP Configuration:**

* `url`: Target endpoint (supports templates)
* `method`: GET, POST, PUT, PATCH, DELETE
* `headers`: HTTP headers (supports templates)
* `params`: Query parameters
* `body`: Request body (supports templates for JSON/text)

## Action Triggers

### Automatic Event Triggers

These actions run automatically when system events occur. They are defined in the `on:` section where the event type is the key.

**Alert Events:**

```yaml  theme={null}
on:
  alert.created:
    # Action configuration here
    script: /path/to/handle-alert.sh
```

**Incident Events:**

```yaml  theme={null}
on:
  incident.mitigated:
    # Action configuration here
    script: /path/to/handle-mitigation.sh
```

**Available Automatic Triggers:**

* `alert.created`, `alert.updated`, `alert.acknowledged`, `alert.resolved`, `alert.deleted`
* `incident.created`, `incident.updated`, `incident.in_triage`, `incident.mitigated`, `incident.resolved`, `incident.cancelled`, `incident.deleted`

<Info>
  Automatic triggers do not require `parameter_definitions` - they execute automatically with event data.
</Info>

### Manual Trigger Events

These actions are triggered manually by users from the Rootly UI. They require `parameter_definitions` to create input forms.

**Action on Alert:**

```yaml  theme={null}
callable:
  restart_affected_service:
    name: "Restart Affected Service"
    trigger: alert.action_triggered
    script: /opt/scripts/restart.sh
    parameter_definitions:
      - name: service_name
        type: string
        required: true
      - name: force_restart
        type: boolean
        default: false
```

**Action on Incident:**

```yaml  theme={null}
callable:
  scale_infrastructure:
    name: "Scale Infrastructure"
    trigger: incident.action_triggered
    script: /opt/scripts/scale.sh
    parameter_definitions:
      - name: target_capacity
        type: number
        required: true
```

**Standalone Action:**

```yaml  theme={null}
callable:
  clear_cache:
    name: "Clear Global Cache"
    # trigger defaults to: action.triggered
    http:
      url: "https://api.example.com/cache/clear"
      method: POST
    parameter_definitions:
      - name: cache_type
        type: string
        required: true
        options: ["redis", "memcached", "all"]
```

## Parameter Definitions

Parameters create user input forms for manually triggered actions.

### Parameter Types

**String:**

```yaml  theme={null}
- name: service_name
  type: string
  required: true
  description: "Name of the service"
```

**Number:**

```yaml  theme={null}
- name: capacity
  type: number
  required: true
  description: "Target capacity percentage"
```

**Boolean:**

```yaml  theme={null}
- name: force_restart
  type: boolean
  default: false
  description: "Force restart without graceful shutdown"
```

**List (Dropdown):**

```yaml  theme={null}
- name: cache_type
  type: list
  options: [redis, memcached, all]
  default: redis
  required: true
  description: "Which cache to clear"
```

<Note>
  Use `type: list` with `options` array for dropdown selections. This is preferred over `type: string` with `options` for clarity.
</Note>

### Parameter Fields

* `name`: Parameter identifier (used in templates as `{{ parameters.name }}`)
* `type`: Data type (string, number, boolean)
* `required`: Whether input is mandatory
* `default`: Default value if not provided
* `options`: List of allowed values (creates dropdown)
* `description`: Help text shown in UI

## Using Templates in Actions

Actions support Liquid templates for dynamic values. See the [Template Syntax](/edge-connectors-templates) guide for detailed documentation.

### Event Data Templates

Access event data in your action configuration:

```yaml  theme={null}
parameters:
  alert_id: "{{ id }}"
  summary: "{{ summary }}"
  severity: "{{ labels.severity }}"
  service: "{{ services.first.name }}"
```

### User Parameter Templates

Access user inputs in manually triggered actions:

```yaml  theme={null}
parameters:
  service: "{{ parameters.service_name }}"
  env: "{{ parameters.environment }}"
  force: "{{ parameters.force_restart }}"
```

### Environment Variables

Access environment variables securely:

```yaml  theme={null}
headers:
  Authorization: "Bearer {{ env.API_TOKEN }}"
  X-API-Key: "{{ env.SECRET_KEY }}"
```

## Complete Examples

### Example 1: Automatic Alert Response

Automatically restart a service when critical alerts are detected:

```yaml  theme={null}
on:
  alert.created:
    script: /opt/scripts/restart-service.sh
    parameters:
      service: "{{ services.first.slug }}"
      environment: "{{ environments.first.slug }}"
      alert_id: "{{ id }}"
      severity: "{{ labels.severity }}"
    timeout: 120
```

### Example 2: Manual Service Scaling

Allow users to manually scale services from incidents:

```yaml  theme={null}
callable:
  scale_service:
    name: "Scale Service Capacity"
    description: |
      Manually scale service capacity.
      Use during incidents to increase capacity.
    trigger: incident.action_triggered
    script: /opt/scripts/scale-service.sh
    parameter_definitions:
      - name: target_capacity
        type: number
        required: true
        description: "Target capacity (50-200%)"
      - name: scaling_speed
        type: string
        required: false
        default: "normal"
        options: ["slow", "normal", "fast"]
        description: "Scaling speed"
    parameters:
      # User inputs: target_capacity and scaling_speed
      # are auto-available as {{ parameters.target_capacity }}, etc.
      # Add extra context here:
      incident_id: "{{ entity_id }}"
      triggered_by: "{{ triggered_by.email }}"
    timeout: 300
```

### Example 3: Webhook Notification

Send HTTP notification when incidents are mitigated:

```yaml  theme={null}
on:
  incident.mitigated:
    http:
      url: "{{ env.SLACK_WEBHOOK_URL }}"
      method: POST
      headers:
        Content-Type: "application/json"
      body: |
        {
          "text": "Incident Mitigated",
          "attachments": [{
            "color": "good",
            "fields": [
              {"title": "Incident", "value": "{{ title }}", "short": false},
              {"title": "Severity", "value": "{{ severity.name }}", "short": true},
              {"title": "Services", "value": "{{ services | map: 'name' | join: ', ' }}", "short": true},
              {"title": "Duration", "value": "{{ mitigated_at | date: '%Y-%m-%d %H:%M' }}", "short": true}
            ]
          }]
        }
    timeout: 10
```

### Example 4: PagerDuty Integration

Create PagerDuty incidents for high-severity Rootly incidents:

```yaml  theme={null}
on:
  incident.created:
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
              "details": "{{ summary }}\n\nAffected services: {{ services | map: 'name' | join: ', ' }}"
            }
          }
        }
    timeout: 15
```

## Best Practices

### Security

* **Store secrets in environment variables**, never in action configuration
* **Use absolute paths** for scripts to prevent path traversal
* **Validate user inputs** in your scripts
* **Limit script permissions** - run with minimal privileges
* **Audit action execution logs** regularly

### Reliability

* **Set appropriate timeouts** based on expected execution time
* **Implement retry logic** in your scripts for transient failures
* **Handle errors gracefully** and return meaningful error messages
* **Test actions thoroughly** before deploying to production
* **Monitor action execution** via Rootly dashboard

### Configuration

* **Use descriptive IDs** (snake\_case: `restart_production_db`)
* **Provide clear names** for UI display
* **Write helpful descriptions** explaining when to use the action
* **Add parameter descriptions** to guide users
* **Use options** for parameters with limited valid values

### Templates

* **Use `default` filter** for optional fields: `{{ field | default: "N/A" }}`
* **Test templates** with sample event data before deploying
* **Keep templates simple** - complex logic belongs in scripts
* **Document template variables** in action descriptions

## Action Configuration File

Actions are defined in an `actions.yml` file with three main sections:

```yaml  theme={null}
# Global defaults (optional) - applied to all actions
defaults:
  timeout: 30                        # Default timeout for all actions
  source_type: local                 # Default source: local or git
  env:                               # Environment variables for all actions
    ENVIRONMENT: production
    LOG_LEVEL: info

# Automatic actions - triggered by system events
# Event type is the KEY
on:
  alert.created:
    script: /path/to/handle-alert.sh
    parameters:
      alert_id: "{{ id }}"
      severity: "{{ labels.severity }}"
    timeout: 60

  incident.created:
    http:
      url: "{{ env.SLACK_WEBHOOK_URL }}"
      method: POST
      body: |
        {"text": "Incident: {{ title }}"}

# Manual actions - triggered by users from UI
# Action slug is the KEY
callable:
  restart_service:
    name: "Restart Service"
    description: "Restart a production service"
    trigger: alert.action_triggered  # Shows on alerts only
    script: /path/to/restart.sh
    parameter_definitions:
      - name: service_name
        type: string
        required: true
    parameters:
      # User inputs are auto-available as {{ parameters.service_name }}
      # This section adds EXTRA context beyond user inputs:
      alert_id: "{{ entity_id }}"
      triggered_by: "{{ triggered_by.email }}"
    timeout: 120

  clear_cache:
    name: "Clear Cache"
    description: "Clear application cache"
    # trigger defaults to: action.triggered (standalone action)
    script: /path/to/clear-cache.sh
    parameter_definitions:
      - name: cache_type
        type: list
        options: [redis, memcached, all]

  run_from_git:
    name: "Run Git-based Script"
    source_type: git                 # Override default source_type
    script: scripts/automation.sh
    git_options:
      url: "https://github.com/org/repo.git"
      branch: main
      poll_interval_sec: 300
```

The Edge Connector reads this file on startup and registers all actions with Rootly.

**Key Concepts:**

* `defaults:` section: Global settings applied to all actions unless overridden
* `on:` section: Automatic actions where event type is the **key**
* `callable:` section: Manual actions where action slug is the **key**
* `source_type`: `local` for filesystem scripts, `git` for repository-based scripts
* `parameter_definitions`: Create user input forms; auto-accessible as `{{ parameters.X }}`
* `parameters:` section: Adds **extra** parameters beyond user inputs
* Scripts receive all parameters as `REC_PARAM_*` environment variables

## Next Steps

* See [Event Examples](/edge-connectors-event-examples) for sample event payloads
* Learn [Template Syntax](/edge-connectors-templates) for dynamic values
* Review the main [Edge Connectors](/edge-connectors) documentation


Built with [Mintlify](https://mintlify.com).