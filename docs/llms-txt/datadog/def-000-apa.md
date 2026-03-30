# Source: https://docs.datadoghq.com/security/default_rules/def-000-apa.md

---
title: MySQL instances should have the 'local_infile' database flag set to 'off'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > MySQL instances should have the
  'local_infile' database flag set to 'off'
---

# MySQL instances should have the 'local_infile' database flag set to 'off'

## Description{% #description %}

Datadog recommends setting the `local_infile` database flag for a Cloud SQL MySQL instance to off.

## Rationale{% #rationale %}

The `local_infile` flag controls the server-side LOCAL capability for LOAD DATA statements. Depending on the `local_infile` setting, the server refuses or permits local data loading by clients that have LOCAL enabled on the client side.

To explicitly cause the server to refuse LOAD DATA LOCAL statements (regardless of how client programs and libraries are configured at build time or runtime), start mysqld with `local_infile` disabled. `local_infile` can also be set at runtime.

Due to security issues associated with the `local_infile` flag, Datadog recommends disabling it. This recommendation is applicable to MySQL database instances.

## Impact{% #impact %}

Disabling `local_infile` causes the server to refuse local data loading by clients that have LOCAL enabled on the client side.

## Remediation{% #remediation %}

## From Console{% #from-console %}

1. In the Google Cloud Console, navigate to [Cloud SQL Instances page](https://console.cloud.google.com/sql/instances).
1. Select the MySQL instance where the database flag needs to be enabled.
1. Click **Edit**.
1. Scroll down to the **Flags** section.
1. To set a flag that has not been set on the instance before, click **Add item**, choose the `local_infile` flag from the dropdown menu, and set its value to **off**.
1. Click **Save**.
1. Confirm the changes under **Flags** on the Overview page.

## From Command Line{% #from-command-line %}

1. List all Cloud SQL database instances using
   ```
   `gcloud sql instances list`.
   ```
1. Configure the `local_infile` database flag for every Cloud SQL MySQL database instance using
   ```
   `gcloud sql instances patch INSTANCE_NAME --database-flags local_infile=off`
   ```
Note: This command overwrites all previously set database flags. To keep these flags and add new ones, include all flag values to be set on the instance. Otherwise, flags that are not specifically included are set to its default value. For flags that do not take a value, specify the flag name followed by an equals sign, for example: `=`.

## Default Value{% #default-value %}

By default, `local_infile` is on.

## References{% #references %}

1. [https://cloud.google.com/sql/docs/mysql/flags](https://cloud.google.com/sql/docs/mysql/flags)
1. [https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_local_infile](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_local_infile)
1. [https://dev.mysql.com/doc/refman/5.7/en/load-data-local.html](https://dev.mysql.com/doc/refman/5.7/en/load-data-local.html)

## Additional Information{% #additional-information %}

This patch modifies database flag values, which may require you to restart your instance. Check the [list of supported flags](https://cloud.google.com/sql/docs/mysql/flags) to see if your instance will restart when this patch is submitted.
