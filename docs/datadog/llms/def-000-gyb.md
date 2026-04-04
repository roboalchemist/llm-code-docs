# Source: https://docs.datadoghq.com/security/default_rules/def-000-gyb.md

---
title: >-
  SQL Server instances should have the 'contained database authentication'
  database flag set to 'off'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SQL Server instances should have the
  'contained database authentication' database flag set to 'off'
---

# SQL Server instances should have the 'contained database authentication' database flag set to 'off'

## Description{% #description %}

It is recommended to set `contained database authentication` database flag for SQL Server instances to `off`.

## Rationale{% #rationale %}

A contained database includes all database settings and metadata required to define the database and has no configuration dependencies on the instance of the Database Engine where the database is installed. Users can connect to the database without authenticating a login at the Database Engine level. Isolating the database from the Database Engine makes it possible to easily move the database to another instance of SQL Server. Contained databases have some unique threats that should be understood and mitigated by SQL Server Database Engine administrators. Most of the threats are related to the `USER WITH PASSWORD` authentication process, which moves the authentication boundary from the Database Engine level to the database level. Hence, disabling this flag is recommended. This recommendation is applicable to SQL Server database instances.

## Impact{% #impact %}

When `contained database authentication` is off (`0`) for the instance, contained databases cannot be created, or attached to the Database Engine. Turning on logging will increase the required storage over time. Mismanaged logs may cause your storage costs to increase. Setting custom flags via the command line on certain instances will cause all omitted flags to be reset to defaults. This may cause you to lose custom flags and could result in unforeseen complications or instance restarts. Because of this, it is recommended that you apply these flag changes during a period of low usage.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the [Cloud SQL Instances](https://console.cloud.google.com/sql/instances) page in the Google Cloud Console.
1. Select the SQL Server instance for which you want to enable the database flag.
1. Click **Edit**.
1. Scroll down to the **Flags** section.
1. To set a flag that has not been set on the instance before, click **Add item**, choose the flag `contained database authentication` from the drop-down menu, and set its value to `off`.
1. Click **Save**.
1. Confirm the changes under **Flags** on the Overview page.

### From the command line{% #from-the-command-line %}

Configure the `contained database authentication` database flag for every SQL Server database instance using the below command.

```
gcloud sql instances patch <INSTANCE_NAME> --database-flags "contained database authentication=off"
```

**Note**: This command will overwrite all database flags previously set. To keep the flags previously set and add new ones, include the values for all flags you want set on the instance; any flag not specifically included is set to its default value. For flags that do not take a value, specify the flag name followed by an equals sign (`=`).

## Additional Information{% #additional-information %}

- Configuring this flag does not restart the SQL Server instance.

- Some database flag settings can affect instance availability or stability and remove the instance from the Cloud SQL SLA. For information about these flags, see Operational Guidelines.

## References{% #references %}

1. [https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)
1. [https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/contained-database-authentication-server-configuration-option?view=sql-server-ver15](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/contained-database-authentication-server-configuration-option?view=sql-server-ver15)
1. [https://docs.microsoft.com/en-us/sql/relational-databases/databases/security-best-practices-with-contained-databases?view=sql-server-ver15](https://docs.microsoft.com/en-us/sql/relational-databases/databases/security-best-practices-with-contained-databases?view=sql-server-ver15)
