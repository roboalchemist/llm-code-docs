# Source: https://docs.datadoghq.com/security/default_rules/def-000-aat.md

---
title: >-
  PostgreSQL instances should have the 'log_min_messages' database flag set to
  at least 'WARNING'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > PostgreSQL instances should have the
  'log_min_messages' database flag set to at least 'WARNING'
---

# PostgreSQL instances should have the 'log_min_messages' database flag set to at least 'WARNING'

## Description{% #description %}

The `log_min_messages` flag defines the minimum message severity level that is considered as an error statement. Messages for error statements are logged with the SQL statement. Valid values include `debug5`, `debug4`, `debug3`, `debug2`, `debug1`, `info`, `notice`, `warning`, `error`, `log`, `fatal`, and `panic`. Each severity level includes the subsequent levels mentioned above. For best practices, set the value to `error`. Changes should only be made in accordance with the organization's logging policy.

### Default value{% #default-value %}

By default `log_min_error_statement` is `warning`.

## Rationale{% #rationale %}

Auditing helps in troubleshooting operational problems and also permits forensic analysis. If `log_min_error_statement` is not set to the correct value, messages may not be classified as error messages appropriately. An organization will need to decide their own threshold for logging `log_min_messages` flag.

### Impact{% #impact %}

Setting the threshold too low will might result in increased log storage size and length, making it difficult to find actual errors. Setting the threshold to `warning` logs most needed error messages. Setting the threshold to a higher severity level may result in some errors (that need troubleshooting) to not be logged.

Note: To effectively turn off logging failing statements, set this parameter to `panic`.

Note: Configuring the above flag does not require restarting the Cloud SQL instance.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the [Cloud SQL Instances page](https://console.cloud.google.com/sql/instances) in the Google Cloud console.
1. Select the PostgreSQL instance for which you want to enable the database flag.
1. Click **Edit**.
1. Scroll down to the Flags section.
1. Click **Add item** to set a flag that has not been set on the instance before. Choose the flag `log_min_messages` from the drop-down menu and set appropriate value.
1. Click **Save**.
1. Confirm your changes under the Flags section on the Overview page.

### From the command line{% #from-the-command-line %}

1. Configure the `log_min_messages` database flag for every Cloud SQL PosgreSQL database instance using the below command.

```
gcloud sql instances patch <INSTANCE_NAME> --database-flags
log_min_messages=<DEBUG5|DEBUG4|DEBUG3|DEBUG2|DEBUG1|INFO|NOTICE|WARNING|ERROR|LOG|FATAL|PANIC>
```

Note: This command overwrites all database flags previously set. To keep flags previously set and add new ones, include the values for all flags you want set on the instance; any flag not specifically included is set to its default value. For flags that do not take a value, specify the flag name followed by an equals sign (=).

## References{% #references %}

1. [https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)
1. [https://www.postgresql.org/docs/9.6/runtime-config-logging.html#RUNTIME-CONFIG-LOGGING-WHEN](https://www.postgresql.org/docs/9.6/runtime-config-logging.html#RUNTIME-CONFIG-LOGGING-WHEN)
