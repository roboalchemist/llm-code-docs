# Source: https://docs.datadoghq.com/security/default_rules/zbs-gp9-gp2.md

---
title: Lambda function should use the latest runtime environment version
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Lambda function should use the latest
  runtime environment version
---

# Lambda function should use the latest runtime environment version
 
## Description{% #description %}

This control ensures that your Amazon Lambda Function is updated to the most recent runtime environment version. Regularly updating your Lambda functions to the latest runtime version is a best practice recommended by Amazon. It is crucial for incorporating security patches, bug fixes, and accessing the latest features, ensuring the security and efficiency of your application.

**Note:** AWS Lambda supports deployment via both container images and .zip file archives. For container images, the runtime is determined during base image creation and is not accessible through configuration data. This is consistent for AWS and Custom base images. Consequently, this check only applies to deployment packages of the `Zip` type.

For details on supported and recent runtimes, see [AWS Lambda Supported Runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html).

## Remediation{% #remediation %}

To learn how to update your Lambda function's runtime, refer to the [AWS Console Documentation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html).
