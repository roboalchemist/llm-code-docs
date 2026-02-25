# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/hostname-verifier-true.md

---
title: HostnameVerifier should check certificates
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > HostnameVerifier should check certificates
---

# HostnameVerifier should check certificates

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/hostname-verifier-true`

**Language:** Java

**Severity:** Error

**Category:** Security

**CWE**: [295](https://cwe.mitre.org/data/definitions/295.html)

## Description{% #description %}

A `HostnameVerifier` implementation should never just return `true`.

#### Learn More{% #learn-more %}

- [HostnameVerifier that accept any signed certificates](https://find-sec-bugs.github.io/bugs.htm#WEAK_HOSTNAME_VERIFIER)
- [CWE-295: Improper Certificate Validation](https://cwe.mitre.org/data/definitions/295.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class AllHosts implements HostnameVerifier {
    public boolean verify(final String hostname, final SSLSession session) {
        return true;
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class AllHosts implements HostnameVerifier {
    public boolean verify(final String hostname, final SSLSession session) {
        if(isValidCertificate) {
            return true;
        }
        return false;
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
