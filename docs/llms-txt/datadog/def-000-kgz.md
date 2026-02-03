# Source: https://docs.datadoghq.com/security/default_rules/def-000-kgz.md

---
title: WAF web ACLs should have at least one rule or rule group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > WAF web ACLs should have at least one
  rule or rule group
---

# WAF web ACLs should have at least one rule or rule group
 
## Description{% #description %}

This control verifies that an AWS WAFV2 web access control list (web ACL) includes at least one rule or rule group. The control is considered non-compliant if a web ACL lacks any rules or rule groups.

A web ACL provides detailed control over all HTTP(S) web requests to your protected resource. It should include a set of rules and rule groups that examine and manage web requests. If a web ACL is empty, web traffic might pass through without being inspected or managed by AWS WAF, depending on the default action.

Please note that AWS WAF Classic ACLs are not evaluated by this control.

## Remediation{% #remediation %}

For guidance on adding rules or rule groups to WAFV2 web ACLs, please refer to the [Editing a web ACL ](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-editing.html)section in the AWS WAF User Guide.
