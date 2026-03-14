# Source: https://developer.cumul.io/guide/guides--querying-data.md

---
title: Querying data
description: Use the Luzmo Data API to query data from your datasets. Learn the API Query Syntax including dimensions, measures, filters, order, limit, and options.
url: https://developer.luzmo.com/guide/guides--querying-data
type: guide
---

# Querying data via API

You can use our API to query the data in your Luzmo dataset. This might be useful in case you'd like to:

- Visualize some data yourself in your application (e.g. in your own custom widget)
- Act based on the result of a query (e.g. only allow access to an embedded dashboard in case enough data was captured to power the dashboard)
- Offer a (scoped) export of data that is not visualized in a dashboard.
  - _If you have an embedded widget that displays your desired data, you could instead use the `getData()` method in your frontend (more info on this method can be found [here](guide/embedding--component-api-reference.md))._
- ...

In this guide, we'll first explain the different properties of the [API Query Syntax](guide/interacting-with-data--querying-data#api-query-syntax), after which you can find [some examples](guide/interacting-with-data--querying-data#query-examples).

# API Query Syntax

Via [the Data API service](api/getData.md), you can fire one or more queries simultaneously to any of the Luzmo datasets to which your token has at least `can use` access. Each query is specified as an object inside the `queries` array. Below you can see the full body structure of an API request to query data via Luzmo:

:::langSpecific{lang=shell type=backend}

```shell
---
type: file
fileName: command
switcher: true
switcherLanguage: shell
switcherType: backend
---
curl https://api.luzmo.com/0.1.0/data \
-H "Content-Type: application/json" \
-d @- << EOF
{
  "action": "get",
  "version": "0.1.0",
  "key":  "$LUZMO_API_KEY",
  "token": "$LUZMO_API_TOKEN",
  "find": {
    "queries": [
      {
        "dimensions": [ { ... }, { ... },  ... ],
        "measures": [ { ... }, { ... }, ... ],
        "where": [ { ... }, { ... }, ... ],
        "order": [ { ... }, { ... }, ... ],
        "limit": { "by": ###, "offset": ### },
        "options": { ... }
      },
      ...
    ]
  }
}
EOF
```

:::

:::langSpecific{lang=javascript type=backend}

```javascript
---
type: file
fileName: server.js
switcher: true
switcherLanguage: javascript
switcherType: backend
---
const Luzmo = require('@luzmo/nodejs-sdk');
const client = new Luzmo({
  api_key: "< your API key >",
  api_token: "< your API token >"
});
const data = await client.query({
  queries: [
    {
      dimensions: [ { ... }, { ... },  ... ],
      measures: [ { ... }, { ... }, ... ],
      where: [ { ... }, { ... }, ... ],
      order: [ { ... }, { ... }, ... ],
      limit: { by: ###, offset: ### },
      options: { ... }
    },
    ...
  ]
});
```

:::

:::langSpecific{lang=php type=backend}

```php
---
type: file
fileName: server.php
switcher: true
switcherLanguage: php
switcherType: backend
---
<?php
$client = Luzmo::initialize(
  "< your API key >",
  "< your API token >"
);

$data = $client->query(
  array(
    "queries" => array(
      array(
        "dimensions" => array(
          array( ... ),
          array( ... ),
          ...
        ),
        "measures" => array(
          array( ... ),
          array( ... ),
          ...
        ),
        "where" => array(
          array( ... ),
          array( ... ),
          ...
        ),
        "order" => array(
          array( ... ),
          array( ... ),
          ...
        ),
        "limit" => array(
          "by" => ###,
          "offset" => ###
        ),
        "options" => array( ... )
      ),
      ...
    )
  )
);
?>
```

:::

:::langSpecific{lang=java type=backend}

```java
---
type: file
fileName: server.java
switcher: true
switcherLanguage: java
switcherType: backend
---
import org.json.JSONObject;
import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableMap;

private Luzmo client = new Luzmo("< Your API key >", "< Your API token >");

private JSONObject data = client.query(
  ImmutableMap.of(
    "queries", ImmutableList.of(
      ImmutableMap.of(
        "dimensions", ImmutableList.of(
          ImmutableMap.of( ... ),
          ImmutableMap.of( ... ),
          ...
        ),
        "measures", ImmutableList.of(
          ImmutableMap.of( ... ),
          ImmutableMap.of( ... ),
          ...
        ),
        "where", ImmutableList.of(
          ImmutableMap.of( ... ),
          ImmutableMap.of( ... ),
          ...
        ),
        "order", ImmutableList.of(
          ImmutableMap.of( ... ),
          ImmutableMap.of( ... ),
          ...
        ),
        "limit", ImmutableMap.of(
          "by", ###,
          "offset", ###
        ),
        "options", ImmutableMap.of( ... )
      ),
      ...
    )
  )
);
```

:::

:::langSpecific{lang=python type=backend}

