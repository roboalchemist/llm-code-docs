# Source: https://docs.datadoghq.com/security/default_rules/31q-rfg-uiu.md

---
title: Classic Load Balancer listener should use a secure configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Classic Load Balancer listener should
  use a secure configuration
---

# Classic Load Balancer listener should use a secure configuration

## Description{% #description %}

Use a secure protocol and cipher to protect communication between the client and your Classic Elastic Load Balancers (ELBs). TLS 1.0 and 1.1 are vulnerable to attacks due to multiple insecurities, for this reason we recommend the use of `ELBSecurityPolicy-TLS-1-2-2017-01` which authorizes TLS 1.2.

## Rationale{% #rationale %}

Insecure communication channels increase the risk of attacks, such as man-in-the-middle, downgrade attacks, and sensitive data breaches. It is recommended to configure listeners to use HTTPS, or SSL, and `ELBSecurityPolicy-TLS-1-2-2017-01`, or a custom policy with an equivalent or more secure [configuration](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html). TLS on port 443 will generate a `pass` condition for this rule only if a secure policy is attached to the listener.

### Protocol and cipher details{% #protocol-and-cipher-details %}

This configuration check tests for a listener configured using HTTPS, SSL, or TLS on port 443, as well as for the absence of [ciphers](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-ssl-security-policy.html) and [protocols](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html) for secure listener configurations that are not recommended by AWS.

## Remediation{% #remediation %}

It is recommended to modify listeners configured to use TLS on port 443, to HTTPS on port 443, and select a secure policy.

### From the console{% #from-the-console %}

1. Follow the [Create an HTTPS/SSL load balancer using the console](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-create-https-ssl-load-balancer.html#create-https-lb-console) documentation to learn how to create an HTTPS/SSL load balancer in the AWS console.
1. Follow the [Update the SSL negotiation configuration using the console](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ssl-config-update.html#ssl-config-update-console) documentation to apply `ELBSecurityPolicy-TLS-1-2-2017-01` or a Custom Security Policy that is as or more secure.

### From the command line{% #from-the-command-line %}

1. Follow the [Create an HTTPS/SSL load balancer using the AWS CLI](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-create-https-ssl-load-balancer.html#create-https-lb-clt) documentation to learn how to create an HTTPS/SSL load balancer in the AWS command line.
1. Follow the [Update the SSL negotiation configuration using the console](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ssl-config-update.html#ssl-config-update-cli) documentation to apply `ELBSecurityPolicy-TLS-1-2-2017-01` or a Custom Security Policy that is as or more secure.
