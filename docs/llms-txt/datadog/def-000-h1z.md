# Source: https://docs.datadoghq.com/security/default_rules/def-000-h1z.md

---
title: User has used a disposable email address
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > User has used a disposable email
  address
---

# User has used a disposable email address
 
## Goal{% #goal %}

Detect when a user is using a disposable email address.

## Strategy{% #strategy %}

Monitor user email address in login events and detects whenever the domain is known to provide a disposable email service.

## Triage and response{% #triage-and-response %}

Investigate the activity of the user with ID `{{@usr.id}}` to determine if this is a throwaway account exploited to misuse your services.
