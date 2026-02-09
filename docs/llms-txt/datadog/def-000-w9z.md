# Source: https://docs.datadoghq.com/security/default_rules/def-000-w9z.md

---
title: PostgreSQL instance should have the 'log_disconnections' database flag enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > PostgreSQL instance should have the
  'log_disconnections' database flag enabled
---

# PostgreSQL instance should have the 'log_disconnections' database flag enabled
 
## Description{% #description %}

Enabling the `log_disconnections` setting logs the end of each session, including the session duration.

## Rationale{% #rationale %}

PostgreSQL does not log session details such as duration and session end by default. Enabling the `log_disconnections` setting will create log entries at the end of each session, which can be useful in troubleshooting issues and determining any unusual activity across a time period. The `log_disconnections` and `log_connections` settings work together and generally, the pair would be enabled or disabled together. This recommendation is applicable to PostgreSQL database instances.

## Impact{% #impact %}

Turning on logging will increase the required storage over time. Mismanaged logs may cause your storage costs to increase. Setting custom flags via command line on certain instances will cause all omitted flags to be reset to defaults. This may cause you to lose custom flags and could result in unforeseen complications or instance restarts. Because of this, it is recommended you apply these flags changes during a period of low usage.

## Remediation{% #remediation %}

## From the console{% #from-the-console %}

1. Go to the [Cloud SQL Instances](https://console.cloud.google.com/sql/instances) page.
1. Select the PostgreSQL instance where the database flag needs to be enabled.
1. Click **Edit**.
1. Scroll down to the **Flags** section.
1. To set a flag that has not been set on the instance before, click **Add item**, choose the flag `log_disconnections` from the drop-down menu and set the value as **on**.
1. Click **Save**.
1. Confirm the changes under **Flags** on the **Overview** page.

## From the command line{% #from-the-command-line %}

1. Configure the `log_disconnections` database flag for every Cloud SQL PosgreSQL database instance using the below command:

   ```
   gcloud sql instances patch <INSTANCE_NAME> --database-flags
   log_disconnections=on
   ```

**Note:** This command will overwrite all previously set database flags. To keep those and add new ones, include the values for all flags to be set on the instance; any flag not specifically included is set to its default value. For flags that do not take a value, specify the flag name followed by an equals sign ("=").

## Default Value{% #default-value %}

By default, `log_disconnections` is off.

## References{% #references %}

1. [https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)
1. [https://www.postgresql.org/docs/9.6/runtime-config-logging.html#RUNTIME-CONFIG-LOGGING-WHAT](https://console.cloud.google.com/sql/instances)

## Additional Information{% #additional-information %}

- Configuring the `log_disconnections` flag does not require restarting the Cloud SQL instance.
- Although the `log_disconnections` flag does not require a restart, you might modify other database flag values when you apply this patch. **Many database flags require restarting the Cloud SQL instance.** Before you modify a database flag, check the [list of supported flags](https://cloud.google.com/sql/docs/postgres/flags) to see if your instance will be restarted when this patch is submitted.
- Some database flag settings can affect instance availability or stability and remove the instance from the Cloud SQL SLA. For information about these flags, see [Operational Guidelines](https://cloud.google.com/sql/docs/operational-guidelines).

## CIS controls{% #cis-controls %}

Version 8, 8.5 Collect Detailed Audit Logs

- Configure detailed audit logging for enterprise assets containing sensitive data. Include event source, date, username, timestamp, source addresses, destination addresses, and other useful elements that could assist in a forensic investigation.
