# Source: https://docs.datadoghq.com/security/default_rules/def-000-ycc.md

---
title: Unauthenticated route with SQL injection vulnerability
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Unauthenticated route with SQL
  injection vulnerability
---

# Unauthenticated route with SQL injection vulnerability

## Description{% #description %}

Unauthenticated users have access to an API that's performing [SQL queries using user controlled parameters](https://app.datadoghq.com/security/appsec/vm/code?query=status%3A%28Open%20OR%20%22In%20progress%22%29%20type%3A%22SQL%20Injection%22&column=score&detection=runtime&order=desc).

An SQL injection attack consists of the insertion or "injection" of a SQL query via the input data from the client to the application.

In case the API does not sanitize parameters correctly, attackers might interact with the database and steal information.

## Rationale{% #rationale %}

This finding works by identifying an API that lacks an authentication mechanism and contains code vulnerabilities permitting full or partial control of database query parameters.

## Remediation{% #remediation %}

- Use of SQL prepared statements
- Avoid generating SQL queries using user parameters without sanitization
- Implement authentication to prevent non-intended users interaction with the database
