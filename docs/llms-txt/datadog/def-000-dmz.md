# Source: https://docs.datadoghq.com/security/default_rules/def-000-dmz.md

---
title: Route vulnerable to Server-Side Request Forgery (SSRF)
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Route vulnerable to Server-Side Request
  Forgery (SSRF)
---

# Route vulnerable to Server-Side Request Forgery (SSRF)
 
## Description{% #description %}

An API endpoint was found [vulnerable to SSRF attacks](https://app.datadoghq.com/security/appsec/vm/code?query=status%3A%28Open%20OR%20%22In%20progress%22%29%20type%3A%22Server-Side%20Request%20Forgery%20%28SSRF%29%22&column=score&detection=runtime&order=desc). Server-Side Request Forgery (SSRF) is a web security vulnerability that allows an attacker to deceive the application and make requests to an unintended location.

In case the API does not properly prevent calling arbitrary web resources, attackers might steal sensitive information or perform unauthorized actions

## Rationale{% #rationale %}

This finding works by identifying an API that contains code vulnerabilities permitting full or partial control of URLs used to fetch a remote resource.

## Remediation{% #remediation %}

- Maintain a URL allowlist to validate the usage of trusted remote resources only
