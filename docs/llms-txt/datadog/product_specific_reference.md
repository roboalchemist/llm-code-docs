# Source: https://docs.datadoghq.com/getting_started/search/product_specific_reference.md

---
title: Product-Specific Search
description: Learn about search capabilities across different Datadog products
breadcrumbs: >-
  Docs > Getting Started > Getting Started with Search in Datadog >
  Product-Specific Search
---

# Product-Specific Search

## Overview{% #overview %}

Each Datadog product offers unique search capabilities optimized for its use case. This page provides a comprehensive index of product-specific search syntax resources to help you find the right documentation for your needs.

## Search syntax families{% #search-syntax-families %}

There are two main families of search syntaxes across Datadog products:

**Metrics-based syntax**: Used by Metrics and Cloud Cost Management for time-series data queries with tag-based filtering and aggregation.

**Event-based syntax**: Used by Log Management and adopted by most other Datadog products including traces, RUM, CI/CD, Observability Pipelines, and more. This syntax provides flexible faceted search with boolean operators and pattern matching.

## Metrics{% #metrics %}

Metrics use a specialized metrics-based syntax for filtering and aggregating time-series data.

For more information, see [Advanced Filtering](https://docs.datadoghq.com/metrics/advanced-filtering).

### Key capabilities{% #key-capabilities %}

- Tag-based filtering with boolean logic (`AND`, `OR`, `NOT`) or symbolic operators (`&&`, `||`, `!`)
- Wildcard matching on metric names and tag values
- Aggregation by multiple tag dimensions
- Template variable filtering for dynamic dashboards
- Metric namespace filtering for organized queries
- **Case-sensitive matching** for metric names

{% collapsible-section %}
##### Syntax examples

```text
# Filter metrics by tag
system.cpu.idle{host:prod-*}

# Boolean operators for tag filtering
avg:system.cpu.user{env:staging AND (availability-zone:us-east-1a OR availability-zone:us-east-1c)} by {availability-zone}

# Combine multiple tag filters
system.disk.used{env:production,datacenter:us-east-1}

# Wildcard filtered query
avg:system.disk.in_use{!device:/dev/loop*} by {device}

# Wildcard matching on tags
aws.ec2.cpuutilization{instance-type:t3.*}

# Exclude specific tags
system.mem.used{env:production AND NOT service:test}
```

{% /collapsible-section %}

## Logs{% #logs %}

Log Management uses event-based search syntax, serving as the foundation for many other products' search capabilities.

For a complete reference for log search operators, wildcards, facets, and advanced queries, see [Log Search Syntax](https://docs.datadoghq.com/logs/explorer/search_syntax).

### Key capabilities{% #key-capabilities-1 %}

- Full-text search across log messages with wildcards and phrase matching
- Structured faceted search on attributes (tags, custom fields, standard attributes)
- Pattern detection and extraction using parsing patterns
- Advanced boolean operators (AND, OR, NOT) and grouping
- Range queries for numerical values and timestamps

{% collapsible-section %}
##### Syntax examples

```text
# Search for error messages containing "timeout"
status:error "timeout"

# Query HTTP errors with status codes 500-599
@http.status_code:[500 TO 599]

# Combine multiple conditions
service:web-api env:(production OR dev) AND @duration:>1000

# Wildcard search for specific services
service:payment-* AND status:error

# Exclude specific values
env:production NOT service:background-worker
```

{% /collapsible-section %}

## Traces{% #traces %}

APM and Distributed Tracing use event-based search syntax for querying spans and traces.

To learn more about querying spans and traces with service, resource, and tag filters, see [Trace Query Syntax](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax).

### Key capabilities{% #key-capabilities-2 %}

- Query spans by service, operation, and resource name
- Filter by trace-level and span-level tags
- Search across distributed traces spanning multiple services
- Duration-based queries for performance analysis
- Error tracking with status codes and error messages

{% collapsible-section %}
##### Syntax examples

```text
# Find errors in a specific service
service:payment-api status:error

# Query by resource and HTTP method
resource_name:"/api/v1/checkout" @http.method:POST

# Search for slow traces
service:web-api* @duration:>1s

# Trace queries across service dependencies
@span.parent.service:frontend service:backend

# Filter by custom span tags
service:database @db.statement:"SELECT *" @db.row_count:>1000
```

{% /collapsible-section %}

## Additional product-specific resources{% #additional-product-specific-resources %}

- [CI Visibility Explorer: Query pipelines, tests, and CI/CD events](https://docs.datadoghq.com/continuous_integration/explorer/search_syntax)
- [CD Visibility Explorer: Search and filter deployment events and executions](https://docs.datadoghq.com/continuous_delivery/explorer/search_syntax)
- [Monitor Search: Find and filter monitors by status, type, tags, and alert conditions](https://docs.datadoghq.com/monitors/manage/search)
- [Observability Pipelines Filter Processor: Query syntax for filtering pipeline data](https://docs.datadoghq.com/observability_pipelines/processors/filter)
- [Product Analytics Explorer Search: Search user interactions and product analytics events](https://docs.datadoghq.com/product_analytics/analytics_explorer/search_syntax)
- [Quality Gates Explorer Syntax: Query quality gate rules and evaluation results](https://docs.datadoghq.com/quality_gates/explorer/search_syntax)
- [RUM Explorer Search: Search user sessions, views, actions, and errors](https://docs.datadoghq.com/real_user_monitoring/explorer/search_syntax)
- [Sensitive Data Scanner Custom Rules: Regex patterns and matching syntax for scanning sensitive data](https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules/custom_rules)
- [Service Management Events Search: Query and filter service management events](https://docs.datadoghq.com/events/explorer/searching)
- [SQL Reference for Logs: SQL syntax for advanced log analysis in Workspaces](https://docs.datadoghq.com/logs/workspaces/sql_reference)
- [Test Optimization Explorer Search Syntax: Search and analyze test execution data](https://docs.datadoghq.com/tests/explorer/search_syntax)
- [Observability Pipelines Search Syntax: Filter logs for your processors](https://docs.datadoghq.com/observability_pipelines/search_syntax/logs)

## Further reading{% #further-reading %}

- [Getting Started with Search](https://docs.datadoghq.com/getting_started/search/)
