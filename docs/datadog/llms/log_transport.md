# Source: https://docs.datadoghq.com/agent/logs/log_transport.md

---
title: Agent Transport for Logs
description: Use the Datadog Agent to collect your logs and send them to Datadog
breadcrumbs: Docs > Agent > Host Agent Log collection > Agent Transport for Logs
---

# Agent Transport for Logs

## Default Agent behavior{% #default-agent-behavior %}

For Agent v6.19+/v7.19+, the default transport used for your logs is compressed HTTPS instead of TCP for the previous versions. When the Agent starts, if log collection is enabled, it runs a HTTPS connectivity test. If successful, then the Agent uses the compressed HTTPS transport, otherwise the Agent falls back to a TCP transport.

This connectivity test mechanism is only running at Agent startup and only test HTTPS. If the Agent has no connectivity for both TCP and HTTP when the agent start, then the Agent will uses TCP transport when the connectivity will be back and this won't change until its next restart.

To check which transport is used by the Agent, run the [Agent status command](https://docs.datadoghq.com/agent/configuration/agent-commands/?tab=agentv6v7#service-status).

{% image
   source="https://datadog-docs.imgix.net/images/agent/logs/agent-status.9c7aa0964a78e25a4cdec814e7c52d60.png?auto=format"
   alt="Agent status" /%}

**Notes**:

- For older Agent versions, TCP transport is used by default. **Datadog strongly recommends** you to enforce HTTPS transport if you are running v6.14+/v7.14+ and HTTPS compression if you are running v6.16+/v7.16+.
- Always enforce a specific transport (either TCP or HTTPS) when using a proxy to forwards logs to Datadog

## Enforce a specific transport{% #enforce-a-specific-transport %}

Enforce the use of TCP or HTTPS transport by using the following configurations.

{% tab title="HTTPS" %}
To enforce HTTPS transport with Agent versions v6.14+/v7.14+ , update the Agent's [main configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/) (`datadog.yaml`) with:

```yaml
logs_enabled: true
logs_config:
  force_use_http: true
```

To send logs with environment variables, configure the following:

- `DD_LOGS_ENABLED=true`
- `DD_LOGS_CONFIG_USE_HTTP=true`

By default, the Datadog Agent uses the port `443` to send its logs to Datadog over HTTPS.

## HTTPS transport{% #https-transport %}

**HTTPS log forwarding is the recommended configuration** for the best log collection reliability as the`200` status code is returned by the Datadog storage system:

{% image
   source="https://datadog-docs.imgix.net/images/agent/HTTPS_intake_reliability_schema.16346defe1d60d1ac9acf2731638e1fa.png?auto=format"
   alt="HTTPS Intake Schema" /%}

Using HTTP, the Agent sends log batches with the following limits:

- Maximum batch size: 1MB
- Maximum size for a single log: 900kB
- Maximum number of logs in a batch: 1,000

### Log compression{% #log-compression %}

The `compression_level` parameter (or `DD_LOGS_CONFIG_COMPRESSION_LEVEL`) accepts values from `0` (no compression) to `9` (maximum compression but higher resource usage). The default value is `6`.

See the [Datadog Agent overhead section](https://docs.datadoghq.com/agent/basic_agent_usage/#agent-overhead) for more information about Agent resource usage when compression is enabled.

For Agent versions prior to 6.19 / 7.19, you need to enforce compression by updating the Agent's [main configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/) (`datadog.yaml`) with:

```yaml
logs_enabled: true
logs_config:
  use_http: true
  use_compression: true
  compression_level: 6
```

### Configure the batch wait time{% #configure-the-batch-wait-time %}

The Agent waits up to 5 seconds to fill each batch (either in content size or number of logs). Therefore, in the worst case scenario (when few logs are generated) switching to HTTPS might add a 5-second latency compared to the TCP transport which sends all logs in real time.

To change the maximum time the Datadog Agent waits to fill each batch, add the following configuration in the Agent's [main configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/) (`datadog.yaml`):

```yaml
logs_config:
  batch_wait: 2
```

Or use the `DD_LOGS_CONFIG_BATCH_WAIT=2` environment variable. The unit is in seconds and must be an integer between `1` and `10`.

### HTTPS proxy configuration{% #https-proxy-configuration %}

When logs are sent through HTTPS, use the same [set of proxy settings](https://docs.datadoghq.com/agent/configuration/proxy/) as the other data types to send logs through a web proxy.
{% /tab %}

{% tab title="TCP" %}

{% callout %}
# Important note for users on the following Datadog sites: app.datadoghq.com, app.datadoghq.eu, us3.datadoghq.com, us5.datadoghq.com, ap1.datadoghq.com, ap2.datadoghq.com

{% alert level="warning" %}
TCP log collection is **not supported**. Datadog provides **no delivery or reliability guarantees** when using TCP, and log data may be lost without notice. For reliable ingestion, use the HTTP intake endpoint, an official Datadog Agent, or forwarder integration instead. For more information, see [Log Collection](https://docs.datadoghq.com/logs/log_collection/?tab=host).
{% /alert %}

To enforce TCP transport, update the Agent's [main configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/) (`datadog.yaml`) with:

```yaml
logs_enabled: true
logs_config:
  force_use_tcp: true
```

To send logs with environment variables, configure the following:

- `DD_LOGS_ENABLED=true`
- `DD_LOGS_CONFIG_FORCE_USE_TCP=true`

By default, the Datadog Agent sends its logs to Datadog over TLS-encrypted TCP. This requires outbound communication (on port `10516` for Datadog US site and port `443`for Datadog EU site).
{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

The TCP endpoint is not supported for this site.
{% /callout %}

{% /tab %}

**Note**: Setting up a [SOCKS5 proxy](https://docs.datadoghq.com/agent/logs/proxy/?tab=socks5) server enforces TCP transport because socks5 proxies are not yet supported in HTTPS with compression.
