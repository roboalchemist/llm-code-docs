# Source: https://docs.datadoghq.com/security/default_rules/def-000-tml.md

---
title: >-
  Publicly Accessible EC2 instance has privileged role and a critical
  vulnerability
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Publicly Accessible EC2 instance has
  privileged role and a critical vulnerability
---

# Publicly Accessible EC2 instance has privileged role and a critical vulnerability

## Description{% #description %}

A publicly accessible EC2 instance has one or more critical severity vulnerabilities.

A compromise of this EC2 instance could lead to potential abuse of the privileges associated with the instance, and could lead to unauthorized access to the account and other resources the instance has access to.

Unpatched vulnerabilities can expose system weaknesses and create an entry point for attackers to gain unauthorized access to the host. This can lead to data breaches, unauthorized modifications, or control of the underlining system.

## Remediation{% #remediation %}

1. Review any associated vulnerability references or advisories.
1. Review the level of access and privileges associated with the EC2 instance and scope them down to the minimum required.
1. Apply the appropriate patch based on remediation guidance. If no patch is available, apply compensating controls such as disabling or removal of the vulnerable component.
1. Assess whether this instance needs to be accessible from the internet. If not, restrict access to the instance.
