# Source: https://clickhouse.ferndocs.com/integrations/astrato.md

---
sidebar_label: Astrato
sidebar_position: 131
slug: /integrations/astrato
keywords:
  - clickhouse
  - Power BI
  - connect
  - integrate
  - ui
  - data apps
  - data viz
  - embedded analytics
  - Astrato
description: >-
  Astrato brings true Self-Service BI to Enterprises & Data Businesses by
  putting analytics in the hands of every user, enabling them to build their own
  dashboards, reports and data apps, enabling the answering of data questions
  without IT help. Astrato accelerates adoption, speeds up decision-making, and
  unifies analytics, embedded analytics, data input, and data apps in one
  platform. Astrato unites action and analytics in one,  introduce live
  write-back, interact with ML models, accelerate your analytics with AI – go
  beyond dashboarding, thanks to pushdown SQL support in Astrato.
title: Connecting Astrato to ClickHouse
doc_type: guide
integration:
  - support_level: partner
  - category: data_visualization
---

import {CommunityMaintainedBadge} from "@site/components/Badges/CommunityMaintainedBadge"

<CommunityMaintainedBadge/>

Astrato uses Pushdown SQL to query ClickHouse Cloud or on-premise deployments directly. This means you can access all of the data you need, powered by the industry-leading performance of ClickHouse.

## Connection data required [#connection-data-required]

When setting up your data connection, you'll need to know:

- Data connection: Hostname, Port

- Database Credentials: Username, Password

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


## Creating the data connection to ClickHouse [#creating-the-data-connection-to-clickhouse]

- Select **Data** in the sidebar, and select the **Data Connection** tab
(or, navigate to this link: https://app.astrato.io/data/sources)
​
- Click on the **New Data Connection** button in the top right side of the screen.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/6242d93cdface35a2f0876ff26cce578c54585c0e63f87b43474e4cb2819e65f/images/integrations/data-visualization/astrato_1_dataconnection.png" alt="Astrato Data Connection" />

- Select **ClickHouse**.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/4570b01db11b9ff85702564fd8cba96b723b1d782b0a788252efcb854b748223/images/integrations/data-visualization/astrato_2a_clickhouse_connection.png" alt="Astrato ClickHouse Data Connection" />

- Complete the required fields in the connection dialogue box

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/0c31391841bd6a2d53664118898da8468b0813bbc82fe53fc92997a29a577095/images/integrations/data-visualization/astrato_2b_clickhouse_connection.png" alt="Astrato connect to ClickHouse required fields" />

- Click **Test Connection**. If the connection is successful, give the data connection a **name** and click **Next.**

- Set the **user access** to the data connection and click **connect.**

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/ac773702796b6fe9e0fcd1c324d1742c2fac3e2db93c0f17d2a030dd7455d10d/images/integrations/data-visualization/astrato_3_user_access.png" alt="Astrato connect to ClickHouse User Access" />

-   A connection is created and a dataview is created.

<Note>
if a duplicate is created, a timestamp is added to the data source name.
</Note>

## Creating a semantic model / data view [#creating-a-semantic-model--data-view]

In our Data View editor, you will see all of your Tables and Schemas in ClickHouse, select some to get started.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/e9a92a758794058d82480abbe16e59af8b8d306c09502133a45a2413687ed2ab/images/integrations/data-visualization/astrato_4a_clickhouse_data_view.png" alt="Astrato connect to ClickHouse User Access" />

Now that you have your data selected, go to define the **data view**. Click define on the top right of the webpage.

In here, you are able to join data, as well as, **create governed dimensions and measures** - ideal for driving consistency in business logic across various teams.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/3334e1412f2fd0308f6cd9783708bfa9a9611d86c7abaa744bb1911c19a65282/images/integrations/data-visualization/astrato_4b_clickhouse_data_view_joins.png" alt="Astrato connect to ClickHouse User Access" />

**Astrato intelligently suggests joins** using your meta data, including leveraging the keys in ClickHouse. Our suggested joins make it easy for you to gets started, working from your well-governed ClickHouse data, without reinventing the wheel. We also show you **join quality** so that you have the option to review all suggestions, in detail, from Astrato.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/c4c5e6205a26821bbda0c814e43b512c3278af3b0c66661d310bf0797617a50d/images/integrations/data-visualization/astrato_4c_clickhouse_completed_data_view.png" alt="Astrato connect to ClickHouse User Access" />

## Creating a dashboard [#creating-a-dashboard]

In just a few steps, you can build your first chart in Astrato.
1. Open visuals panel
2. Select a visual (lets start with Column Bar Chart)
3. Add dimension(s)
4. Add measure(s)

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/dbebe1a92a7e4a178e385ed7f7694028d422567fbe3d3262f68d796c69ab2a98/images/integrations/data-visualization/astrato_5a_clickhouse_build_chart.png" alt="Astrato connect to ClickHouse User Access" />

### View generated SQL supporting each visualization [#view-generated-sql-supporting-each-visualization]

Transparency and accuracy are at the heart of Astrato. We ensure that every query generated is visible, letting you keep full control. All compute happens directly in ClickHouse, taking advantage of its speed while maintaining robust security and governance.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/1ef9d724da754abe45ffb1a3f866038513e77886db7a167d95eadbdf366d5b0a/images/integrations/data-visualization/astrato_5b_clickhouse_view_sql.png" alt="Astrato connect to ClickHouse User Access" />

### Example completed dashboard [#example-completed-dashboard]

A beautiful complete dashboard or data app isn't far away now. To see more of what we've built, head to our demo gallery on our website. https://astrato.io/gallery

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/ddb46dd62c78ac492aad12e4abb97a0957cc8fb592cba21149d91a7540639951/images/integrations/data-visualization/astrato_5c_clickhouse_complete_dashboard.png" alt="Astrato connect to ClickHouse User Access" />
