# Source: https://docs.datadoghq.com/security/default_rules/b7c-ce0-a71.md

---
title: Redshift clusters should use the EC2-VPC platform for better security
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Redshift clusters should use the
  EC2-VPC platform for better security
---

# Redshift clusters should use the EC2-VPC platform for better security

## Description{% #description %}

Confirm [Redshift Clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html) are using the [AWS EC2-VPC platform](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.FindDefaultVPC.html) for better cluster security.

## Rationale{% #rationale %}

The AWS EC2-VPC platform offers better security control and traffic routing for clusters than the outdated EC2-Classic platform.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Use EC2-VPC when you create your cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-platforms) docs to learn how to use the EC2-VPC platform in the console to secure your clusters.

### From the command line{% #from-the-command-line %}

1. Run `describe-clusters` with a `cluster-identifier` to [retrieve cluster metadata](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.FindDefaultVPC.html).

In the `describe-clusters.sh` file:

   ```bash
       aws redshift describe-clusters
        --cluster-identifier cluster-id

```

1. Run `create-cluster` with the metadata to [launch a new cluster within a VPC](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/create-cluster.html).

In the `describe-clusters.sh` file:

   ```bash
           aws redshift create-cluster
               --cluster-identifier cluster-id
               --vpc-security-group-ids id-012a3b4c
               --port 5439
               ...

```

1. Re-run `describe-clusters` with a [custom query filter](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-endpoints-find.html) to retrieve the database cluster endpoint.

In the `describe-clusters.sh` file:

   ```bash
       aws redshift describe-clusters
        --cluster-identifier cluster-id
        --query 'Clusters[*].Endpoint.Address'

```

1. Reload the old cluster data into the new database cluster with the [Unload Copy Utility](https://github.com/awslabs/amazon-redshift-utils/tree/master/src/UnloadCopyUtility).

1. Run `delete-cluster` to [delete the old cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster.html).

In the `delete-cluster.sh` file:

   ```bash
       aws redshift create-cluster
        --cluster-identifier old-cluster-identifier
        ...

```
