# Documents
Source: https://www.meilisearch.com/docs/reference/api/documents

The /documents route allows you to create, manage, and delete documents.

The `/documents` route allows you to create, manage, and delete documents.

[Learn more about documents.](/learn/getting_started/documents)

## Get documents with POST

<RouteHighlighter method="POST" />

Get a set of documents.

Use `offset` and `limit` to browse through documents.

<Warning>
  `filter` will not work without first explicitly adding attributes to the [`filterableAttributes` list](/reference/api/settings#update-filterable-attributes). [Learn more about filters in our dedicated guide.](/learn/filtering_and_sorting/filter_search_results)
</Warning>

### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

### Body

| Name                  | Type                                    | Default Value                                                           | Description                                                           |
| :-------------------- | :-------------------------------------- | :---------------------------------------------------------------------- | :-------------------------------------------------------------------- |
| **`offset`**          | Integer                                 | `0`                                                                     | Number of documents to skip                                           |
| **`limit`**           | Integer                                 | `20`                                                                    | Number of documents to return                                         |
| **`fields`**          | Array of strings/`null`                 | `*`                                                                     | Document attributes to show (case-sensitive, comma-separated)         |
| **`filter`**          | String/Array of array of strings/`null` | N/A                                                                     | Refine results based on attributes in the `filterableAttributes` list |
| **`retrieveVectors`** | Boolean                                 | `false`                                                                 | Return document vector data with search result                        |
| **`sort`**            | `null`                                  | A list of attributes written as an array or as a comma-separated string |                                                                       |
| **`ids`**             | Array of primary keys                   | `null`                                                                  | Return documents based on their primary keys                          |

<Note>
  Sending an empty payload (`--data-binary '{}'`) will return all documents in the index.
</Note>

### Response

| Name          | Type    | Description                            |
| :------------ | :------ | :------------------------------------- |
| **`results`** | Array   | An array of documents                  |
| **`offset`**  | Integer | Number of documents skipped            |
| **`limit`**   | Integer | Number of documents returned           |
| **`total`**   | Integer | Total number of documents in the index |

<Note>
  #### Returned document order

  `/indexes/{index_uid}/documents/fetch` and `/indexes/{index_uid}/documents` responses do not return documents following the order of their primary keys.
</Note>

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST MEILISEARCH_URL/indexes/books/documents/fetch \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "filter": "(rating > 3 AND (genres = Adventure OR genres = Fiction)) AND language = English",
      "fields": ["title", "genres", "rating", "language"],
      "limit": 3
    }'
  ```

  ```javascript JS theme={null}
  client.index('books').getDocuments({
    filter: '(rating > 3 AND (genres = Adventure OR genres = Fiction)) AND language = English',
    fields: ['title', 'genres', 'rating', 'language'],
    limit: 3,
    sort: ['release_date:desc']
  })
  ```

  ```python Python theme={null}
  client.index('books').get_documents({
    'limit':3,
    'fields': ['title', 'genres', 'rating', 'language'],
    'filter': '(rating > 3 AND (genres=Adventure OR genres=Fiction)) AND language=English',
    'sort': 'rating:desc, title:asc'  # comma-separated string format
  })
  ```

  ```php PHP theme={null}
  $client->index('books')->getDocuments(
    (new DocumentsQuery())
      ->setFilter('(rating > 3 AND (genres = Adventure OR genres = Fiction)) AND language = English')
      ->setLimit(3)
      ->setFields(['title', 'genres', 'rating', 'language'])
  );
  ```

  ```java Java theme={null}
  DocumentsQuery query = new DocumentsQuery()
    .setFilter(new String[] {"(rating > 3 AND (genres = Adventure OR genres = Fiction)) AND language = English"})
    .setFields(new String[] {"title", "genres", "rating", "language"})
    .setLimit(3);
  client.index("books").getDocuments(query, TargetClassName.class);
  ```

  ```ruby Ruby theme={null}
  client.index('books').get_documents(
    filter: '(rating > 3 AND (genres = Adventure OR genres = Fiction)) AND language = English',
    limit: 3,
    fields: ['title', 'genres', 'rating', 'language']
  )
  ```

  ```go Go theme={null}
  var result meilisearch.DocumentsResult

  client.Index("books").GetDocuments(&meilisearch.DocumentsQuery{
    Fields: []string{"title", "genres", "rating", "language"},
    Filter: "(rating > 3 AND (genres = Adventure OR genres = Fiction)) AND language = English",
  }, &result)
  ```

  ```csharp C# theme={null}
  await client.Index("movies").GetDocumentsAsync<Movie>(new DocumentsQuery() {
      Limit = 3,
      Fields = new List<string> { "title", "genres", "rating", "language"},
      Filter = "(rating > 3 AND (genres=Adventure OR genres=Fiction)) AND language=English"
  });
  ```

  ```rust Rust theme={null}
  let index = client.index("books");
  let documents: DocumentsResults = DocumentsQuery::new(&index)
    .with_filter("(rating > 3 AND (genres = Adventure OR genres = Fiction)) AND language = English")
    .with_fields(["title", "genres", "rating", "language"])
    .with_limit(2)
    .execute::<Movies>()
    .await
    .unwrap();
  ```

  ```dart Dart theme={null}
  await client.index('movies').getDocuments(
        params: DocumentsQuery(
          filterExpression: Meili.and([
            'language'.toMeiliAttribute().eq('English'.toMeiliValue()),
            Meili.and([
              'rating'.toMeiliAttribute().gt(3.toMeiliValue()),
              Meili.or([
                'genres'.toMeiliAttribute().eq('Adventure'.toMeiliValue()),
                'genres'.toMeiliAttribute().eq('Fiction'.toMeiliValue()),
              ]),
            ]),
          ]),
          fields: ['title', 'genres', 'rating', 'language'],
          limit: 3,
        ),
      );
  ```
</CodeGroup>

#### Response: `200 Ok`

```json theme={null}
{
  "results": [
    {
      "title": "The Travels of Ibn Battuta",
      "genres": [
        "Travel",
        "Adventure"
      ],
      "language": "English",
      "rating": 4.5
    },
    {
      "title": "Pride and Prejudice",
      "genres": [
        "Classics",
        "Fiction",
        "Romance",
        "Literature"
      ],
      "language": "English",
      "rating": 4
    },
    …
  ],
  "offset": 0,
  "limit": 3,
  "total": 5
}
```

## Get documents with GET

<Warning>
  This endpoint will be deprecated in the near future. Consider using POST `/indexes/{index_uid}/documents/fetch` instead.
</Warning>

<RouteHighlighter method="GET" />

Get a set of documents.

Using the query parameters `offset` and `limit`, you can browse through all your documents.`filter` must be a string. To create [filter expressions](/learn/filtering_and_sorting/filter_expression_reference) use `AND` or `OR`.

<Warning>
  `filter` will not work without first explicitly adding attributes to the [`filterableAttributes` list](/reference/api/settings#update-filterable-attributes). [Learn more about filters in our dedicated guide.](/learn/filtering_and_sorting/filter_search_results)
</Warning>

### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

### Query parameters

| Query Parameter       | Default Value | Description                                                           |
| :-------------------- | :------------ | :-------------------------------------------------------------------- |
| **`offset`**          | `0`           | Number of documents to skip                                           |
| **`limit`**           | `20`          | Number of documents to return                                         |
| **`fields`**          | `*`           | Document attributes to show (case-sensitive, comma-separated)         |
| **`filter`**          | N/A           | Refine results based on attributes in the `filterableAttributes` list |
| **`retrieveVectors`** | `false`       | Return document vector data with search result                        |
| **`sort`**            | `null`        | A list of comma-separated attributes                                  |
| **`ids`**             | `null`        | Return documents based on their primary keys                          |

### Response

| Name          | Type    | Description                            |
| :------------ | :------ | :------------------------------------- |
| **`results`** | Array   | An array of documents                  |
| **`offset`**  | Integer | Number of documents skipped            |
| **`limit`**   | Integer | Number of documents returned           |
| **`total`**   | Integer | Total number of documents in the index |

<Note>
  #### Returned document order

  `/indexes/{index_uid}/documents/fetch` and `/indexes/{index_uid}/documents` responses do not return documents following the order of their primary keys.
</Note>

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/movies/documents?limit=2&filter=genres=action'
  ```

  ```javascript JS theme={null}
  client.index('movies').getDocuments({
    limit: 2,
    filter: 'genres = action',
    sort: ['release_date:desc']
  })
  ```

  ```python Python theme={null}
  client.index('movies').get_documents({
    'limit':2, 'filter': 'genres=action',
    'sort': ['rating:desc', 'release_date:asc']  # list format
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->getDocuments((new DocumentsQuery())->setFilter('genres = action')->setLimit(2));
  ```

  ```java Java theme={null}
  DocumentsQuery query = new DocumentsQuery().setLimit(2).setFilter(new String[] {"genres = action"});
  client.index("movies").getDocuments(query, TargetClassName.class);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').get_documents(limit: 2, filter: 'genres = action')
  ```

  ```go Go theme={null}
  var result meilisearch.DocumentsResult

  client.Index("movies").GetDocuments(&meilisearch.DocumentsQuery{
    Limit: 2,
    Filter: "genres = action",
  }, &result)
  ```

  ```csharp C# theme={null}
  await client.Index("movies").GetDocumentsAsync<Movie>(new DocumentsQuery() { Limit = 2, Filter = "genres = action" });
  ```

  ```rust Rust theme={null}
  let index = client.index("movies");
  let documents: DocumentsResults = DocumentsQuery::new(&index)
    .with_filter("genres = action")
    .with_limit(2)
    .execute::<Movies>()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").getDocuments(params: DocumentsQuery(limit: 2)) { (result: Result<DocumentsResults<Movie>, Swift.Error>) in
      switch result {
      case .success(let movies):
          print(movies)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').getDocuments(
        params: DocumentsQuery(
          limit: 2,
          filter: Meili.attr('genres').eq('action'.toMeiliValue()),
        ),
      );
  ```
