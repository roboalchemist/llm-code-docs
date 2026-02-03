# Source: https://docs.datadoghq.com/security/default_rules/62v-0kq-n6b.md

---
title: Elasticsearch domain should enable encryption
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Elasticsearch domain should enable
  encryption
---

# Elasticsearch domain should enable encryption
 
## Description{% #description %}

Implement encryption at rest for your Amazon Elasticsearch (ES) domain with the AWS KMS service.

## Rationale{% #rationale %}

Implementing encryption at rest protects your domain from unauthorized access and ensures security and compliance requirements are met.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Enabling Encryption of Data at Rest](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/encryption-at-rest.html#enabling-ear) docs to learn how to implement encryption for your domain.

### From the command line{% #from-the-command-line %}

1. Run `describe-elasticsearch-domain` with your ES domain to return configuration metadata.

   ```bash
   aws es describe-elasticsearch-domain
       --domain-name your-es-domain
   ```

1. Run `create-elasticsearch-domain` with your domain name and `encryption-at-rest-options`. Use the metadata returned in the previous step to [create and relaunch your ES domain to enable at-rest encryption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/create-elasticsearch-domain.html).

   ```bash
   aws es create-elasticsearch-domain
       --domain-name your-es-domain
       ...
       --encryption-at-rest-options Enabled=true,KmsKeyId="abcdabcd-aaaa-bbbb-cccc-abcdabcdabcd"
   ```
