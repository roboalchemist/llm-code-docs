# Source: https://docs.datadoghq.com/security/default_rules/def-000-a4s.md

---
title: Unauthenticated route write using predictable IDs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Unauthenticated route write using
  predictable IDs
---

# Unauthenticated route write using predictable IDs

## Description{% #description %}

The API accepts predictable identifiers (IDs) without any authentication mechanism. Attackers can leverage this by guessing valid identifiers, to steal sensitive information or perform unauthorized actions.

### What are predictable identifiers?{% #what-are-predictable-identifiers %}

Predictable identifiers pose a security vulnerability in web attacks because they allow attackers to guess or manipulate these identifiers to gain unauthorized access to or control over a resource. For example, if an endpoint is designed to answer to:

- `GET api/v1/user?id=1`
- `GET api/v1/user?id=2`
- `GET api/v1/user?id=3`

An attacker might infer that user IDs are sequential, and can be brute-forced.

## Rationale{% #rationale %}

This finding works by identifying an API that:

- Lacks an [authentication mechanism](https://docs.datadoghq.com/security/application_security/api-inventory/#endpoint-authentication).
- Accepts a numeric user ID parameter within a limited positive integer range.

## Remediation{% #remediation %}

- Validate that the code isn't expecting the user to be authenticated to have access to this resource (AuthN). In case this API it is in fact authenticated, ensure your code is [instrumented correctly](https://docs.datadoghq.com/security/application_security/how-it-works/add-user-info). Datadog auto-instruments many event types, [review](https://app.datadoghq.com/security/appsec/business-logic) your instrumented business logic events.
- Validate that the ID isn't guessable, or that it can't be used to tamper with data. You can use universally unique identifiers (UUIDs) which is a 128-bit number represented as a 36-character string unlikely to be guessed or brute-forced.

JAVA example:

```java
import java.util.UUID;

public class User {
    private String userId;

    public User() {
        this.userId = UUID.randomUUID().toString();
    }

}
```

- Make sure you enforce authorization to resources so that only authorized users can perform the action (AuthZ). Consider the different patterns that are usually followed such as:
  - Role-Based Access Control (RBAC), which is a model that grants resource access to users based on their assigned role. For example, users with the role ADMIN can access the app administrator panel.
  - Attribute-Based Access Control (ABAC), which instead relies on attributes of the user to evaluate. This is a more generic case of the previous method, since the role can be thought of as an attribute.
- Set up rate-limiting using a [detection rule](https://docs.datadoghq.com/security/application_security/policies/custom_rules/#business-logic-abuse-detection-rule) on this API.

### References{% #references %}

| Reference                                                                                                            | Description                                                                             |
| -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| [OWASP - Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) | Authentication Cheat Sheet: guidance on the best practices in the authentication area.  |
| [OWASP - Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)   | Authorization Cheat Sheet: guidance on the best practices to implement access controls. |
