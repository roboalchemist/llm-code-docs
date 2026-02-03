# Source: https://docs.datadoghq.com/security/default_rules/eag-4ke-cj4.md

---
title: Logging and Audits should be configured for Load Balancers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Logging and Audits should be configured
  for Load Balancers
---

# Logging and Audits should be configured for Load Balancers
 
## Description{% #description %}

Set up logging for your AWS Elastic Load Balancers (ELBs) to identify security issues.

## Rationale{% #rationale %}

Access logs allow you to analyze each TCP and HTTP request, which are useful during security audits or troubleshooting.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Enable access logs for your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html) docs to learn how to enable logging for your ELBs.

### From the command line{% #from-the-command-line %}

1. Run `create-bucket` to [create an S3 bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html) that stores the ELB log files.

**Note**: This bucket must be created in the same region as the ELB.

   ```
   aws s3api create-bucket \
       --region us-west-1 \
       --bucket your-elb-logging-bucket
   ```

1. Use the [AWS Policy Generator](http://awspolicygen.s3.amazonaws.com/policygen.html) to create a new policy.

1. Run `put-bucket-policy` to [attach the policy document](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-policy.html) to the S3 bucket.

   ```
   aws s3api put-bucket-policy \
       --bucket your-elb-logging-bucket \
       --policy file://elb-logging-policy.json
   ```

1. Run `modify-load-balancer-attributes` to [enable logging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/modify-load-balancer-attributes.html) for the selected ELB.

   ```gdscript3
   aws elb modify-load-balancer-attributes
       --region us-west-1
       --load-balancer-name YourLoadBalancerName
       --load-balancer-attributes
       "{\"AccessLog\":{\"Enabled\":true,\"EmitInterval\":60,\"S3BucketName\":\"your-logging-bucket\"}}"
   ```
