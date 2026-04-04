# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/message-digest-custom.md

---
title: Do not use custom digest
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use custom digest
---

# Do not use custom digest

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/message-digest-custom`

**Language:** Java

**Severity:** Notice

**Category:** Security

**CWE**: [328](https://cwe.mitre.org/data/definitions/328.html)

## Description{% #description %}

Avoid custom digest. Datadog recommends using existing digests that are proven to be secure. [NIST](https://csrc.nist.gov/projects/hash-functions) recommends the use of SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, or SHA-512/256.

#### Learn More{% #learn-more %}

- [Hash functions from NIST](https://csrc.nist.gov/projects/hash-functions)
- [Message digest is custom](https://find-sec-bugs.github.io/bugs.htm#CUSTOM_MESSAGE_DIGEST)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class MyProprietaryMessageDigest extends MessageDigest {

    @Override
    protected byte[] engineDigest() {
        // Do not use your own digest
        return null;
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class UseExistingDigest {

    protected void usingDigest {
        // instead of defining your own digest, use existing ones
        MessageDigest sha256Digest = MessageDigest.getInstance("SHA256");
        sha256Digest.update(password.getBytes());
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
