# Source: https://docs.datadoghq.com/security/default_rules/def-000-q5r.md

---
title: >-
  PostgreSQL instances should have the 'log_statement' database flag set
  appropriately
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > PostgreSQL instances should have the
  'log_statement' database flag set appropriately
---

# PostgreSQL instances should have the 'log_statement' database flag set appropriately
 
## Description{% #description %}

The value of the `log_statement` flag determines the SQL statements that are logged. Valid values are:

- `none`
- `ddl`
- `mod`
- `all`

The value `ddl` logs all data definition statements. The value `mod` logs all `ddl` statements, plus data-modifying statements.

The statements are logged after a basic parsing is done and the statement type is determined, thus log statements with errors are not logged. When using an extended query protocol, logging occurs after an `Execute` message is received and values of the bind parameters are included.

A value of `ddl` is recommended unless otherwise directed by your organization's logging policy.

## Rationale{% #rationale %}

Auditing helps with forensic analysis. If the `log_statement` is not set to the correct value, too many statements may be logged and lead to issues with finding relevant information from the logs, or too few statements may be logged with relevant information missing from the logs. Setting the `log_statement` to align with your organization's security and logging policies facilitates auditing and review of database activities later on. This recommendation is applicable to PostgreSQL database instances.

### Impact{% #impact %}

Turning on logging will increase the required storage over time. Mismanaged logs may cause your storage costs to increase. Setting custom flags using the command line on certain instances will cause all omitted flags to be reset to defaults. This may cause you to lose custom flags and could result in unforeseen complications or instance restarts. Because of this, it is recommended that you apply these flag changes during a period of low usage.

- **WARNING** This patch modifies database flag values, which may require your instance to be restarted. Check the list of supported flags - [https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags) - to see if your instance will be restarted when this patch is submitted.
- Note: Some database flag settings can affect instance availability or stability and remove the instance from the Cloud SQL SLA. For information about these flags, see Operational Guidelines.
- Note: Configuring the above flag does not require restarting the Cloud SQL instance.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the Cloud SQL Instances page by visiting: [https://console.cloud.google.com/sql/instances](https://console.cloud.google.com/sql/instances)
1. Select the PostgreSQL instance for which you want to enable the database flag.
1. Click **Edit**.
1. Scroll down to the **Flags** section.
1. To set a flag that has not been set on the instance before, click **Add item**. Choose the flag `log_statement` from the drop-down menu and set the appropriate value.
1. Click **Save**.
1. Confirm your changes under **Flags** on the **Overview** page.

### From the command line{% #from-the-command-line %}

1. Configure the `log_statement database` flag for every Cloud SQL PosgreSQL database instance using the below command.

   ```
   gcloud sql instances patch <INSTANCE_NAME> --database-flags log_statement=<ddl|mod|all|none>
   ```

**Note** This command will overwrite all database flags previously set. To keep those and add new ones, include the values for all the flags that you want to set on the instance; any flag not specifically included is set to its default value. For flags that do not take a value, specify the flag name followed by an equals sign ("=").

## References{% #references %}

1. [https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)
1. [https://www.postgresql.org/docs/current/runtime-config-logging.html#RUNTIME-CONFIG-LOGGING-WHAT](https://www.postgresql.org/docs/current/runtime-config-logging.html#RUNTIME-CONFIG-LOGGING-WHAT)
