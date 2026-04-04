# Source: https://docs.datadoghq.com/security/application_security/setup/compatibility/haproxy.md

# Source: https://docs.datadoghq.com/security/application_security/setup/haproxy.md

---
title: Enabling App and API Protection for HAProxy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > App and API Protection > Enabling App and API
  Protection > Enabling App and API Protection for HAProxy
---

# Enabling App and API Protection for HAProxy

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### App and API Protection for HAProxy is in Preview

To try the preview of App and API Protection for HAProxy, use the following setup instructions.
{% /callout %}

You can enable App and API Protection for your HAProxy instances. The Datadog HAProxy integration leverages HAProxy's Stream Processing Offload Engine (SPOE) to inspect and protect traffic for threat detection at the edge of your infrastructure.

## Prerequisites{% #prerequisites %}

- The [Datadog Agent](https://app.datadoghq.com/account/settings#agent) is installed and configured for your environment (host, container, or orchestrator).
- [Configure the Agent with Remote Configuration](https://docs.datadoghq.com/remote_configuration/) in the Datadog UI to block attackers.

## Enabling threat detection{% #enabling-threat-detection %}

### Get started{% #get-started %}

The App and API Protection HAProxy integration uses HAProxy's [Stream Processing Offload Engine](https://www.haproxy.com/blog/extending-haproxy-with-the-stream-processing-offload-engine) (SPOE) to call a Datadog Stream Processing Offload Agent (SPOA). The SPOA analyzes requests and responses.

To enable App and API Protection for HAProxy, do the following:

1. Deploy the Datadog HAProxy SPOA container.
1. Update your HAProxy configuration files to integrate with the SPOA

### SPOA container{% #spoa-container %}

Deploy the Datadog HAProxy SPOA image available in the [Datadog GitHub Container Registry](https://github.com/DataDog/dd-trace-go/pkgs/container/dd-trace-go%2Fhaproxy-spoa). The SPOA listens for SPOE connections from HAProxy and sends security events to your Datadog Agent.

See Configuration for available configuration options about the SPOA container.

### HAProxy configuration files{% #haproxy-configuration-files %}

All required HAProxy configuration files are available in the [repository folder](https://github.com/DataDog/dd-trace-go/tree/main/contrib/haproxy/stream-processing-offload/cmd/spoa/haproxyconf/). For information about updates and changes about the configuration, refer to the [configuration changelog](https://github.com/DataDog/dd-trace-go/blob/main/contrib/haproxy/stream-processing-offload/cmd/spoa/haproxyconf/CHANGELOG.md).

The following files are needed for your setup:

- `spoe.cfg`: Core SPOE engine configuration file.
- `global-config.cfg`: Configuration lines to include in your `global` section.
- `frontend-config.cfg`: Configuration lines to add at the top of each `frontend` you want to protect.
- `backend.cfg`: Defines the SPOA backend used by the SPOE engine.
- `datadog_aap_blocking_response.lua`: Lua script for blocking responses.

Guidance for setting up each file is provided below.

#### spoe.cfg{% #spoecfg %}

The `spoe.cfg` file is responsible for declaring the SPOE agent and its configuration. This file should be saved to disk, for example at `/usr/local/etc/haproxy/spoe.cfg`. The location of this file is referenced via the `DD_SPOA_SPOA_CONF_FILE` environment variable, which is configured within the `global` section.

It is important that no custom modifications are made to this file.

#### global-config.cfg{% #global-configcfg %}

The `global-config.cfg` file loads the required Lua script and configures the necessary variables for the integration. Its contents should be incorporated into the `global` section of your `haproxy.cfg` configuration file.

You can adjust the values as needed for your environment. Review the comments within the file for further guidance on each setting.

#### frontend-config.cfg{% #frontend-configcfg %}

The `frontend-config.cfg` file attaches the SPOE filter to your frontend. This section should be placed at the very top of each `frontend` section you want to protect, before other filters and the router.

This section ensures that:

- Request and response events are sent to the SPOA
- Datadog tracing headers are injected when applicable
- The Lua helper is conditionally invoked for blocking

It is important that no custom modifications are made to this part of the configuration.

#### backend.cfg{% #backendcfg %}

The `backend.cfg` file defines the `spoa-backend` used by the SPOE engine and for health checks. This configuration should be appended near the end of your `haproxy.cfg` file.

Be sure to modify the `server spoa1 <host>:<port>` line so that it references your deployed SPOA container instance.

{% alert level="info" %}
**Note:** For high availability and redundancy, you can configure multiple SPOA agent servers by adding additional `server` lines (for example, `server spoa1 ...`, `server spoa2 ...`, etc.). HAProxy will automatically load-balance and failover between these SPOA agents, ensuring continued protection even if one agent becomes unavailable.
{% /alert %}

#### datadog_aap_blocking_response.lua{% #datadog_aap_blocking_responselua %}

The `datadog_aap_blocking_response.lua` script is responsible for sending a custom blocking response when the SPOA instructs HAProxy to block a request. This script could be stored in a location such as `/etc/haproxy/lua/datadog_aap_blocking_response.lua`, and the `lua-load` directive in the `global` section should reference this path.

It is important that no custom modifications are made to this file.

{% alert level="info" %}
**Note:** This Lua script is not invoked on every request processed by HAProxy. It is only invoked when a request is blocked by App and API Protection. This design ensures optimal performance by avoiding the overhead of running Lua code for all requests.
{% /alert %}

### Validation{% #validation %}

After this configuration is complete, the library collects security data from your application and sends it to the Agent. The Agent sends the data to Datadog, where [out-of-the-box detection rules](https://docs.datadoghq.com/security/default_rules/#cat-application-security) flag attacker techniques and potential misconfigurations so you can take steps to remediate.

1. To see App and API Protection threat detection in action, send known attack patterns to your application. For example, trigger the [Security Scanner Detected](https://docs.datadoghq.com/security/default_rules/security-scan-detected/) rule by running a file that contains the following curl script:

   ```
   for ((i=1;i<=250;i++)); do# Target existing service's routescurl https://your-application-url/existing-route -A dd-test-scanner-log;# Target non existing service's routescurl https://your-application-url/non-existing-route -A dd-test-scanner-log;done
```

**Note**: The `dd-test-scanner-log` value is supported in the most recent releases.

A few minutes after you enable your application and send known attack patterns to it, threat information appears in the [Application Signals Explorer](https://app.datadoghq.com/security/appsec) and vulnerability information appears in the [Vulnerabilities explorer](https://app.datadoghq.com/security/appsec/vm/).

{% video
   url="https://datadog-docs.imgix.net/images//security/application_security/appsec-getstarted-threat-and-vuln_2.mp4" /%}

## Configuration{% #configuration %}

The Datadog HAProxy SPOA container supports the following configuration settings:

| Environment variable                | Default value | Description                                                                                                   |
| ----------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------- |
| `DD_HAPROXY_SPOA_HOST`              | `0.0.0.0`     | Host on which the SPOA and HTTP health server listen.                                                         |
| `DD_HAPROXY_SPOA_PORT`              | `3000`        | Port used by the SPOA that accepts communication with HAProxy.                                                |
| `DD_HAPROXY_SPOA_HEALTHCHECK_PORT`  | `3080`        | Port used for the HTTP server for health checks.                                                              |
| `DD_APPSEC_BODY_PARSING_SIZE_LIMIT` | `0`           | Maximum size of bodies to process in bytes. If `0`, bodies are not processed. Recommended: `10000000` (10MB). |
| `DD_SERVICE`                        | `spoa`        | Service name shown in the Datadog UI.                                                                         |

Configure the SPOA to send traces to your Datadog Agent using the following environment variables:

| Environment variable  | Default value | Description                      |
| --------------------- | ------------- | -------------------------------- |
| `DD_AGENT_HOST`       | `localhost`   | Host of a running Datadog Agent. |
| `DD_TRACE_AGENT_PORT` | `8126`        | Port of a running Datadog Agent. |

### Datadog Go Tracer and HAProxy integration{% #datadog-go-tracer-and-haproxy-integration %}

The HAProxy integration is built on top of the [Datadog Go Tracer](https://github.com/DataDog/dd-trace-go) and inherits all of its environment variables. See [Configuring the Go Tracing Library](https://docs.datadoghq.com/tracing/trace_collection/library_config/go/) and [App and API Protection Library Configuration](https://docs.datadoghq.com/security/application_security/policies/library_configuration/).

{% alert level="info" %}
**Note:** As the Datadog SPOA is built on top of the Datadog Go Tracer, it generally follows the same release process as the tracer, and its Docker images are tagged with the corresponding tracer version (for example, `v2.4.0`). In some cases, early release versions might be published between official tracer releases, and these images are tagged with a suffix such as `-docker.1`.
{% /alert %}

## Keeping your configuration up to date{% #keeping-your-configuration-up-to-date %}

Because HAProxy's SPOE integration involves both a runtime component (the SPOA container image) and HAProxy configuration, upgrades can require changes in both places.

The reference HAProxy configuration and an associated changelog are available to help you monitor and track updates:

- [Reference HAProxy configuration directory](https://github.com/DataDog/dd-trace-go/tree/main/contrib/haproxy/stream-processing-offload/cmd/spoa/haproxyconf/) (SPOE engine, global, frontend/backend snippets, Lua)
- [Configuration changelog](https://github.com/DataDog/dd-trace-go/blob/main/contrib/haproxy/stream-processing-offload/cmd/spoa/haproxyconf/CHANGELOG.md)

### Recommended upgrade practices{% #recommended-upgrade-practices %}

- Pin your SPOA image to a specific version and upgrade intentionally after reviewing the configuration changelog.
- Centralize the Datadog configuration so it is easily updatable.
- Track the reference configuration and changelog and compare your configuration to it when upgrading.

## Limitations{% #limitations %}

The HAProxy integration has the following limitations:

- Asynchronous (observability) mode is not currently supported.

For additional details on the HAProxy integration compatibilities, refer to the [HAProxy integration compatibility page](https://docs.datadoghq.com/security/application_security/setup/compatibility/haproxy).

## Further Reading{% #further-reading %}

- [HAProxy integration's source code](https://github.com/DataDog/dd-trace-go/tree/main/contrib/haproxy/stream-processing-offload/cmd/spoa)
- [HAProxy SPOA Docker image](https://github.com/DataDog/dd-trace-go/pkgs/container/dd-trace-go%2Fhaproxy-spoa)
- [OOTB App and API Protection Rules](https://docs.datadoghq.com/security/default_rules/?category=cat-application-security)
- [Troubleshooting App and API Protection](https://docs.datadoghq.com/security/application_security/troubleshooting)
