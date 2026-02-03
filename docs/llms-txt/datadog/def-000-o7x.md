# Source: https://docs.datadoghq.com/security/default_rules/def-000-o7x.md

---
title: Object-level logging should be enabled for S3 bucket read events
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Object-level logging should be enabled
  for S3 bucket read events
---

# Object-level logging should be enabled for S3 bucket read events
 
## Description{% #description %}

S3 object-level API read event operations, such as `GetObject`, `DeleteObject`, and `PutObject`, are classified as data events, which are not logged by default in CloudTrail. Enabling object-level logging for S3 buckets is recommended to meet data compliance requirements, perform comprehensive security analysis, and monitor user behavior patterns, allowing for immediate actions on object-level API activity using Amazon CloudWatch Events.

## Remediation{% #remediation %}

To satisfy this check, a multi-region CloudTrail should be created using either Advanced or Basic Field Selectors.

Advanced Field Selectors:

````
```
{
    "field": "eventCategory",
    "equals": ["Data"]
},
{
    "field": "resources.type",
    "equals": ["AWS::S3::Object"]
},
{
    "field": "readOnly",
    "equals": ["true"]
},
```
````

Basic Field Selectors: `{ "type": "AWS::S3::Object", "values": ["arn:aws:s3"] }, { "read_write_type": "readOnly" (or `all`) }`

Additional fields such as `eventType` should not be used, as these will filter the scope of logging. For instructions on enabling object-level logging for S3 buckets in CloudTrail, refer to the [AWS CloudTrail User Guide on Logging Data Events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html).
