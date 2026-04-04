# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/cookies-persistence.md

---
title: Cookies should not have a long expiration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Cookies should not have a long expiration
---

# Cookies should not have a long expiration

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/cookies-persistence`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [539](https://cwe.mitre.org/data/definitions/539.html)

## Description{% #description %}

Cookie should not persist for too long. If the computer that stores the cookie is attacked or breached, this can lead to a potential account compromise.

Cookies should not be stored too long and should not be used to store sensitive data (such as personal identifiable information).

#### Learn More{% #learn-more %}

- [Cookie JavaDoc](https://tomcat.apache.org/tomcat-5.5-doc/servletapi/javax/servlet/http/Cookie.html#setMaxAge%28int%29)
- [CWE-539: Use of Persistent Cookies Containing Sensitive Information](https://cwe.mitre.org/data/definitions/539.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class NotCompliant {
    public void setCookie(String field, String value) {
        Cookie cookie = new Cookie("field", value);

        // Set Cookie for a year
        cookie.setMaxAge(2592000);
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Compliant {
    public void setCookie(String field, String value) {
        Cookie cookie = new Cookie("field", value);

        // Set Cookie for a month
        cookie.setMaxAge(216000);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
