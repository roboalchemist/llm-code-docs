# Facet search
Source: https://www.meilisearch.com/docs/reference/api/facet_search

The /facet-search route allows you to search for facet values.

The `/facet-search` route allows you to search for facet values. Facet search supports [prefix search](/learn/engine/prefix) and [typo tolerance](/learn/relevancy/typo_tolerance_settings). The returned hits are sorted lexicographically in ascending order.

<Note>
  Meilisearch does not support facet search on numbers. Convert numeric facets to strings to make them searchable.

  Internally, Meilisearch represents numbers as [`float64`](https://en.wikipedia.org/wiki/Double-precision_floating-point_format). This means they lack precision and can be represented in different ways, making it difficult to search facet values effectively.
</Note>

## Perform a facet search

Search for a facet value within a given facet.

<RouteHighlighter method="POST" />

<Warning>
  This endpoint will not work without first explicitly adding attributes to the [`filterableAttributes`](/reference/api/settings#update-filterable-attributes) list. [Learn more about facets in our dedicated guide.](/learn/filtering_and_sorting/search_with_facet_filters)
</Warning>

<Warning>
  Meilisearch's facet search does not support multi-word facets and only considers the first term in the`facetQuery`.

  For example, searching for `Jane` will return `Jane Austen`, but searching for `Austen` will not return `Jane Austen`.
</Warning>

### Body

| Name                                                                                                  | Type                                                                 | Default value | Description                                                                                                                                        |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`facetName`** \*                                                                                    | String                                                               | `null`        | Facet name to search values on                                                                                                                     |
| **`facetQuery`**                                                                                      | String                                                               | `null`        | Search query for a given facet value. If `facetQuery` isn't specified, Meilisearch returns all facet values for the searched facet, limited to 100 |
| **[`q`](/reference/api/search#query-q)**                                                              | String                                                               | `""`          | Query string                                                                                                                                       |
| **[`filter`](/reference/api/search#filter)**                                                          | [String\*](/learn/filtering_and_sorting/filter_expression_reference) | `null`        | Filter queries by an attribute's value                                                                                                             |
| **[`matchingStrategy`](/reference/api/search#matching-strategy)**                                     | String                                                               | `"last"`      | Strategy used to match query terms within documents                                                                                                |
| **[`attributesToSearchOn`](/reference/api/search##customize-attributes-to-search-on-at-search-time)** | Array of strings                                                     | `null`        | Restrict search to the specified attributes                                                                                                        |
| **`exhaustiveFacetCount`**                                                                            | Boolean                                                              | `false`       | Return an exhaustive count of facets, up to the limit defined by [`maxTotalHits`](/reference/api/settings#pagination)                              |

### Response

| Name                   | Type    | Description                                             |
| :--------------------- | :------ | :------------------------------------------------------ |
| **`facetHits.value`**  | String  | Facet value matching the `facetQuery`                   |
| **`facetHits.count`**  | Integer | Number of documents with a facet value matching `value` |
| **`facetQuery`**       | String  | The original `facetQuery`                               |
| **`processingTimeMs`** | Number  | Processing time of the query                            |

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/books/facet-search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "facetQuery": "fiction",
      "facetName": "genres",
      "filter": "rating > 3"
    }'
  ```

  ```javascript JS theme={null}
  client.index('books').searchForFacetValues({
    facetQuery: 'fiction',
    facetName: 'genres'
    filter: 'rating > 3'
  })
  ```

  ```python Python theme={null}
  client.index('books').facet_search('genres', 'fiction', {
    'filter': 'rating > 3'
  })
  ```

  ```php PHP theme={null}
  $client->index('books')->facetSearch(
    (new FacetSearchQuery())
        ->setFacetQuery('fiction')
        ->setFacetName('genres')
        ->setFilter(['rating > 3'])
  );
  ```

  ```java Java theme={null}
  FacetSearchRequest fsr = FacetSearchRequest.builder().facetName("genres").facetQuery("fiction").filter(new String[]{"rating > 3"}).build();
  client.index("books").facetSearch(fsr);
  ```

  ```ruby Ruby theme={null}
  client.index('books').facet_search('genres', 'fiction', filter: 'rating > 3')
  ```

  ```go Go theme={null}
  client.Index("books").FacetSearch(&meilisearch.FacetSearchRequest{
    FacetQuery: "fiction",
    FacetName: "genres",
    Filter: "rating > 3",
  })
  ```

  ```csharp C# theme={null}
  var query = new SearchFacetsQuery()
  {
    FacetQuery = "fiction",
    Filter = "rating > 3"
  };
  await client.Index("books").FacetSearchAsync("genres", query);
  ```

  ```rust Rust theme={null}
  let res = client.index("books")
    .facet_search("genres")
    .with_facet_query("fiction")
    .with_filter("rating > 3")
    .execute()
    .await
    .unwrap();
  ```

  ```dart Dart theme={null}
  await client.index('books').facetSearch(
        FacetSearchQuery(
          facetQuery: 'fiction',
          facetName: 'genres',
          filter: 'rating > 3',
        ),
      );
  ```
</CodeGroup>

#### Response: `200 Ok`

```json theme={null}
{
  "facetHits": [
    {
      "value": "fiction",
      "count": 7
    }
  ],
  "facetQuery": "fiction",
  "processingTimeMs": 0
}
```