# Source: https://docs.datadoghq.com/security/application_security/security_signals/attacker-explorer.md

---
title: Attackers Explorer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > App and API Protection > Investigate Security
  Signals > Attackers Explorer
---

# Attackers Explorer

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

This topic describes how to use **Attackers Explorer** to investigate and block Flagged Attackers.

## Overview{% #overview %}

Datadog App and API Protection (AAP) identifies attackers as suspicious and flagged. With [Attackers Explorer](https://app.datadoghq.com/security/appsec/attackers), you can investigate and take action against the attackers.

### Definitions{% #definitions %}

- **Suspicious Attackers:** IP addresses that have sent attack traffic in the last 24 hours up to a maximum threshold.

- **Flagged Attackers:** IP addresses that have sent attack traffic, exceeding the threshold of Suspicious Attackers, in the last 24 hours. Flagged Attackers should be reviewed and blocked.

{% alert level="info" %}
**Flagged Attackers** and **Suspicious Attackers** are mutually exclusive. An IP cannot be in both states at the same time.
{% /alert %}

### How Attackers Explorer differs from Signal and Trace explorers{% #how-attackers-explorer-differs-from-signal-and-trace-explorers %}

To understand the difference between the different explorers, review these approaches:

- **Protect:** Automated blocking using AAP Protection configuration. Customers should block attack tools as their first automated blocking action. Blocking attack tools reduces common vulnerability discovery for OWASP threats such as SQLi, command injection, and SSRF.
- **Reactive:** Blocking using Signals or Attackers explorer in response to observed threats.

Each explorer focuses on a specific use case:

- **Signal Explorer**: List of actionable alerts such as Credential Stuffing Attack or Command Injection. Signals have workflow capabilities, a description, severity, and correlated Traces. Interactions include user assignment workflows, automated protection, analytics, search, and pivoting to Trace Explorer.
- **Trace Explorer**: List of evidence for business logic events, such as logins, or attack payloads. Interactions include analytics and search.
- **Users Explorer**: Lists authenticated users associated with one or more traces. Interactions include:
  - Bulk actions for user analytics and blocking
  - Drill-down into the history of any user
  - Search
  - Pivoting to other explorers
- **Attackers Explorer**: List of Flagged and Suspicious Attackers. Interactions include:
  - Bulk actions for attacker analytics and blocking
  - Drill-down into the history of any attacker
  - Search
  - Pivoting to other explorers

### Explore and filter attackers{% #explore-and-filter-attackers %}

To start reviewing attackers, go to [Attackers Explorer](https://app.datadoghq.com/security/appsec/attackers).

There are two sections to the Attackers Explorer:

1. Facets and search. These enable you to filter traffic by service or attacker attributes.
1. The list of attackers with security metrics.

### Investigate an attacker{% #investigate-an-attacker %}

1. In **View by**, click **IP**, **User Agent**, **ASN**, or **Cluster**.
1. Click on any row to view the details pane for the attacker.

An attacker can be blocked or added to the Passlist from its details.

### Attacker details{% #attacker-details %}

Details common to all attacker views:

- **Blocking Status:** Indicates whether the attacker IP is actively being blocked, helping you confirm if immediate action is needed.
- **Threat Intelligence:** Show Datadog definitions **Suspicious** or **Flagged**.
- **Last Information:** Provides contextual network origin (for example, route, public/private status, geolocation), which helps you understand attacker infrastructure and scope.
- **Associated Users:** Shows which user accounts (if any) were affected or linked to the IP, assisting with lateral movement tracking and potential account compromise identification.
- **Security Traces:** Visualizes the timeline and volume of suspicious activity (for example, **151k AAP traces**), helping SOC teams correlate events and identify peaks in attack behavior.

View-specific details:

- IP:
  - **Threat Intel:** See [Threat Intelligence](https://docs.datadoghq.com/security/threat_intelligence).
  - **History:** Displays past activity to detect patterns or repeated attacks.
  - **Associated Users:** Identifies user accounts associated with the IP.
  - **Endpoint Requests:** Lists HTTP requests to reveal attack methods or targets.
  - **Signals:** Displays triggered detections to assess threat severity.
  - **Clusters:** Points to affected app clusters to gauge impact scope.
  - **Top User Agents:** Lists the most frequent user agents used by the attacker (for example, scripts, scanners, or browsers), helping to identify automation tools or custom clients involved in the attack.
- User Agent:
  - **Associated IPs**: Displays IPs using the same User Agent, with trace counts and recent activity bars per IP.
  - **Associated Users** Lists user accounts tied to this User Agent, helping detect possible account compromise.
  - **Blocking History**: Shows past blocks on the User Agent, useful for spotting repeated offenses.
  - **Endpoint Requests**: Detail which endpoints were targeted and how often.
  - **Signals**: Shows triggered alerts from this User Agent, flagging rule violations or suspicious behavior.
- ASN:
  - **AS:** Identifies the Autonomous System, helping to trace malicious traffic back to its network owner or hosting provider.
  - **Signals:** Shows the volume and severity of security alerts (for example, CRITICAL, HIGH), indicating how active or threatening the ASN's traffic is.
  - **Services:** Lists affected services and environments, helping you understand which parts of the infrastructure are being targeted.
  - **Last activity:** Indicates the most recent time malicious activity was observed from this ASN, helping prioritize investigation of current threats.
  - **Traffic Distribution:** Visualizes the proportion of normal vs suspicious traffic, helping analysts assess if an ASN is primarily used for attacks or mixed usage.
- Cluster:
  - **Similarity Overview:** Shows shared attributes across IPs, user agents, locations, and domains.
    - **IPs per ASN:** Identifies autonomous systems used by attackers.
    - **IPs per User Agent:** Detects automation, spoofing, or reuse across campaigns.
    - **IPs per Location:** Identifies geographic distribution of attacking IPs.
    - **IPs per Domain:** Traces attacker infrastructure and detects suspicious domains.
  - **Threat Intel Category:** Classifies the type of threat.
  - **Threat Intel Intention:** Indicates the likely purpose of the malicious activity.
  - **Users per IP:** Measures breadth of compromise or impersonation.
  - **Services:** Identifies impacted services and environments.
  - **Cluster Activity:** Displays behavioral trends and enables trace inspection.

### Best practices for blocking with Attackers Explorer{% #best-practices-for-blocking-with-attackers-explorer %}

1. Account takeover attacks: Use short durations for blocking IP addresses.
1. Add authorized scanners to monitored passlists to observe activity but prevent blocking.
1. Block mobile ISPs with caution. These networks might have large numbers of users and mobile devices behind single IP addresses.

## Block individual IPs{% #block-individual-ips %}

To block an individual IP temporarily or permanently, do the following:

{% image
   source="https://datadog-docs.imgix.net/images/security/application_security/threats/attacker-explorer/block_ip_address.bc8e7eaeff450e8e9cd2848dd23ed410.png?auto=format"
   alt="Block an IP address with AAP Attackers Explorer" /%}

1. Click `Block` on the row.
1. Choose a blocking duration.

## Block IPs in bulk{% #block-ips-in-bulk %}

You can select multiple IPs and block them temporarily or permanently using the Attackers Explorer's **Compare and Block** option.

**Compare and Block** provides metrics about the IPs to help you block with safety and confidence. For example, **Similarity Overview** and **Activity**, described later in this topic.

To compare and block IPs in bulk, do the following:

1. Filter the list of Attackers with a search or facets.

1. Select multiple IPs.

1. Select the **Compare and Block** option.

In the following example, the selected IPs are from the same location and appear to be related. The **Compare and Block** option opens the **Block selected attackers** view, showing metrics and attributes for the selected IP addresses.

   {% image
      source="https://datadog-docs.imgix.net/images/security/application_security/threats/attacker-explorer/attacker_explorer_review_groups2.84ad289063c23891a63a2295f0a892ee.png?auto=format"
      alt="Screenshot of the AAP Attackers Explorer group blocking" /%}

1. To block attackers, click **Block**.

## Block selected attackers metrics{% #block-selected-attackers-metrics %}

When you select the **Compare and Block** option, the **Block selected attackers** view opens, showing metrics and attributes for the selected IP addresses.

{% image
   source="https://datadog-docs.imgix.net/images/security/application_security/threats/attacker-explorer/attacker_explorer_review_groups2.84ad289063c23891a63a2295f0a892ee.png?auto=format"
   alt="Screenshot of the AAP Attackers Explorer group blocking" /%}

{% alert level="info" %}
Metrics for **Similarity Overview** and **Activity** are scoped to the last 30 days.
{% /alert %}

The **Block selected attackers** view metrics are explained in the following sections.

### Selected IPs{% #selected-ips %}

Contains the IPs selected from the explorer. Deselecting an IP removes it from the metrics sections and **Block** action.

### Similarity overview{% #similarity-overview %}

Each column exists to help block with confidence and safety. The provided attributes are also used by AAP's Attacker Similarity feature.

{% dl %}

{% dt %}
ASNs
{% /dt %}

{% dd %}
Autonomous System Numbers. Attacks with large numbers of IP addresses might originate from the same ASN, especially when attacks originate from data centers and cloud IPs.
{% /dd %}

{% dt %}
User Agents
{% /dt %}

{% dd %}
Attackers, commercial scanners, and your own software might use predictable user agents that can help qualify what should be included or excluded from blocking.
{% /dd %}

{% dt %}
Location
{% /dt %}

{% dd %}
Companies might have policies or serviceable markets that determine what countries they allow traffic from.
{% /dd %}

{% dt %}
Domain
{% /dt %}

{% dd %}
The owner of the ASN. This is helpful when an organization owns multiple ASNs.
{% /dd %}

{% dt %}
Users per IPs
{% /dt %}

{% dd %}
The number of users who have authenticated from the IP. IPs with large numbers of logins might indicate a load balancer or many users from the same location, like a company site.
{% /dd %}

{% /dl %}

### Activity{% #activity %}

The time scope for activity is 30 days.

#### Signals{% #signals %}

The signals associated with the IP addresses over the selected time.

#### Traces{% #traces %}

The traces associated with the IP addresses over the selected time.

Benign traffic is sampled APM traffic which are traces without business logic or attack traffic detections.

Attack traffic is all AAP traces, inclusive of business logic.

### Block{% #block %}

This adds the IP addresses to the [Denylist](https://app.datadoghq.com/security/appsec/denylist) for the specified duration.
