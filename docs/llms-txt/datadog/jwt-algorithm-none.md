# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/jwt-algorithm-none.md

---
title: Ensure JWT use an algorithm
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure JWT use an algorithm
---

# Ensure JWT use an algorithm

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/jwt-algorithm-none`

**Language:** Ruby

**Severity:** Warning

**Category:** Security

**CWE**: [327](https://cwe.mitre.org/data/definitions/327.html)

## Description{% #description %}

The rule "Ensure JWT use an algorithm" is important because it checks whether your JSON Web Tokens (JWT) are using a secure encryption algorithm. JWT is a compact, URL-safe means of representing claims to be transferred between two parties. However, if a JWT is encoded without a secure algorithm, it can be easily manipulated and decoded, compromising the security of the data it carries.

The 'none' algorithm is a security vulnerability as it allows a token to be validated without any signature. This means anyone can create a valid token.

To avoid this, always specify a secure algorithm when encoding a JWT. For instance, 'HS256' is a commonly used, secure algorithm. In Ruby, when using the `JWT.encode` method, the third parameter should be a secure algorithm, such as 'HS256'. For example: `jwt_token = JWT.encode content, nil, 'HS256'`. Never use 'none' as the algorithm. This will ensure the integrity and confidentiality of your JWTs.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
jwt_token = JWT.encode content, nil, 'none'
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
jwt_token = JWT.encode content, nil, 'HS256'
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 