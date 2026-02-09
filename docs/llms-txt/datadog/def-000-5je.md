# Source: https://docs.datadoghq.com/security/default_rules/def-000-5je.md

---
title: >-
  Publicly Accessible EC2 instance has a critical vulnerability has access to
  Redis ElasticCache with no AUTH
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Publicly Accessible EC2 instance has a
  critical vulnerability has access to Redis ElasticCache with no AUTH
---

# Publicly Accessible EC2 instance has a critical vulnerability has access to Redis ElasticCache with no AUTH

## Description{% #description %}

A publicly accessible EC2 instance has one or more critical security vulnerabilities with access to Elasticcache with no auth.

Unpatched vulnerabilities can expose system weaknesses and create an entry point for attackers to gain unauthorized access to the host. This can lead to data breaches, unauthorized modifications, or control of the underlining system.

## Remediation{% #remediation %}

1. Review any associated vulnerability references or advisories.
1. Apply the appropriate patch based on remediation guidance. If no patch is available, apply compensating controls such as disabling or removal of the vulnerable component.
1. Assess whether this instance needs to be accessible from the internet. If not, restrict access to the instance.
