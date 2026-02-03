# Source: https://docs.datadoghq.com/security/default_rules/def-000-ijw.md

---
title: >-
  PostgreSQL instances should have the `log_min_error_statement` flag set to
  'ERROR' or stricter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > PostgreSQL instances should have the
  `log_min_error_statement` flag set to 'ERROR' or stricter
---

# PostgreSQL instances should have the `log_min_error_statement` flag set to 'ERROR' or stricter
 
## Description{% #description %}

The `log_min_error_statement` flag defines the minimum message severity level that is considered an error statement. Messages for error statements are logged with the SQL statement. Valid values include `DEBUG5`, `DEBUG4`, `DEBUG3`, `DEBUG2`, `DEBUG1`, `INFO`, `NOTICE`, `WARNING`, `ERROR`, `LOG`, `FATAL`, and `PANIC`. Each severity level includes the subsequent levels mentioned above. Ensure a value of `ERROR` or stricter is set.

## Rationale{% #rationale %}

Auditing helps with troubleshooting operational problems and also permits forensic analysis. If `log_min_error_statement` is not set to the correct value, messages may not be classified as error messages appropriately. If general log messages are considered as error messages, it would be difficult to determine the actual errors. If only stricter severity levels are considered as error messages, true errors might not be logged with their SQL statements. The `log_min_error_statement` flag should be set to `ERROR` or stricter. This recommendation is applicable to PostgreSQL database instances.

## Impact{% #impact %}

Turning on logging will increase the required storage over time. Mismanaged logs may cause your storage costs to increase. Setting custom flags using the command line on certain instances will cause all omitted flags to be reset to defaults. This may cause you to lose custom flags and could result in unforeseen complications or instance restarts. Because of this, it is recommended that you apply these flag changes during a period of low usage.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the Cloud SQL Instances page in the Google Cloud Console by visiting [https://console.cloud.google.com/sql/instances](https://console.cloud.google.com/sql/instances).
1. Select the PostgreSQL instance for which you want to enable the database flag.
1. Click **Edit**.
1. Scroll down to the `Flags` section.
1. Click **Add item** to set a flag that has not been set on the instance before. Choose the flag `log_min_error_statement` from the drop-down menu and set the appropriate value.
1. Click `Save` to save your changes.
1. Confirm your changes under the `Flags` section on the Overview page.

### From Command Line:{% #from-command-line %}

1. Configure the `log_min_error_statement` database flag for every Cloud SQL PosgreSQL database instance using the below command.

   ```
   gcloud sql instances patch <INSTANCE_NAME> --database-flags log_min_error_statement=<DEBUG5|DEBUG4|DEBUG3|DEBUG2|DEBUG1|INFO|NOTICE|WARNING|ERROR>
   ```

Note: This command will overwrite all database flags previously set. To keep those and add new ones, include the values for all flags you want set on the instance; any flag not specifically included is set to its default value. For flags that do not take a value, specify the flag name followed by an equals sign (=).

## Default value{% #default-value %}

By default `log_min_error_statement` is `ERROR`.

## References{% #references %}

1. [https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)
1. [https://www.postgresql.org/docs/9.6/runtime-config-logging.html#RUNTIME-CONFIG-LOGGING-WHEN](https://www.postgresql.org/docs/9.6/runtime-config-logging.html#RUNTIME-CONFIG-LOGGING-WHEN)

## Additional Information{% #additional-information %}

WARNING: This patch modifies database flag values, which may require your instance to be restarted. Check the list of supported flags - [https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags) - to see if your instance will be restarted when this patch is submitted.

Note: Some database flag settings can affect instance availability or stability and remove the instance from the Cloud SQL SLA. For information about these flags, see Operational Guidelines.

Note: Configuring the above flag does not require restarting the Cloud SQL instance.

## CIS controls{% #cis-controls %}

Version 8, 8.5: Collect Detailed Audit Logs

- Configure detailed audit logging for enterprise assets containing sensitive data. Include event source, date, username, timestamp, source addresses, destination addresses, and other useful elements that could assist in a forensic investigation.

Version 7, 6.3: Enable Detailed Logging

- Enable system logging to include detailed information such as an event source, date, user, timestamp, source addresses, destination addresses, and other useful elements.
