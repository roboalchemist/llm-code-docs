# Source: https://clickhouse.ferndocs.com/integrations/deepnote.md

---
sidebar_label: Deepnote
sidebar_position: 11
slug: /integrations/deepnote
keywords:
  - clickhouse
  - Deepnote
  - connect
  - integrate
  - notebook
description: >-
  Efficiently query very large datasets, analyzing and modeling in the comfort
  of known notebook environment.
title: Connect ClickHouse to Deepnote
doc_type: guide
integration:
  - support_level: partner
  - category: data_visualization
  - website: 'https://deepnote.com/launch?template=ClickHouse%20and%20Deepnote'
---

import {CommunityMaintainedBadge} from "@site/components/Badges/CommunityMaintainedBadge"

<CommunityMaintainedBadge/>

<a href="https://www.deepnote.com/" target="_blank">Deepnote</a> is a collaborative data notebook built for teams to discover and share insights. In addition to being Jupyter-compatible, it works in the cloud and provides you with one central place to collaborate and work on data science projects efficiently.

This guide assumes you already have a Deepnote account and that you have a running ClickHouse instance.

## Interactive example [#interactive-example]
If you would like to explore an interactive example of querying ClickHouse from Deepnote data notebooks, click the button below to  launch a template project connected to the [ClickHouse playground](../../../getting-started/playground.md).

[<img src="https://deepnote.com/buttons/launch-in-deepnote.svg" alt="Launch in Deepnote" />](https://deepnote.com/launch?template=ClickHouse%20and%20Deepnote)

## Connect to ClickHouse [#connect-to-clickhouse]

1. Within Deepnote, select the "Integrations" overview and click on the ClickHouse tile.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/c96af0d6d25a55f1783379dcee5992176f6643ee77740ed9bffb48e338952503/images/integrations/data-visualization/deepnote_01.png" alt="ClickHouse integration tile" />

2. Provide the connection details for your ClickHouse instance:
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


   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/ee1ff684831c032c0320c7c2ab3ffef6ae480ec1e33e10c328c8e13b226841a3/images/integrations/data-visualization/deepnote_02.png" alt="ClickHouse details dialog" />

   **_NOTE:_** If your connection to ClickHouse is protected with an IP Access List, you might need to allow Deepnote's IP addresses. Read more about it in [Deepnote's docs](https://docs.deepnote.com/integrations/authorize-connections-from-deepnote-ip-addresses).

3. Congratulations! You have now integrated ClickHouse into Deepnote.

## Using ClickHouse integration. [#using-clickhouse-integration]

1. Start by connecting to the ClickHouse integration on the right of your notebook.

   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/1f900de2a70e570bd2790596a2f7734d5df3d60578b07fadac6b3b262413a901/images/integrations/data-visualization/deepnote_03.png" alt="ClickHouse details dialog" />

2. Now create a new ClickHouse query block and query your database. The query results will be saved as a DataFrame and stored in the variable specified in the SQL block.
3. You can also convert any existing [SQL block](https://docs.deepnote.com/features/sql-cells) to a ClickHouse block.
