# Source: https://docs.datadoghq.com/security/application_security/how-it-works/trace_qualification.md

---
title: Trace Qualification
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > App and API Protection > How App and API Protection
  Works in Datadog > Trace Qualification
---

# Trace Qualification

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

App and API Protection (AAP) provides observability into application-level attacks, and evaluates the conditions in which each trace was generated. AAP trace qualification then labels each attack as harmful or safe to help you take action on the most impactful attacks.

Filter by the **Qualification** facet in the AAP [Traces Explorer](https://app.datadoghq.com/security/appsec/traces) to view the possible qualification results:

## Qualification outcomes{% #qualification-outcomes %}

AAP runs qualification rules (closed-source) on every trace. There are four possible qualification outcomes, as listed in the facet menu:

| Qualification result | Description                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Unknown              | AAP has qualification rules for this attack, but did not have enough information to make a qualification decision. |
| None successful      | AAP determined that attacks in this trace were not harmful.                                                        |
| Harmful              | At least one attack in the trace was successful.                                                                   |
| No value             | AAP does not have qualification rules for this type of attack.                                                     |

### Trace sidepanel{% #trace-sidepanel %}

The qualification result can also be seen when viewing the details of an individual trace.
