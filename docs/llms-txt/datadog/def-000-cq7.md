# Source: https://docs.datadoghq.com/security/default_rules/def-000-cq7.md

---
title: VPCs should have interface endpoint for SSM
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > VPCs should have interface endpoint for
  SSM
---

# VPCs should have interface endpoint for SSM
 
## Description{% #description %}

Virtual private clouds (VPCs) should have interface VPC endpoints configured for AWS Systems Manager (SSM) to enable private access to SSM services. AWS PrivateLink enables customers to access services hosted on AWS while keeping all network traffic within the AWS network, which prevents traffic from service users from traversing the internet.

## Remediation{% #remediation %}

Configure a VPC endpoint for SSM by creating an interface endpoint with the service name **com.amazonaws..ssm**. For guidance on configuring a VPC endpoint, refer to the [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) section of the AWS PrivateLink Guide.
