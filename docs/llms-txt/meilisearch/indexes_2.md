# Indexes
Source: https://www.meilisearch.com/docs/reference/api/indexes

The /indexes route allows you to create, manage, and delete your indexes.

The `/indexes` route allows you to create, manage, and delete your indexes.

[Learn more about indexes](/learn/getting_started/indexes).

## Index object

```json theme={null}
{
  "uid": "movies",
  "createdAt": "2022-02-10T07:45:15.628261Z",
  "updatedAt": "2022-02-21T15:28:43.496574Z",
  "primaryKey": "id"
}
```

| Name             | Type            | Default value | Description                                                                                                                                                                                                                                                  |
| :--------------- | :-------------- | :------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`uid`**        | String          | N/A           | [Unique identifier](/learn/getting_started/indexes#index-uid) of the index. Once created, it cannot be changed                                                                                                                                               |
| **`createdAt`**  | String          | N/A           | Creation date of the index, represented in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. Auto-generated on index creation                                                                                                                         |
| **`updatedAt`**  | String          | N/A           | Latest date of index update, represented in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. Auto-generated on index creation or update                                                                                                              |
| **`primaryKey`** | String / `null` | `null`        | [Primary key](/learn/getting_started/primary_key#primary-field) of the index. If not specified, Meilisearch [guesses your primary key](/learn/getting_started/primary_key#meilisearch-guesses-your-primary-key) from the first document you add to the index |

## List all indexes

<RouteHighlighter method="GET" />

List all indexes. Results can be paginated by using the `offset` and `limit` query parameters.

### Query parameters

| Query parameter | Description                 | Default value |
| :-------------- | :-------------------------- | :------------ |
| **`offset`**    | Number of indexes to skip   | `0`           |
| **`limit`**     | Number of indexes to return | `20`          |

### Response

| Name          | Type    | Description                          |
| :------------ | :------ | :----------------------------------- |
| **`results`** | Array   | An array of [indexes](#index-object) |
| **`offset`**  | Integer | Number of indexes skipped            |
| **`limit`**   | Integer | Number of indexes returned           |
| **`total`**   | Integer | Total number of indexes              |

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes?limit=3'
  ```

  ```javascript JS theme={null}
  client.getIndexes({ limit: 3 })
  ```

  ```python Python theme={null}
  client.get_indexes({'limit': 3})
  ```

  ```php PHP theme={null}
  $client->getIndexes((new IndexesQuery())->setLimit(3));
  ```

  ```java Java theme={null}
  IndexesQuery query = new IndexesQuery().setLimit(3);
  client.getIndexes(query);
  ```

  ```ruby Ruby theme={null}
  client.indexes(limit: 3)
  ```

  ```go Go theme={null}
  client.GetIndexes(&meilisearch.IndexesQuery{
    Limit: 3,
  })
  ```

  ```csharp C# theme={null}
  await client.GetAllIndexesAsync(new IndexesQuery { Limit = 3 });
  ```

  ```rust Rust theme={null}
  let mut indexes = IndexesQuery::new(&client)
    .with_limit(3)
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.getIndexes { (result) in
      switch result {
      case .success(let indexes):
          print(indexes)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.getIndexes(params: IndexesQuery(limit: 3));
  ```
</CodeGroup>

#### Response: `200 Ok`

```json theme={null}
{
  "results": [
    {
      "uid": "books",
      "createdAt": "2022-03-08T10:00:27.377346Z",
      "updatedAt": "2022-03-08T10:00:27.391209Z",
      "primaryKey": "id"
    },
    {
      "uid": "meteorites",
      "createdAt": "2022-03-08T10:00:44.518768Z",
      "updatedAt": "2022-03-08T10:00:44.582083Z",
      "primaryKey": "id"
    },
    {
      "uid": "movies",
      "createdAt": "2022-02-10T07:45:15.628261Z",
      "updatedAt": "2022-02-21T15:28:43.496574Z",
      "primaryKey": "id"
    }
  ],
  "offset": 0,
  "limit": 3,
  "total": 5
}  
```

## Get one index

<RouteHighlighter method="GET" />

Get information about an index.

### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/movies'
  ```

  ```javascript JS theme={null}
  client.index('movies').getRawInfo()
  ```

  ```python Python theme={null}
  client.get_index('movies')
  ```

  ```php PHP theme={null}
  $client->index('movies')->fetchRawInfo();
  ```

  ```java Java theme={null}
  client.getIndex("movies");
  ```

  ```ruby Ruby theme={null}
  client.fetch_index('movies')
  ```

  ```go Go theme={null}
  client.GetIndex("movies")
  ```

  ```csharp C# theme={null}
  await client.GetIndexAsync("movies");
  ```

  ```rust Rust theme={null}
  let movies: Index = client
    .get_index("movies")
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.getIndex("movies") { (result) in
      switch result {
      case .success(let index):
          print(index)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.getIndex('movies');
  ```
</CodeGroup>

#### Response: `200 Ok`

```json theme={null}
{
  "uid": "movies",
  "createdAt": "2022-02-10T07:45:15.628261Z",
  "updatedAt": "2022-02-21T15:28:43.496574Z",
  "primaryKey": "id"
}
```

## Create an index

<RouteHighlighter method="POST" />

Create an index.

### Body

| Name             | Type            | Default value | Description                                                                              |
| :--------------- | :-------------- | :------------ | :--------------------------------------------------------------------------------------- |
| **`uid`** \*     | String          | N/A           | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index                 |
| **`primaryKey`** | String / `null` | `null`        | [`Primary key`](/learn/getting_started/primary_key#primary-field) of the requested index |

```json theme={null}
{
  "uid": "movies",
  "primaryKey": "id"
}
```

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "uid": "movies",
      "primaryKey": "id"
    }'
  ```

  ```javascript JS theme={null}
  client.createIndex('movies', { primaryKey: 'id' })
  ```

  ```python Python theme={null}
  client.create_index('movies', {'primaryKey': 'id'})
  ```

  ```php PHP theme={null}
  $client->createIndex('movies', ['primaryKey' => 'id']);
  ```

  ```java Java theme={null}
  client.createIndex("movies", "id");
  ```

  ```ruby Ruby theme={null}
  client.create_index('movies', primary_key: 'id')
  ```

  ```go Go theme={null}
  client.CreateIndex(&meilisearch.IndexConfig{
    Uid: "movies",
    PrimaryKey: "id",
  })
  ```

  ```csharp C# theme={null}
  TaskInfo task = await client.CreateIndexAsync("movies", "id");
  ```

  ```rust Rust theme={null}
  client.create_index("movies", Some("id"))
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.createIndex(uid: "movies", primaryKey: "id") { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.createIndex('movies', primaryKey: 'id');
  ```
</CodeGroup>

#### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 0,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "indexCreation",
  "enqueuedAt": "2021-08-12T10:00:00.000000Z"
}
```

You can use the response's `taskUid` to [track the status of your request](/reference/api/tasks#get-one-task).

## Update an index

<RouteHighlighter method="PATCH" />

Update an index's [primary key](/learn/getting_started/primary_key#primary-key). You can freely update the primary key of an index as long as it contains no documents.

To change the primary key of an index that already contains documents, you must first delete all documents in that index. You may then change the primary key and index your dataset again.

### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

### Body

| Name                | Type            | Default value | Description                                                                              |
| :------------------ | :-------------- | :------------ | :--------------------------------------------------------------------------------------- |
| **`primaryKey`** \* | String / `null` | N/A           | [`Primary key`](/learn/getting_started/primary_key#primary-field) of the requested index |
| **`uid`** \*        | String / `null` | N/A           | New `uid` of the requested index                                                         |

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PATCH 'MEILISEARCH_URL/indexes/movies' \
    -H 'Content-Type: application/json' \
    --data-binary '{ "primaryKey": "id" }'
  ```

  ```javascript JS theme={null}
  client.updateIndex('movies', { primaryKey: 'id' })
  ```

  ```python Python theme={null}
  client.index('movies').update(primary_key='id')
  ```

  ```php PHP theme={null}
  $client->updateIndex('movies', ['primaryKey' => 'id']);
  ```

  ```java Java theme={null}
  client.updateIndex("movies", "id");
  ```

  ```ruby Ruby theme={null}
  client.index('movies').update(primary_key: 'movie_id')
  ```

  ```go Go theme={null}
  client.Index("movies").UpdateIndex(&meilisearch.UpdateIndexRequestParams{
    PrimaryKey: "id",
  })
  ```

  ```csharp C# theme={null}
  TaskInfo task = await client.UpdateIndexAsync("movies", "id");
  ```

  ```rust Rust theme={null}
  let task = IndexUpdater::new("movies", &client)
    .with_primary_key("movie_review_id")
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").update(primaryKey: "id") { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').update(primaryKey: 'id');
  ```
</CodeGroup>

#### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "indexUpdate",
  "enqueuedAt": "2021-08-12T10:00:00.000000Z"
}
```

You can use the response's `taskUid` to [track the status of your request](/reference/api/tasks#get-one-task).

## Delete an index

<RouteHighlighter method="DELETE" />

Delete an index.

### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/movies'
  ```

  ```javascript JS theme={null}
  client.deleteIndex('movies')
  ```

  ```python Python theme={null}
  client.delete_index('movies')
  // OR
  client.index('movies').delete()
  ```

  ```php PHP theme={null}
  $client->deleteIndex('movies');
  ```

  ```java Java theme={null}
  client.deleteIndex("movies");
  ```

  ```ruby Ruby theme={null}
  client.delete_index('movies')
  ```

  ```go Go theme={null}
  client.DeleteIndex("movies")
  // OR
  client.Index("movies").Delete()
  ```

  ```csharp C# theme={null}
  await client.DeleteIndexAsync("movies");
  ```

  ```rust Rust theme={null}
  client.index("movies")
    .delete()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").delete { (result) in
      switch result {
      case .success:
          print("Index deleted")
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').delete();
  ```
</CodeGroup>

#### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "indexDeletion",
  "enqueuedAt": "2021-08-12T10:00:00.000000Z"
}
```

You can use the response's `taskUid` to [track the status of your request](/reference/api/tasks#get-one-task).

## Swap indexes

<RouteHighlighter method="POST" />

Swap the documents, settings, and task history of two or more indexes. **You can only swap indexes in pairs.** A single request can swap as many index pairs as you wish.

Swapping indexes is an atomic transaction: **either all indexes in a request are successfully swapped, or none are.** You can swap multiple pairs of indexes with a single request. To do so, there must be one object for each pair of indexes to be swapped.

Swapping `indexA` and `indexB` will also replace every mention of `indexA` by `indexB` and vice-versa in the task history. `enqueued` tasks are left unmodified.

[To learn more about index swapping, refer to this short guide.](/learn/getting_started/indexes#swapping-indexes)

### Body

An array of objects with the following fields:

| Name          | Type             | Default value | Description                                        |
| :------------ | :--------------- | :------------ | :------------------------------------------------- |
| **`indexes`** | Array of strings | N/A           | Array of the two `indexUid`s to be swapped         |
| **`rename`**  | Boolean          | `false`       | If `true`, renames an index instead of swapping it |

Each `indexes` array must contain only two elements: the `indexUid`s of the two indexes to be swapped. Sending an empty array (`[]`) is valid, but no swap operation will be performed.

Use `rename: false` if you are swapping two existing indexes. Use `rename: true` if the second index in your array does not exist.

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/swap-indexes' \
    -H 'Content-Type: application/json' \
    --data-binary '[
      {
        "indexes": [
          "indexA",
          "indexB"
        ]
      },
      {
        "indexes": [
          "indexX",
          "indexY"
        ]
      }
    ]'
  ```

  ```javascript JS theme={null}
  client.swapIndexes([
    { 'indexes': ['indexA', 'indexB'] },
    { 'indexes': ['indexX', 'indexY'] }
  ])
  ```

  ```python Python theme={null}
  client.swap_indexes([{'indexes': ['indexA', 'indexB']}, {'indexes': ['indexX', 'indexY']}])
  ```

  ```php PHP theme={null}
  $client->swapIndexes([['indexA', 'indexB'], ['indexX', 'indexY']]);
  ```

  ```java Java theme={null}
  SwapIndexesParams[] params =
          new SwapIndexesParams[] {
              new SwapIndexesParams().setIndexes(new String[] {"indexA", "indexB"}),
              new SwapIndexesParams().setIndexes(new String[] {"indexX", "indexY"})
          };
  TaskInfo task = client.swapIndexes(params);
  ```

  ```ruby Ruby theme={null}
  client.swap_indexes(['indexA', 'indexB'], ['indexX', 'indexY'])
  ```

  ```go Go theme={null}
  client.SwapIndexes([]SwapIndexesParams{
    {Indexes: []string{"indexA", "indexB"}},
    {Indexes: []string{"indexX", "indexY"}},
  })
  ```

  ```csharp C# theme={null}
  await client.SwapIndexesAsync(new List<IndexSwap> { new IndexSwap("indexA", "indexB"), new IndexSwap("indexX", "indexY") } });
  ```

  ```rust Rust theme={null}
  client.swap_indexes([
    &SwapIndexes {
      indexes: (
          "indexA".to_string(),
          "indexB".to_string(),
      ),
    }, &SwapIndexes {
      indexes: (
          "indexX".to_string(),
          "indexY".to_string(),
      ),
  }])
  ```

  ```swift Swift theme={null}
  let task = try await self.client.swapIndexes([
    ("indexA", "indexB"),
    ("indexX", "indexY")
  ])
  ```

  ```dart Dart theme={null}
  await client.swapIndexes([
    SwapIndex(['indexA', 'indexB']),
    SwapIndex(['indexX', 'indexY']),
  ]);
  ```
</CodeGroup>

#### Response

```json theme={null}
{
  "taskUid": 3,
  "indexUid": null,
  "status": "enqueued",
  "type": "indexSwap",
  "enqueuedAt": "2021-08-12T10:00:00.000000Z"
}
```

<Note>
  Since `indexSwap` is a [global task](/learn/async/asynchronous_operations#global-tasks), the `indexUid` is always `null`.
</Note>

You can use the response's `taskUid` to [track the status of your request](/reference/api/tasks#get-one-task).