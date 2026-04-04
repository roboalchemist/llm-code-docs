# Source: https://docs.datadoghq.com/security/default_rules/def-000-lm4.md

---
title: SQL Server instances should have the `user options` database flag disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SQL Server instances should have the
  `user options` database flag disabled
---

# SQL Server instances should have the `user options` database flag disabled

## Description{% #description %}

It is recommended that the `user options` database flag for SQL Server instance not be configured.

## Rationale{% #rationale %}

The `user options` flag specifies global defaults for all users. A list of default query processing options is established for the duration of a user's work session. The user options flag allows you to change the default values of the SET options (if the server's default settings are not appropriate).

A user can override these defaults by using the SET statement. You can configure user options dynamically for new logins. After you change the setting of user options, new login sessions use the new setting; current login sessions are not affected. This recommendation is applicable to SQL Server database instances.

## Impact{% #impact %}

In some instances, setting custom flags via the command line causes all omitted flags to be reset to their defaults. This might cause you to lose custom flags and could result in unforeseen complications or instance restarts. Because of this, it is recommended you apply these flag changes during a period of low usage.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the **Cloud SQL Instances** page in the Google Cloud Console by visiting [https://console.cloud.google.com/sql/instances](https://cloud.google.com/sql/docs/sqlserver/flags).
1. Select the SQL Server instance you want to configure.
1. Click **Edit**.
1. Scroll down to the **Flags** section.
1. Click the **X** next to the **user options** flag shown
1. Click **Save** to save your changes.
1. Confirm your changes under **Flags** on the **Overview** page.

### From the command line{% #from-the-command-line %}

1. List all Cloud SQL database Instances:

   ```
   gcloud sql instances list
   ```

1. Clear the user options database flag for every Cloud SQL SQL Server database instance using either of the below commands:

   - To clear all flags and reset them to their default values:

     ```
     gcloud sql instances patch <INSTANCE_NAME> --clear-database-flags
     ```

   - To clear only the `user options` database flag, re-enter all of database flags that you want to configure and exclude the `user options` flag and its value:

     ```
     gcloud sql instances patch <INSTANCE_NAME> --database-flags [FLAG1=VALUE1,FLAG2=VALUE2]
     ```

**Note**: This command overwrites all database flags previously set. To keep those flags and add new ones, include the values for all flags you want set on the instance. Any flag not specifically included is set to its default value. For flags that do not take a value, specify the flag name followed by an equals sign ("=").

## Default value{% #default-value %}

By default, 'user options' is not configured.

## References{% #references %}

1. [https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)
1. [https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-user-options-server-configuration-option?view=sql-server-ver15](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-user-options-server-configuration-option?view=sql-server-ver15)
1. [https://www.stigviewer.com/stig/ms_sql_server_2016_instance/2018-03-09/finding/V-79335](https://www.stigviewer.com/stig/ms_sql_server_2016_instance/2018-03-09/finding/V-79335)

## Additional information{% #additional-information %}

- Some database flag settings can affect instance availability or stability, and remove the instance from the Cloud SQL SLA. For information about these flags, see [Operational Guidelines](https://cloud.google.com/sql/docs/operational-guidelines).

- Configuring the above flag does not restart the Cloud SQL instance.
