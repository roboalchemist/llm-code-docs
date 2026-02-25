# Source: https://docs.datadoghq.com/security/default_rules/def-000-luu.md

---
title: >-
  SQL Server instances should have the 'external scripts enabled' database flag
  set to 'off'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SQL Server instances should have the
  'external scripts enabled' database flag set to 'off'
---

# SQL Server instances should have the 'external scripts enabled' database flag set to 'off'

## Description{% #description %}

It is recommended to set `external scripts enabled` database flag for SQL Server instance to `off`.

## Rationale{% #rationale %}

The `external scripts enabled` flag enables the execution of scripts with certain remote language extensions. This flag is `off` by default. When Advanced Analytics Services is installed, during the set up, you can optionally set this flag to `on`. The External Scripts Enabled feature allows scripts external to SQL, such as files located in an R library, to be executed, which could adversely affect the security of the system. Hence, the flag should be disabled. This recommendation is applicable to SQL Server database instances.

## Impact{% #impact %}

Setting custom flags through the command line on certain instances can cause all omitted flags to be reset to defaults. This may cause you to lose custom flags and could result in unforeseen complications or instance restarts. Because of this, it is recommended that you apply these flag changes during a period of low usage.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the Cloud SQL Instances page in the Google Cloud Console by visiting [https://console.cloud.google.com/sql/instances](https://console.cloud.google.com/sql/instances).
1. Select the SQL Server instance for which you want to enable the database flag.
1. Click **Edit**.
1. Scroll down to the Flag section.
1. Click **Add item** to set a flag that has not been set on the instance before. Choose the flag `external scripts enabled` from the drop-down menu, and set its value to `off`.
1. Click **Save**.
1. Confirm your changes under the Flags section on the Overview page.

### From the command line{% #from-the-command-line %}

Configure the `external scripts enabled` database flag for every SQL Server database instance using the following command:

```
gcloud sql instances patch <INSTANCE_NAME> --database-flags "external scripts enabled=off"
```

Note: This command overwrites all database flags previously set. To keep those and add new ones, include the values for all flags you want set on the instance; any flag not specifically included is set to its default value. For flags that do not take a value, specify the flag name followed by an equals sign (=).

## Default Value{% #default-value %}

By default `external scripts enabled` is `off`.

## Additional information{% #additional-information %}

- Some database flag settings can affect instance availability or stability, and remove the instance from the Cloud SQL SLA. For information about these flags, see Operational Guidelines.

- Configuring the `external scripts enabled` flag restarts the Cloud SQL instance.

## References{% #references %}

1. [https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/external-scripts-enabled-server-configuration-option?view=sql-server-ver15](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/external-scripts-enabled-server-configuration-option?view=sql-server-ver15)
1. [https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)
1. [https://docs.microsoft.com/en-us/sql/advanced-analytics/concepts/security?view=sql-server-ver15](https://docs.microsoft.com/en-us/sql/advanced-analytics/concepts/security?view=sql-server-ver15)
1. [https://www.stigviewer.com/stig/ms_sql_server_2016_instance/2018-03-09/finding/V-79347](https://www.stigviewer.com/stig/ms_sql_server_2016_instance/2018-03-09/finding/V-79337)

## CIS Controls{% #cis-controls %}

Version 8 - 2.7 Allowlist Authorized Scripts

- Use technical controls, such as digital signatures and version control, to ensure that only authorized scripts, such as specific .ps1, .py, etc., files, are allowed to execute. Block unauthorized scripts from executing. Reassess bi-annually, or more frequently.

Version 7 - 2.9 Implement Application Whitelisting of Scripts

- The organization's application whitelisting software must ensure that only authorized, digitally signed scripts (such as *.ps1, *.py, macros, etc) are allowed to run on a system.
