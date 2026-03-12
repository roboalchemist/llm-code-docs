# Source: https://clickhouse.ferndocs.com/integrations/lookerstudio.md

---
sidebar_label: Looker Studio
slug: /integrations/lookerstudio
keywords:

- clickhouse
- looker
- studio
- connect
- mysql
- integrate
- ui
description: >-
  Looker Studio, formerly Google Data Studio, is an online tool for converting
  data into customizable informative reports and dashboards.
title: Looker Studio
doc_type: guide
integration:
- support_level: core
- category: data_visualization

---

import {PartnerBadge} from '../../../../../components/Badges/PartnerBadge'

<PartnerBadge/>

Looker Studio can connect to ClickHouse via the MySQL interface using the official Google MySQL data source.

## ClickHouse Cloud setup [#clickhouse-cloud-setup]

## On-premise ClickHouse server setup [#on-premise-clickhouse-server-setup]

## Connecting Looker Studio to ClickHouse [#connecting-looker-studio-to-clickhouse]

First, login to https://lookerstudio.google.com using your Google account and create a new Data Source:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/962b45a865d55b4b56e4ddc7390632b6cd1be9cb073c53d9d87a4b850c33bd54/images/integrations/data-visualization/looker_studio_01.png" alt="Creating a new data source in Looker Studio interface" />

Search for the official MySQL connector provided by Google (named just **MySQL**):

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f9e563d7781d57cb0d1d208678191a2ce61494fd763d19667ddfb029944fa4a9/images/integrations/data-visualization/looker_studio_02.png" alt="MySQL connector search in Looker Studio connectors list" />

Specify your connection details. Please note that MySQL interface port is 9004 by default,
and it might be different depending on your server configuration.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/8bc09b6772b0996b900883cf9d68fc921a4228f3504000dc7539223a34bb87f7/images/integrations/data-visualization/looker_studio_03.png" alt="Specifying the ClickHouse MySQL connection details in Looker Studio" />

Now, you have two options on how to fetch the data from ClickHouse. First, you could use the Table Browser feature:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/67f44f7e0f5ebdf37fc097e235f29139344cc707e84e3dc4d3b443a322b68025/images/integrations/data-visualization/looker_studio_04.png" alt="Using the Table Browser to select ClickHouse tables in Looker Studio" />

Alternatively, you could specify a custom query to fetch your data:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/bbebe0dd269e03f658827bad018603f4fd2fc44c723448868915edd2844938a1/images/integrations/data-visualization/looker_studio_05.png" alt="Using a custom SQL query to fetch data from ClickHouse in Looker Studio" />

Finally, you should be able to see the introspected table structure and adjust the data types if necessary.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/741865c08a6d636408a70ac7b904e6bfd0d350aec956a8336442da0a60bc9dc1/images/integrations/data-visualization/looker_studio_06.png" alt="Viewing the introspected ClickHouse table structure in Looker Studio" />

Now you can proceed with exploring your data or creating a new report!

## Using Looker Studio with ClickHouse Cloud [#using-looker-studio-with-clickhouse-cloud]

When using ClickHouse Cloud, you need to enable MySQL interface first. You can do that in connection dialog, "MySQL" tab.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/7e0d6ad19bf2bd66794e71b80d3886a96d2cca072fff79204ceaf03526f57ef9/images/integrations/data-visualization/looker_studio_enable_mysql.png" alt="Enabling MySQL interface in ClickHouse Cloud settings" />

In the Looker Studio UI, choose the "Enable SSL" option. ClickHouse Cloud's SSL certificate is signed by [Let's Encrypt](https://letsencrypt.org/certificates/). You can download this root cert [here](https://letsencrypt.org/certs/isrgrootx1.pem).

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/b110705a3a28624e85d0ce8c8d79a87f8a349284f83922045547164c9c60ce0c/images/integrations/data-visualization/looker_studio_mysql_cloud.png" alt="Looker Studio connection configuration with ClickHouse Cloud SSL settings" />

The rest of the steps are the same as listed above in the previous section.
