# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/unvalidated-redirect.md

---
title: Do not use unvalidated request
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use unvalidated request
---

# Do not use unvalidated request

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/unvalidated-redirect`

**Language:** Java

**Severity:** Error

**Category:** Security

**CWE**: [601](https://cwe.mitre.org/data/definitions/601.html)

## Description{% #description %}

Do not use unvalidated redirect. Always check the redirect URL coming from a request.

#### Learn More{% #learn-more %}

- [Unvalidated Redirect](https://find-sec-bugs.github.io/bugs.htm#UNVALIDATED_REDIRECT)
- [CWE-601 - URL Redirection to Untrusted Site](https://cwe.mitre.org/data/definitions/601.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class MyClass {
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        resp.sendRedirect(req.getParameter("redirectUrl"));
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class MyClass {
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        resp.sendRedirect(validateUrl(req.getParameter("redirectUrl")));
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
