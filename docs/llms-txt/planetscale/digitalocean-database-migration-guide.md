# Source: https://planetscale.com/docs/vitess/imports/digitalocean-database-migration-guide.md

# DigitalOcean database migration guide

## Introduction

In this article, we’ll walk through migrating a MySQL database from DigitalOcean to PlanetScale using the [Import tool](/docs/vitess/imports/database-imports).

<Note>
  This guide assumes you are using MySQL on DigitalOcean. Other database systems available through DigitalOcean will not work with the PlanetScale import tool.
</Note>

We recommend reading through the [Database import documentation](/docs/vitess/imports/database-imports) to learn how our import tool works before proceeding.

## Prerequisites

Before you can start migrating your database, you’ll also need to collect the following information from your DigitalOcean cluster:

* The admin username and password
* The database host
* The port
* Database name

Most of this information is located on the landing page of your cluster.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-overview-of-the-database-cluster.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=c9e7e15e82cf7202d443b36e1c6f70e4" alt="The Overview of the database cluster." data-og-width="1342" width="1342" data-og-height="1059" height="1059" data-path="docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-overview-of-the-database-cluster.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-overview-of-the-database-cluster.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=7df4fb8892c73001128aa6d6d56f52b2 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-overview-of-the-database-cluster.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=64437172759b90063a9bb7e9e6b0a680 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-overview-of-the-database-cluster.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=48643c53388ef8c235bdd63e37050ff0 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-overview-of-the-database-cluster.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=bd02cb6cdf5b1da6161c374c3c63f1c9 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-overview-of-the-database-cluster.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=f2611e7eb2547be58e478cd2409e6fa7 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-overview-of-the-database-cluster.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=8c57f3afe13a6f2b074437af1126c306 2500w" />
</Frame>

You can view the list of databases in the "**Users & Databases**" tab. This article will use the default database created when the cluster was initialized, named `defaultdb`.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-users-and-databases-view-of-the-cluster-with-the-databases-section-highlighted.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=d1988d9296dd60f89781ea4be7491f64" alt="The Users & Databases view of the cluster with the Databases section highlighted." data-og-width="1255" width="1255" data-og-height="939" height="939" data-path="docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-users-and-databases-view-of-the-cluster-with-the-databases-section-highlighted.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-users-and-databases-view-of-the-cluster-with-the-databases-section-highlighted.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=96f9165d512fb484e881405266d68ce3 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-users-and-databases-view-of-the-cluster-with-the-databases-section-highlighted.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=a9a3fd91ff59df0607196c747ac30eea 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-users-and-databases-view-of-the-cluster-with-the-databases-section-highlighted.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=8844885233da239fc9851726f84edb7f 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-users-and-databases-view-of-the-cluster-with-the-databases-section-highlighted.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=861ed4aaaed4bf79e66696e3893269b0 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-users-and-databases-view-of-the-cluster-with-the-databases-section-highlighted.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=353028bec14f5ef8bbc9446460cb65c8 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-users-and-databases-view-of-the-cluster-with-the-databases-section-highlighted.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=fd42ee81d8cecfbbb727200b7d9fd740 2500w" />
</Frame>

<Note>
  If you don’t know the admin password, you can create a new set of credentials using the information on the [Import
  tool user permissions page](/docs/vitess/imports/import-tool-user-requirements) to create an account that can be used to
  import your database.
</Note>

## Update trusted sources

In order for PlanetScale to connect to your DigitalOcean database, you must allow network traffic into the database by adding the necessary IP addresses to the trusted sources list in DigitalOcean. The specific IP addresses you will need to allow depend on the region you plan to host your PlanetScale database. Check the [Import tool public IP addresses page](/docs/vitess/imports/import-tool-migration-addresses) to determine the IP addresses to allow before continuing. This guide will use the **AWS us-east-1 (North Virginia)** region so we’ll allow the following addresses:

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

In the DigitalOcean dashboard, navigate to the “**Settings”** tab of your database and locate **Trusted sources** in the list of configuration items. Click “**Edit”** and the row should change to allow edits to the setting.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-settings-tab-of-the-database-cluster-in-digital-ocean.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=876280400c684db84ca3a19175791793" alt="The Settings tab of the database cluster in Digital Ocean." data-og-width="1238" width="1238" data-og-height="1138" height="1138" data-path="docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-settings-tab-of-the-database-cluster-in-digital-ocean.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-settings-tab-of-the-database-cluster-in-digital-ocean.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=cbb5f3e7ca96add99d099eca7818d56b 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-settings-tab-of-the-database-cluster-in-digital-ocean.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=f8a813ec71c54eb8a87c0d4d65e40686 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-settings-tab-of-the-database-cluster-in-digital-ocean.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=20d823bbae7a4ec5d1a350b7e8fb7e4b 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-settings-tab-of-the-database-cluster-in-digital-ocean.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=d0cf323fa24748dab67f242924a9ac44 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-settings-tab-of-the-database-cluster-in-digital-ocean.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=eda0d8da872cee5617daa5d0c987402a 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-settings-tab-of-the-database-cluster-in-digital-ocean.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=43715ce6485db29b4fd93034c6914dd5 2500w" />
</Frame>

