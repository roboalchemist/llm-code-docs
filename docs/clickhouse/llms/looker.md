# Source: https://clickhouse.ferndocs.com/integrations/looker.md

---
sidebar_label: Looker
slug: /integrations/looker
keywords:
  - clickhouse
  - looker
  - connect
  - integrate
  - ui
description: >-
  Looker is an enterprise platform for BI, data applications, and embedded
  analytics that helps you explore and share insights in real time.
title: Looker
doc_type: guide
integration:
  - support_level: partner
  - category: data_visualization
---

import {PartnerBadge} from '../../../../../components/Badges/PartnerBadge'

<PartnerBadge/>

Looker can connect to ClickHouse Cloud or on-premise deployment via the official ClickHouse data source.

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


## 2. Create a ClickHouse data source [#2-create-a-clickhouse-data-source]

Navigate to Admin -> Database -> Connections and click the "Add Connection" button in the top right corner.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/7c5494bcb9f6a22fe7fada95bc3152001622db5319147081dd06d6238d5a86be/images/integrations/data-visualization/looker_01.png" alt="Adding a new connection in Looker's database management interface" />

Choose a name for your data source, and select `ClickHouse` from the dialect drop-down. Enter your credentials in the form.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/4f0ddb98b923a52dc1f5849d286909851868151ac8d9a8d7498ce30ca31b96d0/images/integrations/data-visualization/looker_02.png" alt="Specifying your ClickHouse credentials in Looker connection form" />

If you are using ClickHouse Cloud or your deployment requires SSL, make sure you have SSL turned on in the additional settings.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9e30d3d5530b33d2e5e1ccb1a366745852fe7b4bfc05a3f6318beec95d137eba/images/integrations/data-visualization/looker_03.png" alt="Enabling SSL for ClickHouse connection in Looker settings" />

Test your connection first, and, once it is done, connect to your new ClickHouse data source.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/58332c60a3ffe7bd3c27922152cb9fcf732e296cad55e0c43dc8c5ad72298d31/images/integrations/data-visualization/looker_04.png" alt="Testing and connecting to the ClickHouse data source" />

Now you should be able to attach ClickHouse Datasource to your Looker project.

## 3. Known limitations [#3-known-limitations]

1. The following data types are handled as strings by default:
   * Array - serialization does not work as expected due to the JDBC driver limitations
   * Decimal* - can be changed to number in the model
   * LowCardinality(...) - can be changed to a proper type in the model
   * Enum8, Enum16
   * UUID
   * Tuple
   * Map
   * JSON
   * Nested
   * FixedString
   * Geo types
     * MultiPolygon
     * Polygon
     * Point
     * Ring
2. [Symmetric aggregate feature](https://cloud.google.com/looker/docs/reference/param-explore-symmetric-aggregates) is not supported
3. [Full outer join](https://cloud.google.com/looker/docs/reference/param-explore-join-type#full_outer) is not yet implemented in the driver
