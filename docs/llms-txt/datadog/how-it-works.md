# Source: https://docs.datadoghq.com/security/application_security/how-it-works.md

---
title: How App and API Protection Works in Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > App and API Protection > How App and API Protection
  Works in Datadog
---

# How App and API Protection Works in Datadog

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Datadog App and API Protection (AAP) provides observability into application and API-level attacks that aim to exploit vulnerabilities and abuse app business logic, and observability into any bad actors targeting your systems. AAP performs actions such as the following:

- Detects and monitors application and API-level attacks
- Flags traces containing attack attempts using APM data
- Highlights exposed services in security views (Software Catalog, Service Page, Traces)
- Identifies bad actors by collecting client IPs and user info
- Provides automatic threat pattern updates and security signals
- Supports built-in protection and attack qualification
- Offers visibility into API threats and attack details
- Helps identify and respond to vulnerabilities like Log4Shell

### Identify services exposed to application attacks{% #identify-services-exposed-to-application-attacks %}

Datadog App and API Protection Threat Management uses the information APM is already collecting to flag traces containing attack attempts. While APM collects a sample of your application traffic, enabling App and API Protection in the tracing library is necessary to effectively monitor and protect your services.

Services exposed to application attacks are highlighted directly in the security views embedded in APM ([Software Catalog](https://docs.datadoghq.com/tracing/software_catalog/#security-view), [Service Page](https://docs.datadoghq.com/tracing/services/service_page/#security), [Traces](https://docs.datadoghq.com/tracing/trace_explorer/trace_view/?tab=security#more-information)).

Datadog Threat Monitoring and Detection identifies bad actors by collecting client IP addresses, login account info (for example, user account/ID), and manually-added user tags on all requests.

{% alert level="info" %}
**1-Click Enablement**If your service is running with [an Agent with Remote Configuration enabled and a tracing library version that supports it](https://docs.datadoghq.com/agent/remote_config/#enabling-remote-configuration), you can [enable App and API Protection](https://app.datadoghq.com/security/configuration/asm/setup) from the Datadog UI without additional configuration of the Agent or tracing libraries.
{% /alert %}

## Compatibility{% #compatibility %}

App and API Protection uses the same libraries as APM, so you don't need to deploy and maintain another library. Steps to enable Datadog App and API Protection are specific to each runtime language. See the [App and API Protection setup guides](https://docs.datadoghq.com/security/application_security/setup/) to check if your language is supported.

## Serverless monitoring{% #serverless-monitoring %}

Datadog App and API Protection for AWS Lambda provides deep visibility into attackers targeting your functions. With distributed tracing providing a context-rich picture of the attack, you can assess the impact and remediate the threat effectively.

Read [Enabling App and API Protection for Serverless](https://docs.datadoghq.com/security/application_security/serverless/) for information on setting it up.

## Performance{% #performance %}

Datadog App and API Protection uses processes already contained in the Agent and APM, so there are negligible performance implications when using it.

When APM is enabled, the Datadog library generates distributed traces. Datadog App and API Protection flags security activity in traces by using known attack patterns. Correlation between the attack patterns and the execution context provided by the distributed trace triggers security signals based on detection rules.

{% image
   source="https://datadog-docs.imgix.net/images/security/application_security/How_Appsec_Works_June2023.79d85d9eb999e067c94548ebcba3098a.png?auto=format"
   alt="A diagram illustrates that the Datadog tracer library operates at the application service level and sends traces to the Datadog backend. The Datadog backend flags actionable security signals and sends a notification to the relevant application, such as PagerDuty, Jira or Slack." /%}

## Data sampling and retention{% #data-sampling-and-retention %}

In the tracing library, Datadog App and API Protection collects all traces that include security data. A default [retention filter](https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/) ensures the retention of all security-related traces in the Datadog platform.

Data for security traces is kept for 90 days. The underlying trace data is kept for 15 days.

## Data privacy{% #data-privacy %}

By default, App and API Protection collects information from security traces to help you understand why the request was flagged as suspicious. Before sending the data, App and API Protection scans it for patterns and keywords that indicate that the data is sensitive. If the data is deemed sensitive, it is replaced with a `<redacted>` flag. This indicates that the request was suspicious, but that the request data could not be collected because of data security concerns.

Here are some examples of data that is flagged as sensitive by default:

- `pwd`, `password`, `ipassword`, `pass_phrase`
- `secret`
- `key`, `api_key`, `private_key`, `public_key`
- `token`
- `consumer_id`, `consumer_key`, `consumer_secret`
- `sign`, `signed`, `signature`
- `bearer`
- `authorization`
- `BEGIN PRIVATE KEY`
- `ssh-rsa`

To configure the information redacted by App and API Protection, refer to the [data security configuration](https://docs.datadoghq.com/security/application_security/policies/library_configuration/#data-security-considerations)

## Threat detection methods{% #threat-detection-methods %}

Datadog uses multiple pattern sources, including the [OWASP ModSecurity Core Rule Set](https://owasp.org/www-project-modsecurity-core-rule-set/) to detect known threats and vulnerabilities in HTTP requests. When an HTTP request matches one of [the OOTB detection rules](https://docs.datadoghq.com/security/default_rules/?category=cat-application-security), a security signal is generated in Datadog.

**Automatic Threat Patterns Updates:** If your service is running with [an Agent with Remote Configuration enabled and a tracing library version that supports it](https://docs.datadoghq.com/agent/remote_config/#enabling-remote-configuration) , the threat patterns being used to monitor your service are automatically updated whenever Datadog publishes updates.

Security Signals are automatically created when Datadog detects meaningful attacks targeting your production services. It provides you with visibility on the attackers and the targeted services. You can set custom detection rules with thresholds to determine which attacks you want to be notified about.

## Built-in protection{% #built-in-protection %}

If your service is running [an Agent with Remote Configuration enabled and a tracing library version that supports it](https://docs.datadoghq.com/agent/guide/how_remote_config_works/), you can block attacks and attackers from the Datadog UI without additional configuration of the Agent or tracing libraries.

AAP Protect goes beyond Threat Detection and enables you to take blocking action to slow down attacks and attackers. Unlike perimeter WAFs that apply a broad range of rules to inspect traffic, AAP uses the full context of your applicationâits databases, frameworks, and programming languageâto narrowly apply the most efficient set of inspection rules.

AAP leverages the same [tracing libraries](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/) as Application Performance Monitoring (APM) to protect your applications against:

- **Attacks**: AAP's In-App WAF inspects all incoming traffic and uses pattern-matching to detect and block malicious traffic (security traces).
- **Attackers**: IP addresses and authenticated users that are launching attacks against your applications are detected from the insights collected by the libraries and flagged in Security Signals.

Security traces are blocked in real time by the Datadog tracing libraries. Blocks are saved in Datadog, automatically and securely fetched by the Datadog Agent, deployed in your infrastructure, and applied to your services. For details, read [How Remote Configuration Works](https://docs.datadoghq.com/agent/guide/how_remote_config_works/).

To start leveraging Protection capabilitiesâIn-App WAF, IP blocking, User blocking and moreâread [Protection](https://docs.datadoghq.com/security/application_security/).

## Attack attempt qualification{% #attack-attempt-qualification %}

Leveraging distributed tracing information, attacks attempts are qualified as safe, unknown, or harmful.

- Attack attempts qualified as safe cannot breach your application, for example, when a PHP injection attack targets a service written in Java.
- An unknown qualification is decided when there is not enough information to make a definitive judgement about the attack's probability of success.
- A harmful qualification is highlighted when there is evidence that a code level vulnerability has been found by the attacker.

## Threat monitoring coverage{% #threat-monitoring-coverage %}

Datadog App and API Protection includes over 100 attack signatures that help protect against [many different kinds of attacks](https://app.datadoghq.com/security/appsec/event-rules), including, but not limited to, the following categories:

- SQL injections
- Code injections
- Shell injections
- NoSQL injections
- Cross-Site Scripting (XSS)
- Server-side Request Forgery (SSRF)

## API security{% #api-security %}

{% alert level="info" %}
API security is in Preview.
{% /alert %}

Datadog App and API Protection provides visibility into threats targeting your APIs. Use the [Endpoints list](https://docs.datadoghq.com/software_catalog/endpoints/) in Software Catalog to monitor API health and performance metrics, where you can view attacks targeting your APIs. This view includes the attacker's IP and authentication information, as well as request headers showing details about how the attack was formed. Using both App and API Protection and API management, you can maintain a comprehensive view of your API attack surface, and respond to mitigate threats.

## How Datadog App and API Protection protects against Log4Shell{% #how-datadog-app-and-api-protection-protects-against-log4shell %}

Datadog App and API Protection identifies Log4j Log4Shell attack payloads and provides visibility into vulnerable apps that attempt to remotely load malicious code. When used in tandem with the rest of [Datadog's Cloud SIEM](https://docs.datadoghq.com/security/cloud_siem/), you can investigate to identify common post-exploitation activity, and proactively remediate potentially vulnerable Java web services acting as an attack vector.