When you enter an IP address from the list, a message will appear below the input box asking if you want to add that IP as an address. Click that message to add it to the list. Repeat this step for each IP address that needs to be added, then click “**Save**” once you are done.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-trusted-sources-section-of-the-settings-tab.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=1c6f421babeb8f50dd29d236b4b6ae91" alt="The Trusted sources section of the Settings tab." data-og-width="959" width="959" data-og-height="217" height="217" data-path="docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-trusted-sources-section-of-the-settings-tab.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-trusted-sources-section-of-the-settings-tab.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=7db4cb24bb79c0e7ec89dc0085037776 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-trusted-sources-section-of-the-settings-tab.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=b7ee64abcb3f544e5d44874979e6312f 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-trusted-sources-section-of-the-settings-tab.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=e28835e70e272e956116885b683d1cd9 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-trusted-sources-section-of-the-settings-tab.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=20e6f58b843b4ff96fa7cfc7840d56c8 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-trusted-sources-section-of-the-settings-tab.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=9106142f106dff2fad18e8388cc2811f 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-trusted-sources-section-of-the-settings-tab.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=712a76156c9a446ec24e06e134637e92 2500w" />
</Frame>

### Disable ANSI\_QUOTES setting

The default settings for MySQL databases on DigitalOcean is to have `ANSI_QUOTES` enabled in the global MySQL settings, which is not supported by PlanetScale. To remove this setting, navigate to the "**Settings**" tab of your cluster and locate the section titled **Global SQL mode**. Click “**Edit**” in that section to change the configuration settings.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-settings-tab-of-the-database-cluster-in-digitalocean-with-the-global-sql-mode-section-highlighted.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=46a07a4b638e150e5e915f9df9190c55" alt="The Settings tab of the database cluster in DigitalOcean with the Global SQL mode section highlighted." data-og-width="1284" width="1284" data-og-height="1123" height="1123" data-path="docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-settings-tab-of-the-database-cluster-in-digitalocean-with-the-global-sql-mode-section-highlighted.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-settings-tab-of-the-database-cluster-in-digitalocean-with-the-global-sql-mode-section-highlighted.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=e0fd887db72f0c8449732a5d51736dc3 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-settings-tab-of-the-database-cluster-in-digitalocean-with-the-global-sql-mode-section-highlighted.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=9e8ab0aae3f9191178fd93224aaa9ee5 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-settings-tab-of-the-database-cluster-in-digitalocean-with-the-global-sql-mode-section-highlighted.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=7d87626df046bc513a366854be38ac82 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-settings-tab-of-the-database-cluster-in-digitalocean-with-the-global-sql-mode-section-highlighted.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=29c9fdb902871c72c86789cbe0cccc0a 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-settings-tab-of-the-database-cluster-in-digitalocean-with-the-global-sql-mode-section-highlighted.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=c67678e09413f45e306b886d3eda1fc4 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/imports/digitalocean-database-migration-guide/the-settings-tab-of-the-database-cluster-in-digitalocean-with-the-global-sql-mode-section-highlighted.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=d629e6f430ad2bb51fef85f4f3b7a11b 2500w" />
</Frame>

