# Source: https://docs.datadoghq.com/security/default_rules/def-000-5bn.md

---
title: VPCs should have an interface VPC endpoint configured for SSM Incident Manager
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > VPCs should have an interface VPC
  endpoint configured for SSM Incident Manager
---

# VPCs should have an interface VPC endpoint configured for SSM Incident Manager

## Description{% #description %}

Virtual private clouds (VPCs) should have interface VPC endpoints configured for SSM Incident Manager to enable private access to AWS Systems Manager Incident Manager services. AWS PrivateLink enables customers to access services hosted on AWS while keeping all network traffic within the AWS network, which prevents traffic from service users from traversing the internet.

## Remediation{% #remediation %}

Configure a VPC endpoint for SSM Incidents by creating an interface endpoint with the service name **com.amazonaws..ssm-incidents**. For guidance on configuring a VPC endpoint, refer to the [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) section of the AWS PrivateLink Guide.