</CodeGroup>

#### Response: `200 Ok`

```json theme={null}
{
  "results": [
    {
      "id": 364,
      "title": "Batman Returns",
      "overview": "While Batman deals with a deformed man calling himself the Penguin, an employee of a corrupt businessman transforms into the Catwoman.",
      "genres": [
        "Action",
        "Fantasy"
      ],
      "poster": "https://image.tmdb.org/t/p/w500/jKBjeXM7iBBV9UkUcOXx3m7FSHY.jpg",
      "release_date": 708912000
    },
    {
      "id": 13851,
      "title": " Batman: Gotham Knight",
      "overview": "A collection of key events mark Bruce Wayne's life as he journeys from beginner to Dark Knight.",
      "genres": [
        "Animation",
        "Action",
        "Adventure"
      ],
      "poster": "https://image.tmdb.org/t/p/w500/f3xUrqo7yEiU0guk2Ua3Znqiw6S.jpg",
      "release_date": 1215475200
    }
  ],
  "offset": 0,
  "limit": 2,
  "total": 5403
}
```

## Get one document

<RouteHighlighter method="GET" />

Get one document using its unique id.

### Path parameters

| Name                 | Type           | Description                                                                             |
| :------------------- | :------------- | :-------------------------------------------------------------------------------------- |
| **`index_uid`** \*   | String         | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index                |
| **`document_id`** \* | String/Integer | [Document id](/learn/getting_started/primary_key#document-id) of the requested document |

### Query parameters

| Query Parameter       | Default Value | Description                                                   |
| :-------------------- | :------------ | :------------------------------------------------------------ |
| **`fields`**          | `*`           | Document attributes to show (case-sensitive, comma-separated) |
| **`retrieveVectors`** | `false`       | Return document vector data with search result                |

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/movies/documents/25684?fields=id,title,poster,release_date'
  ```

  ```javascript JS theme={null}
  client
      .index('movies')
      .getDocument(25684, { fields: ['id', 'title', 'poster', 'release_date'] })
  ```

  ```python Python theme={null}
  client.index('movies').get_document(25684, {
    'fields': ['id', 'title', 'poster', 'release_date']
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->getDocument(25684, ['id', 'title', 'poster', 'release_date']);
  ```

  ```java Java theme={null}
  DocumentQuery query = new DocumentQuery().setFields(new String[] {"id", "title", "poster", "release_date"});
  client.index("movies").getDocument("25684", query);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').document(25684, fields: ['id', 'title', 'poster', 'release_date'])
  ```

  ```go Go theme={null}
  var a interface{}
  client.Index("movies").GetDocument("25684",&meilisearch.DocumentQuery{
    Fields: []string{"id", "title", "poster", "release_date"},
  }, &a)
  ```

  ```csharp C# theme={null}
  await client.Index("movies").GetDocumentAsync<Movie>(25684, new List<string> { "id", "title", "poster", "release_date" });
  ```

  ```rust Rust theme={null}
  let index = client
    .index("movies");
  let document = DocumentQuery::new(&index)
    .with_fields(["id", "title", "poster", "release_date"])
    .execute::<Movie>("25684")
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").getDocument(25684) { (result: Result<Movie, Swift.Error>) in
      switch result {
      case .success(let movie):
          print(movie)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').getDocument(25684,
      fields: ['id', 'title', 'poster', 'release_date']);
  ```
</CodeGroup>

#### Response: `200 Ok`

```json theme={null}
{
  "id": 25684,
  "title": "American Ninja 5",
  "poster": "https://image.tmdb.org/t/p/w1280/iuAQVI4mvjI83wnirpD8GVNRVuY.jpg",
  "release_date": "1993-01-01"
}
```

## Add or replace documents

<RouteHighlighter method="POST" />

Add an array of documents or replace them if they already exist. If the provided index does not exist, it will be created.

If you send an already existing document (same [document id](/learn/getting_started/primary_key#document-id)) the **whole existing document** will be overwritten by the new document. Fields that are no longer present in the new document are removed. For a partial update of the document see the [add or update documents](/reference/api/documents#add-or-update-documents) endpoint.

This endpoint accepts the following content types:

* `application/json`
* `application/x-ndjson`
* `text/csv`

### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

### Query parameters

| Query Parameter      | Default Value | Description                                                                                                                             |
| :------------------- | :------------ | :-------------------------------------------------------------------------------------------------------------------------------------- |
| **`primaryKey`**     | `null`        | [Primary key](/learn/getting_started/primary_key#primary-field) of the index                                                            |
| **`csvDelimiter`**   | `","`         | Configure the character separating CSV fields. Must be a string containing [one ASCII character](https://www.rfc-editor.org/rfc/rfc20). |
| **`customMetadata`** | `null`        | An arbitrary string accessible via the [generated task object](/reference/api/tasks#custommetadata)                                     |
| **`skipCreation`**   | `false`       | If `true`, updates existing documents, but does not add new documents to the index                                                      |

<Warning>
  Configuring `csvDelimiter` and sending data with a content type other than CSV will cause Meilisearch to throw an error.
</Warning>

If you want to [set the primary key of your index on document addition](/learn/getting_started/primary_key#setting-the-primary-key-on-document-addition), it can only be done **the first time you add documents** to the index. After this, the `primaryKey` parameter will be ignored if given.

### Body

An array of documents. Each document is represented as a JSON object.

```json theme={null}
[
  {
    "id": 287947,
    "title": "Shazam",
    "poster": "https://image.tmdb.org/t/p/w1280/xnopI5Xtky18MPhK40cZAGAOVeV.jpg",
    "overview": "A boy is given the ability to become an adult superhero in times of need with a single magic word.",
    "release_date": "2019-03-23"
  }
]
```

#### `_vectors`

`_vectors` is a special document attribute containing an object with vector embeddings for AI-powered search.

Each key of the `_vectors` object must be the name of a configured embedder and correspond to a nested object with two fields, `embeddings` and `regenerate`:

```json theme={null}
[
  {
    "id": 452,
    "title": "Female Trouble",
    "overview": "Delinquent high school student Dawn Davenport runs away from home and embarks upon a life of crime.",
    "_vectors": {
      "default": {
        "embeddings": [0.1, 0.2, 0.3],
        "regenerate": false
      },
      "ollama": {
        "embeddings": [0.4, 0.12, 0.6],
        "regenerate": true
      }
    }
  }
]
```

`embeddings` is an optional field. It must be an array of numbers representing a single embedding for that document. It may also be an array of arrays of numbers representing multiple embeddings for that document. `embeddings` defaults to `null`.

`regenerate` is a mandatory field. It must be a Boolean value. If `regenerate` is `true`, Meilisearch automatically generates embeddings for that document immediately and every time the document is updated. If `regenerate` is `false`, Meilisearch keeps the last value of the embeddings on document updates.

You may also use an array shorthand to add embeddings to a document:

```json theme={null}
"_vectors": {
  "default": [0.003, 0.1, 0.75]
}
```

Vector embeddings added with the shorthand are not replaced when Meilisearch generates new embeddings. The above example is equivalent to:

```json theme={null}
"default": {
  "embeddings": [0.003, 0.1, 0.75],
  "regenerate": false
}
```

<Note>
  If the key for an embedder inside `_vectors` is empty or `null`, Meilisearch treats the document as not having any embeddings for that embedder. This document is then returned last during AI-powered searches.
</Note>

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/documents' \
    -H 'Content-Type: application/json' \
    --data-binary '[
      {
        "id": 287947,
        "title": "Shazam",
        "poster": "https://image.tmdb.org/t/p/w1280/xnopI5Xtky18MPhK40cZAGAOVeV.jpg",
        "overview": "A boy is given the ability to become an adult superhero in times of need with a single magic word.",
        "release_date": "2019-03-23"
      }
    ]'
  ```

  ```javascript JS theme={null}
  client.index('movies').addDocuments([{
      id: 287947,
      title: 'Shazam',
      poster: 'https://image.tmdb.org/t/p/w1280/xnopI5Xtky18MPhK40cZAGAOVeV.jpg',
      overview: 'A boy is given the ability to become an adult superhero in times of need with a single magic word.',
      release_date: '2019-03-23'
  }])
  ```

  ```python Python theme={null}
  client.index('movies').add_documents([{
    'id': 287947,
    'title': 'Shazam',
    'poster': 'https://image.tmdb.org/t/p/w1280/xnopI5Xtky18MPhK40cZAGAOVeV.jpg',
    'overview': 'A boy is given the ability to become an adult superhero in times of need with a single magic word.',
    'release_date': '2019-03-23'
  }], skip_creation=True)
  ```

  ```php PHP theme={null}
  $client->index('movies')->addDocuments([
    [
      'id' => 287947,
      'title' => 'Shazam',
      'poster' => 'https://image.tmdb.org/t/p/w1280/xnopI5Xtky18MPhK40cZAGAOVeV.jpg',
      'overview' => 'A boy is given the ability to become an adult superhero in times of need with a single magic word.',
      'release_date' => '2019-03-23'
    ]
  ]);
  ```

  ```java Java theme={null}
  client.index("movies").addDocuments("[{"
    + "\"id\": 287947,"
    + "\"title\": \"Shazam\","
    + "\"poster\": \"https://image.tmdb.org/t/p/w1280/xnopI5Xtky18MPhK40cZAGAOVeV.jpg\","
    + "\"overview\": \"A boy is given the ability to become an adult superhero in times of need with a single magic word.\","
    + "\"release_date\": \"2019-03-23\""
    + "}]"
  );
  ```

  ```ruby Ruby theme={null}
  client.index('movies').add_documents([
    {
      id: 287947,
      title: 'Shazam',
      poster: 'https://image.tmdb.org/t/p/w1280/xnopI5Xtky18MPhK40cZAGAOVeV.jpg',
      overview: 'A boy is given the ability to become an adult superhero in times of need with a single magic word.',
      release_date: '2019-03-23'
    }
  ])
  ```

  ```go Go theme={null}
  documents := []map[string]interface{}{
    {
      "id":           287947,
      "title":        "Shazam",
      "poster":       "https://image.tmdb.org/t/p/w1280/xnopI5Xtky18MPhK40cZAGAOVeV.jpg",
      "overview":     "A boy is given the ability to become an adult superhero in times of need with a single magic word.",
      "release_date": "2019-03-23",
    },
  }
  options := &meilisearch.DocumentOptions{SkipCreation: false}
  client.Index("movies").AddDocuments(documents, options)
  ```

  ```csharp C# theme={null}
  var movie = new[]
  {
      new Movie
      {
            Id = "287947",
            Title = "Shazam",
            Poster = "https://image.tmdb.org/t/p/w1280/xnopI5Xtky18MPhK40cZAGAOVeV.jpg",
            Overview = "A boy is given the ability to become an adult superhero in times of need with a single magic word.",
            ReleaseDate = "2019-03-23"
      }
  };
  await index.AddDocumentsAsync(movie);
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("movies")
    .add_or_replace(&[
      Movie {
        id: 287947,
        title: "Shazam".to_string(),
        poster: "https://image.tmdb.org/t/p/w1280/xnopI5Xtky18MPhK40cZAGAOVeV.jpg".to_string(),
        overview: "A boy is given the ability to become an adult superhero in times of need with a single magic word.".to_string(),
        release_date: "2019-03-23".to_string(),
      }
    ], None)
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let documentJsonString = """
  [
    {
      "reference_number": 287947,
      "title": "Shazam",
      "poster": "https://image.tmdb.org/t/p/w1280/xnopI5Xtky18MPhK40cZAGAOVeV.jpg",
      "overview": "A boy is given the ability to become an adult superhero in times of need with a single magic word.",
      "release_date": "2019-03-23"
    }
  ]
  """
  let documents: Data = documentJsonString.data(using: .utf8)!

  client.index("movies").addDocuments(documents: documents) { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').addDocuments([
    {
      'id': 287947,
      'title': 'Shazam',
      'poster':
          'https://image.tmdb.org/t/p/w1280/xnopI5Xtky18MPhK40cZAGAOVeV.jpg',
      'overview':
          'A boy is given the ability to become an adult superhero in times of need with a single magic word.',
      'release_date': '2019-03-23'
    }
  ]);
  ```
</CodeGroup>

#### Response: `202 Accepted`

```json theme={null}
{
    "taskUid": 1,
    "indexUid": "movies",
    "status": "enqueued",
    "type": "documentAdditionOrUpdate",
    "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Add or update documents

<RouteHighlighter method="PUT" />

Add a list of documents or update them if they already exist. If the provided index does not exist, it will be created.

If you send an already existing document (same [document id](/learn/getting_started/primary_key#document-id)) the old document will be only partially updated according to the fields of the new document. Any fields not present in the new document are kept and remain unchanged.

<Warning>
  Partial updates apply only to top-level fields. You cannot perform a partial update of a nested field.

  Updating an object replaces the entire object and removes any omitted subfields.

  Using dot notation in an update request creates a new flat attribute instead of updating the existing nested field.
</Warning>

To completely overwrite a document, check out the [add or replace documents route](/reference/api/documents#add-or-replace-documents).

If you want to set the [**primary key** of your index](/learn/getting_started/primary_key#setting-the-primary-key-on-document-addition) through this route, you may only do so **the first time you add documents** to the index. If you try to set the primary key after having added documents to the index, the task will return an error.

This endpoint accepts the following content types:

* `application/json`
* `application/x-ndjson`
* `text/csv`

### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

### Query parameters

| Query Parameter      | Default Value | Description                                                                                                                             |
| :------------------- | :------------ | :-------------------------------------------------------------------------------------------------------------------------------------- |
| **`primaryKey`**     | `null`        | [Primary key](/learn/getting_started/primary_key#primary-field) of the documents                                                        |
| **`csvDelimiter`**   | `","`         | Configure the character separating CSV fields. Must be a string containing [one ASCII character](https://www.rfc-editor.org/rfc/rfc20). |
| **`customMetadata`** | `null`        | An arbitrary string accessible via the [generated task object](/reference/api/tasks#custommetadata)                                     |
| **`skipCreation`**   | `false`       | If `true`, updates existing documents, but does not add new documents to the index                                                      |

<Warning>
  Configuring `csvDelimiter` and sending data with a content type other than CSV will cause Meilisearch to throw an error.
</Warning>

### Body

An array of documents. Each document is represented as a JSON object.

```json theme={null}
[
  {
    "id": 287947,
    "title": "Shazam ⚡️"
  }
]
```

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/movies/documents' \
    -H 'Content-Type: application/json' \
    --data-binary '[
      {
        "id": 287947,
        "title": "Shazam ⚡️",
        "genres": "comedy"
      }
    ]'
  ```

  ```javascript JS theme={null}
  client.index('movies').updateDocuments([{
      id: 287947,
      title: 'Shazam ⚡️',
      genres: 'comedy'
  }])
  ```

  ```python Python theme={null}
  client.index('movies').update_documents([{
      'id': 287947,
      'title': 'Shazam ⚡️',
      'genres': 'comedy'
  }], skip_creation=True)
  ```

  ```php PHP theme={null}
  $client->index('movies')->updateDocuments([
    [
      'id' => 287947,
      'title' => 'Shazam ⚡️',
      'genres' => 'comedy'
    ]
  ]);
  ```

  ```java Java theme={null}
  client.index("movies").updateDocuments("[{
    + "\"id\": 287947,"
    + "\"title\": \"Shazam ⚡️\","
    + "\"genres\": \"comedy\""
    + "}]"
  );
  ```

  ```ruby Ruby theme={null}
  client.index('movies').update_documents([
    {
      id: 287947,
      title: 'Shazam ⚡️',
      genres: 'comedy'
    }
  ])
  ```

  ```go Go theme={null}
  documents := []map[string]interface{}{
    {
      "id":     287947,
      "title":  "Shazam ⚡️",
      "genres": "comedy",
    },
  }
  options := &meilisearch.DocumentOptions{SkipCreation: true}
  client.Index("movies").UpdateDocuments(documents, options)
  ```

  ```csharp C# theme={null}
  var movie = new[]
  {
      new Movie { Id = "287947", Title = "Shazam ⚡️", Genres = "comedy" }
  };
  await index.UpdateDocumentsAsync(movie);
  ```

  ```rust Rust theme={null}
  // Define the type of our documents
  #[derive(Serialize, Deserialize)]
  struct IncompleteMovie {
    id: usize,
    title: String,
    genres: String
  }

  let task: TaskInfo = client
    .index("movies")
    .add_or_update(&[
      IncompleteMovie {
        id: 287947,
        title: "Shazam ⚡️".to_string(),
        genres: "comedy".to_string()
      }
    ], None)
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let documentJsonString = """
  [
    {
      "reference_number": 287947,
      "title": "Shazam ⚡️",
      "genres": "comedy"
    }
  ]
  """
  let documents: Data = documentJsonString.data(using: .utf8)!

  client.index("movies").updateDocuments(documents: documents) { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').updateDocuments([
    {
      'id': 287947,
      'title': 'Shazam ⚡️',
      'genres': 'comedy',
    }
  ]);
  ```
</CodeGroup>

This document is an update of the document found in [add or replace document](/reference/api/documents#add-or-replace-documents).

The documents are matched because they have the same [primary key](/learn/getting_started/documents#primary-field) value `id: 287947`. This route will update the `title` field as it changed from `Shazam` to `Shazam ⚡️` and add the new `genres` field to that document. The rest of the document will remain unchanged.

#### Response: `202 Accepted`

```json theme={null}
{
    "taskUid": 1,
    "indexUid": "movies",
    "status": "enqueued",
    "type": "documentAdditionOrUpdate",
    "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Update documents with function <NoticeTag type="experimental" label="experimental" />

<RouteHighlighter method="POST" />

Use a [RHAI function](https://rhai.rs/book/engine/hello-world.html) to edit one or more documents directly in Meilisearch.

<Note>
  This is an experimental feature. Use the experimental features endpoint to activate it:

  ```sh theme={null}
  curl \
    -X PATCH 'MEILISEARCH_URL/experimental-features/' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "editDocumentsByFunction": true
    }'
  ```
</Note>

### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

### Query parameters

| Query Parameter      | Default Value | Description                                                                                         |
| :------------------- | :------------ | :-------------------------------------------------------------------------------------------------- |
| **`function`**       | `null`        | A string containing a RHAI function                                                                 |
| **`filter`**         | `null`        | A string containing a filter expression                                                             |
| **`context`**        | `null`        | An object with data Meilisearch should make available for the editing function                      |
| **`customMetadata`** | `null`        | An arbitrary string accessible via the [generated task object](/reference/api/tasks#custommetadata) |

#### `function`

`function` must be a string with a RHAI function that Meilisearch will apply to all selected documents. By default this function has access to a single variable, `doc`, representing the document you are currently editing. This is a required field.

#### `filter`

`filter` must be a string containing a filter expression. Use `filter` when you want only to apply `function` to a subset of the documents in your database.

#### `context`

Use `context` to pass data to the `function` scope. By default a function only has access to the document it is editing.

### Example

```sh theme={null}
curl \
-X POST 'MEILISEARCH_URL/indexes/INDEX_NAME/documents/edit' \
-H 'Content-Type: application/json' \
--data-binary '{
  "function": "doc.title = `${doc.title.to_upper()}`"
}'
```

## Delete all documents

<RouteHighlighter method="DELETE" />

Delete all documents in the specified index.

### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

### Query parameters

| Query Parameter      | Default Value | Description                                                                                         |
| :------------------- | :------------ | :-------------------------------------------------------------------------------------------------- |
| **`customMetadata`** | `null`        | An arbitrary string accessible via the [generated task object](/reference/api/tasks#custommetadata) |

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/movies/documents'
  ```

  ```javascript JS theme={null}
  client.index('movies').deleteAllDocuments()
  ```

  ```python Python theme={null}
  client.index('movies').delete_all_documents()
  ```

  ```php PHP theme={null}
  $client->index('movies')->deleteAllDocuments();
  ```

  ```java Java theme={null}
  client.index("movies").deleteAllDocuments();
  ```

  ```ruby Ruby theme={null}
  client.index('movies').delete_all_documents
  ```

  ```go Go theme={null}
  client.Index("movies").DeleteAllDocuments()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").DeleteAllDocumentsAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("movies")
    .delete_all_documents()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").deleteAllDocuments() { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').deleteAllDocuments();
  ```
</CodeGroup>

#### Response: `202 Accepted`

```json theme={null}
{
    "taskUid": 1,
    "indexUid": "movies",
    "status": "enqueued",
    "type": "documentDeletion",
    "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Delete one document

<RouteHighlighter method="DELETE" />

Delete one document based on its unique id.

### Path parameters

| Name                 | Type           | Description                                                                             |
| :------------------- | :------------- | :-------------------------------------------------------------------------------------- |
| **`index_uid`** \*   | String         | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index                |
| **`document_id`** \* | String/Integer | [Document id](/learn/getting_started/primary_key#document-id) of the requested document |

### Query parameters

| Query Parameter      | Default Value | Description                                                                                         |
| :------------------- | :------------ | :-------------------------------------------------------------------------------------------------- |
| **`customMetadata`** | `null`        | An arbitrary string accessible via the [generated task object](/reference/api/tasks#custommetadata) |

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/movies/documents/25684'
  ```

  ```javascript JS theme={null}
  client.index('movies').deleteDocument(25684)
  ```

  ```python Python theme={null}
  client.index('movies').delete_document(25684)
  ```

  ```php PHP theme={null}
  $client->index('movies')->deleteDocument(25684);
  ```

  ```java Java theme={null}
  client.index("movies").deleteDocument("25684");
  ```

  ```ruby Ruby theme={null}
  client.index('movies').delete_document(25684)
  ```

  ```go Go theme={null}
  client.Index("movies").DeleteDocument("25684")
  ```

  ```csharp C# theme={null}
  await client.Index("movies").DeleteOneDocumentAsync("25684");
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("movies")
    .delete_document(25684)
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").deleteDocument("25684") { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').deleteDocument(25684);
  ```
</CodeGroup>

#### Response: `202 Accepted`

```json theme={null}
{
    "taskUid": 1,
    "indexUid": "movies",
    "status": "enqueued",
    "type": "documentDeletion",
    "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Delete documents by filter

<RouteHighlighter method="POST" />

Delete a set of documents based on a filter.

### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

### Query parameters

| Query Parameter      | Default Value | Description                                                                                         |
| :------------------- | :------------ | :-------------------------------------------------------------------------------------------------- |
| **`customMetadata`** | `null`        | An arbitrary string accessible via the [generated task object](/reference/api/tasks#custommetadata) |

### Body

A filter expression written as a string or array of array of strings for the documents to be deleted.

<Warning>
  `filter` will not work without first explicitly adding attributes to the [`filterableAttributes` list](/reference/api/settings#update-filterable-attributes). [Learn more about filters in our dedicated guide.](/learn/filtering_and_sorting/filter_search_results)
</Warning>

```
 "filter": "rating > 3.5"
```

<Warning>
  Sending an empty payload (`--data-binary '{}'`) will return a `bad_request` error.
</Warning>

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST MEILISEARCH_URL/indexes/movies/documents/delete \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "filter": "genres = action OR genres = adventure"
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').deleteDocuments({
    filter: 'genres = action OR genres = adventure'
  })
  ```

  ```python Python theme={null}
  client.index('movies').delete_documents(filter='genres=action OR genres=adventure')
  ```

  ```php PHP theme={null}
  $client->index('movies')->deleteDocuments(['filter' => 'genres = action OR genres = adventure']);
  ```

  ```java Java theme={null}
  String filter = "genres = action OR genres = adventure";
  client.index("movies").deleteDocumentsByFilter(filter);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').delete_documents(filter: 'genres = action OR genres = adventure')
  ```

  ```go Go theme={null}
  client.Index("movies").DeleteDocumentsByFilter("genres=action OR genres=adventure")
  ```

  ```csharp C# theme={null}
  await client.Index("movies").DeleteDocumentsAsync(new DeleteDocumentsQuery() { Filter = "genres = action OR genres = adventure" });
  ```

  ```rust Rust theme={null}
  let index = client.index("movies");
  let task = DocumentDeletionQuery::new(&index)
    .with_filter("genres = action OR genres = adventure")
    .execute()
    .await
    .unwrap();
  ```

  ```dart Dart theme={null}
  await client.index('movies').deleteDocuments(
        DeleteDocumentsQuery(
          filterExpression: Meili.or([
            Meili.attr('genres').eq(Meili.value('action')),
            Meili.attr('genres').eq(Meili.value('adventure')),
          ]),
        ),
      );
  ```
</CodeGroup>

#### Response: `202 Accepted`

```json theme={null}
{
    "taskUid": 1,
    "indexUid": "movies",
    "status": "enqueued",
    "type": "documentDeletion",
    "enqueuedAt": "2023-05-15T08:38:48.024551Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Delete documents by batch

<RouteHighlighter method="POST" />

Delete a set of documents based on an array of document ids.

### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

### Query parameters

| Query Parameter      | Default Value | Description                                                                                         |
| :------------------- | :------------ | :-------------------------------------------------------------------------------------------------- |
| **`customMetadata`** | `null`        | An arbitrary string accessible via the [generated task object](/reference/api/tasks#custommetadata) |

### Body

An array of numbers containing the unique ids of the documents to be deleted.

```json theme={null}
[23488, 153738, 437035, 363869]
```

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/documents/delete-batch' \
    -H 'Content-Type: application/json' \
    --data-binary '[
      23488,
      153738,
      437035,
      363869
    ]'
  ```

  ```javascript JS theme={null}
  client.index('movies').deleteDocuments([23488, 153738, 437035, 363869])
  ```

  ```python Python theme={null}
  client.index('movies').delete_documents([23488, 153738, 437035, 363869])
  ```

  ```php PHP theme={null}
  $client->index('movies')->deleteDocuments([23488, 153738, 437035, 363869]);
  ```

  ```java Java theme={null}
  client.index("movies").deleteDocuments(Arrays.asList(new String[]
  {
    "23488",
    "153738",
    "437035",
    "363869"
  }));
  ```

  ```ruby Ruby theme={null}
  client.index('movies').delete_documents([23488, 153738, 437035, 363869])
  ```

  ```go Go theme={null}
  client.Index("movies").DeleteDocuments([]string{
    "23488",
    "153738",
    "437035",
    "363869",
  })
  ```

  ```csharp C# theme={null}
  await client.Index("movies").DeleteDocumentsAsync(new[] { "23488", "153738", "437035", "363869" });
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("movies")
    .delete_documents(&[23488, 153738, 437035, 363869])
    .await
    .unwrap();
  ```

  ```dart Dart theme={null}
  await client.index('movies').deleteDocuments(
        DeleteDocumentsQuery(
          ids: [23488, 153738, 437035, 363869],
        ),
      );
  ```
</CodeGroup>

#### Response: `202 Accepted`

```json theme={null}
{
    "taskUid": 1,
    "indexUid": "movies",
    "status": "enqueued",
    "type": "documentDeletion",
    "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).