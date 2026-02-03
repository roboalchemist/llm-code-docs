# Source: https://docs.datadoghq.com/security/default_rules/kbp-pln-54a.md

---
title: >-
  The Elasticsearch domain should block unsigned requests over the public
  internet
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Elasticsearch domain should block
  unsigned requests over the public internet
---

# The Elasticsearch domain should block unsigned requests over the public internet
 
## Description{% #description %}

Update publicly accessible Amazon Elasticsearch domains to block unsigned requests.

## Rationale{% #rationale %}

Updating your Amazon Elasticsearch domain to a private domain ensures your data cannot be accessed or altered by unauthorized users.

## Remediation{% #remediation %}

### OpenSearch{% #opensearch %}

If you are using OpenSearch Service Domains, refer to Amazon's [guide for creating and managing Amazon OpenSearch Service domains](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-access-policies) for both console and CLI remediation actions.

### From the console{% #from-the-console %}

Follow the [Configuring Access Policies](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-access-policies) docs to learn how to update your publicly accessible Amazon Elasticsearch domains in the AWS Console.

### From the command line{% #from-the-command-line %}

1. Create a new policy JSON document. You can follow the [Amazon Elasticsearch templated policy](https://docs.aws.amazon.com/kms/latest/developerguide/determining-access-key-policy.html) to create a custom policy that grants domain access only to a specific IP.

In the `ip-based-policy.json` file:

   ```bash
       {
       ...
       "Statement": [
           ...
           "Action": "es:*",
           "Condition": {
               "IpAddress": {
               "aws:SourceIp": [
                   "54.197.25.93/32"
               ]
               }
           },
           "Resource": "arn:aws:es:123456789123:
                       domain/es-cluster/*"
           }
       ]
       }
       
```

1. Run `update-elasticsearch-domain-config` using the name of the [Elasticsearch domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/update-elasticsearch-domain-config.html) created in the previous step.

In the `ip-based-policy.json` file:

   ```bash
       aws es update-elasticsearch-domain-config
           --domain-name es-cluster
           --access-policies file://ip-based-policy.json
       
```
