# Source: https://docs.datadoghq.com/security/application_security/overview.md

---
title: Attack Summary
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > App and API Protection > Attack Summary
---

# Attack Summary

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

The App and API Protection (AAP) [Attack Summary](https://app.datadoghq.com/security/appsec/threat) provides a quick view of your application and API posture. It highlights trends, service exposure, attack traffic, and the impact on business logic. You can pivot from widgets to their related traces.

Each section of **Attack Summary** focuses on a different aspect of security with supporting information.

## Sections{% #sections %}

{% dl %}

{% dt %}
Attack Surface Area
{% /dt %}

{% dd %}
This section provides insights into the exposed services, the tools attackers are using, and the commercial scanners that identify potential vulnerabilities.
{% /dd %}

{% dt %}
Attack Traffic
{% /dt %}

{% dd %}
These graphs identify the classification of attacks, such as SSRF, LFI, SQL and command injection. They allow users to identify spikes in malicious traffic and patterns.
{% /dd %}

{% dt %}
Business Logic
{% /dt %}

{% dd %}
This section focuses on fraud and business logic abuse such as account takeover attempts or any custom business logic events tracked by your application.
{% /dd %}

{% dt %}
Attack Traffic Sources
{% /dt %}

{% dd %}
A global heatmap indicating the sources of attack traffic, providing a visual representation of threats by region.
{% /dd %}

{% /dl %}

## Best practices{% #best-practices %}

1. Review trends and adopt a protection policy that meets your posture needs.
1. Regularly review the **Exposed Services** widget in **Attack Surface Area** to ensure only the correct services are accessible and have a protection policy that meets your risk profile.
1. Block attack tools and ensure that customer scanners are part of an authorized vulnerability management program.
1. Monitor business logic for spikes in credential stuffing attacks or risky payment activity.
1. Use **Attack Traffic Sources** to compare the attack traffic sources with your expected customer locations.
1. Use Powerpacks to enhance your dashboards with the most relevant information.

### Using powerpacks{% #using-powerpacks %}

When adding a widget to a [new dashboard](https://app.datadoghq.com/dashboard/lists) in Datadog, choose the **Powerpacks** section in the tray. Filter on `tag:attack_summary` or type `Attack Summary` in the search box.

Each section in the **Attack Summary** page corresponds to a dedicated powerpack.
