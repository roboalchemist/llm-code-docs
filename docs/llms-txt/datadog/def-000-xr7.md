# Source: https://docs.datadoghq.com/security/default_rules/def-000-xr7.md

---
title: DMS endpoints should require SSL/TLS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > DMS endpoints should require SSL/TLS
---

# DMS endpoints should require SSL/TLS
 
## Description{% #description %}

This control verifies if an AWS DMS endpoint is configured to use an SSL connection. The `ssl_mode` of the endpoint must set to either `require`, `verify-ca` or `verify-full`.

SSL/TLS connections enhance security by encrypting data exchanged between DMS replication instances and your database. Additionally, using certificates adds another layer of protection by ensuring the connection is established with the intended database through server certificate validation. The server certificate is automatically installed on all provisioned database instances. Enabling SSL on your DMS endpoints ensures data confidentiality during migration.

This control skips endpoints that encrypt connections by default. These include S3, DynamoDB, Kinesis, Neptune, and Elasticsearch (see [note about the SSL mode option](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.SSL.html)), which do not have an SSL mode setting available.

## Remediation{% #remediation %}

For guidance on configuring SSL for DMS endpoints, refer to the [Using SSL with AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.SSL.html) section of the AWS Database Migration Service User Guide.
