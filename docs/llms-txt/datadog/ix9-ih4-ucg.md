# Source: https://docs.datadoghq.com/security/default_rules/ix9-ih4-ucg.md

---
title: Application Load Balancers should use HTTPS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Application Load Balancers should use
  HTTPS
---

# Application Load Balancers should use HTTPS

## Description{% #description %}

Use HTTPS to secure communication between your application client and an Elastic Load Balancer (ELB) listener.

## Rationale{% #rationale %}

Without an HTTPS listener, front-end connections are vulnerable to exploits, such as man-in-the-middle (MITM) attacks. Securing all communication between your application client and ELB listener ensures sensitive data is protected.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Create an HTTPS listener for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html) doc to learn how to create a listener that checks for connection requests.

### From the command line{% #from-the-command-line %}

1. Run `list-certificates` to retrieve the ARN of your SSL certificate. If you do not have an SSL certificate, follow the [Create or import an SSL/TLS certificate](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ssl-server-cert.html#create-certificate-acm) doc.

1. Run `create-listener` using the [ARN of the load balancer and SSL certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-listener.html).

   ```gdscript3
    aws elbv2 create-listener \
        --load-balancer-arn arn:aws:elasticloadbalancing:region:123456789012:loadbalancer/app/my-load-balancer/12ab3c456d7e8912 \
        --protocol HTTPS \
        --port 443 \
        --certificates CertificateArn=arn:aws:acm:region:123456789012:certificate/1abc0c41-bd73-5445-9ab9-123456a23456 \
        --ssl-policy ELBSecurityPolicy-2016-08 --default-actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:region:123456789012:targetgroup/my-targets/12ab3c456d7e8912
   ```
