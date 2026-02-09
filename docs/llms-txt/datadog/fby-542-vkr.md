# Source: https://docs.datadoghq.com/security/default_rules/fby-542-vkr.md

---
title: Application Load Balancers should have Access logging enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Application Load Balancers should have
  Access logging enabled
---

# Application Load Balancers should have Access logging enabled
 
## Description{% #description %}

Enable Access Logging for your Amazon Application Load Balancers (ALBs).

## Rationale{% #rationale %}

Logs contain the time a request was received, a client's IP address, latencies, request paths, and server responses. You can use this information to analyze traffic patterns and troubleshoot issues.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the AWS [Enable access logging](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html#enable-access-logging) documentation to enable access logging using the console.

### From the command line{% #from-the-command-line %}

Follow the AWS [Enable access logging](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html#enable-access-logging) documentation to enable access logging using the AWS CLI.
