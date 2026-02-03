# Source: https://docs.datadoghq.com/security/default_rules/def-000-mu3.md

---
title: Authenticated route returns sensitive data
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Authenticated route returns sensitive
  data
---

# Authenticated route returns sensitive data
 
## Description{% #description %}

The API allows authenticated users to access sensitive data, which may not be intended.

### What are considered sensitive data?{% #what-are-considered-sensitive-data %}

Sensitive data is information that, if inadvertently disclosed, could have significant consequences for the data subject. Sensitive data can encompass a wide range of information, including:

- Personally identifiable information (PII), including email, email address, religion, or place of residence.
- Financial information, which includes credit cards or bank account numbers.
- Health information, covering medical records or insurance information.
- Government information, which includes social security information or other government related data.
- Proprietary information, which includes secrets or intellectual property (IP),

## Rationale{% #rationale %}

This finding works by identifying an API that replies with or accepts requests containing sensitive data. While this isn't inherently problematic, inadequate security controls could lead to data leaks.

## Remediation{% #remediation %}

- Make sure you enforce authorization to resources so that only authorized users can perform the action (AuthZ). Consider the different patterns that are usually followed such as:
  - Role-Based Access Control (RBAC), which is a model that grants resource access to users based on their assigned role. For example, users with the role ADMIN can access the app administrator panel.
  - Attribute-Based Access Control (ABAC), instead relies on attributes of the user to evaluate, this is a more generic case of the previous method since the role can be thought of as an attribute.
- Validate whether the API is intended to return sensitive data.

### References{% #references %}

| Reference                                                                                                          | Description                                                                             |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| [OWASP - Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | Authorization Cheat Sheet: guidance on the best practices to implement access controls. |
