# Source: https://docs.datadoghq.com/security/application_security/setup/compatibility/gcp-service-extensions.md

---
title: App and API Protection GCP Service Extensions Compatibility Requirements
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > App and API Protection > Enabling App and API
  Protection > Compatibility Requirements > App and API Protection GCP Service
  Extensions Compatibility Requirements
---

# App and API Protection GCP Service Extensions Compatibility Requirements

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

The following table lists App and API Protection capabilities for GCP Service Extensions according to the specified Datadog Service Extensions callout image version:

| App and API Protection capability      | Minimum App and API Protection Service Extensions callout image version |
| -------------------------------------- | ----------------------------------------------------------------------- |
| Threat Detection                       | 1.71.0                                                                  |
| Threat Protection                      | 1.71.0                                                                  |
| Customize response to blocked requests | 1.71.0                                                                  |
| API Security                           | v2.2.2                                                                  |
| App and API Protection Standalone      | v2.2.2                                                                  |
| Automatic user activity event tracking | not supported                                                           |

Please refer to the [limitations](https://docs.datadoghq.com/security/application_security/setup/gcp/service-extensions) of the App and API Protection GCP Service Extensions integration.

### Body processing support{% #body-processing-support %}

The Datadog Service Extensions callout supports the processing of request and response bodies for the following payload types:

| Payload type | Minimum App and API Protection Service Extensions callout image version |
| ------------ | ----------------------------------------------------------------------- |
| JSON         | v2.2.2                                                                  |

## App and API Protection GCP Service Extensions support{% #app-and-api-protection-gcp-service-extensions-support %}

{% alert level="info" %}
App and API Protection GCP Service Extensions is in Preview.
{% /alert %}

{% alert level="info" %}
If you would like to see support added for any of the unsupported capabilities, let us know! Fill out [this short form to send details](https://forms.gle/gHrxGQMEnAobukfn7).
{% /alert %}
