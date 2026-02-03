# Source: https://docs.datadoghq.com/security/application_security/security_signals/attacker_clustering.md

---
title: Attacker Clustering
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > App and API Protection > Investigate Security
  Signals > Attacker Clustering
---

# Attacker Clustering

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Attacker Clustering improves distributed attack blocking. Datadog App and API Protection (AAP) identifies security signal traffic attacker patterns and to help you mitigate distributed attacks more efficiently.

Attacker clustering highlights a set of common attributes shared by a significant portion of traffic and suggests blocking based on those attributes.

Blocking on attacker attributes means you keep your application or API protected even as the attacker rotates between IPs.

## What signals are used for attacker clusters?{% #what-signals-are-used-for-attacker-clusters %}

The attacker clustering is computed for every [AAP security signal](https://docs.datadoghq.com/security/workload_protection/security_signals/) emitted from a detection rule tagged with `category:account_takeover` or `category:fraud`

Out of the box, attacker clustering is computed for the AAP detection rules that detect API abuse, credential stuffing, or brute force attacks.

If you want the attacker clustering executed on custom detection rules, add these tags in the detection rule editor (see screenshot below).

{% image
   source="https://datadog-docs.imgix.net/images/security/application_security/threats/tag-on-detection-rule.fb1a09bd82b514866ffbdeab57944630.png?auto=format"
   alt="Screenshot of the Detection rule editor showing where to add tags" /%}

## Attacker clustering attributes{% #attacker-clustering-attributes %}

Attacker clustering is computed using the following request attributes:

- Browser name
- Browser version
- OS name
- OS version
- User agent header
- HTTP request headers (for example, `accept-encoding`, `content-type`)
- [Datadog attacker fingerprinting](https://docs.datadoghq.com/security/application_security/security_signals/attacker_fingerprint)

When the attacker attributes are identified, they are displayed on the signal side panel and **Signals** page. Attacker attributes can be a combination of the attributes listed above.

{% image
   source="https://datadog-docs.imgix.net/images/security/application_security/threats/attacker-attributes.86b085e30fb767134ca8b92a592f1109.png?auto=format"
   alt="Screenshot of an AAP signals with attacker attributes identified" /%}

### Custom HTTP request headers{% #custom-http-request-headers %}

If you want to use custom HTTP request headers for attacker clustering, they must be added under the path `@http.request.headers` in your traces. You can add custom headers to your traces by configuring the tracer with the `DD_TRACE_REQUEST_HEADER_TAGS` environment variable. For more information about this configuration, see [Configure the Datadog Tracing Library](https://docs.datadoghq.com/tracing/trace_collection/library_config/).

## Attacker clustering mechanism{% #attacker-clustering-mechanism %}

The clustering algorithm analyzes the frequency of attributes in the attack traffic. It selects attributes that appear frequently while also filtering out typical traffic noise. This process results in attributes that can be blocked to stop or slow the attacker.

The algorithm tracks the changes in the attack traffic by identifying emerging trends as the attacker changes tactics (for example, changing headers, tool, etc.). The attacker cluster is updated with the latest traffic trends.

Traffic associated with threat intelligence is also considered in the clustering mechanism. The more an attribute is correlated with [Threat Intelligence](https://docs.datadoghq.com/security/application_security/how-it-works/threat-intelligence/), the higher the chance to create an attacker cluster around this attribute.

The attacker clustering attributes selected are then shown as regular expressions that can be used to block with AAP's [In-App WAF](https://docs.datadoghq.com/security/application_security/security_signals/) or to filter out traffic in AAP Traces explorer for investigation.

## Custom attacker clustering{% #custom-attacker-clustering %}

If the automatic attacker clustering detection fails to identify the appropriate attributes, you can manually create attacker clusters by selecting attributes from the trace analysis side panel.

To create a custom attacker cluster:

1. Open the trace analysis panel from a security signal.
1. Select the specific attributes that correspond to the attacker's patterns.
1. Create a cluster based on your selected attributes.

{% image
   source="https://datadog-docs.imgix.net/images/security/application_security/threats/create-custom-cluster.fed834ecb14a2cc2ca8dea5af1de24cc.png?auto=format"
   alt="The trace analysis panel with the create cluster from search button highlighted" /%}

This manual approach allows you to create more targeted blocking rules when the automatic detection doesn't capture the right patterns.

{% image
   source="https://datadog-docs.imgix.net/images/security/application_security/threats/custom-clusters.779cc52878bb438388673b6e3ef2aaca.png?auto=format"
   alt="An AAP signal with custom clusters sorted by the attacker attributes" /%}

## Further reading{% #further-reading %}

- [Attacker Fingerprint](https://docs.datadoghq.com/security/application_security/security_signals/attacker_fingerprint)
- [Threat Intelligence](https://docs.datadoghq.com/security/application_security/how-it-works/threat-intelligence/)
- [In-App WAF Rules](https://docs.datadoghq.com/security/application_security/policies/inapp_waf_rules/)
- [Security Signals](https://docs.datadoghq.com/security/application_security/security_signals/)
- [Detect and respond to evolving attacks with Attacker Clustering](https://www.datadoghq.com/blog/attacker-clustering/)
