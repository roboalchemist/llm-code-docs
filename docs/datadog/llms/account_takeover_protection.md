# Source: https://docs.datadoghq.com/security/account_takeover_protection.md

---
title: Account Takeover Protection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Account Takeover Protection
---

# Account Takeover Protection

App and API Protection (AAP) provides account takeover (ATO) protection to detect and mitigate account takeover attacks.

ATO protection has the following benefits:

- Block attackers and disable users.
- Identify targeted and compromised users.
- Differentiate existing users from non-existing users.
- Cluster attackers into logical groups for mitigation.

## Account takeover protection overview{% #account-takeover-protection-overview %}

Account takeover occurs when an attacker gains access to a user's account credentials and assumes control of the account.

The following tables lists the *attacker motivation by business*:

| Monetary Theft                                 | Reselling Accounts                        |
| ---------------------------------------------- | ----------------------------------------- |
| Consumer banking apps                          | SaaS Platforms                            |
| Financial service apps that issue credit cards | Consumer platforms with stored gift cards |

## Attacker strategies{% #attacker-strategies %}

Attacks use publicly available automated tools to compromise a user's account credentials. The sophistication and scale of these tools have varying capabilities.

Here are some common strategies:

{% dl %}

{% dt %}
Credential stuffing
{% /dt %}

{% dd %}
An automated cyberattack where stolen account credentials (usernames, email addresses, passwords, and so on) are used to gain unauthorized access to user accounts. Access is gained through large scale automated login requests directed against a web application.
{% /dd %}

{% dd %}
Credential stuffing relies on credential dumps.
{% /dd %}

{% dt %}
Credential dumps
{% /dt %}

{% dd %}
Credential dumps occur when stolen credentials from a security breach are posted publicly or sold on dark web markets. This often results in the release of a large number of usernames, passwords, and other account details.
{% /dd %}

{% dt %}
Credential cracking
{% /dt %}

{% dd %}
Credential cracking involves attempting to decipher a user's password by systematically trying different combinations of passwords until the correct one is found. This method often uses software tools that apply various password guessing techniques.
{% /dd %}

{% dt %}
Brute force
{% /dt %}

{% dd %}
Brute force is a trial-and-error method used to obtain information such as a user password or personal identification number (PIN). In this attack, automation is used to generate consecutive guesses and gain unauthorized access to a system.
{% /dd %}

{% /dl %}

## Setting up ATO detection and prevention{% #setting-up-ato-detection-and-prevention %}

AAP provides managed detections of ATO attacks.

Effective ATO detection and prevention requires the following:

1. Instrumenting your production login endpoints. This enables detection with AAP-managed rules.
1. Remote configuration. This enables blocking attacks and pushing remote instrumentation from the Datadog user interface.
1. Notifications. Ensures you are notified of compromised accounts.
1. Reviewing your first detection. Understand how automated protection fits in with your attacks and escalation requirements.

## Instrumenting your production login endpoints{% #instrumenting-your-production-login-endpoints %}

The following user activity events are used for ATO tracking.

| Enrichment             | Auto-instrumented | Use case                                                                       |
| ---------------------- | ----------------- | ------------------------------------------------------------------------------ |
| `users.login.success`  | True              | Account takeover detection rule requirement                                    |
| `users.login.failure`  | True              | Account takeover detection rule requirement                                    |
| `users.password_reset` | False             | Detection rule requirement to identify user enumeration through password reset |

Those enrichment need to hold a user identifier (unique to a user, numeric or otherwise) as `usr.id`. In the case of login failures, it also needs to know whether the user existed in the database or not (`usr.exists`). This helps identifying malicious activity that will regularly target missing accounts.

