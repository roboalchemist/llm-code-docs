# Source: https://docs.datadoghq.com/security/default_rules/def-000-aw1.md

---
title: VPCs should have interface endpoint for Amazon ECR API
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > VPCs should have interface endpoint for
  Amazon ECR API
---

# VPCs should have interface endpoint for Amazon ECR API
 
## Description{% #description %}

Virtual private clouds (VPCs) should have interface VPC endpoints configured for Amazon ECR API to enable private access to ECR services. AWS PrivateLink enables customers to access services hosted on AWS while keeping all network traffic within the AWS network, which prevents traffic from service users from traversing the internet.

## Remediation{% #remediation %}

Configure a VPC endpoint for Amazon ECR API by creating an interface endpoint with the service name **com.amazonaws..ecr.api**. For guidance on configuring a VPC endpoint, refer to the [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) section of the AWS PrivateLink Guide.
