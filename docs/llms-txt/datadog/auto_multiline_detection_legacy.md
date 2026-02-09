# Source: https://docs.datadoghq.com/agent/logs/auto_multiline_detection_legacy.md

---
title: (Legacy) Automatic Multi-line Detection and Aggregation
description: >-
  (Legacy) Use the Datadog Agent to detect and aggregate multi-line logs
  automatically
breadcrumbs: >-
  Docs > Agent > Host Agent Log collection > (Legacy) Automatic Multi-line
  Detection and Aggregation
---

# (Legacy) Automatic Multi-line Detection and Aggregation

{% alert level="danger" %}
This document applies to Agent versions earlier than **v7.65.0**, or when the legacy auto multi-line detection is explicitly enabled. For newer Agent versions, please see [Auto Multi-line Detection and Aggregation](https://docs.datadoghq.com/agent/logs/auto_multiline_detection).
{% /alert %}

## Global automatic multi-line aggregation{% #global-automatic-multi-line-aggregation %}

With Agent 7.37+, you can enable `auto_multi_line_detection` to automatically detect [common multi-line patterns](https://github.com/DataDog/datadog-agent/blob/a27c16c05da0cf7b09d5a5075ca568fdae1b4ee0/pkg/logs/internal/decoder/auto_multiline_handler.go#L187) across **all** configured log integrations.

{% tab title="Configuration file" %}
Enable `auto_multi_line_detection` globally in the `datadog.yaml` file:

```yaml
logs_config:
  auto_multi_line_detection: true
```

{% /tab %}

{% tab title="Docker" %}
Use the environment variable `DD_LOGS_CONFIG_AUTO_MULTI_LINE_DETECTION` in the Datadog Agent container to configure a global automatic multi-line aggregation rule. For example:

```shell
DD_LOGS_CONFIG_AUTO_MULTI_LINE_DETECTION=true
```

{% /tab %}

{% tab title="Kubernetes" %}
#### Operator{% #operator %}

Use the `spec.override.nodeAgent.env` parameter in your Datadog Operator manifest to set the `DD_LOGS_CONFIG_AUTO_MULTI_LINE_DETECTION` environment variable to configure a global automatic multi-line aggregation rule. For example:

```yaml
spec:
  override:
    nodeAgent:
      env:
        - name: DD_LOGS_CONFIG_AUTO_MULTI_LINE_DETECTION
          value: "true"
```

#### Helm{% #helm %}

Use the `datadog.logs.autoMultiLineDetection` option in the Helm chart to configure a global automatic multi-line aggregation rule. For example:

```yaml
datadog:
  logs:
    enabled: true
    autoMultiLineDetection: true
```

{% /tab %}

{% alert level="info" %}
In Agent versions 7.65+, you can opt into the legacy behavior by setting to **true** the following:**- logs\_config.force\_auto\_multi\_line\_detection\_v1** in your datadog.yaml fileOR**- LOGS\_CONFIG\_FORCE\_AUTO\_MULTI\_LINE\_DETECTION\_V1** in your environment variable.
{% /alert %}

## Enable multi-line aggregation per integration{% #enable-multi-line-aggregation-per-integration %}

Alternatively, you can enable or disable multi-line aggregation for an individual integration's log collection. Changing the multi-line aggregation for an integration overrides the global configuration.

{% tab title="Configuration file" %}
In a host environment, enable `auto_multi_line_detection` with the [Custom log collection](https://docs.datadoghq.com/agent/logs/?tab=tailfiles#custom-log-collection) method. For example:

```yaml
logs:
  - type: file
    path: /my/test/file.log
    service: testApp
    source: java
    auto_multi_line_detection: true
```

{% /tab %}

{% tab title="Docker" %}
In a Docker environment, use the label `com.datadoghq.ad.logs` on your container to specify the log configuration. For example:

```yaml
 labels:
    com.datadoghq.ad.logs: >-
      [{
        "source": "java",
        "service": "testApp",
        "auto_multi_line_detection": true
      }]
```

{% /tab %}

{% tab title="Kubernetes" %}
In a Kubernetes environment, use the annotation `ad.datadoghq.com/<CONTAINER_NAME>.logs` on your pod to specify the log configuration. For example:

```yaml
apiVersion: apps/v1
metadata:
  name: testApp
spec:
  selector:
    matchLabels:
      app: testApp
  template:
    metadata:
      annotations:
        ad.datadoghq.com/<CONTAINER_NAME>.logs: >-
          [{
            "source": "java",
            "service": "testApp",
            "auto_multi_line_detection": true
          }]
      labels:
        app: testApp
      name: testApp
    spec:
      containers:
        - name: '<CONTAINER_NAME>'
          image: testApp:latest
```

{% /tab %}

## Customize multi-line aggregation configuration{% #customize-multi-line-aggregation-configuration %}

Automatic multi-line detection uses a list of [common regular expressions](https://github.com/DataDog/datadog-agent/blob/a27c16c05da0cf7b09d5a5075ca568fdae1b4ee0/pkg/logs/internal/decoder/auto_multiline_handler.go#L187) to match logs. If the built-in list is not sufficient, you can also add custom patterns and thresholds for detection.

### Custom Patterns{% #custom-patterns %}

{% tab title="Configuration file" %}
In a configuration file, add the `auto_multi_line_extra_patterns` to your `datadog.yaml`:

```yaml
logs_config:
  auto_multi_line_detection: true
  auto_multi_line_extra_patterns:
   - \d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])
   - '[A-Za-z_]+ \d+, \d+ \d+:\d+:\d+ (AM|PM)'
```

### Custom threshold{% #custom-threshold %}

The `auto_multi_line_default_match_threshold` parameter determines how closely logs have to match the patterns in order for the auto multi-line aggregation to work.

If your multi-line logs aren't getting aggregated as expected, you can change the sensitivity of the matching by setting the `auto_multi_line_default_match_threshold` parameter. Add the `auto_multi_line_default_match_threshold` parameter to your configuration file with a value lower (to increase matches) or higher (to decrease matches) than the current threshold value.

Restart the Datadog Agent to apply the new threshold value for newly ingested logs. To find the current threshold value, run the [Agent `status` command](https://docs.datadoghq.com/agent/configuration/agent-commands/#agent-information).

```yaml
logs_config:
  auto_multi_line_detection: true
  auto_multi_line_extra_patterns:
   - \d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])
   - '[A-Za-z_]+ \d+, \d+ \d+:\d+:\d+ (AM|PM)'
  auto_multi_line_default_match_threshold: 0.1
```

{% /tab %}

{% tab title="Docker" %}
In a containerized Agent, add the environment variable `DD_LOGS_CONFIG_AUTO_MULTI_LINE_EXTRA_PATTERNS`:

```yaml
    environment:
      - DD_LOGS_CONFIG_AUTO_MULTI_LINE_DETECTION=true
      - DD_LOGS_CONFIG_AUTO_MULTI_LINE_EXTRA_PATTERNS=\d{4}-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]) [A-Za-z_]+\s\d+,\s\d+\s\d+:\d+:\d+\s(AM|PM)
```

**Note**: The Datadog Agent interprets spaces in the `DD_LOGS_CONFIG_AUTO_MULTI_LINE_EXTRA_PATTERNS` environment variable as separators between multiple patterns. In the following example, the two regex patterns are divided by a space, and `\s` in the second regex pattern matches spaces.

### Custom threshold{% #custom-threshold %}

The `auto_multi_line_default_match_threshold` parameter determines how closely logs have to match the patterns in order for the auto multi-line aggregation to work.

If your multi-line logs are not getting aggregated as expected, you can change the sensitivity of the matching by setting the `auto_multi_line_default_match_threshold` parameter.

Add the `auto_multi_line_default_match_threshold` parameter to your configuration file with a value lower (to increase matches) or higher (to decrease matches) than the current threshold value.

To find the current threshold value, run the [Agent `status` command](https://docs.datadoghq.com/agent/configuration/agent-commands/#agent-information]).

```yaml
    environment:
      - DD_LOGS_CONFIG_AUTO_MULTI_LINE_DETECTION=true
      - DD_LOGS_CONFIG_AUTO_MULTI_LINE_EXTRA_PATTERNS=\d{4}-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]) [A-Za-z_]+\s\d+,\s\d+\s\d+:\d+:\d+\s(AM|PM)
      - DD_LOGS_CONFIG_AUTO_MULTI_LINE_DEFAULT_MATCH_THRESHOLD=0.1
```

{% /tab %}

{% tab title="Kubernetes" %}
In Kubernetes, add the environment variable `DD_LOGS_CONFIG_AUTO_MULTI_LINE_EXTRA_PATTERNS`:

#### Operator{% #operator %}

```yaml
spec:
  override:
    nodeAgent:
      env:
        - name: DD_LOGS_CONFIG_AUTO_MULTI_LINE_EXTRA_PATTERNS
          value: \d{4}-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]) [A-Za-z_]+\s\d+,\s\d+\s\d+:\d+:\d+\s(AM|PM)
```

#### Helm{% #helm %}

```yaml
datadog:
  env:
    - name: DD_LOGS_CONFIG_AUTO_MULTI_LINE_EXTRA_PATTERNS
      value: \d{4}-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]) [A-Za-z_]+\s\d+,\s\d+\s\d+:\d+:\d+\s(AM|PM)
```

**Note**: The Datadog Agent interprets spaces in the `DD_LOGS_CONFIG_AUTO_MULTI_LINE_EXTRA_PATTERNS` environment variable as separators between multiple patterns. In the following example, the two regex patterns are divided by a space, and `\s` in the second regex pattern matches spaces.

### Custom threshold{% #custom-threshold %}

The `auto_multi_line_default_match_threshold` parameter determines how closely logs have to match the patterns in order for the auto multi-line aggregation to work.

If your multi-line logs aren't getting aggregated as expected, you can change the sensitivity of the matching by setting the `auto_multi_line_default_match_threshold` parameter. Add the `auto_multi_line_default_match_threshold` parameter to your configuration file with a value lower (to increase matches) or higher (to decrease matches) than the current threshold value. To find the current threshold value, run the [Agent `status` command](https://docs.datadoghq.com/agent/configuration/agent-commands/#agent-information).

#### Operator{% #operator-1 %}

```yaml
spec:
  override:
    nodeAgent:
      env:
        - name: DD_LOGS_CONFIG_AUTO_MULTI_LINE_EXTRA_PATTERNS
          value: \d{4}-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]) [A-Za-z_]+\s\d+,\s\d+\s\d+:\d+:\d+\s(AM|PM)
        - name: DD_LOGS_CONFIG_AUTO_MULTI_LINE_DEFAULT_MATCH_THRESHOLD
          value: "0.1"
```

#### Helm{% #helm-1 %}

```yaml
datadog:
  env:
    - name: DD_LOGS_CONFIG_AUTO_MULTI_LINE_EXTRA_PATTERNS
      value: \d{4}-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]) [A-Za-z_]+\s\d+,\s\d+\s\d+:\d+:\d+\s(AM|PM)
    - name: DD_LOGS_CONFIG_AUTO_MULTI_LINE_DEFAULT_MATCH_THRESHOLD
      value: "0.1"
```

{% /tab %}

## Detection process{% #detection-process %}

Automatic multi-line detection detects logs that begin and comply with the following date/time formats:

- ANSIC
- RFC822
- RFC822Z
- RFC850
- RFC1123
- RFC1123Z
- RFC3339
- RFC3339Nano
- Ruby Date Format
- Unix Date Format
- Default Java logging SimpleFormatter date format

With multi-line aggregation enabled, the Agent first tries to detect a pattern in each new log file. This detection process takes at most 30 seconds or the first 500 logs, whichever comes first. During the initial detection process, the logs are sent as single lines.

After the detection threshold is met, all future logs for that source are aggregated with the best matching pattern, or as single lines if no pattern is found.

**Note**: If you can control the naming pattern of the rotated log, ensure that the rotated file replaces the previously active file with the same name. The Agent reuses a previously detected pattern on the newly rotated file to avoid re-running detection.

## Further reading{% #further-reading %}

- [Getting started with Logging without Limitsâ¢](https://docs.datadoghq.com/logs/guide/getting-started-lwl/)
- [Use the Datadog Agent for log collection only](https://docs.datadoghq.com/logs/guide/how-to-set-up-only-logs/)
- [Discover how to process your logs](https://docs.datadoghq.com/logs/log_configuration/processors)
- [Learn more about parsing](https://docs.datadoghq.com/logs/log_configuration/parsing)
- [Datadog live tail functionality](https://docs.datadoghq.com/logs/live_tail/)
- [See how to explore your logs](https://docs.datadoghq.com/logs/explorer/)
- [Glossary entry for "tail"](https://docs.datadoghq.com/glossary/#tail)
