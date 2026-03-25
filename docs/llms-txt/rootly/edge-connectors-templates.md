# Source: https://docs.rootly.com/edge-connectors-templates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Template Syntax

> Use Liquid templates to dynamically insert event data and parameters into Edge Connector actions

## Overview

Edge Connectors use **Liquid templates** to dynamically substitute values from events, user parameters, and environment variables into your action configurations.

Templates allow you to:

* Access event data (alerts, incidents, etc.)
* Use user-provided parameters from manual triggers
* Reference environment variables securely
* Transform data with filters

<Info>
  Edge Connectors use the [osteele/liquid](https://github.com/osteele/liquid) library, a Go implementation of Shopify's Liquid template language.
</Info>

## Basic Syntax

### Simple Fields

Access top-level fields directly:

```yaml  theme={null}
{{ id }}              # Event ID
{{ summary }}         # Alert/incident summary
{{ status }}          # Current status
{{ title }}           # Incident title
```

### Nested Fields

Use dot notation for nested objects:

```yaml  theme={null}
{{ labels.severity }}        # Alert severity label
{{ data.host }}              # Custom monitoring data
{{ severity.name }}          # Incident severity object
{{ triggered_by.email }}     # User who triggered action
```

### Array Access

Access array elements by index or using helpers:

```yaml  theme={null}
{{ services[0].name }}       # First service (by index)
{{ services.first.name }}    # First service (helper)
{{ services.last.slug }}     # Last service (helper)
{{ environments[0].slug }}   # First environment
```

### Environment Variables

Securely access environment variables:

```yaml  theme={null}
{{ env.API_KEY }}            # From REC_API_KEY or API_KEY
{{ env.AWS_REGION }}         # From REC_AWS_REGION or AWS_REGION
{{ env.WEBHOOK_URL }}        # From REC_WEBHOOK_URL or WEBHOOK_URL
```

<Warning>
  Store sensitive values like API keys and tokens in environment variables, never in action configuration files.
</Warning>

## Event Data Access

### Alert Events

Common fields available in alert events:

```yaml  theme={null}
{{ id }}                      # Alert UUID
{{ summary }}                 # Alert summary text
{{ status }}                  # open, acknowledged, resolved
{{ source }}                  # datadog, pagerduty, etc.
{{ labels.severity }}         # Severity from monitoring system
{{ data.host }}               # Custom monitoring data
{{ services[0].name }}        # Affected service
{{ environments[0].slug }}    # Environment (production, etc.)
{{ started_at }}              # When alert started
```

### Incident Events

Common fields available in incident events:

```yaml  theme={null}
{{ id }}                      # Incident UUID
{{ sequential_id }}           # Incident number (42, 43, etc.)
{{ title }}                   # Incident title
{{ summary }}                 # Incident summary
{{ status }}                  # started, mitigated, resolved
{{ severity.name }}           # SEV1, SEV2, etc.
{{ severity.slug }}           # sev1, sev2, etc.
{{ services | map: 'name' }}  # All affected services
{{ environments[0].name }}    # Environment name
{{ detected_at }}             # When detected
{{ mitigated_at }}            # When mitigated
{{ resolved_at }}             # When resolved
```

### Action Trigger Events

Fields available when users manually trigger actions:

```yaml  theme={null}
{{ entity_id }}                   # Alert or incident ID
{{ action.name }}                 # Action display name
{{ action.slug }}                 # Action identifier
{{ parameters.service_name }}     # User input parameter
{{ parameters.environment }}      # User input parameter
{{ triggered_by.id }}             # User ID
{{ triggered_by.name }}           # User name
{{ triggered_by.email }}          # User email
```

## Filters

Filters transform values using the pipe (`|`) operator.

### Array Filters

**map** - Extract property from objects:

```yaml  theme={null}
{{ services | map: "name" }}
# [{name: "DB"}, {name: "API"}] → ["DB", "API"]
```

**join** - Combine array elements:

```yaml  theme={null}
{{ services | map: "name" | join: ", " }}
# ["DB", "API", "Cache"] → "DB, API, Cache"
```

**first** - Get first element:

```yaml  theme={null}
{{ services | first }}
# Returns first service object
```

**last** - Get last element:

```yaml  theme={null}
{{ services | last }}
# Returns last service object
```

**sort** - Sort alphabetically:

```yaml  theme={null}
{{ names | sort }}
# ["charlie", "alice", "bob"] → ["alice", "bob", "charlie"]
```

**uniq** - Remove duplicates:

```yaml  theme={null}
{{ items | uniq }}
# [1, 2, 2, 3, 1] → [1, 2, 3]
```

**compact** - Remove nil values:

```yaml  theme={null}
{{ items | compact }}
# [1, nil, 2, nil, 3] → [1, 2, 3]
```

**reverse** - Reverse order:

```yaml  theme={null}
{{ items | reverse }}
# [1, 2, 3] → [3, 2, 1]
```

### String Filters

**upcase** - Convert to uppercase:

```yaml  theme={null}
{{ status | upcase }}
# "open" → "OPEN"
```

**downcase** - Convert to lowercase:

```yaml  theme={null}
{{ severity | downcase }}
# "CRITICAL" → "critical"
```

**capitalize** - Capitalize first letter:

```yaml  theme={null}
{{ name | capitalize }}
# "john doe" → "John doe"
```

**default** - Provide fallback value:

```yaml  theme={null}
{{ field | default: "N/A" }}
# If field is empty → "N/A"
```

**truncate** - Shorten text:

```yaml  theme={null}
{{ summary | truncate: 50 }}
# "Very long summary text..." → "Very long summary text..."
```

**replace** - Replace all occurrences:

```yaml  theme={null}
{{ text | replace: "foo", "bar" }}
# "foo foo" → "bar bar"
```

**remove** - Remove all occurrences:

```yaml  theme={null}
{{ severity | remove: "SEV" }}
# "SEV1" → "1"
```

**strip** - Remove whitespace:

```yaml  theme={null}
{{ text | strip }}
# "  hello  " → "hello"
```

**append** - Add to end:

```yaml  theme={null}
{{ name | append: ".txt" }}
# "file" → "file.txt"
```

**prepend** - Add to beginning:

```yaml  theme={null}
{{ name | prepend: "prefix-" }}
# "name" → "prefix-name"
```

**split** - Split into array:

```yaml  theme={null}
{{ "a,b,c" | split: "," }}
# "a,b,c" → ["a", "b", "c"]
```

### Number Filters

**plus** - Add:

```yaml  theme={null}
{{ count | plus: 1 }}
# 5 → 6
```

**minus** - Subtract:

```yaml  theme={null}
{{ count | minus: 2 }}
# 5 → 3
```

**times** - Multiply:

```yaml  theme={null}
{{ value | times: 10 }}
# 5 → 50
```

**divided\_by** - Divide:

```yaml  theme={null}
{{ value | divided_by: 2 }}
# 10 → 5
```

**modulo** - Remainder:

```yaml  theme={null}
{{ value | modulo: 3 }}
# 10 → 1
```

**abs** - Absolute value:

```yaml  theme={null}
{{ value | abs }}
# -5 → 5
```

**round** - Round number:

```yaml  theme={null}
{{ value | round: 2 }}
# 3.14159 → 3.14
```

**ceil** - Round up:

```yaml  theme={null}
{{ value | ceil }}
# 3.2 → 4
```

**floor** - Round down:

```yaml  theme={null}
{{ value | floor }}
# 3.8 → 3
```

### Date Filters

**date** - Format timestamp:

```yaml  theme={null}
{{ started_at | date: "%Y-%m-%d %H:%M:%S" }}
# "2025-10-26T21:30:00Z" → "2025-10-26 21:30:00"

{{ started_at | date: "%B %d, %Y" }}
# "2025-10-26T21:30:00Z" → "October 26, 2025"
```

Common date format codes:

* `%Y` - Year (2025)
* `%m` - Month (01-12)
* `%d` - Day (01-31)
* `%H` - Hour 24h (00-23)
* `%M` - Minute (00-59)
* `%S` - Second (00-59)
* `%B` - Full month name (January)
* `%b` - Short month name (Jan)

## Real-World Examples

### Example 1: Alert Notification

Format a Slack message with alert details:

```yaml  theme={null}
body: |
  {
    "text": ":warning: New Alert",
    "attachments": [{
      "color": "danger",
      "fields": [
        {"title": "Summary", "value": "{{ summary }}", "short": false},
        {"title": "Severity", "value": "{{ labels.severity | upcase }}", "short": true},
        {"title": "Host", "value": "{{ data.host | default: 'unknown' }}", "short": true},
        {"title": "Services", "value": "{{ services | map: 'name' | join: ', ' }}", "short": false},
        {"title": "Environment", "value": "{{ environments.first.name }}", "short": true},
        {"title": "Time", "value": "{{ started_at | date: '%Y-%m-%d %H:%M' }}", "short": true}
      ]
    }]
  }
```

### Example 2: Incident Summary

Create a concise incident summary:

```yaml  theme={null}
message: "[{{ severity.name }}] {{ title }} - {{ services | map: 'name' | join: ', ' }} ({{ environments.first.slug }})"
# Result: "[SEV1] API Gateway Outage - API Gateway, Auth Service (production)"
```

### Example 3: Script Parameters

Pass structured data to a script:

```yaml  theme={null}
parameters:
  incident_id: "{{ id }}"
  incident_number: "{{ sequential_id }}"
  severity: "{{ severity.slug }}"
  services: "{{ services | map: 'slug' | join: ',' }}"
  environment: "{{ environments.first.slug }}"
  triggered_by: "{{ triggered_by.email | default: 'system' }}"
  timestamp: "{{ started_at | date: '%Y-%m-%d %H:%M:%S' }}"
```

### Example 4: Conditional Values

Use defaults for optional fields:

```yaml  theme={null}
parameters:
  reason: "{{ parameters.reason | default: 'Manual action triggered' }}"
  environment: "{{ parameters.environment | default: 'production' }}"
  force: "{{ parameters.force_restart | default: false }}"
  host: "{{ data.host | default: 'localhost' }}"
```

### Example 5: Complex Transformation

Chain multiple filters:

```yaml  theme={null}
# Extract, sort, and format service names
services_list: "{{ services | map: 'name' | sort | join: ' | ' | upcase }}"
# Result: "API GATEWAY | AUTH SERVICE | DATABASE"

# Format severity without prefix
severity_number: "{{ severity.name | remove: 'SEV' }}"
# "SEV1" → "1"
```

## Advanced Patterns

### Chaining Filters

Combine multiple filters in sequence:

```yaml  theme={null}
{{ services | map: "name" | sort | uniq | join: ", " | upcase }}
# Extract names → sort → remove duplicates → join → uppercase
```

### Nested Array Access

Access deeply nested data:

```yaml  theme={null}
{{ services[0].tags[0] }}              # First service's first tag
{{ data.metrics.values[5] }}           # Sixth metric value
{{ environments.first.config.region }} # Environment config
```

### Safe Navigation

Liquid handles missing values gracefully:

```yaml  theme={null}
{{ missing.field }}                # Returns empty string ""
{{ array[999].name }}              # Returns "" (out of bounds)
{{ undefined | default: "N/A" }}   # Returns "N/A"
```

## Common Patterns

### Service List

```yaml  theme={null}
services: "{{ services | map: 'name' | join: ', ' }}"
# "Database, API Gateway, Cache"
```

### Environment Detection

```yaml  theme={null}
env: "{{ environments.first.slug | default: 'unknown' }}"
# "production"
```

### Severity Formatting

```yaml  theme={null}
severity: "{{ labels.severity | upcase | default: 'UNKNOWN' }}"
# "CRITICAL"
```

### User Context

```yaml  theme={null}
user: "{{ triggered_by.name }} ({{ triggered_by.email }})"
# "John Doe (john@example.com)"
```

### Timestamp Formatting

```yaml  theme={null}
time: "{{ started_at | date: '%Y-%m-%d %H:%M:%S UTC' }}"
# "2025-10-26 21:30:00 UTC"
```

## Limitations

<Note>
  To keep templates simple and secure, the following Liquid features are **not** supported:
</Note>

* **No logic tags**: `{% if %}`, `{% unless %}`, `{% case %}` not supported
* **No loops**: `{% for %}` not supported - use filters like `map` and `join` instead
* **No custom tags**: Only `{{ }}` output tags are supported
* **No assignments**: `{% assign %}` not supported

Use filters and the `default` filter for conditional logic:

```yaml  theme={null}
# Instead of {% if field %}{{ field }}{% else %}N/A{% endif %}
# Use:
{{ field | default: "N/A" }}
```

## Tips & Best Practices

### 1. Use Default Filter

Always provide fallback values for optional fields:

```yaml  theme={null}
{{ data.host | default: "unknown" }}
{{ parameters.timeout | default: 30 }}
```

### 2. Extract Then Join

For arrays of objects, use `map` + `join`:

```yaml  theme={null}
{{ services | map: "name" | join: ", " }}
```

### 3. Test Templates

Test with sample event data before deploying:

* Use the [Event Examples](/edge-connectors-event-examples) for reference payloads
* Verify templates produce expected output
* Handle edge cases (empty arrays, missing fields)

### 4. Keep It Simple

Complex logic belongs in scripts, not templates:

```yaml  theme={null}
# Good: Simple data extraction
service: "{{ services.first.name }}"

# Bad: Complex transformation (do this in a script instead)
# Avoid overly complex filter chains
```

### 5. Environment Variables for Secrets

Never hardcode secrets in templates:

```yaml  theme={null}
# Good
Authorization: "Bearer {{ env.API_TOKEN }}"

# Bad
Authorization: "Bearer sk-1234567890abcdef"
```

### 6. Format for Readability

Use multiline strings for JSON/YAML bodies:

```yaml  theme={null}
body: |
  {
    "field1": "{{ value1 }}",
    "field2": "{{ value2 }}"
  }
```

## Troubleshooting

### Template Returns Empty String

* Check field name spelling
* Verify field exists in event payload (see [Event Examples](/edge-connectors-event-examples))
* Use `default` filter: `{{ field | default: "missing" }}`

### Array Access Fails

* Verify array is not empty
* Use `.first` or `.last` helpers for safety
* Check array index is in bounds

### Filter Not Working

* Verify filter name is correct
* Check filter arguments (some require arguments: `{{ value | round: 2 }}`)
* Ensure input type matches filter (can't `upcase` a number)

### Environment Variable Not Found

* Verify variable is set in environment
* Check variable name (case-sensitive)
* Edge Connector supports both `REC_` prefix and plain names

## Next Steps

* See [Action Configuration](/edge-connectors-actions) to use templates in actions
* Review [Event Examples](/edge-connectors-event-examples) for available fields
* Read the main [Edge Connectors](/edge-connectors) documentation


Built with [Mintlify](https://mintlify.com).