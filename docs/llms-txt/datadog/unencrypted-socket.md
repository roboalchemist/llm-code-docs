# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/unencrypted-socket.md

---
title: Use of socket on HTTP port
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use of socket on HTTP port
---

# Use of socket on HTTP port

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/unencrypted-socket`

**Language:** Java

**Severity:** Error

**Category:** Security

**CWE**: [319](https://cwe.mitre.org/data/definitions/319.html)

## Description{% #description %}

Do not initiate socket on unencrypted ports. Use secure alternatives.

#### Learn More{% #learn-more %}

- [CWE-319: Cleartext Transmission of Sensitive Information](https://cwe.mitre.org/data/definitions/319.html)
- [Use of Unencrypted Socket](https://find-sec-bugs.github.io/bugs.htm#UNENCRYPTED_SOCKET)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Class {

    public void test(){
        Socket soc = new Socket("www.google.com",80);
    }

}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Class {

    public void test(){
        Socket soc = new Socket("www.google.com",443);
    }

}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 