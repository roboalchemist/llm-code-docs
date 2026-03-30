# Source: https://docs.datadoghq.com/security/default_rules/def-000-pup.md

---
title: >-
  Classic Load Balancers should be configured to use defensive or strictest
  desync mitigation mode
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Classic Load Balancers should be
  configured to use defensive or strictest desync mitigation mode
---

# Classic Load Balancers should be configured to use defensive or strictest desync mitigation mode

## Description{% #description %}

This check verifies Classic Load Balancers are set to use either the defensive or strictest desync mitigation mode. HTTP desynchronization issues can lead to request smuggling, making applications vulnerable to request queue or cache poisoning. These vulnerabilities can, in turn, result in credential hijacking or the execution of unauthorized commands. Classic Load Balancers configured with the defensive or strictest desync mitigation mode help protect your application from security risks associated with HTTP desynchronization.

## Remediation{% #remediation %}

To change the desync mitigation mode for a Classic Load Balancer, refer to the [Modify desync mitigation mode in the User Guide for Classic Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-desync-mitigation-mode.html#update-desync-mitigation-mode).
