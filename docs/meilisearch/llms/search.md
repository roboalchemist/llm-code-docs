# Search
Source: https://www.meilisearch.com/docs/reference/api/search

The /search route allows you to search your indexed documents. This route includes a large number of parameters you can use to customize returned search results.

Meilisearch exposes two routes to perform searches:

* A POST route: this is the preferred route when using API authentication, as it allows [preflight request](https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request) caching and better performance
* A GET route: the usage of this route is discouraged, unless you have good reason to do otherwise (specific caching abilities for example)

You may find exhaustive descriptions of the parameters accepted by the two routes [at the end of this article](#search-parameters).

## Search in an index with POST

<RouteHighlighter method="POST" />

Search for documents matching a specific query in the given index.

This is the preferred endpoint to perform search when an API key is required, as it allows for [preflight requests](https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request) to be cached. Caching preflight requests **considerably improves search speed**.

<Note>
  By default, [this endpoint returns a maximum of 1000 results](/learn/resources/known_limitations#maximum-number-of-results-per-search). If you want to scrape your database, use the [get documents endpoint](/reference/api/documents#get-documents-with-post) instead.
</Note>

### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

### Body

| Search Parameter                                                                | Type                       | Default value | Description                                                                         |
| :------------------------------------------------------------------------------ | :------------------------- | :------------ | :---------------------------------------------------------------------------------- |
| **[`q`](#query-q)**                                                             | String                     | `""`          | Query string                                                                        |
| **[`offset`](#offset)**                                                         | Integer                    | `0`           | Number of documents to skip                                                         |
| **[`limit`](#limit)**                                                           | Integer                    | `20`          | Maximum number of documents returned                                                |
| **[`hitsPerPage`](#number-of-results-per-page)**                                | Integer                    | `1`           | Maximum number of documents returned for a page                                     |
| **[`page`](#page)**                                                             | Integer                    | `1`           | Request a specific page of results                                                  |
| **[`filter`](#filter)**                                                         | String or array of strings | `null`        | Filter queries by an attribute's value                                              |
| **[`facets`](#facets)**                                                         | Array of strings           | `null`        | Display the count of matches per facet                                              |
| **[`distinct`](#distinct-attributes-at-search-time)**                           | String                     | `null`        | Restrict search to documents with unique values of specified attribute              |
| **[`attributesToRetrieve`](#attributes-to-retrieve)**                           | Array of strings           | `["*"]`       | Attributes to display in the returned documents                                     |
| **[`attributesToCrop`](#attributes-to-crop)**                                   | Array of strings           | `null`        | Attributes whose values have to be cropped                                          |
| **[`cropLength`](#crop-length)**                                                | Integer                    | `10`          | Maximum length of cropped value in words                                            |
| **[`cropMarker`](#crop-marker)**                                                | String                     | `"…"`         | String marking crop boundaries                                                      |
| **[`attributesToHighlight`](#attributes-to-highlight)**                         | Array of strings           | `null`        | Highlight matching terms contained in an attribute                                  |
| **[`highlightPreTag`](#highlight-tags)**                                        | String                     | `"<em>"`      | String inserted at the start of a highlighted term                                  |
| **[`highlightPostTag`](#highlight-tags)**                                       | String                     | `"</em>"`     | String inserted at the end of a highlighted term                                    |
| **[`showMatchesPosition`](#show-matches-position)**                             | Boolean                    | `false`       | Return matching terms location                                                      |
| **[`sort`](#sort)**                                                             | Array of strings           | `null`        | Sort search results by an attribute's value                                         |
| **[`matchingStrategy`](#matching-strategy)**                                    | String                     | `last`        | Strategy used to match query terms within documents                                 |
| **[`showRankingScore`](#ranking-score)**                                        | Boolean                    | `false`       | Display the global ranking score of a document                                      |
| **[`showRankingScoreDetails`](#ranking-score-details)**                         | Boolean                    | `false`       | Adds a detailed global ranking score field                                          |
| **[`rankingScoreThreshold`](#ranking-score-threshold)**                         | Number                     | `null`        | Excludes results with low ranking scores                                            |
| **[`attributesToSearchOn`](#customize-attributes-to-search-on-at-search-time)** | Array of strings           | `["*"]`       | Restrict search to the specified attributes                                         |
| **[`hybrid`](#hybrid-search)**                                                  | Object                     | `null`        | Return results based on query keywords and meaning                                  |
| **[`vector`](#vector)**                                                         | Array of numbers           | `null`        | Search using a custom query vector                                                  |
| **[`retrieveVectors`](#display-_vectors-in-response)**                          | Boolean                    | `false`       | Return document and query vector data                                               |
| **[`locales`](#query-locales)**                                                 | Array of strings           | `null`        | Explicitly specify languages used in a query                                        |
| **[`media`](#media)**                                                           | Object                     | `null`        | Perform AI-powered search queries with multimodal content                           |
| **[`personalize`](#search-personalization)**                                    | Object                     | `null`        | Perform AI-powered searches that return different results based on a user's profile |

### Response

| Name                     | Type             | Description                                                                        |
| :----------------------- | :--------------- | :--------------------------------------------------------------------------------- |
| **`hits`**               | Array of objects | Results of the query                                                               |
| **`offset`**             | Number           | Number of documents skipped                                                        |
| **`limit`**              | Number           | Number of documents to take                                                        |
| **`estimatedTotalHits`** | Number           | Estimated total number of matches                                                  |
| **`totalHits`**          | Number           | Exhaustive total number of matches                                                 |
| **`semanticHitCount`**   | Number           | Exhaustive number of semantic search matches (only present in AI-powered searches) |
| **`totalPages`**         | Number           | Exhaustive total number of search result pages                                     |
| **`hitsPerPage`**        | Number           | Number of results on each page                                                     |
| **`page`**               | Number           | Current search results page                                                        |
| **`facetDistribution`**  | Object           | **[Distribution of the given facets](#facetdistribution)**                         |
| **`facetStats`**         | Object           | [The numeric `min` and `max` values per facet](#facetstats)                        |
| **`processingTimeMs`**   | Number           | Processing time of the query                                                       |
| **`query`**              | String           | Query originating the response                                                     |
| **`requestUid`**         | String           | A UUID v7 identifying the search request                                           |

#### Exhaustive and estimated total number of search results

By default, Meilisearch only returns an estimate of the total number of search results in a query: `estimatedTotalHits`. This happens because Meilisearch prioritizes relevancy and performance over providing an exhaustive number of search results. When working with `estimatedTotalHits`, use `offset` and `limit` to navigate between search results.

If you require the total number of search results, use the `hitsPerPage` and `page` search parameters in your query. The response to this query replaces `estimatedTotalHits` with `totalHits` and includes an extra field with number of search results pages based on your `hitsPerPage`: `totalPages`. Using `totalHits` and `totalPages` may result in slightly reduced performance, but is recommended when creating UI elements such as numbered page selectors.

Neither `estimatedTotalHits` nor `totalHits` can exceed the limit configured in [the `maxTotalHits` index setting](/reference/api/settings#pagination).

You can [read more about pagination in our dedicated guide](/guides/front_end/pagination).

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{ "q": "american ninja" }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('American ninja')
  ```

  ```python Python theme={null}
  client.index('movies').search('American ninja')
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('american ninja');
  ```

  ```java Java theme={null}
  client.index("movies").search("American ninja");
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('american ninja')
  ```

  ```go Go theme={null}
  client.Index("movies").Search("american ninja", &meilisearch.SearchRequest{})
  ```

  ```csharp C# theme={null}
  await client.Index("movies").SearchAsync<Movie>("American ninja");
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Movie> = client
    .index("movies")
    .search()
    .with_query("american ninja")
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(query: "American ninja")
  client.index("movies").search(searchParameters) { (result: Result<Searchable<Movie>, Swift.Error>) in
      switch result {
      case .success(let searchResult):
          print(searchResult)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').search('American ninja');
  ```
</CodeGroup>

#### Response: `200 Ok`

```json theme={null}
{
  "hits": [
    {
      "id": 2770,
      "title": "American Pie 2",
      "poster": "https://image.tmdb.org/t/p/w1280/q4LNgUnRfltxzp3gf1MAGiK5LhV.jpg",
      "overview": "The whole gang are back and as close as ever. They decide to get even closer by spending the summer together at a beach house. They decide to hold the biggest…",
      "release_date": 997405200
    },
    {
      "id": 190859,
      "title": "American Sniper",
      "poster": "https://image.tmdb.org/t/p/w1280/svPHnYE7N5NAGO49dBmRhq0vDQ3.jpg",
      "overview": "U.S. Navy SEAL Chris Kyle takes his sole mission—protect his comrades—to heart and becomes one of the most lethal snipers in American history. His pinpoint accuracy not only saves countless lives but also makes him a prime…",
      "release_date": 1418256000
    },
    …
  ],
  "offset": 0,
  "limit": 20,
  "estimatedTotalHits": 976,
  "processingTimeMs": 35,
  "query": "american",
  "requestUid": "0198e71e-47d2-7cd3-b507-1d0cc930b1f1"
}
```

## Search in an index with GET

<RouteHighlighter method="GET" />

Search for documents matching a specific query in the given index.

<Warning>
  This endpoint only accepts [string filter expressions](/learn/filtering_and_sorting/filter_expression_reference).
</Warning>

This endpoint should only be used when no API key is required. If an API key is required, use the [POST](/reference/api/search#search-in-an-index-with-post) route instead.

<Note>
  By default, [this endpoint returns a maximum of 1000 results](/learn/resources/known_limitations#maximum-number-of-results-per-search). If you want to scrape your database, use the [get documents endpoint](/reference/api/documents#get-documents-with-post) instead.
</Note>

### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

### Query parameters

| Search Parameter                                                                | Type                       | Default value | Description                                                            |
| :------------------------------------------------------------------------------ | :------------------------- | :------------ | :--------------------------------------------------------------------- |
| **[`q`](#query-q)**                                                             | String                     | `""`          | Query string                                                           |
| **[`offset`](#offset)**                                                         | Integer                    | `0`           | Number of documents to skip                                            |
| **[`limit`](#limit)**                                                           | Integer                    | `20`          | Maximum number of documents returned                                   |
| **[`hitsPerPage`](#number-of-results-per-page)**                                | Integer                    | `1`           | Maximum number of documents returned for a page                        |
| **[`page`](#page)**                                                             | Integer                    | `1`           | Request a specific page of results                                     |
| **[`filter`](#filter)**                                                         | String or array of strings | `null`        | Filter queries by an attribute's value                                 |
| **[`facets`](#facets)**                                                         | Array of strings           | `null`        | Display the count of matches per facet                                 |
| **[`distinct`](#distinct-attributes-at-search-time)**                           | String                     | `null`        | Restrict search to documents with unique values of specified attribute |
| **[`attributesToRetrieve`](#attributes-to-retrieve)**                           | Array of strings           | `["*"]`       | Attributes to display in the returned documents                        |
| **[`attributesToCrop`](#attributes-to-crop)**                                   | Array of strings           | `null`        | Attributes whose values have to be cropped                             |
| **[`cropLength`](#crop-length)**                                                | Integer                    | `10`          | Maximum length of cropped value in words                               |
| **[`cropMarker`](#crop-marker)**                                                | String                     | `"…"`         | String marking crop boundaries                                         |
| **[`attributesToHighlight`](#attributes-to-highlight)**                         | Array of strings           | `null`        | Highlight matching terms contained in an attribute                     |
| **[`highlightPreTag`](#highlight-tags)**                                        | String                     | `"<em>"`      | String inserted at the start of a highlighted term                     |
| **[`highlightPostTag`](#highlight-tags)**                                       | String                     | `"</em>"`     | String inserted at the end of a highlighted term                       |
| **[`showMatchesPosition`](#show-matches-position)**                             | Boolean                    | `false`       | Return matching terms location                                         |
| **[`sort`](#sort)**                                                             | Array of strings           | `null`        | Sort search results by an attribute's value                            |
| **[`matchingStrategy`](#matching-strategy)**                                    | String                     | `last`        | Strategy used to match query terms within documents                    |
| **[`showRankingScore`](#ranking-score)**                                        | Boolean                    | `false`       | Display the global ranking score of a document                         |
| **[`showRankingScoreDetails`](#ranking-score-details)**                         | Boolean                    | `false`       | Adds a detailed global ranking score field                             |
| **[`rankingScoreThreshold`](#ranking-score-threshold)**                         | Number                     | `null`        | Excludes results with low ranking scores                               |
| **[`attributesToSearchOn`](#customize-attributes-to-search-on-at-search-time)** | Array of strings           | `["*"]`       | Restrict search to the specified attributes                            |
| **[`hybrid`](#hybrid-search)**                                                  | Object                     | `null`        | Return results based on query keywords and meaning                     |
| **[`vector`](#vector)**                                                         | Array of numbers           | `null`        | Search using a custom query vector                                     |
| **[`retrieveVectors`](#display-_vectors-in-response)**                          | Boolean                    | `false`       | Return document and query vector data                                  |
| **[`locales`](#query-locales)**                                                 | Array of strings           | `null`        | Explicitly specify languages used in a query                           |

### Response

| Name                     | Type             | Description                                                 |
| :----------------------- | :--------------- | :---------------------------------------------------------- |
| **`hits`**               | Array of objects | Results of the query                                        |
| **`offset`**             | Number           | Number of documents skipped                                 |
| **`limit`**              | Number           | Number of documents to take                                 |
| **`estimatedTotalHits`** | Number           | Estimated total number of matches                           |
| **`totalHits`**          | Number           | Exhaustive total number of matches                          |
| **`totalPages`**         | Number           | Exhaustive total number of search result pages              |
| **`hitsPerPage`**        | Number           | Number of results on each page                              |
| **`page`**               | Number           | Current search results page                                 |
| **`facetDistribution`**  | Object           | **[Distribution of the given facets](#facetdistribution)**  |
| **`facetStats`**         | Object           | [The numeric `min` and `max` values per facet](#facetstats) |
| **`processingTimeMs`**   | Number           | Processing time of the query                                |
| **`query`**              | String           | Query originating the response                              |
| **`requestUid`**         | String           | A UUID v7 identifying the search request                    |

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/movies/search?q=american%20ninja'
  ```

  ```javascript JS theme={null}
  client.index('movies').searchGet('American ninja')
  ```

  ```dart Dart theme={null}
  await client.index('movies').search('American ninja');
  ```
</CodeGroup>

#### Response: `200 Ok`

```json theme={null}
{
  "hits": [
    {
      "id": 2770,
      "title": "American Pie 2",
      "poster": "https://image.tmdb.org/t/p/w1280/q4LNgUnRfltxzp3gf1MAGiK5LhV.jpg",
      "overview": "The whole gang are back and as close as ever. They decide to get even closer by spending the summer together at a beach house. They decide to hold the biggest…",
      "release_date": 997405200
    },
    {
      "id": 190859,
      "title": "American Sniper",
      "poster": "https://image.tmdb.org/t/p/w1280/svPHnYE7N5NAGO49dBmRhq0vDQ3.jpg",
      "overview": "U.S. Navy SEAL Chris Kyle takes his sole mission—protect his comrades—to heart and becomes one of the most lethal snipers in American history. His pinpoint accuracy not only saves countless lives but also makes him a prime…",
      "release_date": 1418256000
    },
    …
  ],
  "offset": 0,
  "limit": 20,
  "estimatedTotalHits": 976,
  "processingTimeMs": 35,
  "query": "american",
  "requestUid": "0198e71e-47d2-7cd3-b507-1d0cc930b1f1"
}
```

## Search parameters

Here follows an exhaustive description of each search parameter currently available when using the search endpoint. Unless otherwise noted, all parameters are valid for the `GET /indexes/{index_uid}/search`, `POST /indexes/{index_uid}/search`, and `/multi-search` routes.

<Warning>
  If [using the `GET` route to perform a search](/reference/api/search#search-in-an-index-with-get), all parameters must be **URL-encoded**.

  This is not necessary when using the `POST` route or one of our [SDKs](/learn/resources/sdks).
</Warning>

### Query (q)

**Parameter**: `q`<br />
**Expected value**: Any string<br />
**Default value**: `null`

Sets the search terms.

<Warning>
  Meilisearch only considers the first ten words of any given search query. This is necessary in order to deliver a [fast search-as-you-type experience](/learn/resources/known_limitations#maximum-number-of-query-words).
</Warning>

#### Example

You can search for films mentioning `shifu` by setting the `q` parameter:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{ "q": "shifu" }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('shifu')
  ```

  ```python Python theme={null}
  client.index('movies').search('shifu')
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('shifu');
  ```

  ```java Java theme={null}
  client.index("movies").search("shifu");
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('shifu')
  ```

  ```go Go theme={null}
  resp, err := client.Index("movies").Search("shifu", &meilisearch.SearchRequest{})
  ```

  ```csharp C# theme={null}
  await client.Index("movies").SearchAsync<Movie>("shifu");
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Movie> = client
    .index("movies")
    .search()
    .with_query("shifu")
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").search(SearchParameters(query: "shifu")) { (result: Result<Searchable<Movie>, Swift.Error>) in
      switch result {
      case .success(let searchResult):
          print(searchResult)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').search('shifu');
  ```
</CodeGroup>

This will give you a list of documents that contain your query terms in at least one attribute.

```json theme={null}
{
  "hits": [
    {
      "id": 50393,
      "title": "Kung Fu Panda Holiday",
      "poster": "https://image.tmdb.org/t/p/w500/rV77WxY35LuYLOuQvBeD1nyWMuI.jpg",
      "overview": "The Winter Feast is Po's favorite holiday. Every year he and his father hang decorations, cook together, and serve noodle soup to the villagers. But this year Shifu informs Po that as Dragon Warrior, it is his duty to host the formal Winter Feast at the Jade Palace.",
      "release_date": 1290729600,
      "genres": [
        "Animation",
        "Family",
        "TV Movie"
      ]
    }
  ],
  "query": "shifu"
}
```

#### Query term normalization

Query terms go through a normalization process that removes [non-spacing marks](https://www.compart.com/en/unicode/category/Mn). Because of this, Meilisearch effectively ignores accents and diacritics when returning results. For example, searching for `"sábia"` returns documents containing `"sábia"`, `"sabiá"`, and `"sabia"`.

Normalization also converts all letters to lowercase. Searching for `"Video"` returns the same results as searching for `"video"`, `"VIDEO"`, or `"viDEO"`.

#### Placeholder search

When `q` isn't specified, Meilisearch performs a **placeholder search**.  A placeholder search returns all searchable documents in an index, modified by any search parameters used and sorted by that index's [custom ranking rules](/learn/relevancy/custom_ranking_rules). Since there is no query term, the [built-in ranking rules](/learn/relevancy/ranking_rules) **do not apply.**

If the index has no sort or custom ranking rules, the results are returned in the order of their internal database position.

<Tip>
  Placeholder search is particularly useful when building a [faceted search interfaces](/learn/filtering_and_sorting/search_with_facet_filters), as it allows users to view the catalog and alter sorting rules without entering a query.
</Tip>

#### Phrase search

If you enclose search terms in double quotes (`"`), Meilisearch will only return documents containing those terms in the order they were given. This is called a **phrase search**.

Phrase searches are case-insensitive and ignore [soft separators such as `-`, `,`, and `:`](/learn/engine/datatypes). Using a hard separator within a phrase search effectively splits it into multiple separate phrase searches: `"Octavia.Butler"` will return the same results as `"Octavia" "Butler"`.

You can combine phrase search and normal queries in a single search request. In this case, Meilisearch will first fetch all documents with exact matches to the given phrase(s), and [then proceed with its default behavior](/learn/relevancy/relevancy).

##### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
  --data-binary '{ "q": "\"african american\" horror" }'
  ```

  ```javascript JS theme={null}
  client.index('movies')
    .search('"african american" horror')
  ```

  ```python Python theme={null}
  client.index('movies').search('"african american" horror')
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('"african american" horror');
  ```

  ```java Java theme={null}
  client.index("movies").search("\"african american\" horror");
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('"african american" horror')
  ```

  ```go Go theme={null}
  resp, err := client.Index("movies").Search("\"african american\" horror", &meilisearch.SearchRequest{})
  ```

  ```csharp C# theme={null}
  await client.Index("movies").SearchAsync<Movie>("\"african american\" horror");
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Movie> = client
    .index("movies")
    .search()
    .with_query("\"african american\" horror")
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(
      query: "\"african american\" horror")
  client.index("movies").search(searchParameters) { (result: Result<Searchable<Movie>, Swift.Error>) in
      switch result {
      case .success(let searchResult):
          print(searchResult)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').search('"african american" horror');
  ```
</CodeGroup>

#### Negative search

Use the minus (`-`) operator in front of a word or phrase to exclude it from search results.

##### Example

The following query returns all documents that do not include the word "escape":

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{ "q": "-escape" }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('-escape')
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('-escape');
  ```

  ```rust Rust theme={null}
  let results = index.search()
    .with_query("-escape")
    .execute()
    .await
    .unwrap();
  ```
</CodeGroup>

Negative search can be used together with phrase search:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{ "q": "-\"escape room\"" }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('-"escape"')
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('-"escape"');
  ```

  ```rust Rust theme={null}
  let results = index.search()
    .with_query("-\"escape room\"")
    .execute()
    .await
    .unwrap();
  ```
</CodeGroup>

### Offset

**Parameter**: `offset`<br />
**Expected value**: Any positive integer<br />
**Default value**: `0`

Sets the starting point in the search results, effectively skipping over a given number of documents.

Queries using `offset` and `limit` only return an estimate of the total number of search results.

You can [paginate search results](/guides/front_end/pagination) by making queries combining both `offset` and `limit`.

<Warning>
  Setting `offset` to a value greater than an [index's `maxTotalHits`](/reference/api/settings#update-pagination-settings) returns an empty array.
</Warning>

#### Example

If you want to skip the **first** result in a query, set `offset` to `1`:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "shifu",
      "offset": 1
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('shifu', {
    offset: 1
  })
  ```

  ```python Python theme={null}
  client.index('movies').search('shifu', {
    'offset': 1
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('shifu', ['offset' => 1]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("shifu").offset(1).build();
  client.index("movies").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('shifu', {
    offset: 1
  })
  ```

  ```go Go theme={null}
  resp, err := client.Index("movies").Search("shifu", &meilisearch.SearchRequest{
    Offset: 1,
  })
  ```

  ```csharp C# theme={null}
  var sq = new SearchQuery
  {
      Offset = 1
  };
  var result = await client.Index("movies").SearchAsync<Movie>("shifu", sq);
  if(result is SearchResult<Movie> pagedResults)
  {
  }
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Movie> = client
    .index("movies")
    .search()
    .with_query("shifu")
    .with_offset(1)
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(
      query: "shifu",
      offset: 1)
  client.index("movies").search(searchParameters) { (result: Result<Searchable<Movie>, Swift.Error>) in
      switch result {
      case .success(let searchResult):
          print(searchResult)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').search('shifu', SearchQuery(offset: 1));
  ```
</CodeGroup>

### Limit

**Parameter**: `limit`<br />
**Expected value**: Any positive integer or zero<br />
**Default value**: `20`

Sets the maximum number of documents returned by a single query.

You can [paginate search results](/guides/front_end/pagination) by making queries combining both `offset` and `limit`.

<Warning>
  A search query cannot return more results than configured in [`maxTotalHits`](/reference/api/settings#pagination-object), even if the value of `limit` is greater than the value of `maxTotalHits`.
</Warning>

#### Example

If you want your query to return only **two** documents, set `limit` to `2`:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "shifu",
      "limit": 2
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('shifu', {
    limit: 2
  })
  ```

  ```python Python theme={null}
  client.index('movies').search('shifu', {
    'limit': 2
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('shifu', ['limit' => 2]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("shifu").limit(2).build();
  client.index("movies").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('shifu', {
    limit: 2
  })
  ```

  ```go Go theme={null}
  resp, err := client.Index("movies").Search("shifu", &meilisearch.SearchRequest{
    Limit: 2,
  })
  ```

  ```csharp C# theme={null}
  var sq = new SearchQuery
  {
      Limit = 2
  };
  var result = await client.Index("movies").SearchAsync<Movie>("shifu", sq);
  if(result is SearchResult<Movie> pagedResults)
  {
  }
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Movie> = client
    .index("movies")
    .search()
    .with_query("shifu")
    .with_limit(2)
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(
      query: "shifu",
      limit: 2)
  client.index("movies").search(searchParameters) { (result: Result<Searchable<Movie>, Swift.Error>) in
      switch result {
      case .success(let searchResult):
          print(searchResult)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').search('shifu', SearchQuery(limit: 2));
  ```
</CodeGroup>

### Number of results per page

**Parameter**: `hitsPerPage`<br />
**Expected value**: Any positive integer<br />
**Default value**: `20`

Sets the maximum number of documents returned for a single query. The value configured with this parameter dictates the number of total pages: if Meilisearch finds a total of `20` matches for a query and your `hitsPerPage` is set to `5`, `totalPages` is `4`.

Queries containing `hitsPerPage` are exhaustive and do not return an `estimatedTotalHits`. Instead, the response body will include `totalHits` and `totalPages`.

If you set `hitsPerPage` to `0`, Meilisearch processes your request, but does not return any documents. In this case, the response body will include the exhaustive value for `totalHits`. The response body will also include `totalPages`, but its value will be `0`.

You can use `hitsPerPage` and `page` to [paginate search results](/guides/front_end/pagination).

<Note>
  `hitsPerPage` and `page` take precedence over `offset` and `limit`. If a query contains either `hitsPerPage` or `page`, any values passed to `offset` and `limit` are ignored.
</Note>

<Warning>
  `hitsPerPage` and `page` are resource-intensive options and might negatively impact search performance. This is particularly likely if [`maxTotalHits`](/reference/api/settings#pagination) is set to a value higher than its default.
</Warning>

#### Example

The following example returns the first 15 results for a query:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "",
      "hitsPerPage": 15
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('', {
    hitsPerPage: 15
  })
  ```

  ```python Python theme={null}
  client.index('movies').search('', {'hitsPerPage': 15})
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('', ['hitsPerPage' => 15]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("").hitsPerPage(15).build();
  SearchResultPaginated searchResult = client.index("movies").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('', hits_per_page: 15)
  ```

  ```go Go theme={null}
  client.Index("movies").Search("", &meilisearch.SearchRequest{
    HitsPerPage: 15,
  })
  ```

  ```csharp C# theme={null}
  var result = await client.Index("movies").SearchAsync<Movie>("", new SearchQuery { HitsPerPage = 15 });
  if(result is PaginatedSearchResult<Movie> pagedResults)
  {
  }
  ```

  ```rust Rust theme={null}
  client.index("movies").search().with_hits_per_page(15).execute().await?;
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(query: "", hitsPerPage: 15)
  client.index("movies").search(searchParameters) { (result: Result<Searchable<Movie>, Swift.Error>) in
    switch result {
    case .success(let searchResult):
        print(searchResult)
    case .failure(let error):
        print(error)
    }
  }
  ```

  ```dart Dart theme={null}
  await client
      .index('movies')
      .search('', SearchQuery(hitsPerPage: 15))
      .asPaginatedResult();
  ```
</CodeGroup>

### Page

**Parameter**: `page`<br />
**Expected value**: Any positive integer<br />
**Default value**: `1`

Requests a specific results page. Pages are calculated using the `hitsPerPage` search parameter.

Queries containing `page` are exhaustive and do not return an `estimatedTotalHits`. Instead, the response body will include two new fields: `totalHits` and `totalPages`.

If you set `page` to `0`, Meilisearch processes your request, but does not return any documents. In this case, the response body will include the exhaustive values for `facetDistribution`, `totalPages`, and `totalHits`.

You can use `hitsPerPage` and `page` to [paginate search results](/guides/front_end/pagination).

<Note>
  `hitsPerPage` and `page` take precedence over `offset` and `limit`. If a query contains either `hitsPerPage` or `page`, any values passed to `offset` and `limit` are ignored.
</Note>

<Warning>
  `hitsPerPage` and `page` are resource-intensive options and might negatively impact search performance. This is particularly likely if [`maxTotalHits`](/reference/api/settings#pagination) is set to a value higher than its default.
</Warning>

#### Example

The following example returns the second page of search results:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "",
      "page": 2
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('', {
    page: 2
  })
  ```

  ```python Python theme={null}
  client.index('movies').search('', {'page': 2})
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('', ['page' => 2]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("").page(15).build();
  SearchResultPaginated searchResult = client.index("movies").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('', page: 2)
  ```

  ```go Go theme={null}
  client.Index("movies").Search("", &meilisearch.SearchRequest{
    Page: 2,
  })
  ```

  ```csharp C# theme={null}
  var result = await client.Index("movies").SearchAsync<Movie>("", new SearchQuery { Page = 2 });
  if(result is PaginatedSearchResult<Movie> pagedResults)
  {
  }
  ```

  ```rust Rust theme={null}
  client.index("movies").search().with_page(2).execute().await?;
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(query: "", page: 15)
  client.index("movies").search(searchParameters) { (result: Result<Searchable<Movie>, Swift.Error>) in
    switch result {
    case .success(let searchResult):
        print(searchResult)
    case .failure(let error):
        print(error)
    }
  }
  ```

  ```dart Dart theme={null}
  await client
      .index('movies')
      .search('', SearchQuery(page: 2))
      .asPaginatedResult();
  ```
</CodeGroup>

### Filter

**Parameter**: `filter`<br />
**Expected value**: A filter expression written as a string or an array of strings<br />
**Default value**: `[]`

Uses filter expressions to refine search results. Attributes used as filter criteria must be added to the [`filterableAttributes` list](/reference/api/settings#filterable-attributes).

For more information, [read our guide on how to use filters and build filter expressions](/learn/filtering_and_sorting/filter_search_results).

#### Example

You can write a filter expression in string syntax using logical connectives:

```
"(genres = horror OR genres = mystery) AND director = 'Jordan Peele'"
```

You can write the same filter as an array:

```
[["genres = horror", "genres = mystery"], "director = 'Jordan Peele'"]
```

You can then use the filter in a search query:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "thriller",
      "filter": [
        [
          "genres = Horror",
          "genres = Mystery"
        ],
        "director = \"Jordan Peele\""
      ]
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies')
    .search('thriller', {
      filter: [['genres = Horror', 'genres = Mystery'], 'director = "Jordan Peele"']
    })
  ```

  ```python Python theme={null}
  client.index('movies').search('thriller', {
    'filter': [['genres = Horror', 'genres = Mystery'], 'director = "Jordan Peele"']
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('thriller', [
    'filter' => [['genres = Horror', 'genres = Mystery'], 'director = "Jordan Peele"']
  ]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest =
    SearchRequest.builder().q("thriller").filterArray(new String[][] {
      new String[] {"genres = Horror", "genres = Mystery"},
      new String[] {"director = \"Jordan Peele\""}}).build();
  client.index("movies").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('thriller', {
    filter: [['genres = Horror', 'genres = Mystery'], 'director = "Jordan Peele"']
  })
  ```

  ```go Go theme={null}
  resp, err := client.Index("movies").Search("thriller", &meilisearch.SearchRequest{
    Filter: [][]string{
      []string{"genres = Horror", "genres = Mystery"},
      []string{"director = \"Jordan Peele\""},
    },
  })
  ```

  ```csharp C# theme={null}
  var sq = new SearchQuery
  {
      Filter = "(genre = 'Horror' AND genre = 'Mystery') OR director = 'Jordan Peele'"
  };
  await client.Index("movies").SearchAsync<Movie>("thriller", sq);
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Movie> = client
    .index("movies")
    .search()
    .with_query("thriller")
    .with_filter("(genres = Horror AND genres = Mystery) OR director = \"Jordan Peele\"")
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(
      query: "thriller",
      filter: [
        [
          "genres = Horror",
          "genres = Mystery"
        ],
        "director = \"Jordan Peele\""
      ])
  client.index("movies").search(searchParameters) { (result: Result<Searchable<Movie>, Swift.Error>) in
      switch result {
      case .success(let searchResult):
          print(searchResult)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').search(
      'thriller',
      SearchQuery(filter: [
        ['genres = Horror', 'genres = Mystery'],
        'director = "Jordan Peele"'
      ]));
  ```
</CodeGroup>

#### Filtering results with `_geoRadius`, `_geoBoundingBox`, and `_geoPolygon`

If your documents contain `_geo` or `_geojson` data, you can use the following built-in filter rules to filter results according to their geographic position:

<Tabs>
  <Tab title="_geoRadius">
    `_geoRadius` establishes a circular area based on a central point and a radius. This filter rule accepts the following parameters: `lat`, `lng`, `distance_in_meters`, `resolution`.

    ```json theme={null}
    _geoRadius(lat, lng, distance_in_meters, resolution)
    ```

    * `lat` and `lng` should be geographic coordinates expressed as floating point numbers.
    * `distance_in_meters` indicates the radius of the area within which you want your results and should be an integer.
    * `resolution` must be an integer between `3` and `1000` inclusive, and is an optional parameter. When using `_geojson` coordinates, `resolution` sets how many points Meilisearch will use to create a polygon that approximates the shape of a circle. Documents using `_geo` data ignore this parameter. Defaults to `125`. Increasing `resolution` may result in performance issues and is only necessary when dealing with large country-sized circles.

    <CodeGroup>
      ```bash cURL theme={null}
      curl \
        -X POST 'MEILISEARCH_URL/indexes/restaurants/search' \
        -H 'Content-type:application/json' \
        --data-binary '{ "filter": "_geoRadius(45.472735, 9.184019, 2000)" }'
      ```

      ```javascript JS theme={null}
      client.index('restaurants').search('', {
        filter: ['_geoRadius(45.472735, 9.184019, 2000)'],
      })
      ```

      ```python Python theme={null}
      client.index('restaurants').search('', {
        'filter': '_geoRadius(45.472735, 9.184019, 2000)'
      })
      ```

      ```php PHP theme={null}
      $client->index('restaurants')->search('', [
        'filter' => '_geoRadius(45.472735, 9.184019, 2000)'
      ]);
      ```

      ```java Java theme={null}
      SearchRequest searchRequest = SearchRequest.builder().q("").filter(new String[] {"_geoRadius(45.472735, 9.184019, 2000)"}).build();
      client.index("restaurants").search(searchRequest);
      ```

      ```ruby Ruby theme={null}
      client.index('restaurants').search('', { filter: '_geoRadius(45.472735, 9.184019, 2000)' })
      ```

      ```go Go theme={null}
      resp, err := client.Index("restaurants").Search("", &meilisearch.SearchRequest{
        Filter: "_geoRadius(45.472735, 9.184019, 2000)",
      })
      ```

      ```csharp C# theme={null}
      SearchQuery filters = new SearchQuery() { Filter = "_geoRadius(45.472735, 9.184019, 2000)" };
      var restaurants = await client.Index("restaurants").SearchAsync<Restaurant>("", filters);
      ```

      ```rust Rust theme={null}
      let results: SearchResults<Restaurant> = client
        .index("restaurants")
        .search()
        .with_filter("_geoRadius(45.472735, 9.184019, 2000)")
        .execute()
        .await
        .unwrap();
      ```

      ```swift Swift theme={null}
      let searchParameters = SearchParameters(
          filter: "_geoRadius(45.472735, 9.184019, 2000)"
      )
      client.index("restaurants").search(searchParameters) { (result: Result<Searchable<Restaurant>, Swift.Error>) in
          switch result {
          case .success(let searchResult):
              print(searchResult)
          case .failure(let error):
              print(error)
          }
      }
      ```

      ```dart Dart theme={null}
      await client.index('restaurants').search(
            '',
            SearchQuery(
              filterExpression: Meili.geoRadius(
                (lat: 45.472735, lng: 9.184019),
                2000,
              ),
            ),
          );
      ```
    </CodeGroup>
  </Tab>

  <Tab title="_geoBoundingBox">
    `_geoBoundingBox` establishes a rectangular area based on the coordinates for its top right and bottom left corners. This filter rule requires two arrays of geographic coordinates:

    ```
    _geoBoundingBox([LAT, LNG], [LAT, LNG])
    ```

    `LAT` and `LNG` should be geographic coordinates expressed as floating point numbers. The first array indicates the top right corner and the second array indicates the bottom left corner of the bounding box.

    <CodeGroup>
      ```bash cURL theme={null}
      curl \
        -X POST 'MEILISEARCH_URL/indexes/restaurants/search' \
        -H 'Content-type:application/json' \
        --data-binary '{ "filter": "_geoBoundingBox([45.494181, 9.214024], [45.449484, 9.179175])" }'
      ```

      ```javascript JS theme={null}
      client.index('restaurants').search('', {
        filter: ['_geoBoundingBox([45.494181, 9.214024], [45.449484, 9.179175])'],
      })
      ```

      ```python Python theme={null}
      client.index('restaurants').search('Batman', {
        'filter': '_geoBoundingBox([45.494181, 9.214024], [45.449484, 9.179175])'
      })
      ```

      ```php PHP theme={null}
      $client->index('restaurants')->search('', [
        'filter' => '_geoBoundingBox([45.494181, 9.214024], [45.449484, 9.179175])'
      ]);
      ```

      ```java Java theme={null}
      SearchRequest searchRequest = SearchRequest.builder().q()("").filter(new String[] {
          "_geoBoundingBox([45.494181, 9.214024], [45.449484, 9.179175])"
        }).build();
      client.index("restaurants").search(searchRequest);
      ```

      ```ruby Ruby theme={null}
      client.index('restaurants').search('', { filter: ['_geoBoundingBox([45.494181, 9.214024], [45.449484, 9.179175])'] })
      ```

      ```go Go theme={null}
      client.Index("restaurants").Search("", &meilisearch.SearchRequest{
        Filter: "_geoBoundingBox([45.494181, 9.214024], [45.449484, 9.179175])",
      })
      ```

      ```csharp C# theme={null}
      SearchQuery filters = new SearchQuery()
      {
          Filter = "_geoBoundingBox([45.494181, 9.214024], [45.449484, 9.179175])"
      };
      var restaurants = await client.Index("restaurants").SearchAsync<Restaurant>("restaurants", filters);
      ```

      ```rust Rust theme={null}
      let results: SearchResults<Restaurant> = client
        .index("restaurants")
        .search()
        .with_filter("_geoBoundingBox([45.494181, 9.214024], [45.449484, 9.179175])")
        .execute()
        .await
        .unwrap();
      ```

      ```swift Swift theme={null}
      let searchParameters = SearchParameters(
          filter: "_geoBoundingBox([45.494181, 9.214024], [45.449484, 9.179175])"
      )
      client.index("restaurants").search(searchParameters) { (result: Result<Searchable<Restaurant>, Swift.Error>) in
          switch result {
          case .success(let searchResult):
              print(searchResult)
          case .failure(let error):
              print(error)
          }
      }
      ```

      ```dart Dart theme={null}
      await client.index('restaurants').search(
            '',
            SearchQuery(
              filter:
                  '_geoBoundingBox([45.494181, 9.214024], [45.449484, 9.179175])',
            ),
          );
      ```
    </CodeGroup>

    Meilisearch will throw an error if the top right corner is under the bottom left corner.
  </Tab>

  <Tab title="_geoPolygon">
    `_geoPolygon` establishes an area based on the coordinates of the specified points. This filter rule requires three arrays or more arrays of geographic coordinates and can only be used with GeoJSON documents:

    ```
    _geoPolygon([LAT, LNG], [LAT, LNG], [LAT, LNG], …)
    ```

    `LAT` and `LNG` should be geographic coordinates expressed as floating point numbers. If your polygon is not closed, Meilisearch will close it automatically. Closed polygons are polygons where the first and last points share the same coordinates.

    <CodeSamplesGeosearchGuideFilterUsage4 />

    Polygons cannot cross the 180th meridian. If a shape crosses the antimeridian, you must make two polygons and join them using the `AND` filter operator.

    `_geoPolygon` is not compatible with documents using only `_geo` data. You must specify a `_geojson` attribute to use `_geoPolygon`.
  </Tab>
</Tabs>

If any parameters are invalid or missing, Meilisearch returns an [`invalid_search_filter`](/reference/errors/error_codes#invalid_search_filter) error.

### Facets

**Parameter**: `facets`<br />
**Expected value**: An array of `attribute`s or `["*"]`<br />
**Default value**: `null`
Returns the number of documents matching the current search query for each given facet. This parameter can take two values:

* An array of attributes: `facets=["attributeA", "attributeB", …]`
* An asterisk—this will return a count for all facets present in `filterableAttributes`

By default, `facets` returns a maximum of 100 facet values for each faceted field. You can change this value using the `maxValuesPerFacet` property of the [`faceting` index settings](/reference/api/settings#faceting).

When `facets` is set, the search results object includes the [`facetDistribution`](#facetdistribution) and [`facetStats`](#facetstats) fields.

<Note>
  If an attribute used on `facets` has not been added to the `filterableAttributes` list, it will be ignored.
</Note>

#### `facetDistribution`

`facetDistribution` contains the number of matching documents distributed among the values of a given facet. Each facet is represented as an object:

```json theme={null}
{
  …
 "facetDistribution": {
    "FACET_A": {
      "FACET_VALUE_X": 6,
      "FACET_VALUE_Y": 1,
    },
    "FACET_B": {
      "FACET_VALUE_Z": 3,
      "FACET_VALUE_W": 9,
    },
  },
  …
}
```

`facetDistribution` contains an object for every attribute passed to the `facets` parameter. Each object contains the returned values for that attribute and the count of matching documents with that value. Meilisearch does not return empty facets.

#### `facetStats`

`facetStats` contains the lowest (`min`) and highest (`max`) numerical values across all documents in each facet. Only numeric values are considered:

```json theme={null}
{
  …
"facetStats": {
  "rating": {
    "min": 2.5,
    "max": 4.7
    }
  }
  …
}
```

If none of the matching documents have a numeric value for a facet, that facet is not included in the `facetStats` object. `facetStats` ignores string values, even if the string contains a number.

#### Example

Given a movie ratings database, the following code sample returns the number of `Batman` movies per genre along with the minimum and maximum ratings:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movie_ratings/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "Batman",
      "facets": ["genres", "rating"]
    }'
  ```

  ```javascript JS theme={null}
  client.index('movie_ratings').search('Batman', { facets: ['genres', 'rating'] })
  ```

  ```python Python theme={null}
  client.index('movie_ratings').search('Batman', {
    'facets': ['genres', 'rating']
  })
  ```

  ```php PHP theme={null}
  $client->index('movie_ratings')->search('Batman', [
    'facets' => ['genres', 'rating']
  ]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("Batman").facets(new String[]
  {
    "genres",
    "rating"
  }).build();
  client.index("movies").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('movie_ratings').search('Batman', {
    facets: ['genres', 'rating']
  })
  ```

  ```go Go theme={null}
  client.Index("movie_ratings").Search("Batman", &meilisearch.SearchRequest{
    Facets: []string{
      "genres",
      "rating",
    },
  })
  ```

  ```csharp C# theme={null}
  var sq = new SearchQuery
  {
    Facets = new string[] { "genres", "rating" }
  };
  await client.Index("movie_ratings").SearchAsync<Movie>("Batman", sq);
  ```

  ```rust Rust theme={null}
  let books = client.index("movie_ratings");
  let results: SearchResults<Book> = SearchQuery::new(&books)
    .with_query("Batman")
    .with_facets(Selectors::Some(&["genres", "rating"))
    .execute()
    .await
    .unwrap();
  ```

  ```dart Dart theme={null}
  await client
      .index('movie_ratings')
      .search('Batman', SearchQuery(facets: ['genres', 'rating']));
  ```
</CodeGroup>

The response shows the facet distribution for `genres` and `rating`. Since `rating` is a numeric field, you get its minimum and maximum values in `facetStats`.

```json theme={null}
{
  …
  "estimatedTotalHits": 22,
  "query": "Batman",
  "facetDistribution": {
    "genres": {
      "Action": 20,
      "Adventure": 7,
      …
      "Thriller": 3
    },
    "rating": {
      "2": 1,
      …
      "9.8": 1
    }
  },
  "facetStats": {
    "rating": {
      "min": 2.0,
      "max": 9.8
    }
  }
}
```

[Learn more about facet distribution in the faceted search guide.](/learn/filtering_and_sorting/search_with_facet_filters)

### Distinct attributes at search time

**Parameter**: `distinct`<br />
**Expected value**: An `attribute` present in the `filterableAttributes` list<br />
**Default value**: `null`

Defines one attribute in the `filterableAttributes` list as a distinct attribute. Distinct attributes indicate documents sharing the same value for the specified field are equivalent and only the most relevant one should be returned in search results.

This behavior is similar to the [`distinctAttribute` index setting](/reference/api/settings#distinct-attribute), but can be configured at search time. `distinctAttribute` acts as a default distinct attribute value you may override with `distinct`.

#### Examples

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/INDEX_NAME/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "QUERY TERMS",
      "distinct": "ATTRIBUTE_A"
    }'
  ```

  ```javascript JS theme={null}
  client.index('INDEX_NAME').search('QUERY TERMS', { distinct: 'ATTRIBUTE_A' })
  ```

  ```python Python theme={null}
  client.index('INDEX_NAME').search('QUERY_TERMS', { distinct: 'ATTRIBUTE_A' })
  ```

  ```php PHP theme={null}
  $client->index('INDEX_NAME')->search('QUERY TERMS', [
    'distinct' => 'ATTRIBUTE_A'
  ]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("QUERY TERMS").distinct("ATTRIBUTE_A").build();
  client.index("INDEX_NAME").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('INDEX_NAME').search('QUERY TERMS', {
    distinct: 'ATTRIBUTE_A'
  })
  ```

  ```go Go theme={null}
  client.Index("INDEX_NAME").Search("QUERY TERMS", &meilisearch.SearchRequest{
    Distinct: "ATTRIBUTE_A",
  })
  ```

  ```csharp C# theme={null}
  var params = new SearchQuery()
  {
    Distinct = "ATTRIBUTE_A"
  };
  await client.Index("INDEX_NAME").SearchAsync<T>("QUERY TERMS", params);
  ```

  ```rust Rust theme={null}
  let res = client
    .index("INDEX_NAME")
    .search()
    .with_query("QUERY TERMS")
    .with_distinct("ATTRIBUTE_A")
    .execute()
    .await
    .unwrap();
  ```
</CodeGroup>

### Attributes to retrieve

**Parameter**: `attributesToRetrieve`<br />
**Expected value**: An array of `attribute`s or `["*"]`<br />
**Default value**: `["*"]`

Configures which attributes will be retrieved in the returned documents.

If no value is specified, `attributesToRetrieve` uses the [`displayedAttributes` list](/reference/api/settings#displayed-attributes), which by default contains all attributes found in the documents.

<Note>
  If an attribute has been removed from `displayedAttributes`, `attributesToRetrieve` will silently ignore it and the field will not appear in your returned documents.
</Note>

#### Example

To get only the `overview` and `title` fields, set `attributesToRetrieve` to `["overview", "title"]`.

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "shifu",
      "attributesToRetrieve": [
        "overview",
        "title"
      ]
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('shifu', {
    attributesToRetrieve: ['overview', 'title']
  })
  ```

  ```python Python theme={null}
  client.index('movies').search('shifu', {
    'attributesToRetrieve': ['overview', 'title']
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('shifu', [
    'attributesToRetrieve' => ['overview', 'title']
  ]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("a").attributesToRetrieve(new String[] {"overview", "title"}).build();
  client.index("movies").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('shifu', {
    attributes_to_retrieve: ['overview', 'title']
  })
  ```

  ```go Go theme={null}
  resp, err := client.Index("movies").Search("shifu", &meilisearch.SearchRequest{
    AttributesToRetrieve: []string{"overview", "title"},
  })
  ```

  ```csharp C# theme={null}
  var sq = new SearchQuery
  {
      AttributesToRetrieve = new[] {"overview", "title"}
  };
  await client.Index("movies").SearchAsync<Movie>("shifu", sq);
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Movie> = client
    .index("movies")
    .search()
    .with_query("shifu")
    .with_attributes_to_retrieve(Selectors::Some(&["overview", "title"]))
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(
      query: "shifu",
      attributesToRetrieve: ["overview", "title"])
  client.index("movies").search(searchParameters) { (result: Result<Searchable<Movie>, Swift.Error>) in
      switch result {
      case .success(let searchResult):
          print(searchResult)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').search(
      'shifu', SearchQuery(attributesToRetrieve: ['overview', 'title']));
  ```
</CodeGroup>

### Attributes to crop

**Parameter**: `attributesToCrop`<br />
**Expected value**: An array of attributes or `["*"]`<br />
**Default value**: `null`

Crops the selected fields in the returned results to the length indicated by the [`cropLength`](#crop-length) parameter. When `attributesToCrop` is set, each returned document contains an extra field called `_formatted`. This object contains the cropped version of the selected attributes.

By default, crop boundaries are marked by the ellipsis character (`…`). You can change this by using the [`cropMarker`](#crop-marker) search parameter.

Optionally, you can indicate a custom crop length for any attributes given to `attributesToCrop`: `attributesToCrop=["attributeNameA:5", "attributeNameB:9"]`. If configured, these values have priority over `cropLength`.

Instead of supplying individual attributes, you can provide `["*"]` as a wildcard: `attributesToCrop=["*"]`. This causes `_formatted` to include the cropped values of all attributes present in [`attributesToRetrieve`](#attributes-to-retrieve).

#### Cropping algorithm

Suppose you have a field containing the following string: `Donatello is a skilled and smart turtle. Leonardo is the most skilled turtle. Raphael is the strongest turtle.`

Meilisearch tries to respect sentence boundaries when cropping. For example, if your search term is `Leonardo` and your `cropLength` is 6, Meilisearch will prioritize keeping the sentence together and return: `Leonardo is the most skilled turtle.`

If a query contains only a single search term, Meilisearch crops around the first occurrence of that term. If you search for `turtle` and your `cropLength` is 7, Meilisearch will return the first instance of that word: `Donatello is a skilled and smart turtle.`

If a query contains multiple search terms, Meilisearch centers the crop around the largest number of unique matches, giving priority to terms that are closer to each other and follow the original query order. If you search for `skilled turtle` with a `cropLength` of 6, Meilisearch will return `Leonardo is the most skilled turtle`.

If Meilisearch does not find any query terms in a field, cropping begins at the first word in that field. If you search for `Michelangelo` with a `cropLength` of 4 and this string is present in another field, Meilisearch will return `Donatello is a skilled …`.

#### Example

If you use `shifu` as a search query and set the value of the `cropLength` parameter to `5`:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "shifu",
      "attributesToCrop": ["overview"],
      "cropLength": 5
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('shifu', {
    attributesToCrop: ['overview'],
    cropLength: 5
  })
  ```

  ```python Python theme={null}
  client.index('movies').search('shifu', {
    'attributesToCrop': ['overview'],
    'cropLength': 5
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('shifu', [
    'attributesToCrop' => ['overview'],
    'cropLength' => 5
  ]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest =
          SearchRequest.builder()
                  .q("shifu")
                  .attributesToCrop(new String[] {"overview"})
                  .cropLength(5)
                  .build();
  client.index("movies").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('shifu', {
    attributes_to_crop: ['overview'],
    crop_length: 5
  })
  ```

  ```go Go theme={null}
  resp, err := client.Index("movies").Search("shifu", &meilisearch.SearchRequest{
    AttributesToCrop: []string{"overview"},
    CropLength:       5,
  })
  ```

  ```csharp C# theme={null}
  var sq = new SearchQuery
  {
      AttributesToCrop = new[] {"overview"},
      CropLength = 5
  };
  await client.Index("movies").SearchAsync<Movie>("shifu", sq);
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Movie> = client
    .index("movies")
    .search()
    .with_query("shifu")
    .with_attributes_to_crop(Selectors::Some(&[("overview", None)]))
    .with_crop_length(5)
    .execute()
    .await
    .unwrap();

  // Get the formatted results
  let formatted_results: Vec<&Movie> = results
    .hits
    .iter()
    .map(|r| r.formatted_result.as_ref().unwrap())
    .collect();
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(
      query: "shifu",
      attributesToCrop: ["overview"],
      cropLength: 5)
  client.index("movies").search(searchParameters) { (result: Result<Searchable<Movie>, Swift.Error>) in
      switch result {
      case .success(let searchResult):
          print(searchResult)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').search(
      'shifu', SearchQuery(attributesToCrop: ['overview'], cropLength: 5));
  ```
</CodeGroup>

You will get the following response with the **cropped text in the `_formatted` object**:

```json theme={null}
{
  "id": 50393,
  "title": "Kung Fu Panda Holiday",
  "poster": "https://image.tmdb.org/t/p/w1280/gp18R42TbSUlw9VnXFqyecm52lq.jpg",
  "overview": "The Winter Feast is Po's favorite holiday. Every year he and his father hang decorations, cook together, and serve noodle soup to the villagers. But this year Shifu informs Po that as Dragon Warrior, it is his duty to host the formal Winter Feast at the Jade Palace. Po is caught between his obligations as the Dragon Warrior and his family traditions: between Shifu and Mr. Ping.",
  "release_date": 1290729600,
  "_formatted": {
    "id": 50393,
    "title": "Kung Fu Panda Holiday",
    "poster": "https://image.tmdb.org/t/p/w1280/gp18R42TbSUlw9VnXFqyecm52lq.jpg",
    "overview": "…this year Shifu informs Po…",
    "release_date": 1290729600
  }
}
```

### Crop length

**Parameter**: `cropLength`<br />
**Expected value**: A positive integer<br />
**Default value**: `10`

Configures the total number of words to appear in the cropped value when using [`attributesToCrop`](#attributes-to-crop). If `attributesToCrop` is not configured, `cropLength` has no effect on the returned results.

Query terms are counted as part of the cropped value length. If `cropLength` is set to `2` and you search for one term (for example, `shifu`), the cropped field will contain two words in total (for example, `"…Shifu informs…"`).

Stop words are also counted against this number. If `cropLength` is set to `2` and you search for one term (for example, `grinch`), the cropped result may contain a stop word (for example, `"…the Grinch…"`).

If `attributesToCrop` uses the `attributeName:number` syntax to specify a custom crop length for an attribute, that value has priority over `cropLength`.

### Crop marker

**Parameter**: `cropMarker`<br />
**Expected value**: A string<br />
**Default value**: `"…"`

Sets a string to mark crop boundaries when using the [`attributesToCrop`](#attributes-to-crop) parameter. The crop marker will be inserted on both sides of the crop. If `attributesToCrop` is not configured, `cropMarker` has no effect on the returned search results.

If `cropMarker` is set to `null` or an empty string, no markers will be included in the returned results.

Crop markers are only added where content has been removed. For example, if the cropped text includes the first word of the field value, the crop marker will not be added to the beginning of the cropped result.

#### Example

When searching for `shifu`, you can use `cropMarker` to change the default `…`:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "shifu",
      "cropMarker": "[…]",
      "attributesToCrop": ["overview"]
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('shifu', {
    attributesToCrop: ['overview'],
    cropMarker: '[…]'
  })
  ```

  ```python Python theme={null}
  client.index('movies').search('shifu', {
    'attributesToCrop': ['overview'],
    'cropMarker': '[…]'
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('shifu', [
    'attributesToCrop' => ['overview'],
    'cropMarker' => '[…]'
  ]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest =
          SearchRequest.builder()
                  .q("shifu")
                  .attributesToCrop(new String[] {"overview"})
                  .cropMarker("[…]")
                  .build();
  client.index("movies").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('shifu', {
    attributes_to_crop: ['overview'],
    crop_marker: '[…]'
  })
  ```

  ```go Go theme={null}
  resp, err := client.Index("movies").Search("shifu", &meilisearch.SearchRequest{
    AttributesToCrop: []string{"overview"},
    CropMarker:       "[…]",
  })
  ```

  ```csharp C# theme={null}
  var sq = new SearchQuery
  {
      AttributesToCrop = new[] {"overview"},
      CropMarker = "[...]"
  };
  await client.Index("movies").SearchAsync<Movie>("shifu", sq);
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Movie> = client
    .index("movies")
    .search()
    .with_query("shifu")
    .with_attributes_to_crop(Selectors::Some(&[("overview", None)]))
    .with_crop_marker("[…]")
    .execute()
    .await
    .unwrap();

  // Get the formatted results
  let formatted_results: Vec<&Movie> = results
    .hits
    .iter()
    .map(|r| r.formatted_result.as_ref().unwrap())
    .collect();
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(
      query: "shifu",
      attributesToCrop: ["overview"],
      cropMarker: "[…]")
  client.index("movies").search(searchParameters) { (result: Result<Searchable<Movie>, Swift.Error>) in
      switch result {
      case .success(let searchResult):
          print(searchResult)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').search(
        'shifu',
        SearchQuery(
          attributesToCrop: ['overview'],
          cropMarker: '[…]',
        ),
      );
  ```
</CodeGroup>

```json theme={null}
{
  "id": 50393,
  "title": "Kung Fu Panda Holiday",
  "poster": "https://image.tmdb.org/t/p/w1280/gp18R42TbSUlw9VnXFqyecm52lq.jpg",
  "overview": "The Winter Feast is Po's favorite holiday. Every year he and his father hang decorations, cook together, and serve noodle soup to the villagers. But this year Shifu informs Po that as Dragon Warrior, it is his duty to host the formal Winter Feast at the Jade Palace. Po is caught between his obligations as the Dragon Warrior and his family traditions: between Shifu and Mr. Ping.",
  "release_date": 1290729600,
  "_formatted": {
    "id": 50393,
    "title": "Kung Fu Panda Holiday",
    "poster": "https://image.tmdb.org/t/p/w1280/gp18R42TbSUlw9VnXFqyecm52lq.jpg",
    "overview": "[…]But this year Shifu informs Po that as Dragon Warrior,[…]",
    "release_date": 1290729600
  }
}
```

### Attributes to highlight

**Parameter**: `attributesToHighlight`<br />
**Expected value**: An array of attributes or `["*"]`<br />
**Default value**: `null`

Highlights matching query terms in the specified attributes.  `attributesToHighlight` only works on values of the following types: string, number, array, object.

When this parameter is set, returned documents include a `_formatted` object containing the highlighted terms.

Instead of a list of attributes, you can use `["*"]`: `attributesToHighlight=["*"]`. In this case, all the attributes present in [`attributesToRetrieve`](#attributes-to-retrieve) will be assigned to `attributesToHighlight`.

By default highlighted elements are enclosed in `<em>` and `</em>` tags. You may change this by using the [`highlightPreTag` and `highlightPostTag` search parameters](#highlight-tags).

<Note>
  `attributesToHighlight` also highlights terms configured as [synonyms](/reference/api/settings#synonyms) and [stop words](/reference/api/settings#stop-words).
</Note>

<Warning>
  `attributesToHighlight` will highlight matches within all attributes added to the `attributesToHighlight` array, even if those attributes are not set as [`searchableAttributes`](/learn/relevancy/displayed_searchable_attributes#searchable-fields).
</Warning>

#### Example

The following query highlights matches present in the `overview` attribute:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "winter feast",
      "attributesToHighlight": ["overview"]
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('winter feast', {
    attributesToHighlight: ['overview']
  })
  ```

  ```python Python theme={null}
  client.index('movies').search('winter feast', {
    'attributesToHighlight': ['overview']
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('winter feast', [
    'attributesToHighlight' => ['overview']
  ]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest =
    new SearchRequest("winter feast").setAttributesToHighlight(new String[] {"overview"});
  client.index("movies").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('winter feast', {
    attributes_to_highlight: ['overview']
  })
  ```

  ```go Go theme={null}
  resp, err := client.Index("movies").Search("winter feast", &meilisearch.SearchRequest{
    AttributesToHighlight: []string{"overview"},
  })
  ```

  ```csharp C# theme={null}
  var sq = new SearchQuery
  {
      AttributesToHighlight = new[] {"overview"}
  };
  await client.Index("movies").SearchAsync<Movie>("winter feast", sq);
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Movie> = client
    .index("movies")
    .search()
    .with_query("winter feast")
    .with_attributes_to_highlight(Selectors::Some(&["overview"]))
    .execute()
    .await
    .unwrap();

  // Get the formatted results
  let formatted_results: Vec<&Movie> = results
    .hits
    .iter()
    .map(|r| r.formatted_result.as_ref().unwrap())
    .collect();
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(
      query: "winter feast",
      attributesToHighlight: ["overview"])
  client.index("movies").search(searchParameters) { (result: Result<Searchable<Movie>, Swift.Error>) in
      switch result {
      case .success(let searchResult):
          print(searchResult)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').search(
      'winter feast', SearchQuery(attributesToHighlight: ['overview']));
  ```
</CodeGroup>

The highlighted version of the text would then be found in the `_formatted` object included in each returned document:

```json theme={null}
{
  "id": 50393,
  "title": "Kung Fu Panda Holiday",
  "poster": "https://image.tmdb.org/t/p/w1280/gp18R42TbSUlw9VnXFqyecm52lq.jpg",
  "overview": "The Winter Feast is Po's favorite holiday. Every year he and his father hang decorations, cook together, and serve noodle soup to the villagers. But this year Shifu informs Po that as Dragon Warrior, it is his duty to host the formal Winter Feast at the Jade Palace. Po is caught between his obligations as the Dragon Warrior and his family traditions: between Shifu and Mr. Ping.",
  "release_date": 1290729600,
  "_formatted": {
    "id": 50393,
    "title": "Kung Fu Panda Holiday",
    "poster": "https://image.tmdb.org/t/p/w1280/gp18R42TbSUlw9VnXFqyecm52lq.jpg",
    "overview": "The <em>Winter Feast</em> is Po's favorite holiday. Every year he and his father hang decorations, cook together, and serve noodle soup to the villagers. But this year Shifu informs Po that as Dragon Warrior, it is his duty to host the formal <em>Winter Feast</em> at the Jade Palace. Po is caught between his obligations as the Dragon Warrior and his family traditions: between Shifu and Mr. Ping.",
    "release_date": 1290729600
  }
}
```

### Highlight tags

**Parameters**: `highlightPreTag` and `highlightPostTag`<br />
**Expected value**: A string<br />
**Default value**: `"<em>"` and `"</em>"` respectively

`highlightPreTag` and `highlightPostTag` configure, respectively, the strings to be inserted before and after a word highlighted by `attributesToHighlight`. If `attributesToHighlight` has not been configured, `highlightPreTag` and `highlightPostTag` have no effect on the returned search results.

It is possible to use `highlightPreTag` and `highlightPostTag` to enclose terms between any string of text, not only HTML tags: `"<em>"`, `"<strong>"`, `"*"`, and `"__"` are all equally supported values.

If `highlightPreTag` or `highlightPostTag` are set to `null` or an empty string, nothing will be inserted respectively at the beginning or the end of a highlighted term.

#### Example

The following query encloses highlighted matches in `<span>` tags with a `class` attribute:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "winter feast",
      "attributesToHighlight": ["overview"],
      "highlightPreTag": "<span class=\"highlight\">",
      "highlightPostTag": "</span>"
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('winter feast', {
    attributesToHighlight: ['overview'],
    highlightPreTag: '<span class="highlight">',
    highlightPostTag: '</span>'
  })
  ```

  ```python Python theme={null}
  client.index('movies').search('winter feast', {
    'attributesToHighlight': ['overview'],
    'highlightPreTag': '<span class="highlight">',
    'highlightPostTag': '</span>'
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('winter feast', [
    'attributesToHighlight' => ['overview'],
    'highlightPreTag' => '<span class="highlight">',
    'highlightPostTag' => '</span>'
  ]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest =
          SearchRequest.builder()
                  .q("winter feast")
                  .attributesToHighlight(new String[] {"overview"})
                  .highlightPreTag("<span class=\"highlight\">")
                  .highlightPostTag("</span>")
                  .build();
  client.index("movies").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('winter feast', {
    attributes_to_highlight: ['overview'],
    highlight_pre_tag: '<span class="highlight">',
    highlight_post_tag: '</span>'
  })
  ```

  ```go Go theme={null}
  resp, err := client.Index("movies").Search("winter feast", &meilisearch.SearchRequest{
    AttributesToHighlight: []string{"overview"},
    HighlightPreTag: "<span class=\"highlight\">",
    HighlightPostTag: "</span>",
  })
  ```

  ```csharp C# theme={null}
  var sq = new SearchQuery
  {
      AttributesToHighlight = new[] {"overview"},
      HighlightPreTag = "<span class=\"highlight\">",
      HighlightPostTag = "</span>"
  };
  await client.Index("movies").SearchAsync<Movie>("winter feast", sq);
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Movie> = client
    .index("movies")
    .search()
    .with_query("winter feast")
    .with_attributes_to_highlight(Selectors::Some(&["overview"]))
    .with_highlight_pre_tag("<span class=\"highlight\">")
    .with_highlight_post_tag("</span>")
    .execute()
    .await
    .unwrap();

  // Get the formatted results
  let formatted_results: Vec<&Movie> = results
    .hits
    .iter()
    .map(|r| r.formatted_result.as_ref().unwrap())
    .collect();
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(
      query: "winter feast",
      attributesToHighlight: ["overview"],
      highlightPreTag: "<span class=\"highlight\">",
      highlightPostTag: "</span>")
  client.index("movies").search(searchParameters) { (result: Result<Searchable<Movie>, Swift.Error>) in
      switch result {
      case .success(let searchResult):
          print(searchResult)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').search(
        'winter feast',
        SearchQuery(
          attributesToHighlight: ['overview'],
          highlightPreTag: '<span class="highlight">',
          highlightPostTag: '</span>',
        ),
      );
  ```
</CodeGroup>

You can find the highlighted query terms inside the `_formatted` property:

```json theme={null}
{
  "id": 50393,
  "title": "Kung Fu Panda Holiday",
  "poster": "https://image.tmdb.org/t/p/w1280/gp18R42TbSUlw9VnXFqyecm52lq.jpg",
  "overview": "The Winter Feast is Po's favorite holiday. Every year he and his father hang decorations, cook together, and serve noodle soup to the villagers. But this year Shifu informs Po that as Dragon Warrior, it is his duty to host the formal Winter Feast at the Jade Palace. Po is caught between his obligations as the Dragon Warrior and his family traditions: between Shifu and Mr. Ping.",
  "release_date": 1290729600,
  "_formatted": {
    "id": 50393,
    "title": "Kung Fu Panda Holiday",
    "poster": "https://image.tmdb.org/t/p/w1280/gp18R42TbSUlw9VnXFqyecm52lq.jpg",
    "overview": "The <span class=\"highlight\">Winter Feast</span> is Po's favorite holiday. Every year he and his father hang decorations, cook together, and serve noodle soup to the villagers. But this year Shifu informs Po that as Dragon Warrior, it is his duty to host the formal <span class=\"highlight\">Winter Feast</span> at the Jade Palace. Po is caught between his obligations as the Dragon Warrior and his family traditions: between Shifu and Mr. Ping.",
    "release_date": 1290729600
  }
}
```

<Warning>
  Though it is not necessary to use `highlightPreTag` and `highlightPostTag` in conjunction, be careful to ensure tags are correctly matched. In the above example, not setting `highlightPostTag` would result in malformed HTML: `<span>Winter Feast</em>`.
</Warning>

### Show matches position

**Parameter**: `showMatchesPosition`<br />
**Expected value**: `true` or `false`<br />
**Default value**: `false`

Adds a `_matchesPosition` object to the search response that contains the location of each occurrence of queried terms across all fields. This is useful when you need more control than offered by our [built-in highlighting](#attributes-to-highlight). `showMatchesPosition` only works for strings, numbers, and arrays of strings and numbers.

<Warning>
  `showMatchesPosition` returns the location of matched query terms within all attributes, even attributes that are not set as [`searchableAttributes`](/learn/relevancy/displayed_searchable_attributes#searchable-fields).
</Warning>

The beginning of a matching term within a field is indicated by `start`, and its length by `length`.

<Warning>
  `start` and `length` are measured in bytes and not the number of characters. For example, `ü` represents two bytes but one character.
</Warning>

#### Example

If you set `showMatchesPosition` to `true` and search for `winter feast`:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "winter feast",
      "showMatchesPosition": true
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('winter feast', {
    showMatchesPosition: true
  })
  ```

  ```python Python theme={null}
  client.index('movies').search('winter feast', {
    'showMatchesPosition': True
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('winter feast', [
    'attributesToHighlight' => ['overview'],
    'showMatchesPosition' => true
  ]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("winter feast").showMatchesPosition(true).build();
  SearchResultPaginated searchResult = client.index("movies").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('winter feast', {
    show_matches_position: true
  })
  ```

  ```go Go theme={null}
  resp, err := client.Index("movies").Search("winter feast", &meilisearch.SearchRequest{
    ShowMatchesPosition:    true,
  })
  ```

  ```csharp C# theme={null}
  await client.Index("movies").SearchAsync<T>(
    "winter feast",
    new SearchQuery
    {
        ShowMatchesPosition = True,
    });
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Movie> = client
    .index("movies")
    .search()
    .with_query("winter feast")
    .with_show_matches_position(true)
    .execute()
    .await
    .unwrap();

  // Get the matches info
  let matches_position: Vec<&HashMap<String, Vec<MatchRange>>> = results
    .hits
    .iter()
    .map(|r| r.matches_position.as_ref().unwrap())
    .collect();
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(
      query: "winter feast",
      showMatchesPosition: true)
  client.index("movies").search(searchParameters) { (result: Result<Searchable<Movie>, Swift.Error>) in
      switch result {
      case .success(let searchResult):
          print(searchResult)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client
      .index('movies')
      .search('winter feast', SearchQuery(showMatchesPosition: true));
  ```
</CodeGroup>

You would get the following response with **information about the matches in the `_matchesPosition` object**. Note how Meilisearch searches for `winter` and `feast` separately because of the whitespace:

```json theme={null}
{
  "id": 50393,
  "title": "Kung Fu Panda Holiday",
  "poster": "https://image.tmdb.org/t/p/w500/rV77WxY35LuYLOuQvBeD1nyWMuI.jpg",
  "overview": "The Winter Feast is Po's favorite holiday. Every year he and his father hang decorations, cook together, and serve noodle soup to the villagers. But this year Shifu informs Po that as Dragon Warrior, it is his duty to host the formal Winter Feast at the Jade Palace. Po is caught between his obligations as the Dragon Warrior and his family traditions: between Shifu and Mr. Ping.",
  "release_date": 1290729600,
  "_matchesPosition": {
    "overview": [
      {
        "start": 4,
        "length": 6
      },
      {
        "start": 11,
        "length": 5
      },
      {
        "start": 234,
        "length": 6
      },
      {
        "start": 241,
        "length": 5
      }
    ]
  }
}
```

### Sort

**Parameter**: `sort`<br />
**Expected value**: A list of attributes written as an array or as a comma-separated string<br />
**Default value**: `null`

Sorts search results at query time according to the specified attributes and indicated order.

Each attribute in the list must be followed by a colon (`:`) and the preferred sorting order: either ascending (`asc`) or descending (`desc`).

<Note>
  Attribute order is meaningful. The first attributes in a list will be given precedence over those that come later.

  For example, `sort="price:asc,author:desc` will prioritize `price` over `author` when sorting results.
</Note>

When using the `POST` route, `sort` expects an array of strings.

When using the `GET` route, `sort` expects the list as a comma-separated string.

[Read more about sorting search results in our dedicated guide.](/learn/filtering_and_sorting/sort_search_results)

#### Example

You can search for science fiction books ordered from cheapest to most expensive:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/books/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "science fiction",
      "sort": ["price:asc"]
    }'
  ```

  ```javascript JS theme={null}
  client.index('books').search('science fiction', {
    sort: ['price:asc'],
  })
  ```

  ```python Python theme={null}
  client.index('books').search('science fiction', {
    'sort': ['price:asc']
  })
  ```

  ```php PHP theme={null}
  $client->index('books')->search('science fiction', ['sort' => ['price:asc']]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("science fiction").sort(new String[] {"price:asc"}).build();
  client.index("search_parameter_guide_sort_1").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('books').search('science fiction', { sort: ['price:asc'] })
  ```

  ```go Go theme={null}
  resp, err := client.Index("books").Search("science fiction", &meilisearch.SearchRequest{
    Sort: []string{
      "price:asc",
    },
  })
  ```

  ```csharp C# theme={null}
  var sq = new SearchQuery
  {
    Sort = new[] { "price:asc" },
  };
  await client.Index("books").SearchAsync<Book>("science fiction", sq);
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Books> = client
    .index("books")
    .search()
    .with_query("science fiction")
    .with_sort(&["price:asc"])
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(
    query: "science fiction",
    sort: ["price:asc"]
  )
  client.index("books").search(searchParameters) { (result: Result<Searchable<Book>, Swift.Error>) in
    switch result {
    case .success(let searchResult):
      print(searchResult)
    case .failure(let error):
      print(error)
    }
  }
  ```

  ```dart Dart theme={null}
  await client
      .index('books')
      .search('science fiction', SearchQuery(sort: ['price:asc']));
  ```
</CodeGroup>

#### Sorting results with `_geoPoint`

When dealing with documents containing `_geo` data, you can use `_geoPoint` to sort results based on their distance from a specific geographic location.

`_geoPoint` is a sorting function that requires two floating point numbers indicating a location's latitude and longitude. You must also specify whether the sort should be ascending (`asc`) or descending (`desc`):

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/restaurants/search' \
    -H 'Content-type:application/json' \
    --data-binary '{ "sort": ["_geoPoint(48.8561446,2.2978204):asc"] }'
  ```

  ```javascript JS theme={null}
  client.index('restaurants').search('', {
    sort: ['_geoPoint(48.8561446, 2.2978204):asc'],
  })
  ```

  ```python Python theme={null}
  client.index('restaurants').search('', {
    'sort': ['_geoPoint(48.8561446,2.2978204):asc']
  })
  ```

  ```php PHP theme={null}
  $client->index('restaurants')->search('', [
    'sort' => ['_geoPoint(48.8561446,2.2978204):asc']
  ]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("").sort(new String[] {"_geoPoint(48.8561446,2.2978204):asc"}).build();
  client.index("restaurants").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('restaurants').search('', { sort: ['_geoPoint(48.8561446, 2.2978204):asc'] })
  ```

  ```go Go theme={null}
  resp, err := client.Index("restaurants").Search("", &meilisearch.SearchRequest{
    Sort: []string{
      "_geoPoint(48.8561446,2.2978204):asc",
    },
  })
  ```

  ```csharp C# theme={null}
  SearchQuery filters = new SearchQuery()
  {
      Sort = new string[] { "_geoPoint(48.8561446,2.2978204):asc" }
  };

  var restaurants = await client.Index("restaurants").SearchAsync<Restaurant>("", filters);
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Restaurant> = client
    .index("restaurants")
    .search()
    .with_sort(&["_geoPoint(48.8561446, 2.2978204):asc"])
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(
      query: "",
      sort: ["_geoPoint(48.8561446, 2.2978204):asc"]
  )
  client.index("restaurants").search(searchParameters) { (result: Result<Searchable<Restaurant>, Swift.Error>) in
      switch result {
      case .success(let task):
        print(task)
      case .failure(let error):
        print(error)
      }
    }
  ```

  ```dart Dart theme={null}
  await client.index('restaurants').search(
      '', SearchQuery(sort: ['_geoPoint(48.8561446, 2.2978204):asc']));
  ```
</CodeGroup>

Queries using `_geoPoint` will always include a `geoDistance` field containing the distance in meters between the document location and the `_geoPoint`:

```json theme={null}
[
  {
    "id": 1,
    "name": "Nàpiz' Milano",
    "_geo": {
      "lat": 45.4777599,
      "lng": 9.1967508
    },
    "_geoDistance": 1532
  }
]
```

Geographic sorting is only compatible with documents containing `_geo` data. `_geoPoint` ignores all data in the `_geojson` object.

[You can read more about location-based sorting in the dedicated guide.](/learn/filtering_and_sorting/geosearch#sorting-results-with-_geopoint)

### Matching strategy

**Parameter**: `matchingStrategy`<br />
**Expected value**: `last`, `all`, or `frequency`<br />
**Default value**: `last`

Defines the strategy used to match query terms in documents.

#### `last`

`last` returns documents containing all the query terms first. If there are not enough results containing all query terms to meet the requested `limit`, Meilisearch will remove one query term at a time, starting from the end of the query.

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "big fat liar",
      "matchingStrategy": "last"
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('big fat liar', {
    matchingStrategy: 'last'
  })
  ```

  ```python Python theme={null}
  client.index('movies').search('big fat liar', {
    'matchingStrategy': 'last'
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('big fat liar', ['matchingStrategy' => 'last']);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("big fat liar").matchingStrategy(MatchingStrategy.LAST).build();
  client.index("movies").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('big fat liar', {
    matching_strategy: 'last'
  })
  ```

  ```go Go theme={null}
  resp, err := client.Index("movies").Search("big fat liar", &meilisearch.SearchRequest{
    MatchingStrategy:    Last,
  })
  ```

  ```csharp C# theme={null}
  SearchQuery params = new SearchQuery() { MatchingStrategy = "last" };
  await client.Index("movies").SearchAsync<Game>("big fat liar", params);
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Movie> = client
  .index("movies")
  .search()
  .with_query("big fat liar")
  .with_matching_strategy(MatchingStrategies::LAST)
  .execute()
  .await
  .unwrap();
  ```

  ```dart Dart theme={null}
  await client.index('movies').search(
      'big fat liar', SearchQuery(matchingStrategy: MatchingStrategy.last));
  ```
</CodeGroup>

With the above code sample, Meilisearch will first return documents that contain all three words. If the results don't meet the requested `limit`, it will also return documents containing only the first two terms, `big fat`, followed by documents containing only `big`.

#### `all`

`all` only returns documents that contain all query terms. Meilisearch will not match any more documents even if there aren't enough to meet the requested `limit`.

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "big fat liar",
      "matchingStrategy": "all"
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('big fat liar', {
    matchingStrategy: 'all'
  })
  ```

  ```python Python theme={null}
  client.index('movies').search('big fat liar', {
    'matchingStrategy': 'all'
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('big fat liar', ['matchingStrategy' => 'all']);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("big fat liar").matchingStrategy(MatchingStrategy.ALL).build();
  client.index("movies").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('big fat liar', {
    matching_strategy: 'all'
  })
  ```

  ```go Go theme={null}
  resp, err := client.Index("movies").Search("big fat liar", &meilisearch.SearchRequest{
    MatchingStrategy:    All,
  })
  ```

  ```csharp C# theme={null}
  SearchQuery params = new SearchQuery() { MatchingStrategy = "all" };
  await client.Index("movies").SearchAsync<Game>("big fat liar", params);
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Movie> = client
  .index("movies")
  .search()
  .with_query("big fat liar")
  .with_matching_strategy(MatchingStrategies::ALL)
  .execute()
  .await
  .unwrap();
  ```

  ```dart Dart theme={null}
  await client.index('movies').search(
      'big fat liar', SearchQuery(matchingStrategy: MatchingStrategy.all));
  ```
</CodeGroup>

The above code sample would only return documents containing all three words.

#### `frequency`

`frequency` returns documents containing all the query terms first. If there are not enough results containing all query terms to meet the requested limit, Meilisearch will remove one query term at a time, starting with the word that is the most frequent in the dataset. `frequency` effectively gives more weight to terms that appear less frequently in a set of results.

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "white shirt",
      "matchingStrategy": "frequency"
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('white shirt', {
    matchingStrategy: 'frequency'
  })
  ```

  ```python Python theme={null}
  client.index('movies').search('big fat liar', {
    'matchingStrategy': 'frequency'
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('white shirt', ['matchingStrategy' => 'frequency']);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("white shirt").matchingStrategy(MatchingStrategy.FREQUENCY).build();
  client.index("movies").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('white shirt', {
    matching_strategy: 'frequency'
  })
  ```

  ```go Go theme={null}
  client.Index("movies").Search("white shirt", &meilisearch.SearchRequest{
    MatchingStrategy: Frequency,
  })
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Movie> = client
  .index("movies")
  .search()
  .with_query("white shirt")
  .with_matching_strategy(MatchingStrategies::FREQUENCY)
  .execute()
  .await
  .unwrap();
  ```
</CodeGroup>

In a dataset where many documents contain the term `"shirt"`, the above code sample would prioritize documents containing `"white"`.

### Ranking score

**Parameter**: `showRankingScore`<br />
**Expected value**: `true` or `false`<br />
**Default value**: `false`

Adds a global ranking score field, `_rankingScore`, to each document. The `_rankingScore` is a numeric value between `0.0` and `1.0`. The higher the `_rankingScore`, the more relevant the document.

The `sort` ranking rule does not influence the `_rankingScore`. Instead, the document order is determined by the value of the field they are sorted on.

<Note>
  A document's ranking score does not change based on the scores of other documents in the same index.

  For example, if a document A has a score of `0.5` for a query term, this value remains constant no matter the score of documents B, C, or D.
</Note>

#### Example

The code sample below returns the `_rankingScore` when searching for `dragon` in `movies`:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "dragon",
      "showRankingScore": true
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('dragon', {
    showRankingScore: true
  })
  ```

  ```python Python theme={null}
  client.index('movies').search('dragon', {
    'showRankingScore': True
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('dragon', [
    'showRankingScore' => true
  ]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("dragon").showRankingScore(true).build();
  client.index("movies").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('dragon', {
    show_ranking_score: true
  })
  ```

  ```go Go theme={null}
  resp, err := client.Index("movies").Search("dragon", &meilisearch.SearchRequest{
    showRankingScore:    true,
  })
  ```

  ```csharp C# theme={null}
  var params = new SearchQuery()
  {
    ShowRankingScore = true
  };
  await client.Index("movies").SearchAsync<MovieWithRankingScore>("dragon", params);
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Movie> = client
    .index("movies")
    .search()
    .with_query("dragon")
    .with_show_ranking_score(true)
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(query: "dragon", showRankingScore: true)
  client.index("movies").search(searchParameters) { (result: Result<Searchable<Movie>, Swift.Error>) in
    switch result {
    case .success(let searchResult):
        print(searchResult.rankingScore)
    case .failure(let error):
        print(error)
    }
  }
  ```

  ```dart Dart theme={null}
  await client
      .index('movies')
      .search('dragon', SearchQuery(showRankingScore: true));
  ```
</CodeGroup>

```json theme={null}
{
  "hits": [
    {
      "id": 31072,
      "title": "Dragon",
      "overview": "In a desperate attempt to save her kingdom…",
      …
      "_rankingScore": 0.92
    },
    {
      "id": 70057,
      "title": "Dragon",
      "overview": "A sinful martial arts expert wants…",
      …
      "_rankingScore": 0.91
    },
    …
  ],
  …
}
```

### Ranking score details

**Parameter**: `showRankingScoreDetails`<br />
**Expected value**: `true` or `false`<br />
**Default value**: `false`

Adds a detailed global ranking score field, `_rankingScoreDetails`, to each document. `_rankingScoreDetails` is an object containing a nested object for each active ranking rule.

#### Ranking score details object

Each ranking rule details its score in its own object. Fields vary per ranking rule.

##### `words`

* `order`: order in which this ranking rule was applied
* `score`: ranking score for this rule
* `matchingWords`: number of words in the query that match in the document
* `maxMatchingWords`: maximum number of words in the query that can match in the document

##### `typo`

* `order`: order in which this specific ranking rule was applied
* `score`: ranking score for this rule
* `typoCount`: number of typos corrected so that the document matches the query term
* `maxTypoCount`: maximum number of typos accepted

##### `proximity`

* `order`: order in which this ranking rule was applied
* `score`: ranking score for this rule

##### `attribute`

* `order`: order in which this ranking rule was applied
* `score`: ranking score for this rule
* `attributeRankingOrderScore`: score computed from the maximum attribute ranking order for the matching attributes
* `queryWordDistanceScore`: score computed from the distance between the position words in the query and the position of words in matched attributes

##### `exactness`

* `order`: order in which this ranking rule was applied
* `score`: ranking score for this rule
* `matchType`: either `exactMatch`, `matchesStart`, or `noExactMatch`:
  * `exactMatch`: document contains an attribute matching all query terms with no other words between them and in the order they were given
  * `matchesStart`: document contains an attribute with all query terms in the same order as the original query
  * `noExactMatch`: document contains an attribute with at least one query term matching the original query
* `matchingWords`: the number of exact matches in an attribute when `matchType` is `noExactMatch`
* `maxMatchingWords`: the maximum number of exact matches in an attribute when `matchType` is `noExactMatch`

##### `field_name:direction`

The `sort` ranking rule does not appear as a single field in the score details object. Instead, each sorted attribute appears as its own field, followed by a colon (`:`) and the sorting direction: `attribute:direction`.

* `order`: order in which this ranking rule was applied
* `value`: value of the field used for sorting

##### `_geoPoint(lat:lng):direction`

* `order`: order in which this ranking rule was applied
* `value`: value of the field used for sorting
* `distance`: same as [\_geoDistance](/learn/filtering_and_sorting/geosearch#finding-the-distance-between-a-document-and-a-_geopoint)

##### `vectorSort(target_vector)`

* `order`: order in which this specific ranking rule was applied
* `value`: vector used for sorting the document
* `similarity`: similarity score between the target vector and the value vector. 1.0 means a perfect similarity, 0.0 a perfect dissimilarity

#### Example

The code sample below returns the `_rankingScoreDetail` when searching for `dragon` in `movies`:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "dragon",
      "showRankingScoreDetails": true
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('dragon', { showRankingScoreDetails: true })
  ```

  ```python Python theme={null}
  client.index('movies').search('dragon', {
    'showRankingScoreDetails': True
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('dragon', [
    'showRankingScoreDetails' => true
  ]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("dragon").showRankingScoreDetails(true).build();
  client.index("movies").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('dragon', {
    show_ranking_score_details: true
  })
  ```

  ```go Go theme={null}
  resp, err := client.Index("movies").Search("dragon", &meilisearch.SearchRequest{
    showRankingScoreDetails:    true,
  })
  ```

  ```csharp C# theme={null}
  var params = new SearchQuery()
  {
    ShowRankingScoreDetails = true
  };
  await client.Index("movies").SearchAsync<MovieWithRankingScoreDetails>("dragon", params);
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Movie> = client
    .index("movies")
    .search()
    .with_query("dragon")
    .with_show_ranking_score_details(true)
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(query: "dragon", showRankingScoreDetails: true)
  let movies: Searchable<Movie> = try await client.index("movies").search(searchParameters)
  ```
</CodeGroup>

```json theme={null}
{
  "hits": [
    {
      "id": 31072,
      "title": "Dragon",
      "overview": "In a desperate attempt to save her kingdom…",
      …
      "_rankingScoreDetails": {
        "words": {
          "order": 0,
          "matchingWords": 4,
          "maxMatchingWords": 4,
          "score": 1.0
        },
        "typo": {
          "order": 2,
          "typoCount": 1,
          "maxTypoCount": 4,
          "score": 0.75
        },
        "name:asc": {
          "order": 1,
          "value": "Dragon"
        }
      }
    },
    …
  ],
  …
}
```

### Ranking score threshold

**Parameter**: `rankingScoreThreshold`<br />
**Expected value**: A number between `0.0` and `1.0`<br />
**Default value**: `null`

Excludes results below the specified ranking score. The threshold applies to all search types including full-text search, semantic search, and hybrid search.

Excluded results do not count towards `estimatedTotalHits`, `totalHits`, and facet distribution.

<Warning>
  Using `rankingScoreThreshold` with `page` and `hitsPerPage` forces Meilisearch to evaluate the ranking score of all matching documents to return an accurate `totalHits`. This may negatively impact search performance.

  Queries with `limit` and `offset` avoid this overhead when using `rankingScoreThreshold`.
</Warning>

#### Example

The following query only returns results with a ranking score bigger than `0.2`:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
  -X POST 'MEILISEARCH_URL/indexes/INDEX_NAME/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
      "q": "badman",
      "rankingScoreThreshold": 0.2
  }'
  ```

  ```javascript JS theme={null}
  client.index('INDEX_NAME').search('badman', { rankingScoreThreshold: 0.2 })
  ```

  ```python Python theme={null}
  client.index('INDEX_NAME').search('badman', { 'rankingScoreThreshold': 0.2 })
  ```

  ```php PHP theme={null}
  $client->index('INDEX_NAME')->search('badman', [
    'rankingScoreThreshold' => 0.2
  ]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("badman").rankingScoreThreshold(0.2).build();
  client.index("INDEX_NAME").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('INDEX_NAME').search('badman', {
    rankingScoreThreshold: 0.2
  })
  ```

  ```go Go theme={null}
  client.Index("INDEX_NAME").Search("badman", &meilisearch.SearchRequest{
    RankingScoreThreshold: 0.2,
  })
  ```

  ```rust Rust theme={null}
  let res = client
    .index("INDEX_NAME")
    .search()
    .with_query("badman")
    .with_ranking_score_threshold(0.2)
    .execute()
    .await
    .unwrap();
  ```
</CodeGroup>

### Customize attributes to search on at search time

**Parameter**: `attributesToSearchOn`<br />
**Expected value**: A list of searchable attributes written as an array<br />
**Default value**: `["*"]`

Configures a query to only look for terms in the specified attributes.

Instead of a list of attributes, you can pass a wildcard value (`["*"]`) and `null` to `attributesToSearchOn`. In both cases, Meilisearch will search for matches in all searchable attributes.

<Warning>
  Attributes passed to `attributesToSearchOn` must also be present in the `searchableAttributes` list.
</Warning>

The order of attributes in `attributesToSearchOn` does not affect relevancy.

#### Example

The following query returns documents whose `overview` includes `"adventure"`:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "adventure",
      "attributesToSearchOn": ["overview"]
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('adventure', {
    attributesToSearchOn: ['overview']
  })
  ```

  ```python Python theme={null}
  client.index('movies').search('adventure', {
    'attributesToSearchOn': ['overview']
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('adventure', [
    'attributesToSearchOn' => ['overview']
  ]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("adventure").attributesToSearchOn(new String[] {"overview"});
  client.index("movies").searchRequest(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('adventure', {
    attributes_to_search_on: ['overview']
  })
  ```

  ```go Go theme={null}
  resp, err := client.Index("movies").Search("adventure", &meilisearch.SearchRequest{
    AttributesToSearchOn: []string{"overview"},
  })
  ```

  ```csharp C# theme={null}
  var searchQuery = new SearchQuery
  {
    AttributesToSearchOn = new[] { "overview" }
  };
  await client.Index("movies").SearchAsync<Movie>("adventure", searchQuery);
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Movie> = client
    .index("movies")
    .search()
    .with_query("adventure")
    .with_attributes_to_search_on(&["overview"])
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(query: "adventure", attributesToSearchOn: ["overview"])
  client.index("movies").search(searchParameters) { (result: Result<Searchable<Movie>, Swift.Error>) in
    switch result {
    case .success(let searchResult):
        print(searchResult)
    case .failure(let error):
        print(error)
    }
  }
  ```

  ```dart Dart theme={null}
  await client.index('books').facetSearch(
        FacetSearchQuery(
          facetQuery: 'c',
          facetName: 'genres',
        ),
      );
  ```
</CodeGroup>

Results would not include documents containing `"adventure"` in other fields such as `title` or `genre`, even if these fields were present in the `searchableAttributes` list.

### Hybrid search

**Parameter**: `hybrid`<br />
**Expected value**: An object with two fields: `embedder` and `semanticRatio`<br />
**Default value**: `null`

Configures Meilisearch to return search results based on a query's meaning and context.

`hybrid` must be an object. It accepts two fields: `embedder` and `semanticRatio`.

`embedder` must be a string indicating an embedder configured with the `/settings` endpoint. It is mandatory to specify a valid embedder when performing AI-powered searches.

`semanticRatio` must be a number between `0.0` and `1.0` indicating the proportion between keyword and semantic search results. `0.0` causes Meilisearch to only return keyword results. `1.0` causes Meilisearch to only return meaning-based results. Defaults to `0.5`.

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST 'MEILISEARCH_URL/indexes/INDEX_NAME/search' \
    -H 'content-type: application/json' \
    --data-binary '{
      "q": "kitchen utensils",
      "hybrid": {
        "semanticRatio": 0.9,
        "embedder": "EMBEDDER_NAME"
      }
    }'
  ```

  ```javascript JS theme={null}
  client.index('INDEX_NAME').search('kitchen utensils', {
    hybrid: {
      semanticRatio: 0.9,
      embedder: 'EMBEDDER_NAME'
    }
  })
  ```

  ```php PHP theme={null}
  $client->index('INDEX_NAME')->search('kitchen utensils', [
    'hybrid' => [
      'semanticRatio' => 0.9,
      'embedder' => 'EMBEDDER_NAME'
    ]
  ]);
  ```

  ```rust Rust theme={null}
  let results = index
    .search()
    .with_query("kitchen utensils")
    .with_hybrid("EMBEDDER_NAME", 0.9)
    .execute()
    .await
    .unwrap();
  ```
</CodeGroup>

```json theme={null}
{
  "query": "PLACEHOLDER_QUERY",
  "processingTimeMs": 10,
  "limit": 20,
  "offset": 0,
  "estimatedTotalHits": 3,
  "semanticHitCount": 3,
  "hits": [
    …
  ]
}
```

### Vector

**Parameter**: `vector`<br />
**Expected value**: an array of numbers<br />
**Default value**: `null`

Use a custom vector to perform a search query. Must be an array of numbers corresponding to the dimensions of the custom vector.

`vector` is mandatory when performing searches with `userProvided` embedders. You may also use `vector` to override an embedder's automatic vector generation.

`vector` dimensions must match the dimensions of the embedder.

<Note>
  If a query does not specify `q`, but contains both `vector` and `hybrid.semanticRatio` bigger than `0`, Meilisearch performs a pure semantic search.

  If `q` is missing and `semanticRatio` is explicitly set to `0`, Meilisearch performs a placeholder search without any vector search results.
</Note>

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST 'MEILISEARCH_URL/indexes/INDEX_NAME/search' \
    -H 'content-type: application/json' \
    --data-binary '{
      "vector": [0, 1, 2],
      "hybrid": {
        "embedder": "EMBEDDER_NAME"
      }
    }'
  ```

  ```rust Rust theme={null}
  let results = index
    .search()
    .with_vector(&[0.0, 1.0, 2.0])
    .with_hybrid("EMBEDDER_NAME", 1.0)
    .execute()
    .await
    .unwrap();
  ```
</CodeGroup>

### Display `_vectors` in response

**Parameter**: `retrieveVectors`<br />
**Expected value**: `true` or `false`<br />
**Default value**: `false`

Return document and query embeddings with search results. If `true`, Meilisearch will display vector data in each [document's `_vectors` field](/reference/api/documents#_vectors).

<Warning>
  `_vectors` must be included in the [displayedAttributes](/reference/api/settings#displayed-attributes) list to be returned in the response.
</Warning>

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST 'MEILISEARCH_URL/indexes/INDEX_NAME/search' \
    -H 'content-type: application/json' \
    --data-binary '{
      "q": "kitchen utensils",
      "retrieveVectors": true,
      "hybrid": {
        "embedder": "EMBEDDER_NAME"
      }
    }'
  ```

  ```javascript JS theme={null}
  client.index('INDEX_NAME').search('kitchen utensils', {
    retrieveVectors: true,
    hybrid: {
      embedder: 'EMBEDDER_NAME'
    }
  })
  ```

  ```php PHP theme={null}
  $client->index('INDEX_NAME')->search('kitchen utensils', [
    'retrieveVectors' => true,
    'hybrid' => [
      'embedder': 'EMBEDDER_NAME'
    ]
  ]);
  ```

  ```ruby Ruby theme={null}
  client.index('INDEX_NAME').search('kitchen utensils', {
    retrieve_vectors: true,
    hybrid: {
      embedder: 'EMBEDDER_NAME'
    }
  })
  ```

  ```rust Rust theme={null}
  let results = index
    .search()
    .with_query("kitchen utensils")
    .with_retrieve_vectors(true)
    .with_hybrid("EMBEDDER_NAME", 0.5)
    .execute()
    .await
    .unwrap();
  ```
</CodeGroup>

```json theme={null}
{
  "hits": [
    {
      "id": 0,
      "title": "DOCUMENT NAME",
      "_vectors": {
        "default": {
          "embeddings": [0.1, 0.2, 0.3],
          "regenerate": true
        }
      }
      …
    },
    …
  ],
  …
}
```

### Query locales

**Parameter**: `locales`<br />
**Expected value**: array of [supported ISO-639 locales](/reference/api/settings#localized-attributes-object)<br />
**Default value**: `[]`

By default, Meilisearch auto-detects the language of a query. Use this parameter to explicitly state the language of a query.

In case of a mismatch between `locales` and the [localized attributes index setting](/reference/api/settings#localized-attributes), this parameter takes precedence.

<Note>
  `locales` and [`localizedAttributes`](/reference/api/settings#localized-attributes) have the same goal: explicitly state the language used in a search when Meilisearch's language auto-detection is not working as expected.

  If you believe Meilisearch is detecting incorrect languages because of the query text, explicitly set the search language with `locales`.

  If you believe Meilisearch is detecting incorrect languages because of document, explicitly set the document language at the index level with `localizedAttributes`.

  For full control over the way Meilisearch detects languages during indexing and at search time, set both `locales` and `localizedAttributes`.
</Note>

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
  -X POST 'MEILISEARCH_URL/indexes/INDEX_NAME/search' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "q": "QUERY TEXT IN JAPANESE",
    "locales": ["jpn"]
  }'
  ```

  ```javascript JS theme={null}
  client.index('INDEX_NAME').search('QUERY TEXT IN JAPANESE', { locales: ['jpn'] })
  ```

  ```python Python theme={null}
  client.index('INDEX_NAME').search('進撃の巨人', { 'locales': ['jpn'] })
  ```

  ```php PHP theme={null}
  $client->index('INDEX_NAME')->search('QUERY TEXT IN JAPANESE', [
    'locales' => ['jpn']
  ]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("QUERY TEXT IN JAPANESE").locales(new String[]{"jpn"}).build();
  client.index("INDEX_NAME").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('INDEX_NAME').search('進撃の巨人', { locales: ['jpn'] })
  ```

  ```go Go theme={null}
  client.index("INDEX_NAME").Search("QUERY TEXT IN JAPANESE", &meilisearch.SearchRequest{
      Locales: []string{"jpn"}
  })
  ```

  ```rust Rust theme={null}
  let res = client
    .index("books")
    .search()
    .with_query("進撃の巨人")
    .with_locales(&["jpn"])
    .execute()
    .await
    .unwrap();
  ```
</CodeGroup>

```json theme={null}
{
  "hits": [
    {
      "id": 0,
      "title": "DOCUMENT NAME",
      "overview_jp": "OVERVIEW TEXT IN JAPANESE"
    }
    …
  ],
  …
}
```

### Media <NoticeTag type="experimental" label="experimental" />

**Parameter**: `media`<br />
**Expected value**: Object<br />
**Default value**: `null`

<Note>
  This is an experimental feature. Use the Meilisearch Cloud UI or the experimental features endpoint to activate it:

  ```sh theme={null}
  curl \
    -X PATCH 'MEILISEARCH_URL/experimental-features/' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "multimodal": true
    }'
  ```
</Note>

Specifies data to populate search fragments when performing multimodal searches.

`media` must be an object whose fields must correspond to the data required by one [search fragment](/reference/api/settings#searchfragments). `media` must match a single search fragment. If `media` matches more than one fragment or no search fragments at all, Meilisearch will return an error.

It is mandatory to specify an embedder when using `media`. `media` is incompatible with `vector`.

#### Example

<CodeSamplesSearchParameterReferenceMedia1 />

```json theme={null}
{
  "hits": [
    {
      "id": 0,
      "title": "DOCUMENT NAME",
      …
    }
    …
  ],
  …
}
```

### Search personalization <NoticeTag type="experimental" label="experimental" />

**Parameter**: `personalize`<br />
**Expected value**: Object<br />
**Default value**: `null`

<Note>
  This is an experimental feature. Contact Meilisearch Cloud support to enable it for your projects. If self-hosting, relaunch your instance providing a Cohere key to the search personalization instance option.
</Note>

Adds user context to [personalize search results according to user profile](/learn/personalization/making_personalized_search_queries).

`personalize` must be an object. It must include a single field, `userContext`.`userContext` must be a string describing the user performing the search.