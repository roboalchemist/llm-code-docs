# Source: https://docs.datadoghq.com/security/default_rules/1f5-hbg-tw6.md

---
title: The Azure PostgreSQL database server should use geo-redundant backups
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Azure PostgreSQL database server
  should use geo-redundant backups
---

# The Azure PostgreSQL database server should use geo-redundant backups
 
## Description{% #description %}

PostgreSQL uses geo-redundant backups.

## Rationale{% #rationale %}

Using geo-redundancy with PostgreSQL creates geographically distributed replicas by default. These replicas assist with achieving data durability, as they protect against data becoming unavailable because of a regional event, such as a natural disaster. You can select this option only at the time of database creation. To modify an existing database to use geo-redundancy, recreate the database.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Follow the instructions listed at [Tutorial: Design an Azure Database for PostgreSQL - Single Server using the Azure portal](https://docs.microsoft.com/en-us/azure/postgresql/tutorial-design-database-using-azure-portal) to create a new PostgreSQL database. Ensure **Geo-redundant** is selected under **Backup redundancy options**.

### From the command line{% #from-the-command-line %}

1. Follow the steps listed at [Tutorial: Design an Azure Database for PostgreSQL - Single Server using Azure CLI](https://docs.microsoft.com/en-us/azure/postgresql/tutorial-design-database-using-azure-cli) to create and deploy a PostgreSQL server.

1. When configuring the [`az postgres server create` Microsoft Azure Module](https://docs.microsoft.com/en-us/cli/azure/postgres/server?view=azure-cli-latest#az-postgres-server-create) ensure that `geoRedundantBackup` is set to `Enabled`, as shown in the example below.

   ```
    az postgres server create 
        -l northeurope 
        -g mygroup 
        -n mysvr 
        -u username 
        -p password 
        --sku-name my_sku
        --ssl-enforcement Enabled 
        --minimal-tls-version TLS1_0 
        --public-network-access Disabled 
        --backup-retention 10 
        --geo-redundant-backup Enabled 
        --storage-size 51200 
        --tags "key=value" 
        --version 11
   ```
