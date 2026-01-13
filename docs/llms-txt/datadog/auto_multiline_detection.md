# Source: https://docs.datadoghq.com/agent/logs/auto_multiline_detection.md

---
title: Automatic Multi-line Detection and Aggregation
description: Use the Datadog Agent to detect and aggregate multi-line logs automatically
breadcrumbs: >-
  Docs > Agent > Host Agent Log collection > Automatic Multi-line Detection and
  Aggregation
source_url: https://docs.datadoghq.com/logs/auto_multiline_detection/index.html
---

# Automatic Multi-line Detection and Aggregation

{% alert level="danger" %}
This feature is available for Agent version **7.65.0+** and above. For older Agent versions or to explicitly enable the legacy implementation, see [Auto Multi-line Detection and Aggregation (Legacy)](https://docs.datadoghq.com/agent/logs/auto_multiline_detection_legacy).
{% /alert %}

## Overview{% #overview %}

Automatic multi-line detection allows the Agent to detect and aggregate common multi-line logs automatically.

## Getting started{% #getting-started %}

To enable the Auto multi-line feature in your Agent configuration, set `auto_multi_line_detection` to `true` in your configuration file, or set the `DD_LOGS_CONFIG_AUTO_MULTI_LINE_DETECTION=true` environment variable:

{% tab title="Configuration file" %}

```yaml
logs_config:
  auto_multi_line_detection: true
```

{% /tab %}

{% tab title="Environment Variable" %}

```shell
DD_LOGS_CONFIG_AUTO_MULTI_LINE_DETECTION=true
```

{% /tab %}

### Default settings{% #default-settings %}

By default, the following features are enabled:

- `enable_datetime_detection`: This configures automatic datetime aggregation. Logs beginning with a datetime format are used to aggregate logs.
- `enable_json_detection`: This configures JSON detection and rejection. JSON-structured logs are never aggregated.

You can disable these features by setting the following to `false` in your configuration file or in your environment variable:

{% tab title="Configuration file" %}

```yaml
logs_config:
  auto_multi_line:
    enable_datetime_detection: false
    enable_json_detection: false
```

{% /tab %}

{% tab title="Environment Variables" %}

```shell
DD_LOGS_CONFIG_AUTO_MULTI_LINE_ENABLE_DATETIME_DETECTION=false
DD_LOGS_CONFIG_AUTO_MULTI_LINE_ENABLE_JSON_DETECTION=false
```

{% /tab %}

### Enable multi-line aggregation per integration{% #enable-multi-line-aggregation-per-integration %}

You can enable or disable multi-line aggregation for a specific integration's log collection:

```yaml
logs:
  - type: file
    path: /my/test/file.log
    service: testApp
    source: java
    auto_multi_line_detection: false
```

#### Per integration multi-line integration settings{% #per-integration-multi-line-integration-settings %}

You can set auto multi-line settings individually on each integration. The integration accepts the same settings as the normal `datadog.yaml` file:

```yaml
logs:
  - type: file
    path: /my/test/file.log
    service: testApp
    source: java
    auto_multi_line_detection: true
    auto_multi_line_detection_custom_samples:
      - sample: "ERROR [DatabaseService]"
    auto_multi_line:
        enable_json_detection: true
        enable_datetime_detection: true
        tokenizer_max_input_bytes: 50
```

### Supported datetime formats{% #supported-datetime-formats %}

Auto multi-line detection uses an algorithm to detect *any* datetime format that occurs in the first 60 bytes of a log line. To prevent false positives, the algorithm requires enough context to consider a datetime format a match.

Your datetime format must include both a *date* and *time* component to be detected.

Examples of valid formats that include enough context to be detected:

- `2021-03-28 13:45:30`
- `2023-03-28T14:33:53.743350Z`
- `Jun 14 15:16:01`
- `2024/05/16 19:46:15`

Examples of formats that do not have enough context to be detected:

- `12:30:2017`
- `12:30:20`
- `2024/05/16`

## Custom pattern configuration{% #custom-pattern-configuration %}

If datetime aggregation is insufficient or your format is too short to be detected automatically, you can customize the feature in two ways:

- Custom Samples
- Regex Patterns

### Custom samples{% #custom-samples %}

A custom sample is a sample of a log on which you want to aggregate. For example, if you want to aggregate a stack trace, the first line of the stack trace would be a good sample to provide. Custom samples are an easier way to aggregate logs than regex patterns.

To configure custom samples, you can use the `logs_config` in your `datadog.yaml` file or set an environment variable. In the following example, the multi-line detection is looking for the sample `"SEVERE Main main Exception occurred"`:

{% tab title="Configuration file" %}

```yaml
logs_config:
  auto_multi_line_detection_custom_samples:
    - sample: "SEVERE Main main Exception occurred"
```

{% /tab %}

{% tab title="Environment Variables" %}

```shell
DD_LOGS_CONFIG_AUTO_MULTI_LINE_DETECTION_CUSTOM_SAMPLES='[{"sample": "SEVERE Main main Exception occurred"}]'
```

{% /tab %}

This aggregates logs where `"SEVERE Main main Exception occurred"` matches the first line. For example:

```text
SEVERE Main main Exception occurred
java.lang.Exception: Something bad happened!
    at Main.funcd(Main.java:50)
    at Main.funcc(Main.java:49)
    at Main.funcb(Main.java:48)
    at Main.funca(Main.java:47)
    at Main.main(Main.java:29)
```

#### How custom samples work{% #how-custom-samples-work %}

Custom samples tokenize the first 60 bytes of a log line and also tokenize the provided sample. Tokens include

- words and their length
- whitespace
- numbers and their length
- special characters
- datetime components.

Each log token is compared to each token in the sample. If 75% of the log's tokens match the sample's, the log is marked for aggregation. Datadog recommends using sample-based matching if your logs have a stable format. If you need more flexible matching, you can use regex.

### Regex patterns{% #regex-patterns %}

Regex patterns work similarly to a `multi_line` rule. If the regex pattern matches the log, it is used for aggregation.

To configure custom regex patterns, you can use the `logs_config` in your `datadog.yaml` file or set an environment variable.

{% tab title="Configuration file" %}

```yaml
logs_config:
  auto_multi_line_detection_custom_samples:
    - regex: "\\[\\w+\\] Main main Exception occurred"
```

{% /tab %}

{% tab title="Environment Variables" %}

```shell
DD_LOGS_CONFIG_AUTO_MULTI_LINE_DETECTION_CUSTOM_SAMPLES='[{"regex": "\\[\\w+\\] Main main Exception occurred"}]'
```

{% /tab %}

You can mix samples and regex patterns to support multiple log formats:

{% tab title="Configuration file" %}

```yaml
logs_config:
  auto_multi_line_detection_custom_samples:
    - sample: "CORE | INFO | (pkg/logs/"
    - regex: "\\d{4}dog.\\s\\w+"
    - sample: "[ERR] Exception"
      label: no_aggregate
```

{% /tab %}

{% tab title="Environment Variables" %}

```shell
DD_LOGS_CONFIG_AUTO_MULTI_LINE_DETECTION_CUSTOM_SAMPLES='[
  {"sample": "CORE | INFO | (pkg/logs/"},
  {"regex": "\\d{4}dog.\\s\\w+"},
  {"sample": "[ERR] Exception", "label": "no_aggregate"}
]'
```

{% /tab %}

**Note**: Existing `auto_multi_line_extra_patterns` configurations are automatically supported [when migrating from V1](https://docs.datadoghq.com/agent/logs/auto_multiline_detection_legacy).

## JSON aggregation{% #json-aggregation %}

In Datadog Agent version 7.67+, pretty-printed or multi-line JSON is automatically detected and aggregated into a single line.

For example, the following log:

```
2024-08-13 17:15:17 INFO My log message 1
2024-08-13 17:15:17 INFO My log message 2
{
    "id": "565290f7-6ce0-4d3d-be7f-685905c27f04",
    "clusters": 6,
    "samples": 1301,
    "top_match": {
        "score": 1317,
        "weight": 1.108
    }
}
2024-08-13 17:15:17 INFO My log message 3
2024-08-13 17:15:17 INFO My log message 4
```

is automatically converted to:

```
2024-08-13 17:15:17 INFO My log message 1
2024-08-13 17:15:17 INFO My log message 2
{"id":"565290f7-6ce0-4d3d-be7f-685905c27f04","clusters":6,"samples": 1301,"top_match":{"score":1317,"weight":1.108}}
2024-08-13 17:15:17 INFO My log message 3
2024-08-13 17:15:17 INFO My log message 4
```

This allows Datadog to identify the JSON as a structured log and allows its attributes to be automatically queryable.

You can disable JSON aggregation with:

{% tab title="Configuration file" %}

```yaml
logs_config:
  auto_multi_line:
    enable_json_aggregation: false
```

{% /tab %}

{% tab title="Environment Variable" %}

```shell
DD_LOGS_CONFIG_AUTO_MULTI_LINE_ENABLE_JSON_AGGREGATION=false
```

{% /tab %}

## Advanced customization{% #advanced-customization %}

Auto multi-line detection uses a labeled aggregation system to aggregate logs. The detection step assigns a label to each log, and the aggregation step aggregates logs based on those labels.

### Labels{% #labels %}

{% dl %}

{% dt %}
`start_group`
{% /dt %}

{% dd %}
Defines *beginning of a multi-line log*- Flushes any buffered multi-line log, if present- Starts a new multi-line log- Only one multi-line log can be buffered at a time
{% /dd %}

{% dt %}
`aggregate`
{% /dt %}

{% dd %}
Is *added to existing multi-line log*- If no multi-line log exists, flushes immediately- Default label when nothing else matches
{% /dd %}

{% dt %}
`no_aggregate`
{% /dt %}

{% dd %}
Declares logs that are *never part of aggregation*- Flushes buffered multi-line log, if present- Flushes sample immediately- Used for JSON logs
{% /dd %}

{% /dl %}

### Label configuration{% #label-configuration %}

You can provide custom labels to each regex or sample to change the aggregation behavior based on the label rules. This is useful if you want to explicitly include or exclude certain log formats in multi-line aggregation.

{% tab title="Configuration file" %}

```yaml
logs_config:
  auto_multi_line_detection_custom_samples:
    # Never aggregate these formats
    - sample: "some service we should not aggregate"
      label: no_aggregate
    - regex: \w*\s(data|dog)
      label: no_aggregate
```

{% /tab %}

{% tab title="Environment Variables" %}

```shell
DD_LOGS_CONFIG_AUTO_MULTI_LINE_DETECTION_CUSTOM_SAMPLES='[
  {"sample": "some service we should not aggregate", "label": "no_aggregate"},
  {"regex": "\\w*\\s(data|dog)", "label": "no_aggregate"}
]'
```

{% /tab %}

## Monitoring and debugging{% #monitoring-and-debugging %}

You can search for multiline logs or truncated logs by enabling the following settings:

```yaml
logs_config:
  tag_multi_line_logs: true
  tag_truncated_logs: true
```

These settings add the following *tags* to your logs, allowing you to search for them in the Logs Explorer:

- `multiline`: Shows the aggregation source (for example, `auto_multiline`, `multiline_regex`)
- `truncated`: Shows truncation source (for example, `single_line`, `multi_line`)

**Note:** The Agent truncates logs that are too long to process. If a line is too long before multiline aggregation, the Agent assigns it the `single_line` tag. If an incorrect pattern causes a log to overflow the aggregation buffer, the Agent applies the `multi_line` tag.

You can also tag aggregated JSON logs.

```yaml
logs_config:
  auto_multi_line:
    tag_aggregated_json: true
```

You can search for this tag by querying `aggregated_json:true` in the Logs Explorer.

## Configuration reference{% #configuration-reference %}

| Setting                                                          | Type   | Default | Description                       |
| ---------------------------------------------------------------- | ------ | ------- | --------------------------------- |
| `logs_config.auto_multi_line_detection_custom_samples`           | Object | Empty   | Custom samples/regex patterns     |
| `logs_config.auto_multi_line.enable_json_detection`              | Bool   | True    | Enable JSON detection & rejection |
| `logs_config.auto_multi_line.enable_datetime_detection`          | Bool   | True    | Enable datetime detection         |
| `logs_config.auto_multi_line.timestamp_detector_match_threshold` | Float  | 0.5     | Timestamp matching threshold      |
| `logs_config.auto_multi_line.tokenizer_max_input_bytes`          | Int    | 60      | Bytes to tokenize                 |

## Further reading{% #further-reading %}

- [Advanced Log Collection](https://docs.datadoghq.com/agent/logs/advanced_log_collection)
- [Auto Multi-line Detection and Aggregation (Legacy)](https://docs.datadoghq.com/agent/logs/auto_multiline_detection_legacy)
