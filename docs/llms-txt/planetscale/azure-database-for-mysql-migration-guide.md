# Source: https://planetscale.com/docs/vitess/imports/azure-database-for-mysql-migration-guide.md

# Azure Database for MySQL migration guide

## Overview

This document will demonstrate how to migrate a database from Azure Database for MySQL to PlanetScale. We recommend reading through the [Database import documentation](/docs/vitess/imports/database-imports) to learn how our import tool works before proceeding.

## Prerequisites

Before you can perform the migration, you’ll need to gather the following information from you MySQL instance in Azure:

* Server name
* Server admin login name
* Server admin password
* Database name

The server name and admin login name can be located on the **Overview** tab of the MySQL instance in Azure.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-server-name-and-server-admin-login-name-located-in-the-azure-dashboard.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=ab06902db06f591fb7bba9cb32d54240" alt="The server name and server admin login name located in the Azure dashboard." data-og-width="1718" width="1718" data-og-height="498" height="498" data-path="docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-server-name-and-server-admin-login-name-located-in-the-azure-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-server-name-and-server-admin-login-name-located-in-the-azure-dashboard.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=0325c637fd86580988221ea7793647b9 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-server-name-and-server-admin-login-name-located-in-the-azure-dashboard.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=4fbd300ea20a99c25ec9b7e4b182bd54 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-server-name-and-server-admin-login-name-located-in-the-azure-dashboard.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=66a68acb59302ecb0e4bce676573e525 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-server-name-and-server-admin-login-name-located-in-the-azure-dashboard.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=0b847cff2e57589b65a5ec30b39767eb 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-server-name-and-server-admin-login-name-located-in-the-azure-dashboard.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=57cd45105387c49785c91f914fc8a5b6 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-server-name-and-server-admin-login-name-located-in-the-azure-dashboard.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=3553eccd702281809393f43625d9102a 2500w" />
</Frame>

The server admin password is the same password you set when initially creating the database instance.

To view your available databases, select the **Databases** tab from the sidebar.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-databases-tab-of-the-azure-dashboard.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=c4f0137e8d4d1e74c6c14a30f1a7ff13" alt="The databases tab of the Azure dashboard." data-og-width="865" width="865" data-og-height="502" height="502" data-path="docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-databases-tab-of-the-azure-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-databases-tab-of-the-azure-dashboard.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=1ec22cfd71ba14b2974094f902de2ce2 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-databases-tab-of-the-azure-dashboard.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=e40edfe07bc174966fb80581733b8882 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-databases-tab-of-the-azure-dashboard.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=8315091123225c46e82a24dad9f38946 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-databases-tab-of-the-azure-dashboard.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=292f473dc25a690150d4ac857a4dbade 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-databases-tab-of-the-azure-dashboard.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=e2dffd1fff7f45765df1b4d557064a92 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-databases-tab-of-the-azure-dashboard.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=3829e160532e4160e236f132606b625e 2500w" />
</Frame>

## Configure firewall rules

In order for PlanetScale to connect to your Azure database, you must allow traffic into the database through the associated security group. The specific IP addresses you will need to allow depend on the region you plan to host your PlanetScale database. Check the [Import tool public IP addresses page](/docs/vitess/imports/import-tool-migration-addresses) to determine the IP addresses to allow before continuing. This guide will use the **AWS us-east-1 (North Virginia)** region so we’ll allow the following addresses:

```
3.209.149.66
3.215.97.46
34.193.111.15
23.23.187.137
52.6.141.108
52.70.2.89
50.17.188.76
52.2.251.189
52.72.234.74
35.174.68.24
52.5.253.172
54.156.81.4
34.200.24.255
35.174.79.154
44.199.177.24
```

To allow traffic into your Azure database, navigate to the “**Networking**” section from the sidebar and locate the **Firewall rules** section. There are already a series of inputs allowing you to add entries into the Firewall rules, each of which will permit network traffic from that IP address. Add a new entry for each address required, then click “Save” from the toolbar.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-networking-tab-of-the-azure-dashboard.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=b4c43428b328d74e2b04fe4aac038a99" alt="The networking tab of the Azure dashboard." data-og-width="1709" width="1709" data-og-height="939" height="939" data-path="docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-networking-tab-of-the-azure-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-networking-tab-of-the-azure-dashboard.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=69283b905bddd01b09112b3cd01bda82 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-networking-tab-of-the-azure-dashboard.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=10d08764b66f8016ac3a80aa92f48cd5 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-networking-tab-of-the-azure-dashboard.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=88d6034957b727585a9f69e268fc58fb 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-networking-tab-of-the-azure-dashboard.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=d451e19cc31a5c4abf52f2028a612046 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-networking-tab-of-the-azure-dashboard.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=9667387b6c046de943001ba45147e19c 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/the-networking-tab-of-the-azure-dashboard.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=d6abcd587ae30b5f90362159af195723 2500w" />
</Frame>

## Configure MySQL server settings

There are three settings that need to be configured before you can import your database:

* gtid\_mode
* enforce\_gtid\_consistency
* binlog\_row\_image

To access these settings in Azure, select “**Server parameters**” from the sidebar and enter “**gtid**” in the search bar. Set both “**enforce\_gtid\_consistency**” and “**gtid\_mode**” to “**ON**”. Next, search for “**binlog\_row\_image**” and set to “**full**”. Click “**Save**”.

<Note>
  For “**gtid\_mode**”, you’ll need to update the value in sequence displayed in the dropdown until it is set to “**ON**”. For example, if the current setting is “**OFF\_PERMISSIVE**”, you’ll need to first change it to “**ON\_PERMISSIVE**”, save the changes, then set it to “**ON**” in that order.
</Note>

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/how-to-access-gtid-settings-in-the-azure-dashboard.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=953cfd080082e485f14b880cf1f0b0f1" alt="How to access gtid settings in the Azure dashboard." data-og-width="2132" width="2132" data-og-height="1274" height="1274" data-path="docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/how-to-access-gtid-settings-in-the-azure-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/how-to-access-gtid-settings-in-the-azure-dashboard.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=b3f2d8018eb69cba4fd43a11dbbad2af 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/how-to-access-gtid-settings-in-the-azure-dashboard.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=b9c9ca3fe51779243fa5356f4a840ef2 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/how-to-access-gtid-settings-in-the-azure-dashboard.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=2d196faebb8ca2ea838da32858d085e0 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/how-to-access-gtid-settings-in-the-azure-dashboard.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=088b295f20f50b12b3d7cb0fec18f1ff 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/how-to-access-gtid-settings-in-the-azure-dashboard.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=73954ad2f4b9fe663f954f35edb9a3f3 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/azure-database-for-mysql-migration-guide/how-to-access-gtid-settings-in-the-azure-dashboard.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=b98bdd22315bbbd7cd3be29cad590c57 2500w" />
</Frame>

## Import your database

Now that your Azure Database for MySQL is configured and ready, follow the [Database Imports guide](/docs/vitess/imports/database-imports) to complete your import.

When filling out the connection form in the import workflow, use the following information:

* **Host name** - Your Azure server name (from Prerequisites)
* **Port** - 3306 (default for Azure MySQL)
* **Database name** - The exact database name to import
* **Username** - Your server admin login name
* **Password** - Your server admin password
* **SSL verification mode** - Select "**Verify Identity**" (Verify certificate and hostname)

The Database Imports guide will walk you through:

* Creating your PlanetScale database
* Connecting to your Azure MySQL database
* Validating your configuration
* Selecting tables to import
* Monitoring the import progress
* Switching traffic and completing the import

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt