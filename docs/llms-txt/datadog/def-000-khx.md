# Source: https://docs.datadoghq.com/security/default_rules/def-000-khx.md

---
title: >-
  Classic Load Balancers with SSL/HTTPS listeners should use a certificate
  issued by AWS Certificate Manager
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Classic Load Balancers with SSL/HTTPS
  listeners should use a certificate issued by AWS Certificate Manager
---

# Classic Load Balancers with SSL/HTTPS listeners should use a certificate issued by AWS Certificate Manager
 
## Description{% #description %}

This control ensures that the Classic Load Balancer leverages HTTPS/SSL certificates issued by AWS Certificate Manager (ACM). The control fails if a Classic Load Balancer is configured to use an HTTPS/SSL listener but does not use an ACM-provided certificate. You can create a certificate either through ACM itself or by using a tool that supports the SSL and TLS protocols, such as OpenSSL. Security Hub recommends using ACM to generate or import certificates for your load balancer. ACM integrates seamlessly with Classic Load Balancers, allowing you to deploy the certificate directly onto your load balancer. Additionally, it is advisable to enable automatic renewal for these certificates.

## Remediation{% #remediation %}

For details on associating an ACM SSL/TLS certificate with a Classic Load Balancer, refer to the AWS Knowledge Center article [How can I associate an ACM SSL/TLS certificate with a Classic, Application, or Network Load Balancer](https://repost.aws/knowledge-center/associate-acm-certificate-alb-nlb)?
