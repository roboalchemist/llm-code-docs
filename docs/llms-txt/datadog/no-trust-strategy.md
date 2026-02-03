# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/no-trust-strategy.md

---
title: Avoid TrustStrategies that trust certificates blindly
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid TrustStrategies that trust certificates blindly
---

# Avoid TrustStrategies that trust certificates blindly

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/no-trust-strategy`

**Language:** Java

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

This rule flags the use of `TrustStrategy` implementations such as `TrustSelfSignedStrategy` and `TrustAllStrategy` that accept certificates without proper validation. These strategies inherently trust certificates blindly, which undermines the security guarantees of SSL/TLS connections and exposes applications to man-in-the-middle attacks.

Using such TrustStrategies is dangerous because it bypasses critical certificate verification steps, allowing potentially untrusted or malicious certificates to be accepted. This can lead to sensitive data exposure, unauthorized access, and other security vulnerabilities in your application.

To comply with this rule, avoid using TrustStrategies that indiscriminately trust certificates. Instead, ensure that your SSLContext is configured with proper trust material that enforces rigorous certificate validation.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
import org.apache.http.conn.ssl.TrustSelfSignedStrategy;
import org.apache.http.conn.ssl.TrustAllStrategy;

public class ContextMaker {
    public static SSLContext makeSelfSigned() {
        return SSLContext.custom().loadTrustMaterial(null, new TrustSelfSignedStrategy()).build();
    }

    public static SSLContext makeAll() {
        TrustStrategy strategy = new TrustAllStrategy();
        return SSLContext.custom().loadTrustMaterial(null, strategy).build();
    }

    public static SSLContext makeSelfSignedFullName() {
        return SSLContext.custom().loadTrustMaterial(null, new org.apache.http.conn.ssl.TrustSelfSignedStrategy()).build();
    }

}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 