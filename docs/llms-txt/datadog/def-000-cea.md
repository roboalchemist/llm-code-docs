# Source: https://docs.datadoghq.com/security/default_rules/def-000-cea.md

---
title: EC2 Transit Gateways should not automatically accept VPC attachment requests
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EC2 Transit Gateways should not
  automatically accept VPC attachment requests
---

# EC2 Transit Gateways should not automatically accept VPC attachment requests
 
## Description{% #description %}

This check verifies whether EC2 transit gateways are set to automatically accept shared VPC attachments. The check will not pass if a transit gateway is configured to automatically accept attachment requests for shared VPCs.

Enabling the AutoAcceptSharedAttachments setting allows a transit gateway to automatically accept VPC attachment requests from other accounts without verification. To adhere to best practices for authorization and authentication, it is advised to disable this feature so that only authorized attachment requests are accepted.

## Remediation{% #remediation %}

For instructions on how to make changes to a transit gateway, refer to the [Modify a transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#tgw-modifying) section in the Amazon VPC Developer Guide.
