# Source: https://docs.datadoghq.com/security/default_rules/vn4-vpi-u7q.md

---
title: Load Balancers should use the latest security policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Load Balancers should use the latest
  security policy
---

# Load Balancers should use the latest security policy

## Description{% #description %}

Secure your Amazon Application Load Balancer (ALB) with the latest predefined AWS security policy.

## Rationale{% #rationale %}

Insecure or deprecated security policies can expose the client and the load balancer to various SSL/TLS vulnerabilities.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Update security policy](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-update-certificates.html#update-security-policy) docs to learn how to update your HTTPS listener with the latest security policy.

### From the command line{% #from-the-command-line %}

Run `modify-listener` with the [ARN of the listener and the recommended SSL policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-listener.html).

```gdscript3
aws elbv2 create-listener
    --load-balancer-arn <insert-lb-arn> \
    --ssl-policy <insert-policy-name> --default-actions <insert-actions>
```

Review the [Security policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies) docs for Amazon-recommended security policies.
