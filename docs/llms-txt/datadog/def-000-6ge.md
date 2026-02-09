# Source: https://docs.datadoghq.com/security/default_rules/def-000-6ge.md

---
title: API Gateways should be associated with a WAF Web ACL
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > API Gateways should be associated with
  a WAF Web ACL
---

# API Gateways should be associated with a WAF Web ACL
 
## Description{% #description %}

This check verifies if an AWS WAF web ACL is linked to an API Gateway stage. Failure occurs if a web ACL is not attached to a REST API Gateway stage.

AWS WAF serves as a web application firewall designed to safeguard web applications and APIs against attacks. It allows you to set up an ACL with rules that allow, block, or monitor web requests based on specified security rules and conditions. Ensure that your API Gateway stage is connected to an AWS WAF web ACL for added protection against malicious attacks.

## Remediation{% #remediation %}

To learn how to link an AWS WAF Regional web ACL with an existing API Gateway API stage using the API Gateway console, refer to the [Using AWS WAF to protect your APIs section in the API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-aws-waf.html).
