# Source: https://docs.datadoghq.com/security/application_security/how-it-works/threat-intelligence.md

---
title: Threat Intelligence
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > App and API Protection > How App and API Protection
  Works in Datadog > Threat Intelligence
---

# Threat Intelligence

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

This topic describes [threat intelligence](https://docs.datadoghq.com/security/threat_intelligence/#threat-intelligence-sources) for App and API Protection (AAP).

Datadog provides built-in threat intelligence [datasets](https://docs.datadoghq.com/security/threat_intelligence/#threat-intelligence-sources) for AAP. This provides additional evidence when acting on security activity and reduces detection thresholds for some business logic detections.

Additionally, AAP supports *bring your own threat intelligence*. This functionality enriches detections with business-specific threat intelligence.

## Best practices{% #best-practices %}

Datadog recommends the following methods for consuming threat intelligence:

1. Reducing detection rule thresholds for business logic threats such as credential stuffing. Users can clone the default [Credential Stuffing](https://app.datadoghq.com/security/appsec/detection-rules?query=type%3Aapplication_security%20defaultRuleId%3Adef-000-yk4) rule and modify it to meet their needs.
1. Using threat intelligence as a indicator of reputation with security activity.

Datadog recommends *against* the following:

1. Blocking threat intelligence traces without corresponding security activity. IP addresses might have many hosts behind them. Detection of a residential proxy means that the associated activity has been observed by a host behind that IP. It does not guarantee that the host running the malware or proxy is the same host communicating with your services.
1. Blocking on all threat intelligence categories, as this is inclusive of benign traffic from corporate VPNs and blocks unmalicious traffic.

## Filtering on threat intelligence in AAP{% #filtering-on-threat-intelligence-in-aap %}

Users can filter threat intelligence on the Signals and Traces explorers using facets and the search bar.

To search for all traces flagged by a specific source, use the following query with the source name:

```
@threat_intel.results.source.name:<SOURCE_NAME> 
```

To query for all traces containing threat intelligence from any source, use the following query:

```
@appsec.threat_intel:true 
```

## Bring your own threat intelligence{% #bring-your-own-threat-intelligence %}

AAP supports enriching and searching traces with threat intelligence indicators of compromise stored in Datadog reference tables. [Reference Tables](https://docs.datadoghq.com/integrations/guide/reference-tables) allow you to combine metadata with information already in Datadog.

For more information, see the [Bring Your Own Threat Intelligence](https://docs.datadoghq.com/security/guide/byoti_guide) guide.

## Threat intelligence in the user interface{% #threat-intelligence-in-the-user-interface %}

When viewing the traces in the AAP Traces Explorer, you can see threat intelligence data under the `@appsec` attribute. The `category` and `security_activity` attributes are both set.

Under `@threat_intel.results` you can always see the full details of what was matched from which source.

## Further Reading{% #further-reading %}

- [Datadog Cloud SIEM: Driving innovation in security operations](https://www.datadoghq.com/blog/cloud-siem-enterprise-security)
