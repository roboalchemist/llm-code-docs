# Source: https://docs.datadoghq.com/feature_flags/server.md

---
title: Server-Side Feature Flags
description: Set up Datadog Feature Flags for server-side applications.
breadcrumbs: Docs > Feature Flags > Server-Side Feature Flags
---

# Server-Side Feature Flags

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### Join the Preview!

Feature Flags are in Preview. Complete the form to request access.

[Request Access](http://datadoghq.com/product-preview/feature-flags/)
{% /callout %}

## Overview{% #overview %}

Datadog Feature Flags for server-side applications allow you to remotely control feature availability, run experiments, and roll out new functionality with confidence. Server-side SDKs integrate with the Datadog APM tracer and use Remote Configuration to receive flag updates in real time.

This guide covers the common setup required for all server-side SDKs, including Agent configuration and application environment variables. Select your language or framework to view SDK-specific setup instructions:

- [.NET](https://docs.datadoghq.com/feature_flags/server/dotnet/)
- [Go](https://docs.datadoghq.com/feature_flags/server/go/)
- [Java](https://docs.datadoghq.com/feature_flags/server/java/)
- [Node.js](https://docs.datadoghq.com/feature_flags/server/nodejs/)
- [Python](https://docs.datadoghq.com/feature_flags/server/python/)
- [Ruby](https://docs.datadoghq.com/feature_flags/server/ruby/)

## Prerequisites{% #prerequisites %}

Before setting up server-side feature flags, ensure you have:

- **Datadog Agent 7.55 or later** installed and running
- **Datadog API key** configured
- **APM tracing** enabled in your application

## Agent configuration{% #agent-configuration %}

Server-side feature flags use [Remote Configuration](https://docs.datadoghq.com/remote_configuration) to deliver flag configurations to your application. Enable Remote Configuration in your Datadog Agent by setting `DD_REMOTE_CONFIGURATION_ENABLED=true` or adding `remote_configuration.enabled: true` to your `datadog.yaml`.

See the [Remote Configuration documentation](https://docs.datadoghq.com/remote_configuration) for detailed setup instructions across different deployment environments.

### Polling interval{% #polling-interval %}

The Agent polls Datadog for configuration updates at a configurable interval. This interval determines the average time between making a flag change in the UI and the change becoming available to your application.

```bash
# Optional: Configure polling interval (default: 60s)
DD_REMOTE_CONFIGURATION_REFRESH_INTERVAL=10s
```

## Application configuration{% #application-configuration %}

Configure your application with the standard Datadog environment variables. These are common across all server-side SDKs:

```bash
# Required: Service identification
DD_SERVICE=<YOUR_SERVICE_NAME>
DD_ENV=<YOUR_ENVIRONMENT>
DD_VERSION=<YOUR_APP_VERSION>

# Agent connection (if not using default localhost:8126)
DD_AGENT_HOST=localhost
DD_TRACE_AGENT_PORT=8126

# Enable Remote Configuration in the tracer
DD_REMOTE_CONFIG_ENABLED=true
```

{% alert level="info" %}
Some SDKs require additional experimental flags to enable feature flagging. See the SDK-specific documentation for details.
{% /alert %}

## Context attribute requirements{% #context-attribute-requirements %}

{% alert level="warning" %}
Evaluation context attributes must be flat primitive values (strings, numbers, booleans). Nested objects and arrays are **not supported** and will cause exposure events to be silently dropped.
{% /alert %}

Use flat attributes in your evaluation context:

```javascript
const evaluationContext = {
  targetingKey: req.session?.userID,
  companyId: req.session?.companyID,
  tier: 'enterprise'
};

const value = client.getBooleanValue('my-flag', false, evaluationContext);
```

Avoid nested objects and arrays:

```javascript
// These attributes will cause exposure events to be dropped
const evaluationContext = {
  targetingKey: req.session?.userID,
  company: { id: req.session?.companyID },  // nested object - NOT SUPPORTED
  roles: ['admin', 'user']                   // array - NOT SUPPORTED
};
```

## Further reading{% #further-reading %}

- [Client-Side Feature Flags](https://docs.datadoghq.com/feature_flags/client/)
- [Remote Configuration](https://docs.datadoghq.com/remote_configuration/)
