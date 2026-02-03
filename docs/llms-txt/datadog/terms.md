# Source: https://docs.datadoghq.com/security/application_security/terms.md

---
title: Terms and Concepts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > App and API Protection > Terms and Concepts
---

# Terms and Concepts

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

Datadog App and API Protection monitors threats and provides protection against application-level attacks that aim to exploit code-level vulnerabilities. It leverages runtime code execution context, trace and error data, and user attribution.

## General App and API Protection terms{% #general-app-and-api-protection-terms %}

{% dl %}

{% dt %}
attack attempt
{% /dt %}

{% dd %}
Which security rule was triggered by the trace.
{% /dd %}

{% dt %}
Datadog library
{% /dt %}

{% dd %}
*also* tracer, tracing library
{% /dd %}

{% dd %}
A programming language-specific library embedded in web applications. Datadog App and API Protection uses the library to monitor and protect. APM uses the same library to instrument code for tracing telemetry.
{% /dd %}

{% dt %}
detection rule
{% /dt %}

{% dd %}
A conditional logic definition that is applied to ingested data and cloud configurations. When at least one case defined in a rule is matched over a given period of time, Datadog generates a *security signal*.
{% /dd %}

{% dd %}
See [Detection rules](https://docs.datadoghq.com/security/detection_rules/).
{% /dd %}

{% dt %}
passlist (formerly exclusion filter)
{% /dt %}

{% dd %}
A mechanism for discarding security traces flagged through the Datadog App and API Protection library and the In-App WAF rules. Passlist is applied as requests are ingested into Datadog (intake). Passlist helps manage false positives and intake costs.
{% /dd %}

{% dd %}
See [Exclusion filters](https://app.datadoghq.com/security/appsec/exclusions) in the app.
{% /dd %}

{% dt %}
In-App WAF rules (formerly event rules)
{% /dt %}

{% dd %}
A set of rules executed in the Datadog libraries to catch security activity. These include Web Application Firewall (WAF) patterns that monitor for attempts to exploit known vulnerabilities.
{% /dd %}

{% dd %}
See [In-App WAF rules](https://docs.datadoghq.com/security/application_security/policies/inapp_waf_rules/).
{% /dd %}

{% dt %}
Remote Configuration
{% /dt %}

{% dd %}
A Datadog platform mechanism that enables the Agent configuration to be updated remotely. Used by Datadog App and API Protection to update In-App WAF rules, activate the product, and block attackers.
{% /dd %}

{% dd %}
See [How Remote Configuration Works](https://docs.datadoghq.com/remote_configuration).
{% /dd %}

{% dt %}
service
{% /dt %}

{% dd %}
A single web application, microservice, API, or function. Usually serves a business function.
{% /dd %}

{% dt %}
signal
{% /dt %}

{% dd %}
A detection of an application attack that impacts your services. Signals identify meaningful threats for you to review, and should be triaged with a high priority.
{% /dd %}

{% dd %}
See [Signals Explorer](https://app.datadoghq.com/security/appsec/signals?query=%40workflow.rule.type%3A%22Application%20Security%22&view=signal) in the app.
{% /dd %}

{% dt %}
severity
{% /dt %}

{% dd %}
An indicator of how quickly an attack attempt should be triaged and addressed. Based on a combination of factors, including the attack's potential impact and risk. Values are Critical, High, Medium, Low, Info.
{% /dd %}

{% dt %}
security trace
{% /dt %}

{% dd %}
A distributed trace for which security activity has been flagged by In-App WAF rules. The underlying trace is shared with APM, allowing deeper and faster investigations.
{% /dd %}

{% dt %}
suspicious request
{% /dt %}

{% dd %}
A distributed trace for which security activity has been flagged by In-App WAF rules. The underlying trace is shared with APM, allowing deeper and faster investigations.
{% /dd %}

{% dt %}
user attribution
{% /dt %}

{% dd %}
A mechanism that maps suspicious requests to known users in your systems.
{% /dd %}

{% dd %}
See [Tracking User Activity](https://docs.datadoghq.com/security/application_security/how-it-works/add-user-info/).
{% /dd %}

{% dt %}
vulnerability
{% /dt %}

{% dd %}
Passive risk within an application. From [OWASP](https://owasp.org/www-community/vulnerabilities/): "A vulnerability is a hole or a weakness in the application, which can be a design flaw or an implementation bug, that allows an attacker to cause harm to the stakeholders of an application. Stakeholders include the application owner, application users, and other entities that rely on the application."
{% /dd %}

{% dt %}
trace qualification
{% /dt %}

{% dd %}
The process by which Datadog helps understand the impact of traces, labeling them as `Harmful Safe or Unknown`.
{% /dd %}

{% dd %}
See [Trace Qualification](https://docs.datadoghq.com/security/application_security/how-it-works/trace_qualification/).
{% /dd %}

{% dt %}
threat intelligence
{% /dt %}

{% dd %}
A set of rules executed in the Datadog libraries to detect threats. These include Web Application Firewall (WAF) patterns that monitor for attempts to exploit known vulnerabilities.
{% /dd %}

{% dd %}
See [Threat Intelligence](https://docs.datadoghq.com/security/application_security/how-it-works/threat-intelligence/)
{% /dd %}

{% dt %}
suspicious attackers
{% /dt %}

{% dd %}
A precursor to Flagged IPs. Suspicious IPs have met a minimum threshold of attack traffic to be classified as suspicious, but not the threshold for Flagged. Thresholds are not user-configurable.
{% /dd %}

{% dd %}
See [Attackers Explorer](https://docs.datadoghq.com/security/application_security/security_signals/attacker-explorer/)
{% /dd %}

{% dt %}
flagged attackers
{% /dt %}

{% dd %}
IPs that send large amounts of attack traffic. We recommend reviewing and blocking Flagged IPs. Thresholds are not user-configurable.
{% /dd %}

{% dd %}
See [Attackers Explorer](https://docs.datadoghq.com/security/application_security/security_signals/attacker-explorer/)
{% /dd %}

{% dt %}
attacker fingerprint
{% /dt %}

{% dd %}
Identifiers computed from request characteristics to track an attacker across multiple requests.
{% /dd %}

{% dd %}
See [Attacker Fingerprint](https://docs.datadoghq.com/security/application_security/security_signals/attacker_fingerprint/)
{% /dd %}

{% dt %}
attacker cluster
{% /dt %}

{% dd %}
A set of attributes identifying an attacker across a distributed attack.
{% /dd %}

{% dd %}
See [Attacker Clustering](https://docs.datadoghq.com/security/application_security/security_signals/attacker_clustering/)
{% /dd %}

{% /dl %}

## Attacks and known vulnerabilities terms{% #attacks-and-known-vulnerabilities-terms %}

{% dl %}

{% dt %}
Open Web App and API Protection Project (OWASP)
{% /dt %}

{% dd %}
A nonprofit foundation with several projects to enhance web application security. OWASP is best known for the [OWASP Top 10](https://owasp.org/www-project-top-ten/), a broad consensus about the most critical security risks to web applications.
{% /dd %}

{% dt %}
Cross-Site Scripting (XSS)
{% /dt %}

{% dd %}
A type of injection attack in which malicious scripts are injected into otherwise benign and trusted websites.
{% /dd %}

{% dd %}
See [XSS on OWASP](https://owasp.org/www-community/attacks/xss/).
{% /dd %}

{% dt %}
Structured Query Language Injection (SQLi, SQL Injection)
{% /dt %}

{% dd %}
A type of injection attack in which a SQL query is executed via the input data from the client to the application. SQL commands are injected into data-plane input in order to affect the execution of predefined SQL commands. A successful SQL injection exploit can read sensitive data from the database, modify database data (Insert/Update/Delete), execute administration operations on the database (such as shutdown the DBMS), recover the content of a given file present on the DBMS file system, and in some cases issue commands to the operating system.
{% /dd %}

{% dd %}
**Related**: Cassandra Query Language Injection (CQLi), NoSQL Injection (NoSQLi) - Similar to SQLi but for the Cassandra Query Language and NoSQL.
{% /dd %}

{% dd %}
See [SQL Injection on OWASP](https://owasp.org/www-community/attacks/SQL_Injection).
{% /dd %}

{% dt %}
Server-Side Request Forgery (SSRF)
{% /dt %}

{% dd %}
A vulnerability where a web application fetches a remote resource without validating the user-supplied URL. It allows an attacker to coerce the application to send a crafted request to an unexpected destination, even when protected by a firewall, VPN, or another type of network access control list (ACL).
{% /dd %}

{% dd %}
See [Server-Side Request Forgery on OWASP](https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/).
{% /dd %}

{% dt %}
Local File Inclusion (LFI)
{% /dt %}

{% dd %}
A vulnerability that allows an attacker to include a file locally present on the server during the processing of the request. In most cases this allows the attacker to read sensitive information stored in files on the server. In more severe cases exploitation can lead to cross-site scripting or remote code execution.
{% /dd %}

{% dd %}
See [Testing for LFI on OWASP](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion).
{% /dd %}

{% dt %}
Remote File Inclusion (RFI)
{% /dt %}

{% dd %}
A vulnerability similar to Local File Inclusion, but allows an attacker to include a remote file during the processing of the request. The files used in Remote File Inclusion attacks most commonly contain malicious code for PHP, JSP, or similar technologies.
{% /dd %}

{% dt %}
Remote Code Execution (RCE)
{% /dt %}

{% dd %}
A vulnerability that allows an attacker to remotely execute code on a machine.
{% /dd %}

{% dt %}
Object-Graph Navigation Language Injection (OGNLi)
{% /dt %}

{% dd %}
A vulnerability that allows an attacker to execute their own OGNL expression in a Java application, most commonly leading to remote code execution.
{% /dd %}

{% dd %}
See [OGNLi in OWASP Top 10](https://owasp.org/www-project-top-ten/2017/A1_2017-Injection).
{% /dd %}

{% /dl %}

## Further reading{% #further-reading %}

- [How App and API Protection Works](https://docs.datadoghq.com/security/application_security/how-it-works)
- [App and API Protection](https://docs.datadoghq.com/security/application_security)
- [Accelerate security investigations with Datadog Threat Intelligence](https://www.datadoghq.com/blog/datadog-threat-intelligence/)
