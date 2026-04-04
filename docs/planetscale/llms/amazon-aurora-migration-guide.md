# Source: https://planetscale.com/docs/vitess/imports/amazon-aurora-migration-guide.md

# Amazon Aurora migration guide

## Overview

This document will demonstrate how to migrate a database from Amazon Aurora (MySQL compatible) to PlanetScale.

<Note>
  This guide assumes you are using Amazon Aurora (MySQL compatible) on RDS. If you are using MySQL on Amazon RDS, follow the [Amazon RDS for MySQL migration guide](/docs/vitess/imports/aws-rds-migration-guide). Other database systems (non-MySQL or MariaDB databases) available through RDS will not work with the PlanetScale import tool.
</Note>

We recommend reading through the [Database import documentation](/docs/vitess/imports/database-imports) to learn how our import tool works before proceeding.

## Prerequisites

Gather the following information from the AWS Console:

* **Database cluster endpoint address** - Located in "**Connectivity & security**" tab (use the regional cluster endpoint, not reader or writer instances)
* **Port number** - Typically 3306
* **Master username and password** - Your Aurora root credentials

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-connectivity-and-security-tab-of-the-database-in-aurora.jpg?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=56d4fa1510f417a6fe99e10aa4b3b9ae" alt="The Connectivity & security tab of the database in RDS." data-og-width="2230" width="2230" data-og-height="1356" height="1356" data-path="docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-connectivity-and-security-tab-of-the-database-in-aurora.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-connectivity-and-security-tab-of-the-database-in-aurora.jpg?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=3435cb44733b8e832b17eea2d64cabc6 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-connectivity-and-security-tab-of-the-database-in-aurora.jpg?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=62a94e0cb1875444df3953b43c1e786f 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-connectivity-and-security-tab-of-the-database-in-aurora.jpg?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=36dbb0ab9720036fed8df7d2e6642564 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-connectivity-and-security-tab-of-the-database-in-aurora.jpg?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=b4cf72c8cee58b663768046d9e6a018d 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-connectivity-and-security-tab-of-the-database-in-aurora.jpg?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=4c6cefc5818fc78ef8b9dd6a3e9de336 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-connectivity-and-security-tab-of-the-database-in-aurora.jpg?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=63aaa1d68457d381c9213d26dfa654c6 2500w" />
</Frame>

## Step 1: Configure server settings

Your Aurora database needs specific server settings configured before you can import. Follow these steps to configure GTID mode, binlog format, and sql\_mode.

### Check your current parameter group

Your Amazon Aurora database is either using the default DB cluster parameter group (e.g., default.aurora-mysql8.0) or a custom one. You can view it in the "**Configuration**" tab of your regional database cluster (not reader or writer instances).

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-configuration-tab-of-the-database-view-in-aurora.jpg?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=b10172341894e593ad7d4260cf505cca" alt="The Configuration tab of the database view in RDS." data-og-width="2232" width="2232" data-og-height="1302" height="1302" data-path="docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-configuration-tab-of-the-database-view-in-aurora.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-configuration-tab-of-the-database-view-in-aurora.jpg?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=836dc59ec2d0bcf2ae6691010f877401 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-configuration-tab-of-the-database-view-in-aurora.jpg?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=82b5eeb7c231b282c706e53260e8eaf3 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-configuration-tab-of-the-database-view-in-aurora.jpg?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=f328e5d7a91bba7cd404e82af99c8adb 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-configuration-tab-of-the-database-view-in-aurora.jpg?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=9b672d57ae4fd703a9503f4da6507f47 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-configuration-tab-of-the-database-view-in-aurora.jpg?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=9ab285a313ce44361e2e1b4ceed24c28 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-configuration-tab-of-the-database-view-in-aurora.jpg?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=9494d911a860ccfe16909d6c8cfe4560 2500w" />
</Frame>

### Configure the parameter group

