# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/jwt-no-verify.md

---
title: Ensure JWT are verified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure JWT are verified
---

# Ensure JWT are verified

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/jwt-no-verify`

**Language:** Ruby

**Severity:** Warning

**Category:** Security

**CWE**: [345](https://cwe.mitre.org/data/definitions/345.html)

## Description{% #description %}

The rule requires that JSON Web Tokens (JWT) should always be verified in Ruby applications. Verification is a crucial security measure that ensures the authenticity of the JWT. If a JWT is not verified, it could be tampered with or manipulated, leading to potential security risks such as unauthorized access or data leakage.

This rule is essential because it directly relates to the security of your application. JWTs are often used to store sensitive information and are used for authentication and authorization purposes. If they are not correctly verified, it could lead to serious security breaches. Therefore, it's crucial to always verify the JWT to ensure that it hasn't been tampered with and is from a trusted source.

To avoid violating this rule, always include the `true` flag when decoding a JWT to ensure that it is verified. For example, use `JWT.decode raw_token, secret, true, { algorithm: 'HS256' }`. The `true` flag indicates that the JWT should be verified. Never set this flag to `false` as it will skip the verification process, which could lead to security vulnerabilities.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
jwt_token = JWT.decode raw_token, secret, false, { algorithm: 'HS256' }
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
jwt_token = JWT.decode raw_token, secret, true, { algorithm: 'HS256' }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
