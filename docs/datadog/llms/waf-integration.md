# Source: https://docs.datadoghq.com/security/application_security/waf-integration.md

---
title: WAF Integrations
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > App and API Protection > WAF Integrations
---

# WAF Integrations

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

Protecting web applications and APIs requires a multi-layered approach that combines in-app monitoring and perimeter defenses. These complementary strategies enable you to have a *defense-in-depth* App and API Protection approach that leverages AWS Web Application Firewall (WAF) as the first line of defense, followed by Exploit Prevention for blocking attacks that slip by the WAF.

For details on how Exploit Prevention differs from In-App WAF, see [Exploit Prevention vs. In-App WAF](https://docs.datadoghq.com/security/application_security/#exploit-prevention-vs-in-app-waf).

### In-app monitoring: deep visibility with distributed tracing{% #in-app-monitoring-deep-visibility-with-distributed-tracing %}

At the application level, Datadog AAP leverages distributed tracing to monitor microservices in real time. The AAP approach provides detailed, context-rich insights into the behavior of requests as they traverse various services. These insights detect sophisticated threats such as:

- SQL Injection (SQLi) and Local File Inclusion (LFI) attempts.
- Application logic abuse, such as bypassing business rules or exploiting edge cases.
- Misuse of exposed endpoints.

### Perimeter defense: blocking threats at the edge with AWS WAF{% #perimeter-defense-blocking-threats-at-the-edge-with-aws-waf %}

At the perimeter, AWS Web Application Firewall (WAF) acts as the first line of defense, filtering traffic before it reaches the application. These solutions are essential for blocking:

- Large-scale botnet attacks or Distributed Denial of Service (DDoS) attacks.
- Malicious bots attempting credential stuffing or scraping.

### The importance of contextual, adaptive protection{% #the-importance-of-contextual-adaptive-protection %}

Depending on the nature of the threat, protection controls should be applied at the appropriate layer: either in-app or at the perimeter. For example:

- Perimeter protection use case: Blocking malicious IPs or volumetric attacks that can be mitigated efficiently at the network edge.
- In-app protection use case: Detecting and blocking vulnerability exploits, abuse of business logic, or subtle anomalies in API usage.

This layered approach ensures threats are neutralized as early as possible without sacrificing the precision needed to protect legitimate traffic.

## AWS WAF integration with AAP{% #aws-waf-integration-with-aap %}

There are two main use cases supported with this [integration](https://app.datadoghq.com/security/appsec/protection?use-case=amazon_waf):

1. Gain visibility of AWS WAF actions in Datadog AAP. For example:

   1. Metrics such as total requests allowed vs. blocked by the AWS WAF.
   1. Drill down and view individual AWS WAF logs (requires you to [ingest AWS WAF logs into Datadog](https://docs.datadoghq.com/integrations/amazon_waf/#log-collection)).
   1. How AWS WAF inspected the request: rules that were applied and the decision made (allow, block, or count).
Important alert (level: info): AAP converts AWS WAF logs into AAP Traces, enabling you to view application activity (traces) and AWS WAF activity (logs converted to AAP traces) in the AAP Trace Explorer.
1. Leverage AWS WAF to block attackers:

   1. Connect your AWS WAF IP set(s) with Datadog AAP. You can use an existing set or create a new one. Datadog will add blocked IP addresses to this IP set. You can block attackers from AAP [Signals](https://app.datadoghq.com/security/appsec/signals?query=@workflow.rule.type:%22Application%20Security%22) or [Traces](https://app.datadoghq.com/security/appsec/traces) explorers.

## Further reading{% #further-reading %}

- [Monitor AWS WAF activity with Datadog](https://www.datadoghq.com/blog/aws-waf-datadog/)
