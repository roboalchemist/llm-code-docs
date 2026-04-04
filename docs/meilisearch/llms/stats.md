# Stats
Source: https://www.meilisearch.com/docs/reference/api/stats

The /stats route you gives extended information and metrics about indexes and the Meilisearch database.

The `/stats` route gives extended information and metrics about indexes and the Meilisearch database.

## Stats object

```json theme={null}
{
  "databaseSize": 447819776,
  "usedDatabaseSize": 196608,
  "lastUpdate": "2019-11-15T11:15:22.092896Z",
  "indexes": {
    "movies": {
      "numberOfDocuments": 19654,
      "numberOfEmbeddedDocuments": 1,
      "numberOfEmbeddings": 1,
      "rawDocumentDbSize": 5320,
      "avgDocumentSize": 92,
      "isIndexing": false,
      "fieldDistribution": {
        "poster": 19654,
        "overview": 19654,
        "title": 19654,
        "id": 19654,
        "release_date": 19654
      }
    },
    "books": {
      "numberOfDocuments": 5,
      "numberOfEmbeddedDocuments": 5,
      "numberOfEmbeddings": 10,
      "rawDocumentDbSize": 8780,
      "avgDocumentSize": 422,
      "isIndexing": false,
      "fieldDistribution": {
        "id": 5,
        "title": 5,
        "author": 5,
        "price": 5, 
        "genres": 5
      }
    }
  }
}
```

| Name                            | Type    | Description                                                                                                  |
| ------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------ |
| **`databaseSize`**              | Integer | Storage space claimed by Meilisearch and LMDB in bytes                                                       |
| **`usedDatabaseSize`**          | Integer | Storage space used by the database in bytes, excluding unused space claimed by LMDB                          |
| **`lastUpdate`**                | String  | When the last update was made to the database in the [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format |
| **`indexes`**                   | Object  | Object containing the statistics for each index found in the database                                        |
| **`numberOfDocuments`**         | Integer | Total number of documents in an index                                                                        |
| **`numberOfEmbeddedDocuments`** | Integer | Total number of documents with at least one embedding                                                        |
| **`numberOfEmbeddings`**        | Integer | Total number of embeddings in an index                                                                       |
| **`rawDocumentDbSize`**         | Integer | Storage space claimed by all documents in the index in bytes                                                 |
| **`avgDocumentDbSize`**         | Integer | Total size of the documents stored in an index divided by the number of documents in that same index         |
| **`isIndexing`**                | Boolean | If `true`, the index is still processing documents and attempts to search will result in undefined behavior  |
| **`fieldDistribution`**         | Object  | Shows every field in the index along with the total number of documents containing that field in said index  |

<Note>
  `fieldDistribution` is not impacted by `searchableAttributes` or `displayedAttributes`. Even if a field is not displayed or searchable, it will still appear in the `fieldDistribution` object.
</Note>

## Get stats of all indexes

<RouteHighlighter method="GET" />

Get stats of all indexes.

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/stats'
  ```

  ```javascript JS theme={null}
  client.getStats()
  ```

  ```python Python theme={null}
  client.get_all_stats()
  ```

  ```php PHP theme={null}
  $client->stats();
  ```

  ```java Java theme={null}
  client.getStats();
  ```

  ```ruby Ruby theme={null}
  client.stats
  ```

  ```go Go theme={null}
  client.GetStats()
  ```

  ```csharp C# theme={null}
  await client.GetStatsAsync();
  ```

  ```rust Rust theme={null}
  let stats: ClientStats = client
    .get_stats()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.allStats { (result) in
      switch result {
      case .success(let stats):
          print(stats)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.getStats();
  ```
</CodeGroup>

#### Response: `200 Ok`

```json theme={null}
{
  "databaseSize": 447819776,
  "usedDatabaseSize": 196608,
  "lastUpdate": "2019-11-15T11:15:22.092896Z",
  "indexes": {
    "movies": {
      "numberOfDocuments": 19654,
      "numberOfEmbeddedDocuments": 1,
      "numberOfEmbeddings": 1,
      "rawDocumentDbSize": 2087,
      "avgDocumentSize": 41,
      "isIndexing": false,
      "fieldDistribution": {
        "poster": 19654,
        "overview": 19654,
        "title": 19654,
        "id": 19654,
        "release_date": 19654
      }
    },
    "books": {
      "numberOfDocuments": 5,
      "numberOfEmbeddedDocuments": 5,
      "numberOfEmbeddings": 10,
      "isIndexing": false,
      "fieldDistribution": {
        "id": 5,
        "title": 5,
        "author": 5,
        "price": 5, 
        "genres": 5
      }
    }
  }
}
```

## Get stats of an index

<RouteHighlighter method="GET" />

Get stats of an index.

### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/movies/stats'
  ```

  ```javascript JS theme={null}
  client.index('movies').getStats()
  ```

  ```python Python theme={null}
  client.index('movies').get_stats()
  ```

  ```php PHP theme={null}
  $client->index('movies')->stats();
  ```

  ```java Java theme={null}
  client.index("movies").getStats();
  ```

  ```ruby Ruby theme={null}
  client.index('movies').stats
  ```

  ```go Go theme={null}
  client.Index("movies").GetStats()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").GetStatsAsync();
  ```

  ```rust Rust theme={null}
  let stats: IndexStats = client
    .index("movies")
    .get_stats()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").stats { (result) in
      switch result {
      case .success(let stats):
          print(stats)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').getStats();
  ```
</CodeGroup>

#### Response: `200 Ok`

```json theme={null}
{
  "numberOfDocuments": 19654,
  "numberOfEmbeddedDocuments": 1,
  "numberOfEmbeddings": 1,
  "rawDocumentDbSize": 3618,
  "avgDocumentSize": 104,
  "isIndexing": false,
  "fieldDistribution": {
    "poster": 19654,
    "overview": 19654,
    "title": 19654,
    "id": 19654,
    "release_date": 19654
  }
}
```