To remove the `ANSI_QUOTES` setting, click the “**x**” next to the tag and click “**Save**.” The change should apply immediately.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/digitalocean-database-migration-guide/an-example-of-removing-the-ansi_quotes-setting-from-the-global-sql-mode-settings.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=46afdb19de1802b33a4d7d1c3b244aff" alt="An example of removing the ANSI_QUOTES setting from the Global SQL mode settings." data-og-width="1197" width="1197" data-og-height="517" height="517" data-path="docs/images/assets/docs/imports/digitalocean-database-migration-guide/an-example-of-removing-the-ansi_quotes-setting-from-the-global-sql-mode-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/digitalocean-database-migration-guide/an-example-of-removing-the-ansi_quotes-setting-from-the-global-sql-mode-settings.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=50e6ea837ad6c5a2ea8fa48309ecb1b0 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/digitalocean-database-migration-guide/an-example-of-removing-the-ansi_quotes-setting-from-the-global-sql-mode-settings.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=ca1c83660b8782fe58e55dd71bcf0c1f 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/digitalocean-database-migration-guide/an-example-of-removing-the-ansi_quotes-setting-from-the-global-sql-mode-settings.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=f9cbc7dac22a3e23756bdc3992fba68e 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/digitalocean-database-migration-guide/an-example-of-removing-the-ansi_quotes-setting-from-the-global-sql-mode-settings.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=d61300f8358d8186bd3eae13e12445ce 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/digitalocean-database-migration-guide/an-example-of-removing-the-ansi_quotes-setting-from-the-global-sql-mode-settings.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=3f8819115ee251c66df4181340fe3b2c 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/imports/digitalocean-database-migration-guide/an-example-of-removing-the-ansi_quotes-setting-from-the-global-sql-mode-settings.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=71c7c554c673ca661ce0998a857994d2 2500w" />
</Frame>

### Set the Binlog Retention Period

The binary log related [MySQL server variables](/docs/vitess/imports/database-imports#server-configuration-issues) required for PlanetScale's importer are already set to acceptable values by default on Digital Ocean managed MySQL servers but there's one more variable to check on the "**Settings**" tab of your existing cluster.

Scroll down to "**Advanced configurations**" and ensure the "**Binlog Retention Period**" is set to the maximum value of `86400` seconds.

<img src="https://mintcdn.com/planetscale-cad1a68a/fA2eqC-FBQpMQJbO/docs/vitess/imports/digitalocean-binlog-retention.png?fit=max&auto=format&n=fA2eqC-FBQpMQJbO&q=85&s=c61467df267e15c65b1893f4f153d662" alt="Setting the binlog retention period under Advanced Configurations" data-og-width="1998" width="1998" data-og-height="582" height="582" data-path="docs/vitess/imports/digitalocean-binlog-retention.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/fA2eqC-FBQpMQJbO/docs/vitess/imports/digitalocean-binlog-retention.png?w=280&fit=max&auto=format&n=fA2eqC-FBQpMQJbO&q=85&s=4579a5703be560eb0ba103b98ef18eea 280w, https://mintcdn.com/planetscale-cad1a68a/fA2eqC-FBQpMQJbO/docs/vitess/imports/digitalocean-binlog-retention.png?w=560&fit=max&auto=format&n=fA2eqC-FBQpMQJbO&q=85&s=f2dba67341d67840b29ba44481936346 560w, https://mintcdn.com/planetscale-cad1a68a/fA2eqC-FBQpMQJbO/docs/vitess/imports/digitalocean-binlog-retention.png?w=840&fit=max&auto=format&n=fA2eqC-FBQpMQJbO&q=85&s=75bac6e6b6d11501a37ae009823d0e64 840w, https://mintcdn.com/planetscale-cad1a68a/fA2eqC-FBQpMQJbO/docs/vitess/imports/digitalocean-binlog-retention.png?w=1100&fit=max&auto=format&n=fA2eqC-FBQpMQJbO&q=85&s=a6e0fab28f5bb6c5aab6562b3d2595cc 1100w, https://mintcdn.com/planetscale-cad1a68a/fA2eqC-FBQpMQJbO/docs/vitess/imports/digitalocean-binlog-retention.png?w=1650&fit=max&auto=format&n=fA2eqC-FBQpMQJbO&q=85&s=4d18aec047292186c60cbf629599b10d 1650w, https://mintcdn.com/planetscale-cad1a68a/fA2eqC-FBQpMQJbO/docs/vitess/imports/digitalocean-binlog-retention.png?w=2500&fit=max&auto=format&n=fA2eqC-FBQpMQJbO&q=85&s=4fd0886af7792b3e30e01fa65c74f201 2500w" />

## Importing your database

Now that your DigitalOcean database is configured and ready, follow the [Database Imports guide](/docs/vitess/imports/database-imports) to complete your import.

When filling out the connection form in the import workflow, use the following information:

* **Host name** - Your DigitalOcean database host (from Prerequisites)
* **Port** - Your port (typically 25060 for DigitalOcean)
* **Database name** - The exact database name to import (e.g., `defaultdb`)
* **Username** - Your admin username
* **Password** - Your admin password
* **SSL verification mode** - Select based on your DigitalOcean SSL configuration

The Database Imports guide will walk you through:

* Creating your PlanetScale database
* Connecting to your DigitalOcean database
* Validating your configuration
* Selecting tables to import
* Monitoring the import progress
* Switching traffic and completing the import

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt