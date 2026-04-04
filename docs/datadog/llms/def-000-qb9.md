# Source: https://docs.datadoghq.com/security/default_rules/def-000-qb9.md

---
title: >-
  Publicly accessible Google VM instance contains critical vulnerabilities found
  in CISA KEV with greater than 15 days exposure time
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Publicly accessible Google VM instance
  contains critical vulnerabilities found in CISA KEV with greater than 15 days
  exposure time
---

# Publicly accessible Google VM instance contains critical vulnerabilities found in CISA KEV with greater than 15 days exposure time

## Description{% #description %}

Unpatched vulnerabilities can increase the likelihood of exposing system weaknesses creating an entry point for attackers to gain unauthorized access to the host. This can lead to data breaches, unauthorized modifications, or control of the underlining system.

## Remediation{% #remediation %}

1. Review any associated vulnerability references or advisories.
1. Apply the appropriate patch based on remediation guidance. If no patch is available, apply compensating controls such as disabling or removal of the vulnerable component.
1. Assess whether this instance needs to be accessible from the internet. If not, restrict access to the instance.
