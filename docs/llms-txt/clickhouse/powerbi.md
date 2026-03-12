# Source: https://clickhouse.ferndocs.com/integrations/powerbi.md

---
sidebar_label: Power BI
slug: /integrations/powerbi
keywords:

- clickhouse
- Power BI
- connect
- integrate
- ui
description: >-
  Microsoft Power BI is an interactive data visualization software product
  developed by Microsoft with a primary focus on business intelligence.
title: Power BI
doc_type: guide
integration:
- support_level: core
- category: data_visualization

---

import {ClickHouseSupportedBadge} from '../../../../../components/Badges/ClickHouseSupported'

<ClickHouseSupportedBadge/>

Microsoft Power BI can query or load into memory data from [ClickHouse Cloud](https://clickhouse.com/cloud) or a self-managed deployment.

There are several flavours of Power BI that you can use to visualise your data:

- Power BI Desktop: A Windows desktop application for creating Dashboards and Visualisations
- Power BI Service: Available within Azure as a SaaS to host the Dashboards created on Power BI Desktop

Power BI requires you to create your dashboards within the Desktop version and publish them to Power BI Service.

This tutorial will guide you through the process of:

- [Installing the ClickHouse ODBC Driver](#install-the-odbc-driver)
- [Installing the ClickHouse Power BI Connector into Power BI Desktop](#power-bi-installation)
- [Querying data from ClickHouse for visualization in Power BI Desktop](#query-and-visualise-data)
- [Setting up an on-premise data gateway for Power BI Service](#power-bi-service)

## Prerequisites [#prerequisites]

### Power BI Installation [#power-bi-installation]

This tutorial assumes you have Microsoft Power BI Desktop installed on your Windows machine. You can download and install Power BI Desktop [here](https://www.microsoft.com/en-us/download/details.aspx?id=58494)

We recommend updating to the latest version of Power BI. The ClickHouse Connector is available by default from version `2.137.751.0`.

### Gather your ClickHouse connection details [#gather-your-clickhouse-connection-details]

You'll need the following details for connecting to your ClickHouse instance:

- Hostname - ClickHouse
- Username - User credentials
- Password - Password of the user
- Database - Name of the database on the instance you want to connect to

## Power BI desktop [#power-bi-desktop]

To get started with querying data in Power BI Desktop, you'll need to complete the following steps:

1. Install the ClickHouse ODBC Driver
2. Find the ClickHouse Connector
3. Connect to ClickHouse
4. Query and Visualize you data

### Install the ODBC Driver [#install-the-odbc-driver]

Download the most recent [ClickHouse ODBC release](https://github.com/ClickHouse/clickhouse-odbc/releases).

Execute the supplied `.msi` installer and follow the wizard.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/51c2815e9ce12f0ef8dbe8ec161140bc6313af58afad4e074a77868035574ae4/images/integrations/data-visualization/powerbi_odbc_install.png" alt="ClickHouse ODBC driver installation wizard showing installation options" />

<Note>
`Debug symbols` are optional and not required
</Note>

#### Verify ODBC driver [#verify-odbc-driver]

When the driver installation is completed, you can verify the installation was successful by:

Searching for ODBC in the Start menu and select "ODBC Data Sources **(64-bit)**".

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/462b1d999b65a9d6fddc72c71b5e8c30a6d4a734d0929cc3543d3b54ef846fa3/images/integrations/data-visualization/powerbi_odbc_search.png" alt="Windows search showing ODBC Data Sources (64-bit) option" />

Verify the ClickHouse Driver is listed.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/ec6077983ddc8091a0c0ac171f1032f3c937ee6d537dd44b53305acb0f7b61ee/images/integrations/data-visualization/powerbi_odbc_verify.png" alt="ODBC Data Source Administrator showing ClickHouse drivers in the Drivers tab" />

### Find the ClickHouse Connector [#find-the-clickhouse-connector]

<Note>
Available in version `2.137.751.0` of Power BI Desktop
</Note>

On the Power BI Desktop start screen, click "Get Data".

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/543c03a224097569c62e1d4a4b539f68bb7f158b68490f113932f24ad0b77af5/images/integrations/data-visualization/powerbi_get_data.png" alt="Power BI Desktop home screen showing the Get Data button" />

Search for "ClickHouse"

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/4107a45574158c73e77c1269f87b8f7debca41fec9ee7254a1d0b4c43d80d50b/images/integrations/data-visualization/powerbi_search_clickhouse.png" alt="Power BI Get Data dialog with ClickHouse searched in the search bar" />

### Connect to ClickHouse [#connect-to-clickhouse]

Select the connector, and enter in the ClickHouse instance credentials:

- Host (required) - Your instance domain/address. Make sure to add it with no prefixes/suffixes.
- Port (required) - Your instance port.
- Database - Your database name.
- Options - Any ODBC option as listed
  in [ClickHouse ODBC GitHub Page](https://github.com/ClickHouse/clickhouse-odbc#configuration)
- Data Connectivity mode - DirectQuery

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/b787b5fec379f12ad4fa0fe7b540c73b0e79f40a6a60ba4823ffb85e2a7fed5c/images/integrations/data-visualization/powerbi_connect_db.png" alt="ClickHouse connection dialog showing host, port, database and connectivity mode fields" />

<Note>
We advise selecting DirectQuery for querying ClickHouse directly.

If you have a use case that has a small amount of data, you can choose import mode, and the entire data will be loaded to Power BI.
</Note>

- Specify username and password

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/c26f643967c0373b324364c36bb88f2c9e9edc0c58e86111e3529e22fb1c1daa/images/integrations/data-visualization/powerbi_connect_user.png" alt="ClickHouse connection credentials dialog for username and password" />

### Query and Visualise Data [#query-and-visualise-data]

Finally, you should see the databases and tables in the Navigator view. Select the desired table and click "Load" to
import the data from ClickHouse.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f3e92d8f0f2296768950d722890ce1ac4e05907a1488571b286420777b21db9f/images/integrations/data-visualization/powerbi_table_navigation.png" alt="Power BI Navigator view showing ClickHouse database tables and sample data" />

Once the import is complete, your ClickHouse Data should be accessible in Power BI as usual.
<br/>

## Power BI service [#power-bi-service]

In order to use Microsoft Power BI Service, you need to create an [on-premise data gateway](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-onprem).

For more details on how to setup custom connectors, please refer to Microsoft's documentation on how to [use custom data connectors with an on-premises data gateway](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-custom-connectors).

## ODBC driver (import only) [#odbc-driver-import-only]

We recommend using the ClickHouse Connector that uses DirectQuery.

Install the [ODBC Driver](#install-the-odbc-driver) onto the on-premise data gateway instance and [verify](#verify-odbc-driver) as outlined above.

### Create a new User DSN [#create-a-new-user-dsn]

When the driver installation is complete, an ODBC data source can be created. Search for ODBC in the Start menu and select "ODBC Data Sources (64-bit)".

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/462b1d999b65a9d6fddc72c71b5e8c30a6d4a734d0929cc3543d3b54ef846fa3/images/integrations/data-visualization/powerbi_odbc_search.png" alt="Windows search showing ODBC Data Sources (64-bit) option" />

We need to add a new User DSN here. Click "Add" button on the left.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/3441c48bcab26067f6da62fdd8fceb08861cabd6484fe0e94a896f3e8a7a0cc7/images/integrations/data-visualization/powerbi_add_dsn.png" alt="ODBC Data Source Administrator with Add button highlighted for creating new DSN" />

Choose the Unicode version of the ODBC driver.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/c676451cbeebf57f245aed8aa88dd30ec55236d48182ec748c78739439d08fb0/images/integrations/data-visualization/powerbi_select_unicode.png" alt="Create New Data Source dialog showing ClickHouse Unicode Driver selection" />

Fill in the connection details.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/3d2d275f7a687e875fb2f337396c82081769f79770f61d297eb0efc9cf3d7a7d/images/integrations/data-visualization/powerbi_connection_details.png" alt="ClickHouse ODBC Driver configuration dialog with connection parameters" />

<Note>
If you are using a deployment that has SSL enabled (e.g. ClickHouse Cloud or a self-managed instance), in the `SSLMode` field you should supply `require`.

- `Host` should always have the protocol (i.e. `http://` or `https://`) omitted.
- `Timeout` is an integer representing seconds. Default value: `30 seconds`.
</Note>

### Get data into Power BI [#get-data-into-power-bi]

In case you don't have Power BI installed
yet, [download and install Power BI Desktop](https://www.microsoft.com/en-us/download/details.aspx?id=58494).

On the Power BI Desktop start screen, click "Get Data".

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/543c03a224097569c62e1d4a4b539f68bb7f158b68490f113932f24ad0b77af5/images/integrations/data-visualization/powerbi_get_data.png" alt="Power BI Desktop home screen showing the Get Data button" />

Select "Other" -> "ODBC".

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/afad5e3de255d36fde3ee505e5c58103bd454f6a385e865ba1677d6e8fce95ad/images/integrations/data-visualization/powerbi_select_odbc.png" alt="Power BI Get Data dialog with ODBC option selected under the Other category" />

Select your previously created data source from the list.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/d8a814dee3a4fa5d4035e6a7bb14b94cfbb2b5a81a7a6184d02012fbf7d8b490/images/integrations/data-visualization/powerbi_select_dsn.png" alt="ODBC driver selection dialog showing the configured ClickHouse DSN" />

<Note>
If you did not specify credentials during the data source creation, you will be prompted to specify username and password.
</Note>

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/61cc2e11f41924b668e48a1a0035682f0ec690575985b9e9ec2cd20685897d3c/images/integrations/data-visualization/powerbi_dsn_credentials.png" alt="Credentials dialog for the ODBC DSN connection" />

Finally, you should see the databases and tables in the Navigator view. Select the desired table and click "Load" to import the data from ClickHouse.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f3e92d8f0f2296768950d722890ce1ac4e05907a1488571b286420777b21db9f/images/integrations/data-visualization/powerbi_table_navigation.png" alt="Power BI Navigator view showing ClickHouse database tables and sample data" />

Once the import is complete, your ClickHouse Data should be accessible in Power BI as usual.

## Known limitations [#known-limitations]

### UInt64 [#uint64]

Unsigned integer types such as UInt64 or bigger won't be loaded into the dataset automatically, as Int64 is the maximum whole number type support by Power BI.

<Note>
To import the data properly, before hitting the "Load" button in the Navigator, click "Transform Data" first.
</Note>

In this example, `pageviews` table has a UInt64 column, which is recognized as "Binary" by default.
"Transform Data" opens Power Query Editor, where we can reassign the type of the column, setting it as, for example,
Text.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/8b0e823a84a3f81c31422fa332b943004ce3703ab9928cfcd55d1fb0f1e5e8e9/images/integrations/data-visualization/powerbi_16.png" alt="Power Query Editor showing data type transformation for UInt64 column" />

Once finished, click "Close & Apply" in the top left corner, and proceed with loading the data.
