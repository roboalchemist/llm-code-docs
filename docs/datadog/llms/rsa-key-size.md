# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/rsa-key-size.md

---
title: Ensure RSA keys are large enough
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure RSA keys are large enough
---

# Ensure RSA keys are large enough

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/rsa-key-size`

**Language:** Ruby

**Severity:** Warning

**Category:** Security

**CWE**: [326](https://cwe.mitre.org/data/definitions/326.html)

## Description{% #description %}

This rule pertains to the size of RSA keys used in your Ruby applications. RSA is a widely used encryption algorithm and the size of the key is crucial for the security of the data it protects. If the key is too small, it can be easily cracked using modern computational power, exposing sensitive data to potential threats.

The importance of this rule cannot be overstated. In modern security standards, a minimum of 2048 bits is recommended for RSA keys. Using a key size less than this, such as 512 bits, can lead to vulnerabilities that can be exploited by attackers.

To adhere to good coding practices and avoid violating this rule, always ensure that the size of your RSA keys is at least 2048 bits. This can be done by initializing your RSA key with the value `2048` as shown in the compliant code example: `OpenSSL::PKey::RSA.new 2048`. Avoid initializing your RSA keys with smaller values such as `512` to prevent potential security risks.

## Arguments{% #arguments %}

- `min-length`: Minimum length for an RSA key. Default: 2048.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
OpenSSL::PKey::RSA.new 512
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
OpenSSL::PKey::RSA.new 2048
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