{% alert level="info" %}
You can use the [Suggested Rules](https://app.datadoghq.com/security/appsec/policies/in-app-waf?config_by=suggested-rules) feature to automatically analyze application traffic and propose rules to help monitor and protect login and API flows. See [Suggested Rules.](https://docs.datadoghq.com/security/application_security/policies/inapp_waf_rules/#suggested-rules)
{% /alert %}

For steps on enabling tracking for events that are not automatically instrumented, go to [User Monitoring and Protection](https://docs.datadoghq.com/security/application_security/how-it-works/add-user-info/).

For the latest list of relevant detections and instrumentation requirements, go to [Detection Rules](https://app.datadoghq.com/security/configuration/asm/rules?query=type%3Aapplication_security%20defaultRule%3Atrue%20dependency%3A%28business_logic.users.%2A%29%20&deprecated=hide&groupBy=none&sort=rule_name) page.

[Automatic instrumentation](https://app.datadoghq.com/security/configuration/asm/rules?query=type%3Aapplication_security%20defaultRule%3Atrue%20dependency%3A%28business_logic.users.%2A%29%20&deprecated=hide&groupBy=none&sort=rule_name) is a Datadog capability that automatically identifies user login success and failure for many authentication implementations.

You are not limited to how Datadog defines these enrichments. Many platform products opt to add additional enrichments, such as identifying the customer organization or user role.

## Remote Configuration{% #remote-configuration %}

[Remote Configuration](https://docs.datadoghq.com/tracing/guide/remote_config/) enables AAP users to instrument apps with custom [business logic](https://app.datadoghq.com/security/appsec/business-logic) data in near real time.

## Notifications{% #notifications %}

[Notifications](https://docs.datadoghq.com/security/notifications/rules/) are a flexible method to ensure the correct team members are informed of an attack. Collaboration [Integrations](https://app.datadoghq.com/integrations?category=Collaboration) with common communication methods are available out of the box.

## Review your first detection{% #review-your-first-detection %}

AAP highlights the most relevant information and suggests actions to take based on the detection type. It also indicates what actions have been taken.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/review_first_detection2.b63d9c215d4247be389a9972f323c07a.png?auto=format"
   alt="An Account Takeover signal showing different highlighted areas of interest" /%}

**Compromised Users**

Compromised and targeted users can be reviewed and blocked within **Signals** and **Traces**.

**Signals**

Individual users can be blocked in **Signals** using **Targeted Users**.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/compromised_users_signals2.3bada5dc870869db0abd4abb51835635.png?auto=format"
   alt="Compromised users shown on a security signal" /%}

**Traces**

Individual users can be blocked on **Traces**, in **User**. Click on any user to show this option.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/traces_block_user.15c1414d15923ef5f97a5e47a24da087.png?auto=format"
   alt="Compromised users shown in the security trace explorer" /%}

## Best practices for signal review and protection{% #best-practices-for-signal-review-and-protection %}

Review the following best practices to help you detect and mitigate account takeover attacks.

### Develop an incident response plan{% #develop-an-incident-response-plan %}

Review the following sections to help you develop an incident response plan.

#### Do you use authenticated scanners?{% #do-you-use-authenticated-scanners %}

Identify trusted IPs, preventing them from being automatically blocked. This step is useful for the following:

- Approved scanning sources that attempt to log in.
- Corporate sites with large numbers of users behind single IP addresses.

To configure trusted IPs, use [Passlist](https://app.datadoghq.com/security/appsec/passlist) and add a `Monitored` entry. Monitored entries are excluded from automated blocking.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/passlist2.e542e347b2162812d834fdf7c97389df.png?auto=format"
   alt="Monitored passlist" /%}

#### Know your customer authentication profile{% #know-your-customer-authentication-profile %}

Review the networks your customers authenticate from, such as:

- Mobile ISPs
- Corporate VPNs
- Residential IPs
- Data centers

Understanding authentication sources can inform your blocking strategy.

For example, you might *not* expect customers to authenticate with your consumer application from data centers. Consequently, you might have more freedom to block the IPs associated with that data center.

Nevertheless, if your customers source entirely from Mobile ISPs, you might have an impact to legitimate traffic if you block those ISPs.

Consider who your customers are, and their account name structure.

Do your customers match these attributes?

- Employees with an expected ID format such as integers, corporate domains, or combinations of numbers and text.
- SaaS customers using domain names associated with the customer company.
- Consumers using free providers such as Gmail or Proton Mail.

Understanding your customers' account name structure helps you determine if attacks are targeted or blind attempts at credential stuffing.

### Distributed attacks{% #distributed-attacks %}

Blocking advanced distributed attacks is often a business decision because attacks can impact availability, user funds, and legitimate users.

Here are three critical components for success in mitigating these attacks:

1. Proper onboarding: Are you configured for blocking with AAP?
1. Proper configuration: Ensure you have correctly set client IPs and X-Forwarded-For (XFF) HTTP headers.
1. Internal communication plans: Communication with security teams, service owners, and product leads is critical to understanding the impact of mitigating large scale attacks.

{% alert level="info" %}
Responders can identify service owners using the tags in all AAP signals.
{% /alert %}

### Know your trends{% #know-your-trends %}

Use the [Threats Overview](https://app.datadoghq.com/security/appsec/threat) to monitor business logic trends, such as spikes in failed logins against your services.

{% image
   source="https://datadog-docs.imgix.net/images/security/ato/threats_overview2.1aca7c63bc97a1b7791408706b904bf9.png?auto=format"
   alt="Threats Overview" /%}

### Signal review{% #signal-review %}

Review the following best practices for signals.

#### IP addresses{% #ip-addresses %}

Use short durations for blocking attackers. 15 minutes or less is recommended. It is uncommon for attackers to reuse IP addresses in distributed account takeovers.

#### Data centers{% #data-centers %}

Some attacks are launched using inexpensive virtual private servers (VPS) and hosting providers. Attackers are motivated by how their low cost and automation enables access to new IP addresses at the data center.

Many consumer applications have low occurrences of user authentication from data centers, especially low cost data centers and VPS providers. Consider blocking the entire data center or ASN when the network range is small, and not within your expected user authentication behavior.

{% alert level="info" %}
Datadog uses third party data sources such as IPinfo and Spur to determine if an IP is a hosting provider. Datadog processes this data within Datadog infrastructure.
{% /alert %}

#### Proxies{% #proxies %}

Datadog uses [Spur](https://docs.datadoghq.com/security/threat_intelligence#threat-intelligence-sources) to determine if an IP is a proxy. Datadog correlates indicators of compromise (IOCs) with account takeover attacks for faster detection with the AAP-managed account takeover rules.

Datadog recommends never blocking IP addresses solely based on threat intelligence IOCs for IP addresses. See our threat intelligence [best practices](https://docs.datadoghq.com/security/threat_intelligence#best-practices-in-threat-intelligence) for details.

Details on IPs, including ownership and threat intelligence, are available in the IP address details. Click on an IP addresses to view these details.

Two types of proxies are frequently seen in distributed account takeovers:

- Hosting proxies: Proxies that exist at data centers, and are often the result of a compromised host at that data center. Guidance for interacting with hosting proxies is similar to data centers.

- Residential proxies: Proxies that exist behind residential IPs. Residential proxies are frequently enabled by mobile application SDKs or browser plugins. The user of the SDK or plugin is typically unaware that they are running a proxy. It is common to see benign traffic from IP addresses identified as residential proxies.

#### Mobile ISPs{% #mobile-isps %}

Datadog uses third parties such as IPinfo and Spur to determine if an IP is a Mobile ISP.

Exercise caution when blocking Mobile ISPs. Mobile ISPs use [CGNAT](https://en.wikipedia.org/wiki/Carrier-grade_NAT) and frequently have large numbers of phones behind each IP address.

#### Attacker attributes{% #attacker-attributes %}

Use attacker attributes to target response actions.

Datadog clusters attackers by the similarity of their attributes. Responders can use custom rules to block the attributes of persistent attackers.

### Protection{% #protection %}

Review the following best practices for protection.

#### Automated protection{% #automated-protection %}

Evaluate the managed ruleset to determine which rules fit your internal automated blocking policies.

If you do not have a policy, review your existing detections and start with the suggested responses in **Signals**. Build your policy based on the most relevant actions taken over time.

#### Users{% #users %}

In **Signals**, the **What Happened** and **Targeted Users** sections provide examples of the attempted usernames.

The **Traces** section identifies if the users exist. Understanding if users exist can influence your incident response decisions.

Develop an incident response plan using the following post compromise steps:

1. Monitoring compromised user accounts.
1. Plan to invalidate credentials and contact users to update credentials.
1. Consider blocking users using AAP.

Attack motivation can influence post-compromise activity. Attackers wanting to resell accounts are unlikely to use accounts immediately after a compromise. Attackers attempting to access stored funds will use accounts immediately after compromise.

Consider blocking compromised users in addition to blocking the attacker.

To export a list of compromised or targeted users from a signal:

1. Go to the notification settings in a detection rule condition.
1. Add a recipient and turn on *Notify for every new `@usr.id` detected*. This allows you to export the list when updates occur.

{% image
   source="https://datadog-docs.imgix.net/images/security/application_security/threats/notify-on-update.ed4e77e0d95468507903ccadb8a53529.png?auto=format"
   alt="Notify on update toggle on detection rule editor" /%}

Notification targets set in the detection rule condition receive a message when new user IDs are detected. However, notification profiles monitoring these signals do not receive alerts for new user IDs.

To receive targeted and compromised user IDs with a webhook, set up a webhook using the Datadog webhook integration. Include the `$SECURITY_SIGNAL_ATTRIBUTES` variable in the webhook payload. The user IDs are stored under the `@usr.id` path in the JSON payload.

{% image
   source="https://datadog-docs.imgix.net/images/security/application_security/threats/notify-on-update-payload.c6b92b782480a44f463f786ed0477a49.png?auto=format"
   alt="Notify on update example payload" /%}

## Further reading{% #further-reading %}

- [AAP Terms and Concepts](https://docs.datadoghq.com/security/application_security/terms/)
- [User Monitoring and Protection](https://docs.datadoghq.com/security/application_security/how-it-works/add-user-info/?tab=set_user)
- [App and API Protection Guides](https://docs.datadoghq.com/security/application_security/guide/)
