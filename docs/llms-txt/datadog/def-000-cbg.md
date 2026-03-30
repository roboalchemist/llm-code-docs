# Source: https://docs.datadoghq.com/security/default_rules/def-000-cbg.md

---
title: >-
  PostgreSQL instances should have the 'log_connections' database flag set to
  'on'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > PostgreSQL instances should have the
  'log_connections' database flag set to 'on'
---

# PostgreSQL instances should have the 'log_connections' database flag set to 'on'

## Description{% #description %}

By enabling the `log_connections` setting, every attempted server connection is logged along with the successful completion of client authentication. Once the session starts, you cannot change this parameter.

## Rationale{% #rationale %}

By default, PostgreSQL does not log attempted connections. By enabling the `log_connections` setting, you can create log entries for every attempted connection as well as the successful completion of client authentication. This can be useful in troubleshooting issues and determining any unusual connection attempts to the server. This recommendation is applicable to PostgreSQL database instances.

## Impact{% #impact %}

By turning on logging, the required storage increaess over time. Mismanaged logs may cause your storage costs to increase.

Setting custom flags through the command line on certain instances can cause all omitted flags to reset to defaults. This may cause you to lose custom flags and can result in unforeseen complications or instance restarts. Because of this, Datadog recommends applying these flag changes during a period of low usage.

## Remediation{% #remediation %}

## From the console{% #from-the-console %}

1. In the Google Cloud Console, navigate to the [Cloud SQL Instances page](https://console.cloud.google.com/sql/instances).
1. Select the PostgreSQL instance that you want to enable the database flag for.
1. Click **Edit**.
1. Scroll down to the **Flags** section.
1. To set a flag that has not been set on the instance before, click **Add item**, choose the **log\_connections** flag from the dropdown menu, and set the value as **on**.
1. Click **Save**.
1. Confirm the changes under **Flags** on the Overview page.

## From the command line{% #from-the-command-line %}

Configure the `log_connections` database flag for every Cloud SQL PosgreSQL database instance using the following command:

```
gcloud sql instances patch <INSTANCE_NAME> --database-flags
log_connections=on
```

This command overwrites all previously set database flags. To keep these flags and add new ones, include all flag values to be set on the instance. Otherwise, flags that are not specifically included are set to its default value. For flags that do not take a value, specify the flag name followed by an equals sign, for example: `=`.

You do not need to restart the Cloud SQL instance.

## Default Value{% #default-value %}

By default, `log_connections` is off.

## References{% #references %}

1. [https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)
1. [https://www.postgresql.org/docs/9.6/runtime-config-logging.html#RUNTIME-CONFIG-LOGGING-WHAT](https://www.postgresql.org/docs/9.6/runtime-config-logging.html#RUNTIME-CONFIG-LOGGING-WHAT)

## Additional Information{% #additional-information %}

This patch modifies database flag values, which may require you to restart your instance. Check the [list of supported flags](https://cloud.google.com/sql/docs/postgres/flags) to see if your instance will restart when this patch is submitted.

Some database flag settings can affect instance availability or stability, and may remove the instance from the Cloud SQL SLA.

For information about these flags, see the Operational Guidelines.

## CIS Controls{% #cis-controls %}

Version 8, 8.5 - Collect Detailed Audit Logs

- Configure detailed audit logging for enterprise assets containing sensitive data. Include event source, date, username, timestamp, source addresses, destination addresses, and other useful elements that could assist in a forensic investigation.
