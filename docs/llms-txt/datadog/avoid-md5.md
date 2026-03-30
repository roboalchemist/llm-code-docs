# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-security/avoid-md5.md

---
title: Avoid md5
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid md5
---

# Avoid md5

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-security/avoid-md5`

**Language:** Swift

**Severity:** Warning

**Category:** Security

**CWE**: [328](https://cwe.mitre.org/data/definitions/328.html)

## Description{% #description %}

This rule flags the use of the MD5 hashing algorithm in Swift code. MD5 is considered cryptographically broken and unsuitable for further use due to its vulnerability to collision attacks, where two different inputs produce the same hash output. Using MD5 can compromise the security and integrity of data, especially in contexts like password hashing, digital signatures, or data verification.

To maintain strong security standards, developers should avoid MD5 and instead use more secure hashing algorithms such as SHA-256. These algorithms provide better resistance against collision and preimage attacks, ensuring the integrity and authenticity of hashed data. For example, replacing `message.md5()` with `message.sha256()` significantly improves security.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
let digest = message.md5();
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
let digest = message.sha256();
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
