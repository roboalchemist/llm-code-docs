# Source: https://docs.datadoghq.com/security/application_security/security_signals/users_explorer.md

---
title: Users Explorer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > App and API Protection > Investigate Security
  Signals > Users Explorer
---

# Users Explorer

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

This topic describes how to use the App and API Protection [Users explorer](https://app.datadoghq.com/security/appsec/users) to investigate the risks associated with the users tracked by security [traces](https://app.datadoghq.com/security/appsec/traces).

## Overview{% #overview %}

Datadog populates the Users explorer by associating users with security traces from events like login attempts. This makes the Users explorer an inventory of tracked users. Users are identified by user ID (`@usr.id`) and, when available, user name and email address. See [Adding authenticated user information to traces and enabling user blocking capability](https://docs.datadoghq.com/security/application_security/how-it-works/add-user-info/?tab=java#adding-authenticated-user-information-to-traces-and-enabling-user-blocking-capability).

Typically, users in the Users explorer are not a risk. However, the explorer helps you identify user accounts that are at risk or are actively being attacked (for example, through attempts to compromise an account).

With the Users explorer, you can investigate and take action on the user accounts flagged as risks using **risk categories**.

### Risk categories{% #risk-categories %}

The Users explorer assigns one or more of the following risk categories to a user identified as a risk:

- **New Geolocation:** User activity from an unfamiliar location might indicate unauthorized access or legitimate travel requiring verification.
- **Impossible Travel:** Occurs when a user logs in from two distant locations in an unrealistically short time, indicating possible credential compromise. A caveat with this category is it can falsely identify users on the same VPN as impossible travel.
- **Compromised User:** A user's credentials are stolen or hacked, allowing attackers to perform malicious activities with their identity.
- **Disposable Email:** A disposable email is an email address that is temporary.

{% alert level="info" %}
When a user ID, email, or name is associated with a trace, but does not match a risk category, it still appears in the Users explorer.
{% /alert %}

### How the Users explorer differs from other explorers{% #how-the-users-explorer-differs-from-other-explorers %}

To understand the difference between the different explorers, review these security approaches they support:

- **Protect:** Automatically block attackers (IPs and authenticated users) using App and API Protection [Policies](https://docs.datadoghq.com/security/application_security/policies/). Customers should block attack tools as their first automated blocking action. Blocking attack tools reduces common vulnerability discovery for OWASP threats such as SQLi, command injection, and SSRF.
- **React:** Blocking attackers in response to observed threats using the [Signals](https://app.datadoghq.com/security), [Traces](https://app.datadoghq.com/security/appsec/traces), Users, [Attackers](https://docs.datadoghq.com/security/application_security/security_signals/attacker-explorer/) explorers.

Each explorer focuses on a specific use case:

- **Signals explorer**: Provides a list of actionable alerts such as `Credential Stuffing Attack` or `Command Injection`. Signals have workflow capabilities, a description, severity, and correlated Traces. Interactions include user assignment workflows, automated protection, analytics, search, and pivoting to Traces Explorer.
- **Traces explorer**: Lists evidence for business logic events, such as logins, or attack payloads. Interactions include analytics and search.
- **Attackers explorer**: Identifies attackers as `suspicious` (IP addresses that have attacked in the last 24 hours up to a threshold) and `flagged` (IP addresses that have exceeded that threshold).
- **Users explorer**: Lists authenticated users associated with one or more traces. Interactions include:
  - Bulk actions for user analytics and blocking
  - Drill-down into the history of any user
  - Search
  - Pivoting to other explorers

## Explore and filter users{% #explore-and-filter-users %}

To start reviewing users, go to the [Users explorer](https://app.datadoghq.com/security/appsec/users).

The main sections in the Users explorer are:

- Facets and search. These enable you to filter users by multiple user attributes.
- The list of users with security metrics.
  - Click a user to examine their risks, IPs, locations, endpoints, and signals.
  - You can block an individual user from the list or its details drawer.
  - To block multiple users, select one or more users and click **Compare and Block**.

## Block a user{% #block-a-user %}

To block an individual user, do the following:

1. Click **Block** in the user's row, and choose a blocking duration.

1. In **Select Security Responses**, select **Block with Datadog's Library**.

Permanently or temporarily blocked authenticated users are added to the [Denylist](https://docs.datadoghq.com/security/application_security/policies/#denylist). Manage the list on the Datadog [Denylist](https://app.datadoghq.com/security/appsec/denylist) page.

## Compare and block multiple users{% #compare-and-block-multiple-users %}

When you select two or more users, you can use the **Compare and Block** button to compare datapoints across potentially compromised users.

When you click **Compare and Block**, several metrics are displayed in **Block selected users**. These metrics help you detect whether you are dealing with **a single attacker**, **a larger coordinated campaign**, or **widespread credential exposure**.

Here's a breakdown of the benefits of comparing each datapoint across two (or more) compromised users.

### Users per ASN{% #users-per-asn %}

**Benefit:** Identifies if compromised accounts are accessed from the same internet service provider (ISP) or network operator.

If multiple users are compromised from the same ASN (Autonomous System Number), it could suggest:

- A botnet operating from that network.
- A VPN or proxy exit node.
- A targeted attack from a specific ISP region (for example, a university or corporate network).

### Users per User Agent{% #users-per-user-agent %}

**Benefit:** Reveals if the attacker is using automated tools or a specific browser configuration.

Matching user agents could mean:

- Same malware toolkit (for example, info-stealer like RedLine or Raccoon).
- Use of headless browsers or scripts.
- Credential stuffing using a shared toolset.

### Users per Location (Geo-IP){% #users-per-location-geo-ip %}

**Benefit:** Exposes if access attempts are coming from the same country or region.

If multiple users are being accessed from the same location (especially foreign or unexpected ones), it:

- Points to targeted regional attacks.
- Helps detect suspicious login anomalies (for example, impossible travel).
- May indicate TOR exit nodes or VPN clusters.

### Users per Domain{% #users-per-domain %}

**Benefit:** Groups affected users by IP domain, which typically represents their organization.

Benefits include:

- Identifying organization-wide breaches.
- Highlighting phishing campaigns targeting a specific company or domain.
- Supporting incident response and alert prioritization.

### Threat Intel Category{% #threat-intel-category %}

**Benefit:** Shows the associated [Threat Intelligence Category](https://docs.datadoghq.com/security/threat_intelligence/#threat-intelligence-categories).

Comparing helps you:

- Understand the vector of compromise.
- Prioritize responses (for example, `corp_vpn`, which are IPs used by businesses, and `hosting_proxy`, which is largely malicious).

### Threat Intel Intention{% #threat-intel-intention %}

**Benefit:** Provides insights about the attacker reputation based on IP. Flagged IPs aren't necessarily malicious, but they are known to be misused. Misuse is often without the user knowing, for example, in the case of `residential_proxy`. These users are worth closer attention.

Matching intentions reveal:

- Common attacker **goals**.
- Whether your users were part of a **targeted vs opportunistic** campaign.
- Whether you should expect **further action**, like BEC (business email compromise) or internal movement.

### IPs per User{% #ips-per-user %}

**Benefit:** Highlights whether multiple (especially **anomalous or malicious**) IPs were used to access one user.

Overlap between users might indicate:

- Use of the **same attacker infrastructure**.
- Office buildings shared by a group of users.
- Centralized control (for example, with a **command-and-control server**).
- Account access from **known malicious IPs** (check threat feeds).

### Summary of comparison details{% #summary-of-comparison-details %}

| Detail                 | Value of Comparison                                |
| ---------------------- | -------------------------------------------------- |
| Users per ASN          | Identify shared attacker infrastructure or VPN use |
| Users per User Agent   | Spot common tooling or automation                  |
| Users per Location     | Detect geolocation-based threat patterns           |
| Users per Domain       | Pinpoint org-wide targeting or breaches            |
| Threat Intel Category  | Understand attack type (phishing, malware, etc.)   |
| Threat Intel Intention | Determine attacker's objective                     |
| IPs per User           | Trace attacker network behavior and connections    |

## Tracking compromised credentials{% #tracking-compromised-credentials %}

Here are some investigation tips for comparing each datapoint across two (or more) compromised users:

1. Breaches are only the beginning. A leaked credential is the entry point into a wider investigation.
1. Look for patterns. Compare ASN, IP, user agent, geo, domain. If multiple users share infrastructure, it's likely one actor or campaign.
1. Geo anomalies matter more than location. The country of origin isn't as important as asking whether the location is normal for the user.
1. Domains reveal the scope. The same attack across multiple users or domains can mean coordinated targeting, not random hits.
1. IP/User Agent overlap equals attacker fingerprint. Toolkits reuse browser strings, scripts, and proxies. Overlap shows the attacker infrastructure.
1. Threat intel context guides response. To triage effectively, combine the category with the intention. This combination tells you if it's phishing, malware, or fraud.
