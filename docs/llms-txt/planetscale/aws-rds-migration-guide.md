# Source: https://planetscale.com/docs/vitess/imports/aws-rds-migration-guide.md

# AWS RDS migration guide

## Overview

This document will demonstrate how to migrate a database from AWS Relational Database Services (RDS) to PlanetScale.

<Note>
  This guide assumes you are using MySQL on Amazon RDS. If you are using Amazon Aurora (MySQL compatible) on RDS, follow the [Amazon Aurora migration guide](/docs/vitess/imports/amazon-aurora-migration-guide). Other database systems (non-MySQL or MariaDB databases) available through RDS will not work with the PlanetScale import tool.
</Note>

We recommend reading through the [Database import documentation](/docs/vitess/imports/database-imports) to learn how our import tool works before proceeding.

## Prerequisites

Gather the following information from the AWS Console:

* **Database endpoint address** - Located in "**Connectivity & security**" tab of your database instance
* **Port number** - Typically 3306
* **Master username and password** - Your RDS root credentials

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-connectivity-and-security-tab-of-the-database-in-rds.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=f494ca71daef8abd319078a18d2b3ec9" alt="The Connectivity & security tab of the database in RDS." data-og-width="1394" width="1394" data-og-height="970" height="970" data-path="docs/images/assets/docs/imports/aws-rds-migration-guide/the-connectivity-and-security-tab-of-the-database-in-rds.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-connectivity-and-security-tab-of-the-database-in-rds.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=e2bfaccfab57a3ab7f04c75c32a42afc 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-connectivity-and-security-tab-of-the-database-in-rds.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=0200bfd0239ca5855079e6a429f98bc1 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-connectivity-and-security-tab-of-the-database-in-rds.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=c3b4adea68ef69f8627189e202f373b1 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-connectivity-and-security-tab-of-the-database-in-rds.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=cc77bb96590d2a2a22423555965b931f 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-connectivity-and-security-tab-of-the-database-in-rds.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=23a433819344efa6d6b6896b86c29052 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-connectivity-and-security-tab-of-the-database-in-rds.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=d4924d8090823e86bc42e510ad42702f 2500w" />
</Frame>

## Step 1: Configure server settings

Your RDS database needs specific server settings configured before you can import. Follow these steps to configure GTID mode, binlog format, and sql\_mode.

### Check your current parameter group

Your Amazon RDS database is either using the default DB parameter group (e.g., default.mysql8.0) or a custom one. You can view it in the "**Configuration**" tab of your database instance.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-configuration-tab-of-the-database-view-in-rds.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=17e6b06053635fa8cdc53a25352c841c" alt="The Configuration tab of the database view in RDS." data-og-width="1362" width="1362" data-og-height="885" height="885" data-path="docs/images/assets/docs/imports/aws-rds-migration-guide/the-configuration-tab-of-the-database-view-in-rds.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-configuration-tab-of-the-database-view-in-rds.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=dc6ae79957ea6ae6ef45e2a05a5e050b 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-configuration-tab-of-the-database-view-in-rds.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=49096617798791817260f45ba6c82068 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-configuration-tab-of-the-database-view-in-rds.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=ad4b49fe29add1a38122f4c2723672c6 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-configuration-tab-of-the-database-view-in-rds.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=e78c833db058be60e5ee45f22794c5cc 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-configuration-tab-of-the-database-view-in-rds.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=1fa9ec4b16695b72a55132f5b8777cb2 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-configuration-tab-of-the-database-view-in-rds.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=5fbcb7bf7531cc6154a3b144d6f4f021 2500w" />
</Frame>

### Configure the parameter group

