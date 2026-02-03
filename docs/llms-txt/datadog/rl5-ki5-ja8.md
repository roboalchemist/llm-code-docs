# Source: https://docs.datadoghq.com/security/default_rules/rl5-ki5-ja8.md

---
title: Lambda function should not be accessible over the public internet
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Lambda function should not be
  accessible over the public internet
---

# Lambda function should not be accessible over the public internet
 
## Description{% #description %}

Identify instances where a Lambda function can be invoked by anyone, either directly or through a Lambda function URL. Allowing unrestricted access to your Amazon Lambda functions poses significant risks.

**Note:** Allowing anonymous users to invoke Lambda functions can lead to data loss, exposure, and unexpected AWS billing charges.

## Remediation{% #remediation %}

To learn how to update your AWS Lambda function permissions, refer to the [AWS Documentation on resource-based policies for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html).
