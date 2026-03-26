# Source: https://docs.infrahub.app/sync/adapters/prometheus.md

# Prometheus adapter

## What is Prometheus?[​](#what-is-prometheus "Direct link to What is Prometheus?")

Prometheus is an open-source monitoring and alerting toolkit that collects and stores metrics as time series data. It is widely used for monitoring infrastructure, applications, and services through its pull-based model and powerful query language (PromQL).

## Requirements[​](#requirements "Direct link to Requirements")

This adapter uses the [prometheus-client](https://pypi.org/project/prometheus-client) library for parsing the Prometheus exposition format.

## Sync directions supported[​](#sync-directions-supported "Direct link to Sync directions supported")

* Prometheus → Infrahub

note

Currently, the Prometheus adapter supports only **one-way synchronization** from Prometheus to Infrahub. Writing data back to Prometheus is not supported as Prometheus is a read-only metrics store.

## Operating modes[​](#operating-modes "Direct link to Operating modes")

The Prometheus adapter supports two modes of operation:

### Scrape mode (default)[​](#scrape-mode-default "Direct link to Scrape mode (default)")

Directly scrapes a Prometheus text exposition endpoint (for example, from `node_exporter`, application metrics endpoints). Best for collecting metrics from individual exporters.

### API mode[​](#api-mode "Direct link to API mode")

Queries the Prometheus HTTP API using PromQL. Best for aggregating data from multiple targets or performing complex queries with joins.

## Configuration[​](#configuration "Direct link to Configuration")

### Scrape mode configuration[​](#scrape-mode-configuration "Direct link to Scrape mode configuration")

* Scrape Mode
* API Mode

```
---
name: from-node-exporter
source:
  name: prometheus
  settings:
    mode: scrape
    url: "http://localhost:9100"
    endpoint: "/metrics"
    timeout: 10           # Optional, seconds
    verify_ssl: true      # Optional

destination:
  name: infrahub
  settings:
    url: "http://localhost:8000"
```

```
---
name: from-prometheus-api
source:
  name: prometheus
  settings:
    mode: api
    url: "http://prometheus:9090"
    endpoint: "/api/v1/query"
    promql:
      resources:
        node_info: 'node_uname_info'
        node_memory: 'node_memory_MemTotal_bytes'
        node_cpu: 'count(node_cpu_seconds_total{mode="idle"}) by (instance)'

destination:
  name: infrahub
  settings:
    url: "http://localhost:8000"
```

### Environment variables[​](#environment-variables "Direct link to Environment variables")

| Variable                     | Description                                      |
| ---------------------------- | ------------------------------------------------ |
| `PROM_URL` or `PROM_ADDRESS` | Prometheus server URL (overrides `settings.url`) |
| `PROM_TOKEN`                 | Bearer token for authentication                  |
| `PROM_USERNAME`              | Username for basic authentication                |
| `PROM_PASSWORD`              | Password for basic authentication                |

### Settings reference[​](#settings-reference "Direct link to Settings reference")

| Setting            | Type    | Required | Default                                      | Description                                            |
| ------------------ | ------- | -------- | -------------------------------------------- | ------------------------------------------------------ |
| `mode`             | string  | No       | `scrape`                                     | Operating mode: `scrape` or `api`                      |
| `url`              | string  | Yes      | -                                            | Prometheus server or exporter URL                      |
| `endpoint`         | string  | No       | `/metrics` (scrape) or `/api/v1/query` (API) | Target endpoint                                        |
| `timeout`          | number  | No       | 10                                           | Request timeout in seconds                             |
| `verify_ssl`       | boolean | No       | true                                         | Verify SSL certificates                                |
| `auth_method`      | string  | No       | `none`                                       | Authentication: `none`, `basic`, or `bearer`           |
| `username`         | string  | No       | -                                            | Username for basic auth                                |
| `password`         | string  | No       | -                                            | Password for basic auth                                |
| `token`            | string  | No       | -                                            | Token for bearer auth                                  |
| `headers`          | object  | No       | -                                            | Additional HTTP headers                                |
| `params`           | object  | No       | -                                            | Query parameters for scrape mode                       |
| `promql.resources` | object  | No       | -                                            | PromQL queries for API mode (`resource_name`: `query`) |

## Schema mapping[​](#schema-mapping "Direct link to Schema mapping")

The Prometheus adapter normalizes metrics into a consistent format for schema mapping:

```
# Each metric sample contains:
# - __metric__: metric name
# - labels: { label_key: label_value, ... }
# - value: numeric value
# - timestamp: optional timestamp
# - help: metric help text
# - type: metric type (counter, gauge, etc.)
```

### Basic field mapping[​](#basic-field-mapping "Direct link to Basic field mapping")

Map fields using dot notation to access metric properties:

```
schema_mapping:
  - name: VirtualizationVirtualMachine
    mapping: node_uname_info          # Metric name to load from
    identifiers: ["name"]
    fields:
      - name: name
        mapping: labels.nodename      # Access label value
      - name: os_name
        mapping: labels.sysname
      - name: os_kernel
        mapping: labels.release
```

### Using the lookup function[​](#using-the-lookup-function "Direct link to Using the lookup function")

The `lookup()` function allows you to join data from different metrics:

```
transforms:
  # Syntax: lookup(metric_name, match_criteria, value_path [, default])

  # Get total memory from a different metric
  - field: mem_total_bytes
    expression: "{{ lookup('node_memory_MemTotal_bytes', {}, 'value') or 0 }}"

  # Match by label value
  - field: mac_address
    expression: "{{ lookup('node_network_info', {'device': labels.device}, 'labels.address') or '' }}"

  # With default value
  - field: status
    expression: "{{ lookup('node_time_seconds', {}, 'value', 0) }}"
```

### Lookup function parameters[​](#lookup-function-parameters "Direct link to Lookup function parameters")

| Parameter        | Description                                                            |
| ---------------- | ---------------------------------------------------------------------- |
| `metric_name`    | Name of the metric to look up                                          |
| `match_criteria` | Dict of label conditions to match (empty `{}` matches first record)    |
| `value_path`     | Dot-notation path to extract (for example: `value`, `labels.hostname`) |
| `default`        | Optional default value if lookup fails                                 |

## Example: Node Exporter to Infrahub[​](#example-node-exporter-to-infrahub "Direct link to Example: Node Exporter to Infrahub")

[Node Exporter Examplehttps://github.com/opsmill/infrahub-sync/tree/main/examples/prometheus\_to\_infrahub%20(node\_exporter)](https://github.com/opsmill/infrahub-sync/tree/main/examples/prometheus_to_infrahub%20\(node_exporter\))

This example syncs `node_exporter` metrics to create virtual machine records in Infrahub:

```
schema_mapping:
  - name: VirtualizationVirtualMachine
    mapping: node_uname_info
    identifiers: ["name"]
    fields:
      - name: name
        mapping: labels.nodename
      - name: os_name
        mapping: labels.sysname
      - name: mem_total_bytes
        mapping: mem_total_t
      - name: status
        mapping: status_t

    transforms:
      # Join memory info from separate metric
      - field: mem_total_t
        expression: "{{ lookup('node_memory_MemTotal_bytes', {}, 'value') or 0 }}"

      # Derive status from exporter availability
      - field: status_t
        expression: "{{ 'active' if ((lookup('node_time_seconds', {}, 'value') | float) > 0) else 'unknown' }}"

  - name: VirtualizationVMNetworkInterface
    mapping: node_network_mtu_bytes
    identifiers: ["virtual_machine", "name"]
    fields:
      - name: virtual_machine
        mapping: vm_name
      - name: name
        mapping: labels.device
      - name: mtu
        mapping: value

    transforms:
      # Link to parent VM
      - field: vm_name
        expression: "{{ lookup('node_uname_info', {}, 'labels.nodename') or 'unknown' }}"
```

## Generating the models[​](#generating-the-models "Direct link to Generating the models")

Use the generate command to produce Python models from your configuration:

```
poetry run infrahub-sync generate --name from-node-exporter --directory examples/
```

## Common issues and troubleshooting[​](#common-issues-and-troubleshooting "Direct link to Common issues and troubleshooting")

### Connection errors[​](#connection-errors "Direct link to Connection errors")

* Verify the exporter or Prometheus server is running and accessible
* Check firewall rules allow connections to the metrics endpoint
* For scrape mode, ensure the endpoint returns Prometheus text format

### Empty results[​](#empty-results "Direct link to Empty results")

* In scrape mode, verify the `/metrics` endpoint returns data
* In API mode, test your PromQL queries directly in Prometheus UI first
* Check that `schema_mapping.mapping` matches actual metric names

### Lookup failures[​](#lookup-failures "Direct link to Lookup failures")

* Ensure the metric being looked up exists in the scraped data
* Verify label names match exactly (case-sensitive)
* Use empty dict `{}` for `match_criteria` to get the first matching record
* Provide default values for optional lookup operations

### Authentication issues[​](#authentication-issues "Direct link to Authentication issues")

* For basic auth, set both `username` and `password`
* For bearer auth, set `auth_method: bearer` and provide `token`
* Use environment variables (`PROM_USERNAME`, `PROM_PASSWORD`, `PROM_TOKEN`) for credentials

### API mode specific[​](#api-mode-specific "Direct link to API mode specific")

* Ensure `promql.resources` is a dict mapping resource names to PromQL queries
* Verify queries return vector or scalar results (other types not supported)
* Test queries in Prometheus UI before using in configuration
