# Geosearch
Source: https://www.meilisearch.com/docs/learn/filtering_and_sorting/geosearch

Filter and sort search results based on their geographic location.

Meilisearch allows you to filter and sort results based on their geographic location. This can be useful when you only want results within a specific area or when sorting results based on their distance from a specific location.

<Warning>
  Due to Meilisearch allowing malformed `_geo` fields in the following versions (v0.27, v0.28 and v0.29), please ensure the `_geo` field follows the correct format.
</Warning>

## Preparing documents for location-based search

To start filtering documents based on their geographic location, you must make sure they contain a valid `_geo` or `_geojson` field. If you also want to sort documents geogeraphically, they must have a valid `_geo` field.

`_geo` and `_geojson` are reserved fields. If you include one of them in your documents, Meilisearch expects its value to conform to a specific format.

When using JSON and NDJSON, `_geo` must contain an object with two keys: `lat` and `lng`. Both fields must contain either a floating point number or a string indicating, respectively, latitude and longitude:

```json theme={null}
{
  …
  "_geo": {
    "lat": 0.0,
    "lng": "0.0"
  }
}
```

`_geojson` must be an object whose contents follow the [GeoJSON specification](https://geojson.org/):

```json theme={null}
{
  …
  "_geojson": {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [0.0, 0.0]
    }
  }
}
```

Meilisearch does not support transmeridian shapes. If your document includes a transmeridian shape, split it into two separate shapes grouped as a `MultiPolygon` or `MultiLine`. Transmeridian shapes are polygons or lines that cross the 180th meridian.

**Meilisearch does not support polygons with holes**. If your polygon consists of an external ring and an inner empty space, Meilisearch ignores the hole and treats the polygon as a solid shape.

<Note>
  ### Using `_geo` and `_geojson` together

  If your application requires both sorting by distance to a point and filtering by shapes other than a circle or a rectangle, you will need to add both `_geo` and `_geojson` to your documents.

  When handling documents with both fields, Meilisearch:

  * Ignores `_geojson` values when sorting
  * Ignores `_geo` values when filtering with `_geoPolygon`
  * Matches both `_geo` and `_geojson` values when filtering with `_geoRadius` and `_geoBoundingBox`
</Note>

### Examples

Suppose we have a JSON array containing a few restaurants:

```json theme={null}
[
  {
    "id": 1,
    "name": "Nàpiz' Milano",
    "address": "Viale Vittorio Veneto, 30, 20124, Milan, Italy",
    "type": "pizza",
    "rating": 9
  },
  {
    "id": 2,
    "name": "Bouillon Pigalle",
    "address": "22 Bd de Clichy, 75018 Paris, France",
    "type": "french",
    "rating": 8
  },
  {
    "id": 3,
    "name": "Artico Gelateria Tradizionale",
    "address": "Via Dogana, 1, 20123 Milan, Italy",
    "type": "ice cream",
    "rating": 10
  }
]
```

Our restaurant dataset looks like this once we add `_geo` data:

```json theme={null}
[
  {
    "id": 1,
    "name": "Nàpiz' Milano",
    "address": "Viale Vittorio Veneto, 30, 20124, Milan, Italy",
    "type": "pizza",
    "rating": 9,
    "_geo": {
      "lat": 45.4777599,
      "lng": 9.1967508
    }
  },
  {
    "id": 2,
    "name": "Bouillon Pigalle",
    "address": "22 Bd de Clichy, 75018 Paris, France",
    "type": "french",
    "rating": 8,
    "_geo": {
      "lat": 48.8826517,
      "lng": 2.3352748
    }
  },
  {
    "id": 3,
    "name": "Artico Gelateria Tradizionale",
    "address": "Via Dogana, 1, 20123 Milan, Italy",
    "type": "ice cream",
    "rating": 10,
    "_geo": {
      "lat": 45.4632046,
      "lng": 9.1719421
    }
  }
]
```

<Warning>
  Trying to index a dataset with one or more documents containing badly formatted `_geo` values will cause Meilisearch to throw an [`invalid_document_geo_field`](/reference/errors/error_codes#invalid_document_geo_field) error. In this case, the update will fail and no documents will be added or modified.
</Warning>

### Using `_geo` with CSV

If your dataset is formatted as CSV, the file header must have a `_geo` column. Each row in the dataset must then contain a column with a comma-separated string indicating latitude and longitude:

```csv theme={null}
"id:number","name:string","address:string","type:string","rating:number","_geo:string"
"1","Nàpiz Milano","Viale Vittorio Veneto, 30, 20124, Milan, Italy","pizzeria",9,"45.4777599,9.1967508"
"2","Bouillon Pigalle","22 Bd de Clichy, 75018 Paris, France","french",8,"48.8826517,2.3352748"
"3","Artico Gelateria Tradizionale","Via Dogana, 1, 20123 Milan, Italy","ice cream",10,"48.8826517,2.3352748"
```

CSV files do not support the `_geojson` attribute.

## Filtering results with `_geoRadius`, `_geoBoundingBox`, and `_geoPolygon`

You can use `_geo` and `_geojson` data to filter queries so you only receive results located within a given geographic area.

### Configuration

To filter results based on their location, you must add `_geo` or `_geojson` to the `filterableAttributes` list:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/restaurants/settings/filterable-attributes' \
    -H 'Content-type:application/json' \
    --data-binary '["_geo"]'
  ```

  ```javascript JS theme={null}
  client.index('restaurants')
  .updateFilterableAttributes([
    '_geo'
  ])
  ```

  ```python Python theme={null}
  client.index('restaurants').update_filterable_attributes([
    '_geo'
  ])
  ```

  ```php PHP theme={null}
  $client->index('restaurants')->updateFilterableAttributes([
    '_geo'
  ]);
  ```

  ```java Java theme={null}
  Settings settings = new Settings();
  settings.setFilterableAttributes(new String[] {"_geo"});
  client.index("restaurants").updateSettings(settings);
  ```

  ```ruby Ruby theme={null}
  client.index('restaurants').update_filterable_attributes(['_geo'])
  ```

  ```go Go theme={null}
  filterableAttributes := []interface{}{
    "_geo",
  }
  client.Index("restaurants").UpdateFilterableAttributes(&filterableAttributes)
  ```

  ```csharp C# theme={null}
  List<string> attributes = new() { "_geo" };
  TaskInfo result = await client.Index("movies").UpdateFilterableAttributesAsync(attributes);
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("restaurants")
    .set_filterable_attributes(&["_geo"])
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("restaurants").updateFilterableAttributes(["_geo"]) { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('restaurants').updateFilterableAttributes(['_geo']);
  ```
</CodeGroup>

Meilisearch will rebuild your index whenever you update `filterableAttributes`. Depending on the size of your dataset, this might take a considerable amount of time.

[You can read more about configuring `filterableAttributes` in our dedicated filtering guide.](/learn/filtering_and_sorting/filter_search_results)

### Usage

Use the [`filter` search parameter](/reference/api/search#filter) along with `_geoRadius` and `_geoBoundingBox`. These are special filter rules that ensure Meilisearch only returns results located within a specific geographic area. If you are using GeoJSON for your documents, you may also filter results with `_geoPolygon`.

### `_geoRadius`

```
_geoRadius(lat, lng, distance_in_meters, resolution)
```

### `_geoBoundingBox`

```
_geoBoundingBox([LAT, LNG], [LAT, LNG])
```

### `_geoPolygon`

```
_geoPolygon([LAT, LNG], [LAT, LNG], [LAT, LNG], …)
```

### Examples

Using our <a href="/assets/datasets/restaurants.json">example dataset</a>, we can search for places to eat near the center of Milan with `_geoRadius`:

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

We also make a similar query using `_geoBoundingBox`:

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

And with `_geoPolygon`:

<CodeSamplesGeosearchGuideFilterUsage4 />

```json theme={null}
[
  {
    "id": 1,
    "name": "Nàpiz' Milano",
    "address": "Viale Vittorio Veneto, 30, 20124, Milan, Italy",
    "type": "pizza",
    "rating": 9,
    "_geo": {
      "lat": 45.4777599,
      "lng": 9.1967508
    }
  },
  {
    "id": 3,
    "name": "Artico Gelateria Tradizionale",
    "address": "Via Dogana, 1, 20123 Milan, Italy",
    "type": "ice cream",
    "rating": 10,
    "_geo": {
      "lat": 45.4632046,
      "lng": 9.1719421
    }
  }
]
```

It is also possible to combine `_geoRadius`, `_geoBoundingBox`, and `_geoPolygon` with other filters. We can narrow down our previous search so it only includes pizzerias:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/restaurants/search' \
    -H 'Content-type:application/json' \
    --data-binary '{ "filter": "_geoRadius(45.472735, 9.184019, 2000) AND type = pizza" }'
  ```

  ```javascript JS theme={null}
  client.index('restaurants').search('', {
    filter: ['_geoRadius(45.472735, 9.184019, 2000) AND type = pizza'],
  })
  ```

  ```python Python theme={null}
  client.index('restaurants').search('', {
    'filter': '_geoRadius(45.472735, 9.184019, 2000) AND type = pizza'
  })
  ```

  ```php PHP theme={null}
  $client->index('restaurants')->search('', [
    'filter' => '_geoRadius(45.472735, 9.184019, 2000) AND type = pizza'
  ]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("").filter(new String[] {"_geoRadius(45.472735, 9.184019, 2000) AND type = pizza"}).build();
  client.index("restaurants").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('restaurants').search('', { filter: '_geoRadius(45.472735, 9.184019, 2000) AND type = pizza' })
  ```

  ```go Go theme={null}
  resp, err := client.Index("restaurants").Search("", &meilisearch.SearchRequest{
    Filter: "_geoRadius(45.472735, 9.184019, 2000) AND type = pizza",
  })
  ```

  ```csharp C# theme={null}
  SearchQuery filters = new SearchQuery()
  {
      Filter = new string[] { "_geoRadius(45.472735, 9.184019, 2000) AND type = pizza" }
  };

  var restaurants = await client.Index("restaurants").SearchAsync<Restaurant>("restaurants", filters);
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Restaurant> = client
    .index("restaurants")
    .search()
    .with_filter("_geoRadius(45.472735, 9.184019, 2000) AND type = pizza")
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(
      filter: "_geoRadius(45.472735, 9.184019, 2000) AND type = pizza"
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
          filterExpression: Meili.and([
            Meili.geoRadius(
              (lat: 45.472735, lng: 9.184019),
              2000,
            ),
            Meili.attr('type').eq('pizza'.toMeiliValue())
          ]),
        ),
      );
  ```
</CodeGroup>

```json theme={null}
[
  {
    "id": 1,
    "name": "Nàpiz' Milano",
    "address": "Viale Vittorio Veneto, 30, 20124, Milan, Italy",
    "type": "pizza",
    "rating": 9,
    "_geo": {
      "lat": 45.4777599,
      "lng": 9.1967508
    }
  }
]
```

<Warning>
  `_geo`, `_geoDistance`, and `_geoPoint` are not valid filter rules. Trying to use any of them with the `filter` search parameter will result in an [`invalid_search_filter`](/reference/errors/error_codes#invalid_search_filter) error.
</Warning>

## Sorting results with `_geoPoint`

### Configuration

Before using geosearch for sorting, you must add the `_geo` attribute to the [`sortableAttributes` list](/learn/filtering_and_sorting/sort_search_results):

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/restaurants/settings/sortable-attributes' \
    -H 'Content-type:application/json' \
    --data-binary '["_geo"]'
  ```

  ```javascript JS theme={null}
  client.index('restaurants').updateSortableAttributes([
    '_geo'
  ])
  ```

  ```python Python theme={null}
  client.index('restaurants').update_sortable_attributes([
    '_geo'
  ])
  ```

  ```php PHP theme={null}
  $client->index('restaurants')->updateSortableAttributes([
    '_geo'
  ]);
  ```

  ```java Java theme={null}
  client.index("restaurants").updateSortableAttributesSettings(new String[] {"_geo"});
  ```

  ```ruby Ruby theme={null}
  client.index('restaurants').update_sortable_attributes(['_geo'])
  ```

  ```go Go theme={null}
  sortableAttributes := []string{
    "_geo",
  }
  client.Index("restaurants").UpdateSortableAttributes(&sortableAttributes)
  ```

  ```csharp C# theme={null}
  List<string> attributes = new() { "_geo" };
  TaskInfo result = await client.Index("restaurants").UpdateSortableAttributesAsync(attributes);
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("restaurants")
    .set_sortable_attributes(&["_geo"])
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("restaurants").updateSortableAttributes(["_geo"]) { (result) in
    switch result {
    case .success(let task):
      print(task)
    case .failure(let error):
      print(error)
    }
  }
  ```

  ```dart Dart theme={null}
  await client.index('restaurants').updateSortableAttributes(['_geo']);
  ```
</CodeGroup>

<Danger>
  It is not possible to sort documents based on the `_geojson` attribute.
</Danger>

### Usage

```
_geoPoint(0.0, 0.0):asc
```

### Examples

The `_geoPoint` sorting function can be used like any other sorting rule. We can order documents based on how close they are to the Eiffel Tower:

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

With our <a href="/assets/datasets/restaurants.json">restaurants dataset</a>, the results look like this:

```json theme={null}
[
  {
    "id": 2,
    "name": "Bouillon Pigalle",
    "address": "22 Bd de Clichy, 75018 Paris, France",
    "type": "french",
    "rating": 8,
    "_geo": {
      "lat": 48.8826517,
      "lng": 2.3352748
    }
  },
  {
    "id": 3,
    "name": "Artico Gelateria Tradizionale",
    "address": "Via Dogana, 1, 20123 Milan, Italy",
    "type": "ice cream",
    "rating": 10,
    "_geo": {
      "lat": 45.4632046,
      "lng": 9.1719421
    }
  },
  {
    "id": 1,
    "name": "Nàpiz' Milano",
    "address": "Viale Vittorio Veneto, 30, 20124, Milan, Italy",
    "type": "pizza",
    "rating": 9,
    "_geo": {
      "lat": 45.4777599,
      "lng": 9.1967508
    }
  }
]
```

`_geoPoint` also works when used together with other sorting rules. We can sort restaurants based on their proximity to the Eiffel Tower and their rating:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/restaurants/search' \
    -H 'Content-type:application/json' \
    --data-binary '{
      "sort": [
        "_geoPoint(48.8561446,2.2978204):asc",
        "rating:desc"
      ]
    }'
  ```

  ```javascript JS theme={null}
  client.index('restaurants').search('', {
    sort: ['_geoPoint(48.8561446, 2.2978204):asc', 'rating:desc'],
  })
  ```

  ```python Python theme={null}
  client.index('restaurants').search('', {
    'sort': ['_geoPoint(48.8561446,2.2978204):asc', 'rating:desc']
  })
  ```

  ```php PHP theme={null}
  $client->index('restaurants')->search('', [
    'sort' => ['_geoPoint(48.8561446,2.2978204):asc', 'rating:desc']
  ]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q()("").sort(new String[] {
      "_geoPoint(48.8561446,2.2978204):asc",
      "rating:desc",
    }).build();
  client.index("restaurants").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('restaurants').search('', { sort: ['_geoPoint(48.8561446, 2.2978204):asc', 'rating:desc'] })
  ```

  ```go Go theme={null}
  resp, err := client.Index("restaurants").Search("", &meilisearch.SearchRequest{
    Sort: []string{
      "_geoPoint(48.8561446,2.2978204):asc",
      "rating:desc",
    },
  })
  ```

  ```csharp C# theme={null}
  SearchQuery filters = new SearchQuery()
  {
      Sort = new string[] {
            "_geoPoint(48.8561446,2.2978204):asc",
            "rating:desc"
      }
  };

  var restaurants = await client.Index("restaurants").SearchAsync<Restaurant>("restaurants", filters);
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Restaurant> = client
    .index("restaurants")
    .search()
    .with_sort(&["_geoPoint(48.8561446, 2.2978204):asc", "rating:desc"])
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(
      query: "",
      sort: ["_geoPoint(48.8561446, 2.2978204):asc", "rating:desc"]
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
          sort: ['_geoPoint(48.8561446, 2.2978204):asc', 'rating:desc']));
  ```
</CodeGroup>

```json theme={null}
[
  {
    "id": 2,
    "name": "Bouillon Pigalle",
    "address": "22 Bd de Clichy, 75018 Paris, France",
    "type": "french",
    "rating": 8,
    "_geo": {
      "lat": 48.8826517,
      "lng": 2.3352748
    }
  },
  {
    "id": 3,
    "name": "Artico Gelateria Tradizionale",
    "address": "Via Dogana, 1, 20123 Milan, Italy",
    "type": "ice cream",
    "rating": 10,
    "_geo": {
      "lat": 45.4632046,
      "lng": 9.1719421
    }
  },
  {
    "id": 1,
    "name": "Nàpiz' Milano",
    "address": "Viale Vittorio Veneto, 30, 20124, Milan, Italy",
    "type": "pizza",
    "rating": 9,
    "_geo": {
      "lat": 45.4777599,
      "lng": 9.1967508
    }
  }
]
```