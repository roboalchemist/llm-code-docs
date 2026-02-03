# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/no-http.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/apex-security/no-http.md

---
title: Avoid HTTP url
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid HTTP url
---

# Avoid HTTP url

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `apex-security/no-http`

**Language:** Apex

**Severity:** Warning

**Category:** Security

**CWE**: [319](https://cwe.mitre.org/data/definitions/319.html)

## Description{% #description %}

This rule flags the use of HTTP URLs in Apex code. Using HTTP instead of HTTPS can expose data transmitted between the client and server to interception or tampering, leading to potential security vulnerabilities. Ensuring URLs use HTTPS helps protect sensitive information by encrypting the communication channel.

To comply with this rule, always use HTTPS URLs when making network calls or referencing external resources. For example, instead of `String url = 'http://example.com/api';`, use `String url = 'https://example.com/api';`. Additionally, review and update any hardcoded URLs in your codebase to ensure they use HTTPS to maintain secure communication standards.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```
public class AccountHelper {

    public void foo() {
        String foo = 'http://subdomain.salesforce.com/something';
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```
public class AccountHelper {

    public void foo() {
        String foo = 'https://subdomain.salesforce.com/something';
        String sanitizedUrl = url.replace('http://', 'https://');
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 