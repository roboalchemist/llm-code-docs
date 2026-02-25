# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/unsafe-deserialization.md

---
title: Do not use unsafe deserialization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use unsafe deserialization
---

# Do not use unsafe deserialization

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/unsafe-deserialization`

**Language:** Ruby

**Severity:** Warning

**Category:** Security

**CWE**: [502](https://cwe.mitre.org/data/definitions/502.html)

## Description{% #description %}

This rule advises against the use of unsafe deserialization in Ruby, particularly with the `Marshal.load` method. Deserialization is the process of converting data from a binary or string format back into an object. However, if the data was tampered with, it could lead to arbitrary code execution when the data is deserialized.

This is important because it can lead to serious security vulnerabilities. An attacker could exploit the deserialization process to execute malicious code, alter program flow, or perform other harmful actions. This is particularly dangerous if your application runs with high privileges.

To avoid this, use safe deserialization methods. Instead of using `Marshal.load`, consider using JSON or YAML for serialization and deserialization, as they are safer. For example, you could use `JSON.parse(data)` or `YAML.load(data)` instead. Additionally, always ensure that the data you are deserializing comes from a trusted source.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
obj = Marshal.load(data)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
