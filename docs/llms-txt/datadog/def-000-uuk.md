# Source: https://docs.datadoghq.com/security/default_rules/def-000-uuk.md

---
title: >-
  SQL Server instances should have the 'cross db ownership chaining' database
  flag set to 'off'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SQL Server instances should have the
  'cross db ownership chaining' database flag set to 'off'
---

# SQL Server instances should have the 'cross db ownership chaining' database flag set to 'off'

## Description{% #description %}

It is recommended that you set the `cross db ownership chaining` database flag for SQL Server instance to `off`.

## Rationale{% #rationale %}

The `cross db ownership` option is used to configure cross-database ownership chaining for an instance of Microsoft SQL Server. This server option allows you to control cross-database ownership chaining at the database level or to allow cross-database ownership chaining for all databases. Enabling `cross db ownership` is not recommended unless all of the databases hosted by the instance of SQL Server must participate in cross-database ownership chaining, and you are aware of the security implications of this setting. This recommendation is applicable to SQL Server database instances.

### Impact{% #impact %}

Updating flags may cause the database to restart. This may cause the database to be unavailable for a short amount of time, so this is best done at a time of low usage. You should also determine if the tables in your databases reference another table without using credentials for that database, as turning off cross database ownership will break this relationship.

- Some database flag settings can affect instance availability or stability, and remove the instance from the Cloud SQL SLA. For information about these flags, see Operational Guidelines.

- Configuring the `cross db ownership chaining` flag does not restart the Cloud SQL instance.

- Note: The command to set database flags overwrites all database flags previously set. To keep the existing settings while adding new flags, include the values for all flags to be set on the instance. Cloud SQL sets any flag not specifically included in the list to its default value. For flags that do not take a value, specify the flag name followed by an equals sign ("=").

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the [Cloud SQL Instances page](https://console.cloud.google.com/sql/instances) in Google Cloud Console.
1. Select the SQL Server instance for which you want to enable to database flag.
1. Click **Edit**.
1. Scroll down to the **Flags** section.
1. To set a flag that has not been set on the instance before, click **Add item**, choose the flag `cross db ownership chaining` from the drop-down menu, and set its value to `off`.
1. Click **Save**.
1. Confirm the changes under **Flags** on the Overview page.

### From the command line{% #from-the-command-line %}

Configure the `cross db ownership chaining` database flag for every SQL Server database instance using the below command:

```
gcloud sql instances patch <INSTANCE_NAME> --database-flags "cross db ownership chaining=off"
```

## References{% #references %}

1. [https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)
1. [https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/cross-db-ownership-chaining-server-configuration-option?view=sql-server-ver15](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/cross-db-ownership-chaining-server-configuration-option?view=sql-server-ver15)
