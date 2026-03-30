# Source: https://docs.datadoghq.com/security/default_rules/def-000-7to.md

---
title: >-
  Application Load Balancers should be configured to use defensive or strictest
  desync mitigation mode
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Application Load Balancers should be
  configured to use defensive or strictest desync mitigation mode
---

# Application Load Balancers should be configured to use defensive or strictest desync mitigation mode

## Description{% #description %}

This check verifies whether an Application Load Balancer is set to use either the defensive or strictest desync mitigation mode. The verification is considered unsuccessful if the Application Load Balancer is not configured with one of these modes.

HTTP desynchronization issues can result in request smuggling, exposing applications to vulnerabilities such as request queue or cache poisoning. These vulnerabilities can, in turn, lead to credential stuffing or the execution of unauthorized commands. By configuring your Application Load Balancer with either the defensive or strictest desync mitigation mode, you can safeguard your application from security risks associated with HTTP desynchronization.

## Remediation{% #remediation %}

To change the desync mitigation mode for an Application Load Balancer, refer to the [Desync Mitigation Mode section in the Application Load Balancers User Guide].
