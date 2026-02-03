# Source: https://docs.datadoghq.com/security/default_rules/def-000-mbs.md

---
title: CloudFront distributions should be configured with a default root object
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > CloudFront distributions should be
  configured with a default root object
---

# CloudFront distributions should be configured with a default root object
 
## Description{% #description %}

This evaluation determines if an Amazon CloudFront distribution is set up to provide a designated object as the default root object. The evaluation is marked as failed if the CloudFront distribution lacks a configured default root object.

When a user accesses the root URL of the distribution rather than a specific file, having a default root object specified helps to prevent the disclosure of the entire contents of the web distribution.

## Remediation{% #remediation %}

For instructions on setting up a default root object in a CloudFront distribution, refer to the section on [specifying a default root object in the Amazon CloudFront Developer Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html#DefaultRootObjectHowToDefine).
