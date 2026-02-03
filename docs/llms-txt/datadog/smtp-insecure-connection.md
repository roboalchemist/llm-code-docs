# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/smtp-insecure-connection.md

---
title: SMTP server identify must be enforced
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > SMTP server identify must be enforced
---

# SMTP server identify must be enforced

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/smtp-insecure-connection`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [297](https://cwe.mitre.org/data/definitions/297.html)

## Description{% #description %}

When a program establish an SMTP connection, server identity should be checked.

#### Learn More{% #learn-more %}

- [CWE-297: Improper Validation of Certificate with Host Mismatch](https://cwe.mitre.org/data/definitions/297.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class NotCompliant {
    public void myMethod() {
        Email email = new SimpleEmail();
        email.setHostName("smtp.servermail.com");
        email.setSmtpPort(465);
        email.setAuthenticator(new DefaultAuthenticator(username, password));
        // email.setSSLOnConnect(true);
        email.setFrom("user@gmail.com");
        email.setSubject("TestMail");
        email.setMsg("This is a test mail ... :-)");
        email.addTo("foo@bar.com");
        email.send();
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Compliant {
    public void myMethod() {
        Email email = new SimpleEmail();
        email.setHostName("smtp.servermail.com");
        email.setSmtpPort(465);
        email.setAuthenticator(new DefaultAuthenticator(username, password));
        email.setSSLOnConnect(true);
        email.setFrom("user@gmail.com");
        email.setSubject("TestMail");
        email.setMsg("This is a test mail ... :-)");
        email.addTo("foo@bar.com");
        email.setSSLCheckServerIdentity(true);
        email.send();
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 