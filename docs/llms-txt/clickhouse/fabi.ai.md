# Source: https://clickhouse.ferndocs.com/integrations/fabi.ai.md

---
sidebar_label: Fabi.ai
slug: /integrations/fabi.ai
keywords:

- clickhouse
- Fabi.ai
- connect
- integrate
- notebook
- ui
- analytics
description: >-
  Fabi.ai is an all-in-one collaborate data analysis platform. You can leverage
  SQL, Python, AI, and no-code to build dashboard and data workflows faster than
  ever before
title: Connect ClickHouse to Fabi.ai
doc_type: guide

---

import {CommunityMaintainedBadge} from "@site/components/Badges/CommunityMaintainedBadge"

<CommunityMaintainedBadge/>

<a href="https://www.fabi.ai/" target="_blank">Fabi.ai</a> is an all-in-one collaborate data analysis platform. You can leverage SQL, Python, AI, and no-code to build dashboard and data workflows faster than ever before. Combined with the scale and power of ClickHouse, you can build and share your first highly performant dashboard on a massive dataset in minutes.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/031e72ed3714dc3ab842368d0e893093e1b2f703728fdcfb0c3e2e98887ad527/images/integrations/data-visualization/fabi_01.png" alt="Fabi.ai data exploration and workflow platform" />

## Gather Your Connection Details [#gather-your-connection-details]

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

## Create your Fabi.ai account and connect ClickHouse [#connect-to-clickhouse]

Log in or create your Fabi.ai account: https://app.fabi.ai/

1. You’ll be prompted to connect your database when you first create your account, or if you already have an account, click on the data source panel on the left of any Smartbook and select Add Data Source.

   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5f35aaa91f5d22aadaed9e82e727f89c5bca6d0a304b98492940a184e8c7ec4f/images/integrations/data-visualization/fabi_02.png" alt="Add data source" />

2. You’ll then be prompted to enter your connection details.

   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f6beb20409ec7aacff72aeb6681c788d85385231f860ae25545b94c0aaddd9f2/images/integrations/data-visualization/fabi_03.png" alt="ClickHouse credentials form" />

3. Congratulations! You have now integrated ClickHouse into Fabi.ai.

## Querying ClickHouse. [#querying-clickhouse]

Once you’ve connected Fabi.ai to ClickHouse, go to any [Smartbook](https://docs.fabi.ai/analysis_and_reporting/smartbooks) and create a SQL cell. If you only have one data source connected to your Fabi.ai instance, the SQL cell will automatically default to ClickHouse, otherwise you can choose the source to query from the source dropdown.

   <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/df0b7a939278682e6df6b6e9a1992ea9917da4baae33c5822c7311dbf15ec257/images/integrations/data-visualization/fabi_04.png" alt="Querying ClickHouse" />

## Additional Resources [#additional-resources]

[Fabi.ai](https://www.fabi.ai) documentation: https://docs.fabi.ai/introduction

[Fabi.ai](https://www.fabi.ai) getting started tutorial videos: https://www.youtube.com/playlist?list=PLjxPRVnyBCQXxxByw2CLC0q7c-Aw6t2nl
