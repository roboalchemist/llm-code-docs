# Source: https://docs.startree.ai/corecapabilities/security/audit/pinot-audit-logs.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Pinot Audit Configuration Guide

<Info>
  Audit logging support is a new capability available in Apache Pinot. This is available in StarTree Cloud starting 0.11.1 release ([Release notes](https://docs.startree.ai/reference/startree-release-notes/0.11.1#pinot-audit-logs)) for auditing Controller Logs. Broker audit logs are supported starting StarTree Cloud version 0.12.0.
</Info>

## Overview

Apache Pinot provides a comprehensive audit logging framework that captures API requests across different components (Controller, Broker). The audit system logs structured JSON events containing request details, user information, and payload data for security monitoring and compliance purposes.

## Log Management

By default, audit logs are stored in the same bucket as the Pinot deep store under this path: `audit-logs/`. Default retention is 30 days.

## Configuration Properties

All audit configurations follow the pattern: `pinot.audit.{component}.{property}`

Where component can be:

* controller - For Pinot Controller instances
* broker - For Pinot Broker instances

The different properties available are as follows:

### 1. enabled

**Type:** Boolean\
**Default:** false\
**Description:** Master switch to enable/disable audit logging for the component.\
**Example:**

```shellscript  theme={null}
pinot.audit.controller.enabled=true
```

### 2. capture.request.payload.enabled

**Type:** Boolean\
**Default:** false\
**Description:** Enables capturing of request body payloads in audit logs. When enabled, POST/PUT request bodies will be logged (subject to size limits).\
**Example**

```shellscript  theme={null}
pinot.audit.controller.capture.request.payload.enabled=true
```

### 3. capture.request.headers

**Type:** String (comma-separated list)\
**Default:**"" (empty)\
**Description:** Comma-separated list of HTTP headers to capture in audit logs. Headers are matched case-insensitively.\
**Example**

```shellscript  theme={null}
pinot.audit.controller.capture.request.headers=Content-Type,X-Request-Id,Authorization
```

### 4. request.payload.size.max.bytes

**Type:** Integer\
\*\*Default:\*\*8192 (8KB)\
\*\*Maximum:\*\*65536 (64KB - hard limit)\
**Description:** Maximum size of request payload to capture in bytes. Payloads exceeding this limit will be truncated with a marker.\
**Example**

```shellscript  theme={null}
pinot.audit.controller.request.payload.size.max.bytes=20480
```

### 5. url.filter.exclude.patterns

**Type:** String (comma-separated list) **Default:** "" (empty) **Description:** Comma-separated list of URL patterns to exclude from audit logging. Useful for excluding health checks, metrics endpoints, etc. Exclusion patterns have priority over inclusion patterns.

**Note:**

* Since this is a comma-separated list, individual patterns cannot contain commas. Use multiple separate patterns instead of glob alternatives like api,v1.
* Patterns should NOT start with '/'. The patterns are matched against the URL path without the leading slash.

**Example**

```shellscript  theme={null}
pinot.audit.controller.url.filter.exclude.patterns=health,metrics,swagger.*
```

### 6. url.filter.include.patterns

**Type:** String (comma-separated list) **Default:** "" (empty) **Description:** Comma-separated list of URL patterns to include in audit logging. When specified, only URLs matching these patterns will be audited (unless excluded). If not specified, all URLs are audited by default (except excluded ones).

**Note:**

* Since this is a comma-separated list, individual patterns cannot contain commas. Use multiple separate patterns instead of glob alternatives like api,v1.
* Patterns should NOT start with '/'. The patterns are matched against the URL path without the leading slash.

**Pattern Priority:**

1. **Exclusion always wins**: URLs matching exclude patterns are never audited, even if they match include patterns
2. **Include acts as allowlist**: When include patterns are defined, only matching URLs are audited
3. **Default behavior**: Without include patterns, all non-excluded URLs are audited

**Example:**

```shellscript  theme={null}
# Only audit table and schema operations, but never audit health checks
pinot.audit.controller.url.filter.include.patterns=tables/**,schemas/**,segments/**
pinot.audit.controller.url.filter.exclude.patterns=health,metrics
```

### 7. userid.header

**Type:** String\
**Default:** "" (empty)\
**Description:** HTTP header name containing the user identifier. Takes precedence over JWT claim if both are configured.\
**Example**

```shellscript  theme={null}
pinot.audit.controller.userid.header=X-User-Id
```

### 8. userid.jwt.claim

**Type:** String\
**Default:** "" (empty)\
**Description:** JWT claim name to extract user identity from Authorization Bearer tokens. Used when userid.header is not found.\
**Example**

```shellscript  theme={null}
pinot.audit.controller.userid.jwt.claim=sub
```

### 9. capture.response.enabled

**Type:** Boolean\
**Default:** false\
**Description:** Enables capturing of HTTP response information in audit logs. When enabled, response status codes, request IDs, and response duration will be logged along with request details.\
**Example**

```shellscript  theme={null}
pinot.audit.controller.capture.response.enabled=true
```

## Audit Event Structure

Audit events are logged as structured JSON with the following fields:

```json  theme={null}
{
  "timestamp": "2024-01-15T10:30:45.123Z",
  "service_id": "Controller_192.168.1.10_9000",
  "endpoint": "/schemas",
  "method": "POST",
  "origin_ip_address": "10.0.0.5",
  "user_id": {
    "principal": "john.doe@example.com"
  },
  "request_id": "req-abc-123-456",
  "response_code": 201,
  "duration_ms": 1245,
  "request": {
    "query_params": {
      "override": "true"
    },
    "headers": {
      "Content-Type": "application/json",
      "X-Request-Id": "abc-123"
    },
    "body": "{\"schemaName\":\"myTable\",\"schema\":{...}}",
    "error": null
  }
}
```

## URL Pattern Syntax

Both include and exclude patterns support powerful pattern matching using glob and regex patterns:

### Glob Patterns (default)

* \* - matches any characters within a path segment
* \*\* - matches any characters across multiple path segments
* ? - matches a single character
* \[abc] - matches any character in the set
* \[a-z] - matches any character in the range
* \[!abc] - matches any character NOT in the set

**Important Note:** Patterns containing commas (like api,v1,v2) are NOT supported because the configuration uses comma-separated lists. Each pattern must be specified separately.

**Examples:**

* health - exact match for /health
* tables/\* - matches /tables/myTable but not /tables/myTable/segments
* tables/\*\* - matches /tables/myTable and /tables/myTable/segments
* schemas/\* - matches /schemas/mySchema
* segments/\*/metadata - matches /segments/mySegment/metadata

**Note:** Patterns should not start with '/' as they are matched against paths without the leading slash.

### Regex Patterns

Prefix with regex: to use regular expressions:

**Important Note:** Avoid using commas in regex patterns as they will be interpreted as list separators. Use character classes or alternation without commas instead.

**Examples:**

* regex:tables/\[a-zA-Z0-9\_]+\$ - matches table names with alphanumeric characters
* regex:^health(check)?\$ - matches only "health" or "healthcheck"
* regex:segments/.\*\\.tar\\.gz\$ - matches segment tar.gz files
* regex:tables/(realtime|offline)/.\* - matches realtime or offline table operations

## Complete Configuration Examples

### Controller with Full Audit Logging

```shellscript  theme={null}
# Enable audit logging
pinot.audit.controller.enabled=true

# Capture request payloads
pinot.audit.controller.capture.request.payload.enabled=true

# Capture response information
pinot.audit.controller.capture.response.enabled=true

# Capture specific headers
pinot.audit.controller.capture.request.headers=Content-Type,X-Request-Id,Authorization,X-Correlation-Id

# Set payload size limit to 20KB
pinot.audit.controller.request.payload.size.max.bytes=20480

# Exclude health and metrics endpoints
pinot.audit.controller.url.filter.exclude.patterns=health,metrics,swagger.*,api-docs.*

# User identification from header
pinot.audit.controller.userid.header=X-User-Email

# Fallback to JWT claim if header not found
pinot.audit.controller.userid.jwt.claim=email
```

### Broker with Security-Focused Configuration

```shellscript  theme={null}
# Enable audit logging
pinot.audit.broker.enabled=true

# Capture payloads for query auditing
pinot.audit.broker.capture.request.payload.enabled=true

# Capture response information for query performance tracking
pinot.audit.broker.capture.response.enabled=true

# Capture auth headers
pinot.audit.broker.capture.request.headers=Authorization,X-User-Id

# Limit payload to 16KB
pinot.audit.broker.request.payload.size.max.bytes=16384

# User identification from JWT
pinot.audit.broker.userid.jwt.claim=sub
```

### Controller with Include Pattern Allowlist

```shellscript  theme={null}
# Enable audit logging
pinot.audit.controller.enabled=true

# Only audit specific API endpoints (allowlist approach)
pinot.audit.controller.url.filter.include.patterns=schemas/**,tables/**,segments/**,tenants/**

# But always exclude health, status and size checks even if they match include patterns
pinot.audit.controller.url.filter.exclude.patterns=health,tables/*/size,tables/*/stats,segments/*/metadata

# Capture request details
pinot.audit.controller.capture.request.payload.enabled=true
pinot.audit.controller.capture.response.enabled=true
pinot.audit.controller.capture.request.headers=Content-Type,Authorization
```

## Audit Metrics

The audit system includes built-in metrics collection to monitor performance and health of the audit logging infrastructure. These metrics are automatically exposed through Pinot's metrics system and can be monitored via JMX or other metrics collection systems.

### Available Metrics

The audit system tracks the following metrics:

* **Audit processing time**: Duration of audit event processing
* **Audit event count**: Number of audit events processed
* **Audit errors**: Count of errors during audit processing
* **Request processing**: Time spent processing requests for audit logging

### Metrics Integration

Audit metrics are automatically integrated with:

* **Controller Metrics**: When audit is enabled on Controller instances
* **Broker Metrics**: When audit is enabled on Broker instances

No additional configuration is required - metrics are automatically collected when audit logging is enabled for any component.

## Dynamic Configuration Updates

The audit configuration supports dynamic updates through Pinot's cluster configuration mechanism. Changes to audit settings are applied without requiring service restarts.

## Log Output Configuration

Audit logs are written using SLF4J to the logger named org.apache.pinot.audit. Configure your logging framework (e.g., Log4j2) to direct these logs appropriately:

```java  theme={null}
<!-- Log4j2 example -->
<Logger name="org.apache.pinot.audit" level="INFO" additivity="false">
    <AppenderRef ref="AuditFileAppender"/>
</Logger>
```

## Best Practices

### Security Considerations

1. **Sensitive Data**: Be cautious when enabling payload capture as it may log sensitive information
2. **Header Selection**: Only capture necessary headers to minimize exposure of authentication tokens
3. **Payload Size**: Keep payload limits reasonable to prevent logging excessive data
4. **Log Storage**: Ensure audit logs are stored securely with appropriate access controls
5. **Log Rotation**: Implement proper log rotation to manage disk space

### Performance Considerations

1. **Selective Enabling**: Only enable audit logging for components that require it
2. **URL Filtering**: Exclude high-frequency endpoints like health checks and metrics
3. **Payload Capture**: Disable payload capture for high-throughput services if not required
4. **Header Filtering**: Limit captured headers to only what's necessary

### Monitoring and Alerting

1. Set up monitoring for audit log volume and errors
2. Alert on authentication failures or unauthorized access patterns
3. Regularly review audit logs for suspicious activity
4. Integrate with SIEM systems for centralized security monitoring

## Troubleshooting

### Audit Logs Not Appearing

1. Verify enabled is set to true for the component
2. Check the logging configuration for org.apache.pinot.audit logger
3. Ensure the service has reloaded configuration after changes

### Payload Truncation

If payloads are being truncated:

1. Check the request.payload.size.max.bytes setting
2. Remember the hard limit is 64KB (65536 bytes)
3. Look for ...\[truncated] marker in logs

### User Identity Not Captured

1. Verify userid.header or userid.jwt.claim is correctly configured
2. Ensure the specified header is present in requests
3. For JWT claims, verify the Authorization header contains a valid Bearer token

## Migration Notes

When migrating from older Pinot versions:

* The configuration prefix has changed from a global pinot.audit to per-component prefixes
* Update your configuration to use pinot.audit.controller or [pinot.audit.broker](http://pinot.audit.broker)
* Each component now maintains its own audit configuration independently

Built with [Mintlify](https://mintlify.com).
