# Source: https://docs.datadoghq.com/security/default_rules/def-000-4ph.md

---
title: Authentication route is not protected by AAP's ATO Detection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Authentication route is not protected
  by AAP's ATO Detection
---

# Authentication route is not protected by AAP's ATO Detection
 
## Description{% #description %}

This rule identifies when an authentication route is not protected from Account Takeover Attacks (ATO) by App & API Protection's ATO Detection.

An account takeover occurs when an attacker gains access to a user's account credentials and assumes control of the account. Datadog can detect and protect against common strategies implemented by attackers, such as **Credential Stuffing** or **Brute Forcing**. For more information on this works, see [ASM account takeover protection](https://docs.datadoghq.com/security/account_takeover_protection/#account-takeover-protection-overview).

## Rationale{% #rationale %}

This finding identifies authentication endpoints that are not instrumented to provide `business_logic.users.login.success` or `business_logic.users.login.failure` user activity events to Datadog, resulting in no security observability to detect the ATO attacks. [Review](https://app.datadoghq.com/security/appsec/business-logic) your instrumented business logic events.

## Remediation{% #remediation %}

- [Instrument your code](https://docs.datadoghq.com/security/account_takeover_protection/#instrumenting-your-production-login-endpoints) to enable Datadog ASM's ATO Detection on your login endpoints.
