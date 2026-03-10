# Similar documents
Source: https://www.meilisearch.com/docs/reference/api/similar

The /similar route accepts one search result and uses AI-powered search to return a number of similar documents.

The `/similar` route uses AI-powered search to return a number of documents similar to a target document.

Meilisearch exposes two routes for retrieving similar documents: `POST` and `GET`. In the majority of cases, `POST` will offer better performance and ease of use.

## Get similar documents with `POST`

<RouteHighlighter method="POST" />

Retrieve documents similar to a specific search result.

### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

### Body

| Parameter                                                                    | Type             | Default value | Description                                               |
| ---------------------------------------------------------------------------- | ---------------- | ------------- | --------------------------------------------------------- |
| **`id`**                                                                     | String or number | `null`        | Identifier of the target document (mandatory)             |
| **[`embedder`](/reference/api/search#hybrid-search)**                        | String           | `null`        | Embedder to use when computing recommendations. Mandatory |
| **[`attributesToRetrieve`](/reference/api/search#attributes-to-retrieve)**   | Array of strings | `["*"]`       | Attributes to display in the returned documents           |
| **[`offset`](/reference/api/search#offset)**                                 | Integer          | `0`           | Number of documents to skip                               |
| **[`limit`](/reference/api/search#limit)**                                   | Integer          | `20`          | Maximum number of documents returned                      |
| **[`filter`](/reference/api/search#filter)**                                 | String           | `null`        | Filter queries by an attribute's value                    |
| **[`showRankingScore`](/reference/api/search#ranking-score)**                | Boolean          | `false`       | Display the global ranking score of a document            |
| **[`showRankingScoreDetails`](/reference/api/search#ranking-score-details)** | Boolean          | `false`       | Display detailed ranking score information                |
| **[`rankingScoreThreshold`](/reference/api/search#ranking-score-threshold)** | Number           | `null`        | Exclude results with low ranking scores                   |
| **[`retrieveVectors`](/reference/api/search#display-_vectors-in-response)**  | Boolean          | `false`       | Return document vector data                               |

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/INDEX_NAME/similar' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer DEFAULT_SEARCH_API_KEY' \
    --data-binary '{
      "id": TARGET_DOCUMENT_ID,
      "embedder": "EMBEDDER_NAME"
    }'
  ```

  ```javascript JS theme={null}
  client.index('INDEX_NAME').searchSimilarDocuments({ id: 'TARGET_DOCUMENT_ID', embedder: 'default' })
  ```

  ```python Python theme={null}
  client.index("INDEX_NAME").get_similar_documents({"id": "TARGET_DOCUMENT_ID", "embedder": "default"})
  ```

  ```php PHP theme={null}
  $similarQuery = new SimilarDocumentsQuery('TARGET_DOCUMENT_ID', 'default');
  $client->index('INDEX_NAME')->searchSimilarDocuments($similarQuery);
  ```

  ```java Java theme={null}
  SimilarDocumentRequest query = new SimilarDocumentRequest() .setId("143") .setEmbedder("manual"); client.index("movies").searchSimilarDocuments(query)
  ```

  ```ruby Ruby theme={null}
  client.index('INDEX_NAME').search_similar_documents('TARGET_DOCUMENT_ID', embedder: 'default')
  ```

  ```go Go theme={null}
  resp := new(meilisearch.SimilarDocumentResult)
  client.Index("INDEX_NAME").SearchSimilarDocuments(&meilisearch.SimilarDocumentQuery{
    Id: "TARGET_DOCUMENT_ID",
    Embedder: "default",
  }, resp)
  ```

  ```rust Rust theme={null}
  let results = index
    .similar_search("TARGET_DOCUMENT_ID", "EMBEDDER_NAME")
    .execute()
    .await
    .unwrap();
  ```
</CodeGroup>

#### Response: `200 OK`

```json theme={null}
{
  "hits": [
    {
      "id": "299537",
      "title": "Captain Marvel"
    },
    {
      "id": "166428",
      "title": "How to Train Your Dragon: The Hidden World"
    }
    {
      "id": "287947",
      "title": "Shazam!"
    }
  ],
  "id": "23",
  "processingTimeMs": 0,
  "limit": 20,
  "offset": 0,
  "estimatedTotalHits": 3
}
```

## Get similar documents with `GET`

<RouteHighlighter method="GET" />

Retrieve documents similar to a specific search result.

### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

### Query parameters

| Parameter                                                                    | Type             | Default value | Description                                               |
| ---------------------------------------------------------------------------- | ---------------- | ------------- | --------------------------------------------------------- |
| **`id`**                                                                     | String or number | `null`        | Identifier of the target document (mandatory)             |
| **[`embedder`](/reference/api/search#hybrid-search)**                        | String           | `"default"`   | Embedder to use when computing recommendations. Mandatory |
| **[`attributesToRetrieve`](/reference/api/search#attributes-to-retrieve)**   | Array of strings | `["*"]`       | Attributes to display in the returned documents           |
| **[`offset`](/reference/api/search#offset)**                                 | Integer          | `0`           | Number of documents to skip                               |
| **[`limit`](/reference/api/search#limit)**                                   | Integer          | `20`          | Maximum number of documents returned                      |
| **[`filter`](/reference/api/search#filter)**                                 | String           | `null`        | Filter queries by an attribute's value                    |
| **[`showRankingScore`](/reference/api/search#ranking-score)**                | Boolean          | `false`       | Display the global ranking score of a document            |
| **[`showRankingScoreDetails`](/reference/api/search#ranking-score-details)** | Boolean          | `false`       | Display detailed ranking score information                |
| **[`rankingScoreThreshold`](/reference/api/search#ranking-score-threshold)** | Number           | `null`        | Exclude results with low ranking scores                   |
| **[`retrieveVectors`](/reference/api/search#display-_vectors-in-response)**  | Boolean          | `false`       | Return document vector data                               |

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/INDEX_NAME/similar?id=TARGET_DOCUMENT_ID&embedder=EMBEDDER_NAME'
  ```
</CodeGroup>

#### Response: `200 OK`

```json theme={null}
{
  "hits": [
    {
      "id": "299537",
      "title": "Captain Marvel"
    },
    {
      "id": "166428",
      "title": "How to Train Your Dragon: The Hidden World"
    }
    {
      "id": "287947",
      "title": "Shazam!"
    }
  ],
  "id": "23",
  "processingTimeMs": 0,
  "limit": 20,
  "offset": 0,
  "estimatedTotalHits": 3
}
```