```python
---
type: file
fileName: server.py
switcher: true
switcherLanguage: python
switcherType: backend
---
from luzmo.luzmo import Luzmo

client = Luzmo(
  "<your Luzmo API key>",
  "<your Luzmo API token>",
  "https://api.luzmo.com"
)

data = client.get("data",
  {
    "queries": [
      {
        "dimensions": [ { ... }, { ... },  ... ],
        "measures": [ { ... }, { ... }, ... ],
        "where": [ { ... }, { ... }, ... ],
        "order": [ { ... }, { ... }, ... ],
        "limit": {
          "by": ###,
          "offset": ###
        },
        "options": { ... }
      },
      ...
    ]
  }
)
```

:::

:::langSpecific{lang=csharp type=backend}

```csharp
---
type: file
fileName: server.cs
switcher: true
switcherLanguage: csharp
switcherType: backend
---
Luzmo client = new Luzmo("< Your API key >", "< Your API token >");

dynamic query = new {
  dimensions = new List<dynamic> {
    new { ... },
    new { ... },
    ...
  },
  measures = new List<dynamic> {
    new { ... },
    new { ... },
    ...
  },
  where = new List<dynamic> {
    new { ... },
    new { ... },
    ...
  },
  order = new List<dynamic> {
    new { ... },
    new { ... },
    ...
  },
  limit = new {
    by = ###,
    offset = ###
  },
  options = new { ... }
};

dynamic queries = new { queries = new List<dynamic> { query } };

dynamic data = client.query(queries);
Console.WriteLine(data);
// Prints: [["spicy", 1256],
//          ["sweet",  913]]
```

:::

:::info

**Note:**
The above API request can be made with

- an **API key &#x26; token**, and should in that case **happen in your backend** to not expose your API key and token
- or with an **end user's Embed key &#x26; token**, and can be made **in your frontend or backend** in that case

The token must have **at least `can use` access right to the dataset(s)** to allow querying the dataset freely (more info about different access rights in [this Academy article](https://academy.luzmo.com/article/fj43vjtj)).

When querying data with an Embed token, its context will be taken into account; e.g. [parameter overrides](guide/dashboard-embedding--handling-multi-tenant-data.md) to filter to specific data points, [connection overrides](guide/dashboard-embedding--handling-multi-tenant-data.md) (account_overrides) to point towards different data sources, etc.
:::


## Section Index

This reference is split into separate files. **For LLM agents**: Match the user's question to the headers below and read only the relevant sub-file(s).

### [Dimensions](https://developer.luzmo.com/guide/guides--querying-data--dimensions.md)


### [Measures](https://developer.luzmo.com/guide/guides--querying-data--measures.md)

- Aggregating a column
- Aggregation formula

### [Where](https://developer.luzmo.com/guide/guides--querying-data--where.md)

- Filter groups
- Filters
- Filter examples
  - Single filter
  - And filter group
  - Or filter group
  - Nested filter groups

### [Having](https://developer.luzmo.com/guide/guides--querying-data--having.md)

- Having filters
- Having filter examples
  - Simple "having" filter examples
  - "Having" filter group examples

### [Order](https://developer.luzmo.com/guide/guides--querying-data--order.md)


### [Limit](https://developer.luzmo.com/guide/guides--querying-data--limit.md)


### [Options](https://developer.luzmo.com/guide/guides--querying-data--options.md)


### [Simple example](https://developer.luzmo.com/guide/guides--querying-data--simple-example.md)


### [Advanced example](https://developer.luzmo.com/guide/guides--querying-data--advanced-example.md)


### [Formulas example](https://developer.luzmo.com/guide/guides--querying-data--formulas-example.md)



---

## Related Pages

- [Retrieving Luzmo resource IDs](https://developer.luzmo.com/guide/guides--retrieving-luzmo-resource-ids.md): Learn how to find unique identifiers for Luzmo resources like dashboards, charts, datasets, columns, connections, and collections through the UI or API.
- [Pushing data](https://developer.luzmo.com/guide/guides--pushing-data.md): Learn to programmatically store data in Luzmo's OLAP database using the Data API to create new datasets, append or replace data in existing datasets.
- [Developing custom charts](https://developer.luzmo.com/guide/guides--custom-charts.md): Create specialized data visualizations with complete flexibility using Luzmo's Custom Chart Builder. Design exactly the chart types your data needs.
- [Creating a Flex chart](https://developer.luzmo.com/guide/guides--creating-a-column-flex-chart.md): Step-by-step walkthrough to create a simple Column chart using Luzmo's Flex SDK, including slots, options, filters, and interactivity features.
- [Creating an AI Chat Assistant](https://developer.luzmo.com/guide/guides--creating-an-iq-chat-component.md)


---

## Sitemap

- [Official best practices and implementation guidelines](https://developer.luzmo.com/AGENTS.md)
- [Overview of all docs pages](https://developer.luzmo.com/llms.txt)