<Steps>
  <Step>
    If you are using the default DB cluster parameter group, you'll need to create a new parameter group to reconfigure settings.

    To create a parameter group, select "**Parameter groups**" from the left nav and then "**Create parameter group**".

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-parameter-groups-view-in-rds.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=8795d1b9c39dc35098d6a7c7ad6cfb1e" alt="The Parameter groups view in RDS." data-og-width="1715" width="1715" data-og-height="729" height="729" data-path="docs/images/assets/docs/imports/aws-rds-migration-guide/the-parameter-groups-view-in-rds.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-parameter-groups-view-in-rds.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=8a6a08244de4f421f9a9bf398d3ac394 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-parameter-groups-view-in-rds.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=7b1c2cb6e0743e250108cb12923a12f8 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-parameter-groups-view-in-rds.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=2821d5901e5847f9d60b88cf242f0cfc 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-parameter-groups-view-in-rds.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=183a6cc3efc5d55075e3396176bb7afe 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-parameter-groups-view-in-rds.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=1eb294b513db63c06bc3d09fb0a06459 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-parameter-groups-view-in-rds.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=1fc4a1b5250f596aee5653160c34a435 2500w" />
    </Frame>

    Specify the **Parameter group family**, **Type**, **Group name**, and **Description**. All fields are required.

    * Parameter group family: aurora-mysql8.0
    * Type: DB Cluster Parameter Group (Note: Not "DB Parameter Group" type)
    * Group name: psmigrationgroup (or your choice)
    * Description: Parameter group for PlanetScale migration

    You'll be brought back to the list of available parameter groups when you save.
  </Step>

  <Step>
    Edit the settings in your custom DB cluster parameter group. Select your parameter group from the list.

    Click "**Edit parameters**" to unlock editing.

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-header-of-the-view-when-editing-a-parameter-group.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=08119cc3d744db24b15237d4f15f457a" alt="The header of the view when editing a parameter group." data-og-width="1374" width="1374" data-og-height="293" height="293" data-path="docs/images/assets/docs/imports/aws-rds-migration-guide/the-header-of-the-view-when-editing-a-parameter-group.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-header-of-the-view-when-editing-a-parameter-group.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=00baeaf3bac5809c23f19760f1a93f0a 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-header-of-the-view-when-editing-a-parameter-group.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=a0e8a0d6f172998869c40d81ca810681 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-header-of-the-view-when-editing-a-parameter-group.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=7a4c06d0ec5d068c7ca41c07cc67746b 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-header-of-the-view-when-editing-a-parameter-group.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=728ab3b88fdc122275609a986206edcf 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-header-of-the-view-when-editing-a-parameter-group.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=34898994ff2c9df7142a1bc273d0d825 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-header-of-the-view-when-editing-a-parameter-group.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=1c1a820d2e98fad946ddac9ad8dc6132 2500w" />
    </Frame>

    Search for "**gtid**" and update:

    * gtid-mode: ON
    * enforce\_gtid\_consistency: ON

    Search for "**sql\_mode**" and update:

    * sql\_mode: NO\_ZERO\_IN\_DATE,NO\_ZERO\_DATE,ONLY\_FULL\_GROUP\_BY

    Search for "**binlog\_format**" and update:

    * binlog\_format: ROW

    Click "**Save changes**".
  </Step>

  <Step>
    Associate the DB cluster parameter group to your database. Select "**Databases**" from the left nav, select your regional cluster (not writer or reader instance), and click "**Modify**".

    Scroll to **Additional configuration** section. Update the **DB cluster parameter group** to your new parameter group. Click "**Continue**".

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-additional-configuration-section-of-the-database-configuration-view.jpg?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=82138d9a79c3812f3cf7e5c3d8c764ec" alt="The Additional configuration section of the database configuration view." data-og-width="1576" width="1576" data-og-height="808" height="808" data-path="docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-additional-configuration-section-of-the-database-configuration-view.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-additional-configuration-section-of-the-database-configuration-view.jpg?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=9aedef4e72bdde152946f45737149445 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-additional-configuration-section-of-the-database-configuration-view.jpg?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=3b121c208be069162796fad087cc89f9 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-additional-configuration-section-of-the-database-configuration-view.jpg?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=029b44de7c22cadd9f61d2b3201bef2b 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-additional-configuration-section-of-the-database-configuration-view.jpg?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=deaeff2a02c3c6b3e04f40efa38488fe 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-additional-configuration-section-of-the-database-configuration-view.jpg?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=574a3e511b876c08bbe3fd53966550b2 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-additional-configuration-section-of-the-database-configuration-view.jpg?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=c78db817555447c52ca24d742206b50d 2500w" />
    </Frame>

    Choose when to apply:

    * **Apply during the next scheduled maintenance window** - Applied during maintenance window
    * **Apply immediately** - Applied now, but requires manual reboot

    Click "**Modify DB instance**".
  </Step>

  <Step>
    Reboot your database's writer instance to apply the settings. Click "**Actions**" > "**Reboot**". (Make sure you're selecting the writer instance, not the regional cluster.)

    <Warning>
      This will briefly disconnect active users! The parameter group changes won't take effect without a reboot.
    </Warning>

    Confirm the reboot. You can check the status in the databases list (click refresh to update).
  </Step>
