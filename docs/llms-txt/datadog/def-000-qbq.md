# Source: https://docs.datadoghq.com/security/default_rules/def-000-qbq.md

---
title: >-
  SQL Server instances should have the 'remote access' database flag set to
  'off'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SQL Server instances should have the
  'remote access' database flag set to 'off'
---

# SQL Server instances should have the 'remote access' database flag set to 'off'
 
## Description{% #description %}

It is recommended to set the `remote access` database flag for Cloud SQL SQL Server instances to `off`.

## Rationale{% #rationale %}

The remote access option controls the execution of stored procedures from local or remote servers on which instances of SQL Server are running. The default value for this option is 1. This grants permission to run local stored procedures from remote servers or remote stored procedures from the local server. To prevent local stored procedures from being run from a remote server or remote stored procedures from being run on the local server, this must be disabled. Remote access functionality can be abused to launch a Denial-of-Service (DoS) attack on remote servers by off-loading query processing to a target, so it should be disabled. This recommendation is applicable to SQL Server database instances.

## Impact{% #impact %}

Setting custom flags through the command line on certain instances causes all omitted flags to be reset to defaults. This may cause you to lose custom flags and could result in unforeseen complications or instance restarts. Because of this, it is recommended you apply these flag changes during a period of low usage.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the Cloud SQL Instances page in the Google Cloud Console by visiting [https://console.cloud.google.com/sql/instances](https://console.cloud.google.com/sql/instances).
1. Select the SQL Server instance for which you want to enable the database flag.
1. Click `Edit`.
1. Scroll down to the `Flags` section.
1. To set a flag that has not been set on the instance before, click `Add item`, choose the flag `remote access` from the drop-down menu, and set its value to `off`.
1. Click `Save` to save your changes.
1. Confirm your changes under `Flags` on the Overview page.

### From the command line{% #from-the-command-line %}

Configure the remote access database flag for every Cloud SQL SQL Server database instance using the following command:

```
gcloud sql instances patch <INSTANCE_NAME> --database-flags "remote access=off"
```

### Note:{% #note %}

This command overwrites all database flags previously set. To keep those and add new ones, include the values for all flags you want set on the instance; any flag not specifically included is set to its default value. For flags that do not take a value, specify the flag name followed by an equals sign ("=").

## Default Value{% #default-value %}

Remote access is `on` by default.

## Additional information{% #additional-information %}

Configuring the remote access database flag does not restart the Cloud SQL instance.

## References{% #references %}

1. [https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)
1. [https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-remote-access-server-configuration-option?view=sql-server-ver15](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-remote-access-server-configuration-option?view=sql-server-ver15)
1. [https://www.stigviewer.com/stig/ms_sql_server_2016_instance/2018-03-09/finding/V-79337](https://www.stigviewer.com/stig/ms_sql_server_2016_instance/2018-03-09/finding/V-79337)

## CIS Controls{% #cis-controls %}

Version 8 - 4.8 Uninstall or Disable Unnecessary Services on Enterprise Assets and Software

- Uninstall or disable unnecessary services on enterprise assets and software, such as an unused file sharing service, web application module, or service function.

Version 7 - 9.2 Ensure Only Approved Ports, Protocols and Services Are Running

- Ensure that only network ports, protocols, and services with validated business needs are listening on a system.
