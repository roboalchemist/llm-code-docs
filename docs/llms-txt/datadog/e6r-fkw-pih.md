# Source: https://docs.datadoghq.com/security/default_rules/e6r-fkw-pih.md

---
title: SNS Topic should have access restrictions set for subscription
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SNS Topic should have access
  restrictions set for subscription
---

# SNS Topic should have access restrictions set for subscription
 
## Description{% #description %}

Update your Amazon Simple Notification Service (SNS) topic [resource-based policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html) to prevent unintended access to the resource.

## Rationale{% #rationale %}

When a `*` is specified as a `Principal`, along with an `Allow` `Effect` it grants [anyone](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-anonymous) the ability to perform actions on a resource. In this situation, if the policy includes the `sns:Subscribe` `Action`, it would permit anyone the ability to receive messages from the topic, resulting in an impact to the confidentiality of the application.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Preventative best practices](https://docs.aws.amazon.com/sns/latest/dg/sns-security-best-practices.html#preventative-best-practices) docs to learn how to implement least-privilege access or use IAM roles for your applications and AWS services.

### From the command line{% #from-the-command-line %}

1. Update your [resource-based policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) with an appropriate `Principal` ARN or a `Condition` element. Save the file as `policy.json`.

   ```
   {
     ...
     "Statement": [
       ...
       {
         "Sid": "console_sub",
         "Effect": "Allow",
         "Principal": {
           "AWS": "arn:aws:iam::123456789012:root"
         },
         "Action": [
           "SNS:Subscribe"
         ],
         ...
       }
     ]
   }
   ```

1. Run `set-topic-attributes` with the [ARN of the SNS topic](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/set-topic-attributes.html#set-topic-attributes).

   ```
   aws sns set-topic-attributes \
     --topic-arn arn:aws:sns:region:123456789012:YourTopic \
     --attribute-name Policy \
     --attribute-value file://policy.json
   ```
