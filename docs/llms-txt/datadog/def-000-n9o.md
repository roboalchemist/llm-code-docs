# Source: https://docs.datadoghq.com/security/default_rules/def-000-n9o.md

---
title: Kinesis streams should be encrypted at rest
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Kinesis streams should be encrypted at
  rest
---

# Kinesis streams should be encrypted at rest
 
## Description{% #description %}

This control verifies whether Kinesis Data Streams are encrypted at rest using server-side encryption. The control fails if a Kinesis stream is not encrypted at rest with this method.

Server-side encryption in Amazon Kinesis Data Streams automatically secures data at rest by utilizing an AWS KMS key. The data is encrypted before being stored in the Kinesis stream storage layer and decrypted when accessed. This ensures that your data remains encrypted at rest within the Amazon Kinesis Data Streams service.

## Remediation{% #remediation %}

For guidance on enabling server-side encryption for Kinesis streams, refer to the [How do I get started with server-side encryption?](https://docs.aws.amazon.com/streams/latest/dev/getting-started-with-sse.html) section of the Amazon Kinesis Developer Guide.
