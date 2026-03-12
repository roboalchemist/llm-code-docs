# Source: https://clickhouse.ferndocs.com/integrations/hashboard.md

---
sidebar_label: Hashboard
sidebar_position: 132
slug: /integrations/hashboard
keywords:
  - clickhouse
  - Hashboard
  - connect
  - integrate
  - ui
  - analytics
description: >-
  Hashboard is a robust analytics platform that can be easily integrated with
  ClickHouse for real-time data analysis.
title: Connecting ClickHouse to Hashboard
doc_type: guide
---

import {CommunityMaintainedBadge} from "@site/components/Badges/CommunityMaintainedBadge"

<CommunityMaintainedBadge/>

[Hashboard](https://hashboard.com) is an interactive data exploration tool that enables anyone in your organization to track metrics and discover actionable insights. Hashboard issues live SQL queries to your ClickHouse database and is particularly useful for self-serve, ad hoc data exploration use cases.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/a9648b0b951961db4e2afb5be375e5a01f8cbb08b3942a336acd696cf9404e32/images/integrations/data-visualization/hashboard_01.png" alt="Hashboard data explorer interface showing interactive query builder and visualization" />

<br/>

This guide will walk you through the steps to connect Hashboard with your ClickHouse instance. This information is also available on Hashboard's [ClickHouse integration documentation](https://docs.hashboard.com/docs/database-connections/clickhouse).

## Pre-requisites [#pre-requisites]

- A ClickHouse database either hosted on your own infrastructure or on [ClickHouse Cloud](https://clickhouse.com/).
- A [Hashboard account](https://hashboard.com/getAccess) and project.

## Steps to connect Hashboard to ClickHouse [#steps-to-connect-hashboard-to-clickhouse]

### 1. Gather your connection details [#1-gather-your-connection-details]

To connect to ClickHouse with native TCP you need this information:

| Parameter(s)              | Description                                                                                                   |
|---------------------------|---------------------------------------------------------------------------------------------------------------|
| `HOST` and `PORT`         | Typically, the port is 9440 when using TLS, or 9000 when not using TLS.                                       |
| `DATABASE NAME`           | Out of the box there is a database named `default`, use the name of the database that you want to connect to. |
| `USERNAME` and `PASSWORD` | Out of the box the username is `default`. Use the username appropriate for your use case.                     |

The details for your ClickHouse Cloud service are available in the ClickHouse Cloud console.
Select the service that you will connect to and click **Connect**:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9de2a784fe6ef2c5c51be720b96cb4bb7ebd0838901449759f587e0df6d9034a/images/_snippets/cloud-connect-button.png" alt="ClickHouse Cloud service connect button"/>

Choose **Native**, and the details are available in an example `clickhouse-client` command.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/1ee67fa3dad36e2eae368f91c239fb2fcb17f9486a89e29b7347c0267fa1ceb7/images/_snippets/connection-details-native.png" alt="ClickHouse Cloud Native TCP connection details"/>

If you are using self-managed ClickHouse, the connection details are set by your ClickHouse administrator.


### 2. Add a new database connection in Hashboard [#2-add-a-new-database-connection-in-hashboard]

1. Navigate to your [Hashboard project](https://hashboard.com/app).
2. Open the Settings page by clicking the gear icon in the side navigation bar.
3. Click `+ New Database Connection`.
4. In the modal, select "ClickHouse."
5. Fill in the **Connection Name**, **Host**, **Port**, **Username**, **Password**, and **Database** fields with the information gathered earlier.
6. Click "Test" to validate that the connection is configured successfully.
7. Click "Add"

Your ClickHouse database is now be connected to Hashboard and you can proceed by building [Data Models](https://docs.hashboard.com/docs/data-modeling/add-data-model), [Explorations](https://docs.hashboard.com/docs/visualizing-data/explorations), [Metrics](https://docs.hashboard.com/docs/metrics), and [Dashboards](https://docs.hashboard.com/docs/dashboards). See the corresponding Hashboard documentation for more detail on these features.

## Learn more [#learn-more]

For more advanced features and troubleshooting, visit [Hashboard's documentation](https://docs.hashboard.com/).
