# Source: https://docs.datadoghq.com/security/application_security/setup/kubernetes/envoy-gateway.md

# Source: https://docs.datadoghq.com/security/application_security/setup/compatibility/envoy-gateway.md

---
title: Envoy Gateway Compatibility Requirements
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > App and API Protection > Enabling App and API
  Protection > Compatibility Requirements > Envoy Gateway Compatibility
  Requirements
---

# Envoy Gateway Compatibility Requirements

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

The following table lists App and API Protection capabilities for the Envoy Gateway integration according to the specified Datadog External Processor image version:

| App and API Protection capability              | Minimum Datadog External Processor image version |
| ---------------------------------------------- | ------------------------------------------------ |
| Threat Detection                               | v2.4.0                                           |
| Threat Protection                              | v2.4.0                                           |
| Customize response to blocked requests         | v2.4.0                                           |
| Non blocking asynchronous mode (observability) | not supported                                    |
| API Security                                   | v2.4.0                                           |
| App and API Protection Standalone              | v2.4.0                                           |
| Automatic user activity event tracking         | not supported                                    |

### Body processing support{% #body-processing-support %}

The Datadog External Processor service supports the processing of request and response bodies for the following payload types:

| Payload type | Minimum Datadog External Processor image version |
| ------------ | ------------------------------------------------ |
| JSON         | v2.4.0                                           |

## Envoy Gateway version support{% #envoy-gateway-version-support %}

### Supported Envoy Gateway versions{% #supported-envoy-gateway-versions %}

Envoy Gateway relies on Envoy Proxy and the Gateway API, and runs within a Kubernetes cluster. Datadog supports only nonâEOL Envoy Gateway versions; see the official [Envoy Gateway Compatibility Matrix](https://gateway.envoyproxy.io/news/releases/matrix/) for the current list of supported versions and upstream dependencies (Envoy Proxy, Gateway API, Kubernetes).

### Envoy version support{% #envoy-version-support %}

The Datadog Envoy integration for App and API Protection relies on features that might not be present in every Envoy version. The following table shows which Envoy versions support each feature.

| Feature                    | Minimum Envoy version |
| -------------------------- | --------------------- |
| External Processing Filter | v1.27.0               |
| Observability mode         | v1.30.0               |

## Datadog Envoy Gateway integration support{% #datadog-envoy-gateway-integration-support %}

{% alert level="info" %}
The Datadog Envoy Gateway integration for App and API Protection is in Preview.
{% /alert %}

Only the Linux version and both the amd64 and arm64 architectures are supported.

{% alert level="info" %}
If you would like to see support added for any of the unsupported capabilities, let us know! Fill out [this short form to send details](https://forms.gle/gHrxGQMEnAobukfn7).
{% /alert %}
