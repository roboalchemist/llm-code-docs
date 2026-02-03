# Source: https://docs.datadoghq.com/agent/logs/proxy.md

# Source: https://docs.datadoghq.com/agent/configuration/proxy.md

---
title: Datadog Agent Proxy Configuration
description: >-
  Configure the Datadog Agent to send traffic through HTTP/HTTPS proxies with
  authentication and bypass options.
breadcrumbs: Docs > Agent > Agent Configuration > Datadog Agent Proxy Configuration
---

# Datadog Agent Proxy Configuration

You can configure the Datadog Agent to send traffic through an HTTP/HTTPS proxy. A proxy is typically used to send traffic from a host that is not directly connected to the public internet.

## Configure the Datadog Agent{% #configure-the-datadog-agent %}

There are two options for configuring the Datadog Agent to use a proxy.

- You can use the Agent configuration file.
- You can use environment variables. Environment variables override configuration file settings.

### Configuration file{% #configuration-file %}

To configure a proxy using a configuration file, edit or add the `proxy` section to the main Agent configuration file (`datadog.yaml`) and then [restart the Datadog Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/#restart-the-agent).

```yaml
proxy:
  # Required: Proxy endpoint for HTTP connections
  http: http://<USER>:<PASSWORD>@<PROXY_HOST>:<PROXY_PORT>
  # Required: Proxy endpoint for HTTPS connections (most Datadog traffic)
  https: http://<USER>:<PASSWORD>@<PROXY_HOST>:<PROXY_PORT>

  # Optional: List of hosts or CIDR ranges to bypass the proxy
  # Example:
  # no_proxy:
  #   - 192.168.0.0/24
  #   - localhost
  #   - .myinternaldomain.com
  no_proxy:
    - <HOST_TO_BYPASS_1>
    - <HOST_TO_BYPASS_2>

# Recommended: Set to true to ensure no_proxy behaves in a standard way
no_proxy_nonexact_match: true

# Recommended: Force the Agent to use HTTP to send logs (if logs is enabled)
logs_config:
  force_use_http: true
```

- Replace `<USER>`, `<PASSWORD>`, `<PROXY_HOST>`, and `<PROXY_PORT>` with your proxy credentials and address.
- A username and password are optional.
- Specify `http`, `https`, or both, depending on your proxy setup and needs. Most Datadog traffic uses HTTPS.
- Use `no_proxy` to specify hosts the Agent should connect to directly, bypassing the proxy.
- **[Restart the Datadog Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/#restart-the-agent)** for changes to take effect.

For more information on locating the configuration file on your operating system, see [Agent Configuration Files](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/#main-configuration-file).

### Environment variables{% #environment-variables %}

Alternatively, you can configure a proxy by setting the following environment variables. When you're done, [restart the Datadog Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/#restart-the-agent).

```bash
DD_PROXY_HTTP="http://<USER>:<PASSWORD>@<PROXY_HOST>:<PROXY_PORT>"
DD_PROXY_HTTPS="http://<USER>:<PASSWORD>@<PROXY_HOST>:<PROXY_PORT>"

DD_PROXY_NO_PROXY="<HOST_TO_BYPASS_1> <HOST_TO_BYPASS_2>"
DD_NO_PROXY_NONEXACT_MATCH=true

DD_LOGS_CONFIG_FORCE_USE_HTTP=true
```

## Proxy Server Setup Examples{% #proxy-server-setup-examples %}

If you don't have an existing proxy server, Datadog recommends using an HTTP proxy like **Squid**.

1. **Squid (Recommended)**: A robust HTTP/HTTPS proxy that simplifies configuration by transparently proxying all outbound HTTP/HTTPS Agent traffic. [Using a Squid proxy](https://docs.datadoghq.com/agent/configuration/proxy_squid/).
1. **HAProxy (Not Recommended)**: Can forward traffic to Datadog, but this requires maintaining an up-to-date list of Datadog domains and is more complex to manage. [See HAProxy Example Setup](https://docs.datadoghq.com/agent/faq/proxy_example_haproxy/).
1. **NGINX (Not Recommended)**: Similar to HAProxy, using NGINX to forward traffic to Datadog is discouraged due to the maintenance overhead of keeping domain lists current. [See NGINX Example Setup](https://docs.datadoghq.com/agent/faq/proxy_example_nginx/).

Datadog discourages forwarding traffic using software like HAProxy or NGINX because it requires you to manually configure and maintain the list of specific Datadog endpoints the Agent needs to reach. This list can change, leading to potential data loss if not kept up-to-date. The only exception is if you need Deep Packet Inspection (DPI) capabilities, in which case you might consider using HAProxy or NGINX as they allow you to disable TLS or use your own TLS certificates and inspect the traffic.

## Verification{% #verification %}

Check the Agent status command and review the Agent logs (`agent.log`, `trace-agent.log`, etc.) for any connection errors after restarting.

## FIPS Proxy (US1-FED){% #fips-proxy-us1-fed %}

For information on setting up the Datadog Agent FIPS Proxy with the Datadog Agent, see [Datadog FIPS Compliance](https://docs.datadoghq.com/agent/configuration/fips-compliance/). The FIPS proxy is only available in the US1-FED region. The Datadog Agent FIPS Proxy cannot be used together with a regular proxy.

## Further reading{% #further-reading %}

- [Collect your logs](https://docs.datadoghq.com/logs/)
- [Collect your processes](https://docs.datadoghq.com/infrastructure/process/)
- [Collect your traces and profiles](https://docs.datadoghq.com/tracing/)
- [Datadog FIPS Compliance](https://docs.datadoghq.com/agent/configuration/fips-compliance)
