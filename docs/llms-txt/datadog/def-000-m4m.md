# Source: https://docs.datadoghq.com/security/default_rules/def-000-m4m.md

---
title: Improper collection of metadata on login requests
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Improper collection of metadata on
  login requests
---

# Improper collection of metadata on login requests
 
## Description{% #description %}

This authentication endpoint lacks metadata to effectively detect Account Takeover Attacks (ATO) attempts by App & API Protection.

An account takeover occurs when an attacker gains access to a user's account credentials and assumes control of the account. Datadog can detect and protect against common strategies implemented by attackers, such as **Credential Stuffing** or **Brute Forcing**. For more information on this works, see [ASM account takeover protection](https://docs.datadoghq.com/security/account_takeover_protection/#account-takeover-protection-overview).

## Rationale{% #rationale %}

For Datadog's ATO detection to work properly, the library has to compute fingerprints based on the user's original request. That means access to the IP of the user and every header from the original request. We detect improper header or IP propagation through the absence of common headers (`User-Agent` & `Accept-Encoding`) and by checking whether the request originates from a private IP (which may ocurr if the real IP address is not propagated with the `X-Forwarded-For` header).

## Remediation{% #remediation %}

Two options are available:

- (Recommended) Instrument the service that received the complete user request and have it record the login information returned by the authentication service. This would mean instrumenting an edge service rather than the actual authentication service; or
- Manually propagate the headers and the original IP to the service you instrumented by including them in the requests the upstream services perform to the service you instrumented. You can propagate the original client IP by sending it in a header called `X-Forwarded-For`
