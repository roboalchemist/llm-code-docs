# Source: https://clickhouse.ferndocs.com/integrations/explo.md

---
sidebar_label: Explo
sidebar_position: 131
slug: /integrations/explo
keywords:
  - clickhouse
  - Explo
  - connect
  - integrate
  - ui
description: >-
  Explo is an easy-to-use, open source UI tool for asking questions about your
  data.
title: Connecting Explo to ClickHouse
doc_type: guide
integration:
  - support_level: partner
  - category: data_visualization
---

import {CommunityMaintainedBadge} from "@site/components/Badges/CommunityMaintainedBadge"

<CommunityMaintainedBadge/>

Customer-facing analytics for any platform. Designed for beautiful visualization. Engineered for simplicity.

## Goal [#goal]

In this guide you will connect your data from ClickHouse to Explo and visualize the results.  The chart will look like this:
<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5a97a401e64a70fac92474533a9928dc08e96d3ec971c25ba7d2ebcec42f97d7/images/integrations/data-visualization/explo_15.png" alt="Explo Dashboard"/>

<p/>

<Tip title="Add some data">
If you do not have a dataset to work with you can add one of the examples.  This guide uses the [UK Price Paid](/getting-started/example-datasets/uk-price-paid.md) dataset, so you might choose that one.  There are several others to look at in the same documentation category.
</Tip>

## 1. Gather your connection details [#1-gather-your-connection-details]
To connect to ClickHouse with HTTP(S) you need this information:

| Parameter(s)            | Description                                                                                                   |
|-------------------------|---------------------------------------------------------------------------------------------------------------|
|`HOST` and `PORT`        | Typically, the port is 8443 when using TLS or 8123 when not using TLS.                                        |
|`DATABASE NAME`          | Out of the box, there is a database named `default`, use the name of the database that you want to connect to.|
|`USERNAME` and `PASSWORD`| Out of the box, the username is `default`. Use the username appropriate for your use case.                    |

The details for your ClickHouse Cloud service are available in the ClickHouse Cloud console.
Select a service and click **Connect**:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9de2a784fe6ef2c5c51be720b96cb4bb7ebd0838901449759f587e0df6d9034a/images/_snippets/cloud-connect-button.png" alt="ClickHouse Cloud service connect button" />

Choose **HTTPS**. Connection details are displayed in an example `curl` command.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/710d528cac4deb00e877550b033fe8d67e19e1a8f825c75889eb0573ab25f7b0/images/_snippets/connection-details-https.png" alt="ClickHouse Cloud HTTPS connection details" />

If you are using self-managed ClickHouse, the connection details are set by your ClickHouse administrator.


## 2.  Connect Explo to ClickHouse [#2--connect-explo-to-clickhouse]

1. Sign up for an Explo account.

2. Click on the Explo **data** tab on the left hand sidebar.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5149ca73ad775a6a61eca1614c8005823cc23c705f51bd72deeffc126d45119b/images/integrations/data-visualization/explo_01.png" alt="Data Tab"/>

3. Click **Connect Data Source** in the upper right hand side.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/1d151c37a790e29128c2171ca3a2443b933db5851559314a652a1911b7256ab3/images/integrations/data-visualization/explo_02.png" alt="Connect Data Source"/>

4. Fill out the information on the **Getting Started** page

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/8c49485a22e58a9cc5f8bc54da768ebc9cc8458f4c7a254b8b2dd5d03f4677c0/images/integrations/data-visualization/explo_03.png" alt="Getting Started"/>

5. Select **Clickhouse**

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/e80c3e53f3277cdeb6178f976116f313c8c5815af1a8231a9186b84ab19decec/images/integrations/data-visualization/explo_04.png" alt="Clickhouse"/>

6. Enter your **Clickhouse Credentials**.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/7598d1f53234f3fe750cd860181b5372632b049683e61bb48f510d624b6671b5/images/integrations/data-visualization/explo_05.png" alt="Credentials"/>

7. Configure **Security**

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9c38af64ca14179a8c0ac7b6f851bd1815154c8281af26f595f795ecc8dfff28/images/integrations/data-visualization/explo_06.png" alt="Security"/>

8. Within Clickhouse, **Whitelist the Explo IPs**.
`
54.211.43.19, 52.55.98.121, 3.214.169.94, and 54.156.141.148
`

## 3. Create a Dashboard [#3-create-a-dashboard]

1. Navigate to **Dashboard** tab on the left side nav bar.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/b2e25e8ef627b740d99d8ad5caa25d680bdfacb7072aa5cbd7b6337a28580453/images/integrations/data-visualization/explo_07.png" alt="Dashboard"/>

2. Click **Create Dashboard** in the upper right corner and name your dashboard. You've now created a dashboard!

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9dd72900912a6e806f8f19146e573215c02960bb461c20ed86a208a702513044/images/integrations/data-visualization/explo_08.png" alt="Create Dashboard"/>

3. You should now see a screen that is similar to this:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/beccb9ea9b84f6fc25ef6d338ce626d6b55efdeb7273b147e8a92605a9065bd4/images/integrations/data-visualization/explo_09.png" alt="Explo Dashboard"/>

## 4. Run a SQL query [#4-run-a-sql-query]

1. Get your table name from the right hand sidebar under your schema title. You should then put the following command into your dataset editor:
`
SELECT * FROM YOUR_TABLE_NAME
LIMIT 100
`

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/77571580c42c48e07affb89aed387655595fa0ff56c77d4d745dc40e1521f998/images/integrations/data-visualization/explo_10.png" alt="Explo Dashboard"/>

2. Now click run and go to the preview tab to see your data.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/ef59125f7b76b292922ae4262b1ba9c0e2398f985d3169b9953fcbc0960acf33/images/integrations/data-visualization/explo_11.png" alt="Explo Dashboard"/>

## 5. Build a Chart [#5-build-a-chart]

1. From the left hand side, drag the bar chart icon onto the screen.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/96574000d270d917260f5c03f78c0580be87e50c3d4697ada47e8c1e377c18b6/images/integrations/data-visualization/explo_16.png" alt="Explo Dashboard"/>

2. Select the dataset. You should now see a screen like the following:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/52d86da29a573469dc51bc458715fd55a45651ed96c0c889871b29073361c0ac/images/integrations/data-visualization/explo_12.png" alt="Explo Dashboard"/>

3. Fill out the **county** in the X Axis and **Price** in the Y Axis Section like so:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/e14f86a3db4db10121ad785df6c9852ab84ba707afc2340e7d9396843918c485/images/integrations/data-visualization/explo_13.png" alt="Explo Dashboard"/>

4. Now, change the aggregation to **AVG**.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/e813ed57df6c2d92dc7f1676f054a9f4102d681578cc0f9451bb3861d5f40704/images/integrations/data-visualization/explo_14.png" alt="Explo Dashboard"/>

5. We now have average price of homes broken down by price!

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5a97a401e64a70fac92474533a9928dc08e96d3ec971c25ba7d2ebcec42f97d7/images/integrations/data-visualization/explo_15.png" alt="Explo Dashboard"/>

## Learn more [#learn-more]

Find more information about Explo and how to build dashboards by <a href="https://docs.explo.co/" target="_blank">visiting the Explo documentation</a>.