<Steps>
  <Step>
    If you are using the default DB parameter group, you'll need to create a new parameter group to reconfigure settings.

    To create a parameter group, select "**Parameter groups**" from the left nav and then "**Create parameter group**".

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-parameter-groups-view-in-rds.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=8795d1b9c39dc35098d6a7c7ad6cfb1e" alt="The Parameter groups view in RDS." data-og-width="1715" width="1715" data-og-height="729" height="729" data-path="docs/images/assets/docs/imports/aws-rds-migration-guide/the-parameter-groups-view-in-rds.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-parameter-groups-view-in-rds.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=8a6a08244de4f421f9a9bf398d3ac394 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-parameter-groups-view-in-rds.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=7b1c2cb6e0743e250108cb12923a12f8 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-parameter-groups-view-in-rds.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=2821d5901e5847f9d60b88cf242f0cfc 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-parameter-groups-view-in-rds.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=183a6cc3efc5d55075e3396176bb7afe 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-parameter-groups-view-in-rds.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=1eb294b513db63c06bc3d09fb0a06459 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-parameter-groups-view-in-rds.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=1fc4a1b5250f596aee5653160c34a435 2500w" />
    </Frame>

    Specify the **Parameter group family**, **Type**, **Group name**, and **Description**. All fields are required.

    * Parameter group family: mysql8.0 (or your MySQL version)
    * Type: DB Parameter Group (Note: Not "DB Cluster Parameter Group" type)
    * Group name: psmigrationgroup (or your choice)
    * Description: Parameter group for PlanetScale migration

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-form-used-to-create-a-parameter-group.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=dd2d6d551bbf121b67db6f1bea6af761" alt="The form used to create a parameter group." data-og-width="851" width="851" data-og-height="625" height="625" data-path="docs/images/assets/docs/imports/aws-rds-migration-guide/the-form-used-to-create-a-parameter-group.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-form-used-to-create-a-parameter-group.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=243521b4880e7246d561e8534d0fede3 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-form-used-to-create-a-parameter-group.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=f73d6b599275bb198ba31041d115171e 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-form-used-to-create-a-parameter-group.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=a1a2f076186dffeb59a2c86d43f9b9c9 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-form-used-to-create-a-parameter-group.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=19d0f482501e4f1a28873e95f01caa21 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-form-used-to-create-a-parameter-group.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=5426eee226a619781d098649963b6162 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-form-used-to-create-a-parameter-group.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=a6fa1846653b8fb669427cc636d756cb 2500w" />
    </Frame>

    You'll be brought back to the list of available parameter groups when you save.
  </Step>

  <Step>
    Edit the settings in your custom DB parameter group. Select your parameter group from the list.

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-list-of-parameter-groups-in-rds.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=2e5df4ee64d051a761d4dac61bccb402" alt="The list of parameter groups in RDS." data-og-width="1398" width="1398" data-og-height="296" height="296" data-path="docs/images/assets/docs/imports/aws-rds-migration-guide/the-list-of-parameter-groups-in-rds.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-list-of-parameter-groups-in-rds.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=0c9830a2300a8367386c3c15189b1e51 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-list-of-parameter-groups-in-rds.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=3d2664f422302e241eff62f3e60f6ff2 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-list-of-parameter-groups-in-rds.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=0fe73391304d28a2f7fce64ec866f526 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-list-of-parameter-groups-in-rds.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=bc0404939d1aebe6ea383de31c60cd23 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-list-of-parameter-groups-in-rds.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=1b9dbdc40d713b858fa9658aeb97a307 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-list-of-parameter-groups-in-rds.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=e21fe21bac05d00b82613b92de2bb69e 2500w" />
    </Frame>

    Click "**Edit parameters**" to unlock editing.

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-header-of-the-view-when-editing-a-parameter-group.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=08119cc3d744db24b15237d4f15f457a" alt="The header of the view when editing a parameter group." data-og-width="1374" width="1374" data-og-height="293" height="293" data-path="docs/images/assets/docs/imports/aws-rds-migration-guide/the-header-of-the-view-when-editing-a-parameter-group.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-header-of-the-view-when-editing-a-parameter-group.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=00baeaf3bac5809c23f19760f1a93f0a 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-header-of-the-view-when-editing-a-parameter-group.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=a0e8a0d6f172998869c40d81ca810681 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-header-of-the-view-when-editing-a-parameter-group.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=7a4c06d0ec5d068c7ca41c07cc67746b 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-header-of-the-view-when-editing-a-parameter-group.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=728ab3b88fdc122275609a986206edcf 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-header-of-the-view-when-editing-a-parameter-group.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=34898994ff2c9df7142a1bc273d0d825 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-header-of-the-view-when-editing-a-parameter-group.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=1c1a820d2e98fad946ddac9ad8dc6132 2500w" />
    </Frame>

    Search for "**binlog\_format**" and update:

    * binlog\_format: ROW

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-binlog_format-configuration-required.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=f1b3bd8971ffcf58dc357a310e21a0e0" alt="The binlog_format configuration required." data-og-width="1389" width="1389" data-og-height="347" height="347" data-path="docs/images/assets/docs/imports/aws-rds-migration-guide/the-binlog_format-configuration-required.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-binlog_format-configuration-required.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=dac891bcd462c138468ca2dd01de4933 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-binlog_format-configuration-required.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=793872209ea6a2be557f996849a73bf4 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-binlog_format-configuration-required.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=664c5c79ed73161b9be6de2b2d7ec12d 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-binlog_format-configuration-required.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=50e5ade40c608e28bf1b13d44e3f0a1e 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-binlog_format-configuration-required.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=86136925c73293f699e4b206ac6ca625 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-binlog_format-configuration-required.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=5613c34282fe236222d7540f8ed56268 2500w" />
    </Frame>

    Search for "**gtid**" and update:

    * gtid-mode: ON
    * enforce\_gtid\_consistency: ON

    Search for "**sql\_mode**" and update:

    * sql\_mode: NO\_ZERO\_IN\_DATE,NO\_ZERO\_DATE,ONLY\_FULL\_GROUP\_BY

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-gtid-configurations-that-are-required.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=55edf3b3c4455e133be34024547e390c" alt="The GTID configurations that are required." data-og-width="1377" width="1377" data-og-height="977" height="977" data-path="docs/images/assets/docs/imports/aws-rds-migration-guide/the-gtid-configurations-that-are-required.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-gtid-configurations-that-are-required.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=4456f5b16ad17fcd2c82848e05e30ea2 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-gtid-configurations-that-are-required.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=08338d920e050cf67a2daf99eca3b545 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-gtid-configurations-that-are-required.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=87c61a4e4fbbf89c5194b0ad1e5028b0 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-gtid-configurations-that-are-required.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=9e57f4be6d349c121dd9c2f717c328fa 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-gtid-configurations-that-are-required.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=b3213ef7eaa9f71d407f6c75bb594757 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-gtid-configurations-that-are-required.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=99bdbca00d7c7341c6435459e0cb6540 2500w" />
    </Frame>

    Click "**Save changes**".
  </Step>

  <Step>
    Associate the parameter group to your database. Select "**Databases**" from the left nav, check the **select box** next to your database instance, and click "**Modify**".

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-list-of-databases-in-rds.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=96eeb7470cdab8debb088431bd19dfcf" alt="The list of databases in RDS." data-og-width="1406" width="1406" data-og-height="782" height="782" data-path="docs/images/assets/docs/imports/aws-rds-migration-guide/the-list-of-databases-in-rds.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-list-of-databases-in-rds.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=b068c468f0ee86a1b41b5377e2a47747 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-list-of-databases-in-rds.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=dfb55df507086ec41e5da6ad370d02ea 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-list-of-databases-in-rds.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=0b594c9ea0dba0e21f1093c49b75f11f 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-list-of-databases-in-rds.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=0fdb4eb5c94b3844337176efda0a1650 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-list-of-databases-in-rds.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=90bf8770dcf1b6ff28c9ec69fdedd240 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-list-of-databases-in-rds.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=ee687367d153fbeb45f08f0a48ed0fe7 2500w" />
    </Frame>

    Scroll to **Additional configuration** section. Update the **DB parameter group** to your new parameter group. Click "**Continue**".

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-additional-configuration-section-of-the-database-configuration-view.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=9ad37f2425a5f9dcd1dff618d683689a" alt="The Additional configuration section of the database configuration view." data-og-width="816" width="816" data-og-height="307" height="307" data-path="docs/images/assets/docs/imports/aws-rds-migration-guide/the-additional-configuration-section-of-the-database-configuration-view.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-additional-configuration-section-of-the-database-configuration-view.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=dfae9771e8f0607d24eb671c4b5aaa82 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-additional-configuration-section-of-the-database-configuration-view.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=1ead96bd4d4e2897fb3c6d631e463718 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-additional-configuration-section-of-the-database-configuration-view.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=3feaac5cc81f88822f736cad33f03b65 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-additional-configuration-section-of-the-database-configuration-view.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=c7a533ddedfddfffee5d347e9ec8c987 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-additional-configuration-section-of-the-database-configuration-view.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=3531db2c381faf6295e74a56e3d68e0f 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-additional-configuration-section-of-the-database-configuration-view.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=d5c9c7eaf15ef58dc92165054b6bf311 2500w" />
    </Frame>

    Choose when to apply:

    * **Apply during the next scheduled maintenance window** - Applied during maintenance window
    * **Apply immediately** - Applied now, but requires manual reboot

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-confirmation-view-that-is-displayed-when-modifying-rds-database-settings.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=1ee70e0553a9158d61f67317f530bd56" alt="The confirmation view that is displayed when modifying RDS database settings." data-og-width="805" width="805" data-og-height="643" height="643" data-path="docs/images/assets/docs/imports/aws-rds-migration-guide/the-confirmation-view-that-is-displayed-when-modifying-rds-database-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-confirmation-view-that-is-displayed-when-modifying-rds-database-settings.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=e8ff88d65cd326a7151057a07b6d5e8e 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-confirmation-view-that-is-displayed-when-modifying-rds-database-settings.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=cc30674f7a363dbe0fb9d110bf2d0f05 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-confirmation-view-that-is-displayed-when-modifying-rds-database-settings.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=9844c443eb94bb6ee803a88a6c9d6c40 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-confirmation-view-that-is-displayed-when-modifying-rds-database-settings.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=c036b5d81df84dc52d6c8f65da610b78 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-confirmation-view-that-is-displayed-when-modifying-rds-database-settings.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=d356b434c83d9844a353788906991286 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-confirmation-view-that-is-displayed-when-modifying-rds-database-settings.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=b79870916839e51e2edeeed5dd1655f3 2500w" />
    </Frame>

    Click "**Modify DB instance**".
  </Step>

  <Step>
    Reboot your database instance to apply the settings. Click "**Actions**" > "**Reboot**".

    <Warning>
      This will briefly disconnect active users! The parameter group changes won't take effect without a reboot.
    </Warning>

    You'll be presented with a page to confirm the database you want to reboot. Click "**Confirm**" and the database will begin rebooting.

    If you opted to apply changes immediately, monitor the status on the "**Configuration**" tab. The page does not automatically update, so refresh to check status.

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-configuration-tab-with-the-new-parameter-group-applying.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=189da81d821db253e547ac212270178a" alt="The configuration tab with the new parameter group applying." data-og-width="1378" width="1378" data-og-height="888" height="888" data-path="docs/images/assets/docs/imports/aws-rds-migration-guide/the-configuration-tab-with-the-new-parameter-group-applying.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-configuration-tab-with-the-new-parameter-group-applying.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=de27ad5c4f397f20dff9abb112752993 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-configuration-tab-with-the-new-parameter-group-applying.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=67f8bda0d1224ff2709cbe890ffc2fea 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-configuration-tab-with-the-new-parameter-group-applying.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=cee1585da284ea0fea4b1c8613f38509 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-configuration-tab-with-the-new-parameter-group-applying.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=5c5e50029370069cf34e160b8837a6de 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-configuration-tab-with-the-new-parameter-group-applying.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=b91215045b11fa8064a398621f9d6a63 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-configuration-tab-with-the-new-parameter-group-applying.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=15f2c9de6f4dc231d24662c2d97e9ee9 2500w" />
    </Frame>
  </Step>
