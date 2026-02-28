# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-security/avoid-sha1.md

---
title: Avoid sha1
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid sha1
---

# Avoid sha1

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-security/avoid-sha1`

**Language:** Swift

**Severity:** Warning

**Category:** Security

**CWE**: [328](https://cwe.mitre.org/data/definitions/328.html)

## Description{% #description %}

This rule flags the usage of the SHA-1 hashing algorithm in Swift code. SHA-1 is considered cryptographically weak and vulnerable to collision attacks, which can compromise data integrity and security. Using SHA-1 can expose applications to potential exploits, especially in security-sensitive contexts like password hashing, digital signatures, or data verification.

To ensure stronger security, developers should avoid calling `.sha1()` and instead use more secure hashing algorithms such as SHA-256. For example, replacing `message.sha1()` with `message.sha256()` significantly improves resistance against cryptographic attacks. Adopting modern and robust algorithms helps maintain the confidentiality and integrity of data.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
let digest = message.sha1();
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
let digest = message.sha256();
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
