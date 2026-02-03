# Source: https://docs.datadoghq.com/security/default_rules/def-000-g1w.md

---
title: Redshift clusters should enable SSL/TLS for client connections
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Redshift clusters should enable SSL/TLS
  for client connections
---

# Redshift clusters should enable SSL/TLS for client connections
 
## Description{% #description %}

Enable the `require_ssl` parameter for your Amazon Redshift cluster.

## Rationale{% #rationale %}

Redshift clusters that do not require an SSL connection are vulnerable to exploits, such as man-in-the-middle attacks. Securing your connections protects your sensitive and private data.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Amazon Redshift Clusters use AWS Certificate Manager (ACM)] to manage SSL certificates. To configure Redshift parameter groups in the console, follow the [Managing parameter groups using the console](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-parameter-groups-console.html) docs.

### From the command line{% #from-the-command-line %}

1. Run `modify-cluster-parameter-group` with name of [the default parameter group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-parameter-group.html#synopsis) you want to modify and the required parameters for SSL. This returns the group name and status if successful.

In the `modify-cluster-parameter-group.sh` file:

```bash
  aws redshift modify-cluster-parameter-group
    --parameter-group-name your-parameter-group
    --parameters ParameterName=require_ssl,ParameterValue=true

  
```
Run `reboot-cluster` with your [cluster identifier](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/reboot-cluster.html#synopsis) to enable the configuration changes.