</Steps>

## Step 2: Enable binary logging

Binary logging must be enabled for the import to work. On RDS, binary logging is tied to automated backups.

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

PlanetScale needs to connect to your RDS database over the internet. Check that your database is publicly accessible.

In your database instance, go to "**Connectivity & security**" tab. Under "**Security**", check if **Publicly accessible** is set to "Yes". If it says "No", you'll need to modify the database settings to enable public access.

If you cannot make the database publicly accessible, [contact us](https://planetscale.com/contact) to discuss alternative import options.

## Step 5: Create a migration user

Create a dedicated user with limited privileges for the import process.

Connect to your RDS database using the MySQL command line with your master credentials:

```bash  theme={null}
mysql -u admin -p -h [your-rds-endpoint]
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

Navigate to "**Connectivity & security**" tab of your database instance and click the VPC security group link.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-connectivity-and-security-tab-of-the-database-view-in-rds.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=870e66547a25ea0fe921cf9f76434045" alt="The Connectivity & security tab of the database view in RDS." data-og-width="1382" width="1382" data-og-height="970" height="970" data-path="docs/images/assets/docs/imports/aws-rds-migration-guide/the-connectivity-and-security-tab-of-the-database-view-in-rds.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-connectivity-and-security-tab-of-the-database-view-in-rds.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=01072f83f4a0c3b2c218dbaa3a8dd8b6 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-connectivity-and-security-tab-of-the-database-view-in-rds.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=952f795452721e33f4b1a30c1d25e560 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-connectivity-and-security-tab-of-the-database-view-in-rds.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=5978d00aa27bf9a2fd417e91e5bc8f4e 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-connectivity-and-security-tab-of-the-database-view-in-rds.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=d3ddfff1680a82a748bb36cbdac364be 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-connectivity-and-security-tab-of-the-database-view-in-rds.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=7c4695ec2d28bbb69338d71d8398ff25 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-connectivity-and-security-tab-of-the-database-view-in-rds.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=31e2b24301f8349cfbfd23f5766ddd68 2500w" />
</Frame>

Select "**Inbound rules**" tab, then "**Edit inbound rules**".

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-view-of-security-groups-associated-with-the-rds-instance.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=3b08f2a427d49727fc071e4ed86628e5" alt="The view of security groups associated with the RDS instance." data-og-width="1440" width="1440" data-og-height="981" height="981" data-path="docs/images/assets/docs/imports/aws-rds-migration-guide/the-view-of-security-groups-associated-with-the-rds-instance.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-view-of-security-groups-associated-with-the-rds-instance.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=4361d5f6db9992f61cff08bf4fca6b00 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-view-of-security-groups-associated-with-the-rds-instance.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=8898bad933120556731dd9697c830c7d 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-view-of-security-groups-associated-with-the-rds-instance.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=875859633e5875a7b367ff14c82160d8 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-view-of-security-groups-associated-with-the-rds-instance.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=ae2a1524936bb8d70e73ef517cc305ee 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-view-of-security-groups-associated-with-the-rds-instance.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=d6228cb6a412d00dea0ef241691dfb63 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-view-of-security-groups-associated-with-the-rds-instance.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=14195e865041f44f93373829eac5a713 2500w" />
</Frame>

Click "**Add rule**", then:

* **Type**: Select `MYSQL/Aurora`
* **Source**: Enter the first PlanetScale IP address (AWS will format it as `x.x.x.x/32`)

Repeat for each IP address in your region, then click "**Save rules**".

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-edit-inbound-rules-view-where-source-traffic-can-be-allowed.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=6f47823af9b1ac30ac4539403d1a0215" alt="The Edit inbound rules view where source traffic can be allowed." data-og-width="1419" width="1419" data-og-height="597" height="597" data-path="docs/images/assets/docs/imports/aws-rds-migration-guide/the-edit-inbound-rules-view-where-source-traffic-can-be-allowed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-edit-inbound-rules-view-where-source-traffic-can-be-allowed.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=299ad1895dd115798b1f074186f94665 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-edit-inbound-rules-view-where-source-traffic-can-be-allowed.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=9a4db15d937996c2536f0f8146dc5b62 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-edit-inbound-rules-view-where-source-traffic-can-be-allowed.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=282321b8f65b2b2103eacc14078e4a12 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-edit-inbound-rules-view-where-source-traffic-can-be-allowed.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=ef4dd2841399ed274fde95bf2284a2af 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-edit-inbound-rules-view-where-source-traffic-can-be-allowed.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=e9134bff585bde08831853c5f760b064 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/aws-rds-migration-guide/the-edit-inbound-rules-view-where-source-traffic-can-be-allowed.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=0b4a9650b59e4d07cc63cba65021873d 2500w" />
</Frame>

## Importing your database

Now that your RDS database is configured, follow the [Database Imports guide](/docs/vitess/imports/database-imports) to complete your import.

When filling out the connection form in the import workflow, use:

* **Host name** - Your RDS endpoint address (from Prerequisites)
* **Port** - 3306 (or your custom port)
* **Database name** - The exact database name to import
* **Username** - `migration_user`
* **Password** - The password you set in Step 5
* **SSL verification mode** - Select based on your RDS SSL configuration

The Database Imports guide will walk you through:

* Creating your PlanetScale database
* Connecting to your RDS database
* Validating your configuration
* Selecting tables to import
* Monitoring the import progress
* Switching traffic and completing the import

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt