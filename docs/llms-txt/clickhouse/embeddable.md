# Source: https://clickhouse.ferndocs.com/integrations/embeddable.md

---
sidebar_label: Embeddable
slug: /integrations/embeddable
keywords:
  - clickhouse
  - Embeddable
  - connect
  - integrate
  - ui
description: >-
  Embeddable is a developer toolkit for building fast, interactive, fully-custom
  analytics experiences directly into your app.
title: Connecting Embeddable to ClickHouse
doc_type: guide
---

import {CommunityMaintainedBadge} from "@site/components/Badges/CommunityMaintainedBadge"

<CommunityMaintainedBadge/>

In [Embeddable](https://embeddable.com/) you define [Data Models](https://docs.embeddable.com/data-modeling/introduction) and [Components](https://docs.embeddable.com/development/introduction) in code (stored in your own code repository) and use our **SDK** to make these available for your team in the powerful Embeddable **no-code builder.**

The end result is the ability to deliver fast, interactive customer-facing analytics directly in your product; designed by your product team; built by your engineering team; maintained by your customer-facing and data teams. Exactly the way it should be.

Built-in row-level security means that every user only ever sees exactly the data they're allowed to see. And two levels of fully-configurable caching mean you can deliver fast, real time analytics at scale.

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


## 2. Create a ClickHouse connection type [#2-create-a-clickhouse-connection-type]

You add a database connection using Embeddable API. This connection is used to connect to your ClickHouse service. You can add a connection using the following API call:

```javascript
// for security reasons, this must *never* be called from your client-side
fetch('https://api.embeddable.com/api/v1/connections', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json',
    Authorization: `Bearer ${apiKey}` /* keep your API Key secure */,
  },
  body: JSON.stringify({
    name: 'my-clickhouse-db',
    type: 'clickhouse',
    credentials: {
      host: 'my.clickhouse.host',
      user: 'clickhouse_user',
      port: 8443,
      password: '*****',
    },
  }),
});

Response:
Status 201 { errorMessage: null }
```

The above represents a `CREATE` action, but all `CRUD` operations are available.

The `apiKey` can be found by clicking "**Publish**" on one of your Embeddable dashboards.

The `name` is a unique name to identify this connection.
- By default your data models will look for a connection called "default", but you can supply your models with different `data_source` names to support connecting different data models to different connections (simply specify the data_source name in the model)

The `type` tells Embeddable which driver to use

- Here you'll want to use `clickhouse`, but you can connect multiple different data sources to one Embeddable workspace so you may use others such as: `postgres`, `bigquery`, `mongodb`, etc.

The `credentials` is a JavaScript object containing the necessary credentials expected by the driver
- These are securely encrypted and only used to retrieve exactly the data you have described in your data models.
Embeddable strongly encourage you to create a read-only database user for each connection (Embeddable will only ever read from your database, not write).

In order to support connecting to different databases for prod, qa, test, etc (or to support different databases for different customers) you can assign each connection to an environment (see [Environments API](https://docs.embeddable.com/data/environments)).
