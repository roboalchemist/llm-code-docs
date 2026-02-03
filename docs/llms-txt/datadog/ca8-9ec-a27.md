# Source: https://docs.datadoghq.com/security/default_rules/ca8-9ec-a27.md

---
title: Redshift clusters should be encrypted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Redshift clusters should be encrypted
---

# Redshift clusters should be encrypted
 
## Description{% #description %}

Ensure that AWS RedShift clusters are encrypted.

## Rationale{% #rationale %}

Encrypting Redshift clusters protects your sensitive data from unauthorized access.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Changing cluster encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/changing-cluster-encryption.html) docs to ensure your clusters are encrypted.

### From the command line{% #from-the-command-line %}

1. Run `describe-clusters` with your [cluster identifier](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-clusters.html).

   ```
    aws redshift describe-clusters \
        --cluster-identifier cluster-name
   ```

1. Run `create-cluster` using the configuration details returned in step 1 along with the [`encrypted` flag](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster.html).

   ```
    aws redshift create-cluster \
        --cluster-identifier cluster-name \
        --encrypted
   ```

1. Run `describe-cluster` with a [query filter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-clusters.html) to expose the new endpoint address.

   ```
    aws redshift describe-clusters \
        --cluster-identifier cluster-name \
        --query 'Clusters[*].Endpoint.Address'
   ```

1. Use the cluster endpoint URL with the [Amazon Redshift Unload/Copy](https://github.com/awslabs/amazon-redshift-utils/tree/master/src/UnloadCopyUtility) tool.

1. Update your encrypted Redshift cluster configuration with the new Redshift cluster endpoint URL.

1. Once the endpoint is changed, run `delete-cluster` to [remove the old unencrypted cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster.html).

   ```
    aws redshift delete-cluster \
        --cluster-identifier old-cluster \
        --final-cluster-snapshot-identifier old-cluster-finalsnapshot
   ```
