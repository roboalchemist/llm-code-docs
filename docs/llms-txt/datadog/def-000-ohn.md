# Source: https://docs.datadoghq.com/security/default_rules/def-000-ohn.md

---
title: >-
  EC2 should be configured to use AWS VPC endpoints created for the Amazon EC2
  service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EC2 should be configured to use AWS VPC
  endpoints created for the Amazon EC2 service
---

# EC2 should be configured to use AWS VPC endpoints created for the Amazon EC2 service

## Description{% #description %}

This check verifies the presence of a service endpoint for Amazon EC2 within each VPC. It registers a failure if a VPC does not have an Amazon EC2 service endpoint created.

This evaluation is limited to resources within a single AWS account and cannot assess resources across multiple accounts. Consequently, AWS Config and Security Hub reports FAILED findings for VPCs shared across accounts. Security Hub suggests suppressing these FAILED findings.

Enhance the security of your VPC by configuring Amazon EC2 to use an interface VPC endpoint. These endpoints leverage AWS PrivateLink technology to enable private access to Amazon EC2 API operations, ensuring that all network traffic between your VPC and Amazon EC2 remains on the Amazon network. You can use interface endpoints to [connect from the same region](https://docs.datadoghq.com/agent/guide/private-link/#connect-from-the-same-region) or [connect from other regions](https://docs.datadoghq.com/agent/guide/private-link/#connect-from-other-regions).

For further information on setting up VPC endpoints for Amazon EC2, refer to the [Amazon EC2 User Guide for Linux Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interface-vpc-endpoints.html).

## Remediation{% #remediation %}

For instructions on establishing an interface endpoint to Amazon EC2 via the Amazon VPC console, refer to the [Create a VPC endpoint section in the AWS PrivateLink Guide](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws). When specifying the Service name, select **com.amazonaws.region.ec2**.

Additionally, you have the option to create and link an endpoint policy to your VPC endpoint to manage access to the Amazon EC2 API. To learn how to craft a VPC endpoint policy, consult the [Create an endpoint policy section in the Amazon EC2 User Guide for Linux Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interface-vpc-endpoints.html#endpoint-policy).
