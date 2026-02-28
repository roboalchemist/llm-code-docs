# Source: https://docs.datadoghq.com/security/default_rules/8e1-hf3-j3b.md

---
title: Logging for Redshift clusters should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Logging for Redshift clusters should be
  enabled
---

# Logging for Redshift clusters should be enabled

## Description{% #description %}

Enable logging for your Amazon Redshift cluster.

## Rationale{% #rationale %}

Logging data from Amazon Redshift clusters is helpful when troubleshooting or completing security and compliance audits.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the Amazon Redshift [Configuring auditing using the console](https://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing-console.html) docs to enable logging, create audit log files, and store them in an Amazon S3 bucket.

### From the command line{% #from-the-command-line %}

1. Run `enable-logging` with your [cluster ID and the S3 bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/enable-logging.html#synopsis) where log files are to be stored.

In the `list-buckets.sh` file:

```bash
  aws redshift enable-logging
    --cluster-identifier your-cluster-id
    --bucket-name aws-redshift-logs

```
