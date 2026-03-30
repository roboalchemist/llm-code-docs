# Source: https://docs.datadoghq.com/security/default_rules/cut-36a-zvo.md

---
title: VPC endpoint should restrict public access
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > VPC endpoint should restrict public
  access
---

# VPC endpoint should restrict public access

## Description{% #description %}

Harden your VPC endpoint by restricting AWS actions that can be invoked through it.

## Rationale{% #rationale %}

VPC endpoints can be hardened by setting a non-default [VPC endpoint policy](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html), limiting the AWS actions that can be taken when an AWS service is invoked through this VPC endpoint.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Add or remove permissions for your endpoint service](https://docs.aws.amazon.com/vpc/latest/privatelink/add-endpoint-service-permissions.html) AWS console docs.

### From the command line{% #from-the-command-line %}

1. Edit your existing Amazon VPC endpoint access policy and replace untrusted AWS identifiers. To create a new policy document, [use the AWS policy generator](https://awspolicygen.s3.amazonaws.com/policygen.html).

   ```
   {
     "Id": "insert-vpc-policy-id",
     "Version": "2012-10-17",
     "Statement": [
       {
         "Action": "*",
         "Effect": "Allow",
         "Resource": "*",
         "Principal": {
           "AWS": [
             "insert-allowed-arns"
           ]
         }
       }
     ]
   }
   ```

1. Run the `modify-vpc-endpoint` command with your [VPC endpoint ID and the updated or new policy document](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-endpoint.html#synopsis) to replace the existing policy.

   ```
   aws ec2 modify-vpc-endpoint \
   --region insert-region-here
   --vpc-endpoint-id insert-vpc-endpoint-id \
   --policy-document file://insert-new-vpc-policy-filename.json
   ```

1. Repeat steps 1 & 2 for all non-compliant VPC Endpoints in the current region.

1. Repeat steps 1 & 2 for all non-compliant VPC Endpoints in other regions.