</Steps>

## Step 2: Enable binary logging

Binary logging must be enabled for the import to work. On Aurora/RDS, binary logging is tied to automated backups.

To enable binary logging, [enable automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.Enabling) by setting the backup retention period to any value greater than zero days.

Verify binary logging is enabled:

```sql  theme={null}
mysql> show variables like 'log_bin';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| log_bin       | ON    |
+---------------+-------+
```

## Step 3: Configure binlog retention

Set the binary log retention period to ensure logs aren't purged during the import. For most cases, 48 hours is sufficient, but larger imports may need more time.

<Warning>
  Longer retention periods use more disk space. Evaluate your binlog size to avoid running out of disk space. Contact [PlanetScale Support](https://support.planetscale.com/hc/en-us) if you need assistance.
</Warning>

Set the retention period using the `mysql.rds_set_configuration()` procedure:

```sql  theme={null}
CALL mysql.rds_set_configuration('binlog retention hours', 48);
```

Verify the setting:

```sql  theme={null}
CALL mysql.rds_show_configuration;
```

Expected output:

```
+------------------------+-------+-----------------------------------------------------------------------------------------------------------+
| name                   | value | description                                                                                               |
+------------------------+-------+-----------------------------------------------------------------------------------------------------------+
| binlog retention hours | 48    | binlog retention hours specifies the duration in hours before binary logs are automatically deleted.      |
+------------------------+-------+-----------------------------------------------------------------------------------------------------------+
```

## Step 4: Ensure database is publicly accessible

PlanetScale needs to connect to your Aurora database over the internet. Check that your database is publicly accessible.

In the writer instance, go to "**Connectivity & security**" tab. Under "**Security**", check if **Publicly accessible** is set to "Yes". If it says "No", you'll need to modify the database settings to enable public access.

If you cannot make the database publicly accessible, [contact us](https://planetscale.com/contact) to discuss alternative import options.

## Step 5: Create a migration user

Create a dedicated user with limited privileges for the import process.

Connect to your Aurora database using the MySQL command line with your master credentials:

```bash  theme={null}
mysql -u admin -p -h [your-aurora-endpoint]
```

Run the following script, replacing the placeholders:

* `<SUPER_STRONG_PASSWORD>` - Password for the migration\_user account
* `<DATABASE_NAME>` - Name of the database you're importing

```sql  theme={null}
CREATE USER 'migration_user'@'%' IDENTIFIED BY '<SUPER_STRONG_PASSWORD>';
GRANT PROCESS, REPLICATION SLAVE, REPLICATION CLIENT, RELOAD ON *.* TO 'migration_user'@'%';
GRANT SELECT, INSERT, UPDATE, DELETE, SHOW VIEW, LOCK TABLES ON `<DATABASE_NAME>`.* TO 'migration_user'@'%';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER ON `ps\_import\_%`.* TO 'migration_user'@'%';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER ON `_vt`.* TO 'migration_user'@'%';
GRANT EXECUTE ON PROCEDURE mysql.rds_show_configuration TO 'migration_user'@'%';
GRANT SELECT ON mysql.db TO 'migration_user'@'%';
GRANT SELECT ON mysql.func TO 'migration_user'@'%';
GRANT SELECT ON mysql.tables_priv TO 'migration_user'@'%';
GRANT SELECT ON mysql.user TO 'migration_user'@'%';
GRANT SELECT ON performance_schema.* TO 'migration_user'@'%';
FLUSH PRIVILEGES;
```

Save the username and password securely - you'll need them for the import.

## Step 6: Configure RDS security group

Allow PlanetScale to connect by adding PlanetScale's IP addresses to your security group.

The specific IP addresses depend on your PlanetScale database region. These will be shown during the import workflow on the **Connect to external database** step. See the [Import public IP addresses](/docs/vitess/imports/import-tool-migration-addresses) page for more details.

### Add IP addresses to security group

1. Navigate to "**Connectivity & security**" tab of your writer instance
2. Click the VPC security group link

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-connectivity-and-security-tab-of-the-database-view-in-aurora.jpg?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=6a7b857e848b0af7e7f5937365489c1a" alt="The Connectivity & security tab of the database view in RDS." data-og-width="2230" width="2230" data-og-height="1346" height="1346" data-path="docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-connectivity-and-security-tab-of-the-database-view-in-aurora.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-connectivity-and-security-tab-of-the-database-view-in-aurora.jpg?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=121d0c141db1e1b2cac3c9309c5b89d6 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-connectivity-and-security-tab-of-the-database-view-in-aurora.jpg?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=eff3ed1dcd20cd6043838b09262533fb 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-connectivity-and-security-tab-of-the-database-view-in-aurora.jpg?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=10477f61a03b78d09682cabdd1ffca60 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-connectivity-and-security-tab-of-the-database-view-in-aurora.jpg?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=c6df3fc2c1ed1268312f5e08db69f309 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-connectivity-and-security-tab-of-the-database-view-in-aurora.jpg?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=bbc1925d231063f51495a5c2427c9f77 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/amazon-aurora-migration-guide/the-connectivity-and-security-tab-of-the-database-view-in-aurora.jpg?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=9b44971e88332cd55682c8dcec17156b 2500w" />
</Frame>

3. Select "**Inbound rules**" tab, then "**Edit inbound rules**"

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-view-of-security-groups-associated-with-the-rds-instance.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=3b08f2a427d49727fc071e4ed86628e5" alt="The view of security groups associated with the RDS instance." data-og-width="1440" width="1440" data-og-height="981" height="981" data-path="docs/images/assets/docs/imports/aws-rds-migration-guide/the-view-of-security-groups-associated-with-the-rds-instance.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-view-of-security-groups-associated-with-the-rds-instance.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=4361d5f6db9992f61cff08bf4fca6b00 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-view-of-security-groups-associated-with-the-rds-instance.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=8898bad933120556731dd9697c830c7d 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-view-of-security-groups-associated-with-the-rds-instance.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=875859633e5875a7b367ff14c82160d8 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-view-of-security-groups-associated-with-the-rds-instance.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=ae2a1524936bb8d70e73ef517cc305ee 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-view-of-security-groups-associated-with-the-rds-instance.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=d6228cb6a412d00dea0ef241691dfb63 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-view-of-security-groups-associated-with-the-rds-instance.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=14195e865041f44f93373829eac5a713 2500w" />
</Frame>

4. Click "**Add rule**"
5. **Type**: Select `MYSQL/Aurora`
6. **Source**: Enter the first PlanetScale IP address (AWS will format it as `x.x.x.x/32`)
7. Repeat for each IP address in your region
8. Click "**Save rules**"

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-edit-inbound-rules-view-where-source-traffic-can-be-allowed.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=6f47823af9b1ac30ac4539403d1a0215" alt="The Edit inbound rules view where source traffic can be allowed." data-og-width="1419" width="1419" data-og-height="597" height="597" data-path="docs/images/assets/docs/imports/aws-rds-migration-guide/the-edit-inbound-rules-view-where-source-traffic-can-be-allowed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-edit-inbound-rules-view-where-source-traffic-can-be-allowed.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=299ad1895dd115798b1f074186f94665 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-edit-inbound-rules-view-where-source-traffic-can-be-allowed.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=9a4db15d937996c2536f0f8146dc5b62 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-edit-inbound-rules-view-where-source-traffic-can-be-allowed.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=282321b8f65b2b2103eacc14078e4a12 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-edit-inbound-rules-view-where-source-traffic-can-be-allowed.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=ef4dd2841399ed274fde95bf2284a2af 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-edit-inbound-rules-view-where-source-traffic-can-be-allowed.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=e9134bff585bde08831853c5f760b064 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-edit-inbound-rules-view-where-source-traffic-can-be-allowed.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=0b4a9650b59e4d07cc63cba65021873d 2500w" />
</Frame>

## Importing your database

Now that your Aurora database is configured, follow the [Database Imports guide](/docs/vitess/imports/database-imports) to complete your import.

When filling out the connection form in the import workflow, use:

* **Host name** - Your Aurora cluster endpoint address (from Prerequisites)
* **Port** - 3306 (or your custom port)
* **Database name** - The exact database name to import
* **Username** - `migration_user`
* **Password** - The password you set in Step 5
* **SSL verification mode** - Select based on your Aurora SSL configuration

The Database Imports guide will walk you through:

* Creating your PlanetScale database
* Connecting to your Aurora database
* Validating your configuration
* Selecting tables to import
* Monitoring the import progress
* Switching traffic and completing the import

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt