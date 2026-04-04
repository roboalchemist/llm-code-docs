# Displayed and searchable attributes
Source: https://www.meilisearch.com/docs/learn/relevancy/displayed_searchable_attributes

Displayed and searchable attributes define what data Meilisearch returns after a successful query and which fields Meilisearch takes in account when searching. Knowing how to configure them can help improve your application's performance.

By default, whenever a document is added to Meilisearch, all new attributes found in it are automatically added to two lists:

* [`displayedAttributes`](/learn/relevancy/displayed_searchable_attributes#displayed-fields): Attributes whose fields are displayed in documents
* [`searchableAttributes`](/learn/relevancy/displayed_searchable_attributes#the-searchableattributes-list): Attributes whose values are searched for matching query words

By default, every field in a document is **displayed** and **searchable**. These properties can be modified in the [settings](/reference/api/settings).

## Displayed fields

The fields whose attributes are added to the [`displayedAttributes` list](/reference/api/settings#displayed-attributes) are **displayed in each matching document**.

Documents returned upon search contain only displayed fields. If a field attribute is not in the displayed-attribute list, the field won't be added to the returned documents.

**By default, all field attributes are set as displayed**.

### Example

Suppose you manage a database that contains information about movies. By adding the following settings, documents returned upon search will contain the fields `title`, `overview`, `release_date` and `genres`.

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/movies/settings/displayed-attributes' \
    -H 'Content-Type: application/json' \
    --data-binary '[
        "title",
        "overview",
        "genres",
        "release_date"
      ]'
  ```

  ```javascript JS theme={null}
  client.index('movies').updateDisplayedAttributes([
      'title',
      'overview',
      'genres',
      'release_date',
    ]
  )
  ```

  ```python Python theme={null}
  client.index('movies').update_displayed_attributes([
      'title',
      'overview',
      'genres',
      'release_date'
  ])
  ```

  ```php PHP theme={null}
  $client->index('movies')->updateDisplayedAttributes([
    'title',
    'overview',
    'genres',
    'release_date'
  ]);
  ```

  ```java Java theme={null}
  String[] attributes = {"title", "overview", "genres", "release_date"}
  client.index("movies").updateDisplayedAttributesSettings(attributes);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').update_settings({
    displayed_attributes: [
      'title',
      'overview',
      'genres',
      'release_date'
    ]
  })
  ```

  ```go Go theme={null}
  displayedAttributes := []string{
    "title",
    "overview",
    "genres",
    "release_date",
  }
  client.Index("movies").UpdateDisplayedAttributes(&displayedAttributes)
  ```

  ```csharp C# theme={null}
  await client.Index("movies").UpdateDisplayedAttributesAsync(new[]
  {
      "title",
      "overview",
      "genres",
      "release_date"
  });
  ```

  ```rust Rust theme={null}
  let displayed_attributes = [
    "title",
    "overview",
    "genres",
    "release_date"
  ];

  let task: TaskInfo = client
    .index("movies")
    .set_displayed_attributes(&displayed_attributes)
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let displayedAttributes: [String] = [
      "title",
      "overview",
      "genres",
      "release_date"
  ]
  client.index("movies").updateDisplayedAttributes(displayedAttributes) { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').updateDisplayedAttributes([
    'title',
    'overview',
    'genres',
    'release_date',
  ]);
  ```
</CodeGroup>

## Searchable fields

A field can either be **searchable** or **non-searchable**.

When you perform a search, all searchable fields are checked for matching query words and used to assess document relevancy, while non-searchable fields are ignored entirely. **By default, all fields are searchable.**

Non-searchable fields are most useful for internal information that's not relevant to the search experience, such as URLs, sales numbers, or ratings used exclusively for sorting results.

<Tip>
  Even if you make a field non-searchable, it will remain [stored in the database](#data-storing) and can be made searchable again at a later time.
</Tip>

### The `searchableAttributes` list

Meilisearch uses an ordered list to determine which attributes are searchable. The order in which attributes appear in this list also determines their [impact on relevancy](/learn/relevancy/attribute_ranking_order), from most impactful to least.

In other words, the `searchableAttributes` list serves two purposes:

1. It designates the fields that are searchable
2. It dictates the [attribute ranking order](/learn/relevancy/attribute_ranking_order)

There are two possible modes for the `searchableAttributes` list.

#### Default: Automatic

**By default, all attributes are automatically added to the `searchableAttributes` list in their order of appearance.** This means that the initial order will be based on the order of attributes in the first document indexed, with each new attribute found in subsequent documents added at the end of this list.

This default behavior is indicated by a `searchableAttributes` value of `["*"]`. To verify the current value of your `searchableAttributes` list, use the [get searchable attributes endpoint](/reference/api/settings#get-searchable-attributes).

If you'd like to restore your searchable attributes list to this default behavior, [set `searchableAttributes` to an empty array `[]`](/reference/api/settings#update-searchable-attributes) or use the [reset searchable attributes endpoint](/reference/api/settings#reset-searchable-attributes).

#### Manual

You may want to make some attributes non-searchable, or change the [attribute ranking order](/learn/relevancy/attribute_ranking_order) after documents have been indexed. To do so, place the attributes in the desired order and send the updated list using the [update searchable attributes endpoint](/reference/api/settings#update-searchable-attributes).

After manually updating the `searchableAttributes` list, **subsequent new attributes will no longer be automatically added** unless the settings are [reset](/reference/api/settings#reset-searchable-attributes).

<Warning>
  Due to an implementation bug, manually updating `searchableAttributes` will change the displayed order of document fields in the JSON response. This behavior is inconsistent and will be fixed in a future release.
</Warning>

#### Example

Suppose that you manage a database of movies with the following fields: `id`, `overview`, `genres`, `title`, `release_date`. These fields all contain useful information. However, **some are more useful to search than others**. To make the `id` and `release_date` fields non-searchable and re-order the remaining fields by importance, you might update the searchable attributes list in the following way.

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/movies/settings/searchable-attributes' \
    -H 'Content-Type: application/json' \
    --data-binary '[
        "title",
        "overview",
        "genres"
      ]'
  ```

  ```javascript JS theme={null}
  client.index('movies').updateSearchableAttributes([
      'title',
      'overview',
      'genres',
    ]
  )
  ```

  ```python Python theme={null}
  client.index('movies').update_searchable_attributes([
      'title',
      'overview',
      'genres'
  ])
  ```

  ```php PHP theme={null}
  $client->index('movies')->updateSearchableAttributes([
    'title',
    'overview',
    'genres'
  ]);
  ```

  ```java Java theme={null}
  String[] attributes = {"title", "overview", "genres"}
  client.index("movies").updateSearchableAttributesSettings(attributes);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').update_searchable_attributes([
    'title',
    'overview',
    'genres'
  ])
  ```

  ```go Go theme={null}
  searchableAttributes := []string{
    "title",
    "overview",
    "genres",
  }
  client.Index("movies").UpdateSearchableAttributes(&searchableAttributes)
  ```

  ```csharp C# theme={null}
  await client.Index("movies").UpdateSearchableAttributesAsync(new[]
  {
      "title",
      "overview",
      "genres"
  });
  ```

  ```rust Rust theme={null}
  let searchable_attributes = [
    "title",
    "overview",
    "genres"
  ];

  let task: TaskInfo = client
    .index("movies")
    .set_searchable_attributes(&searchable_attributes)
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let searchableAttributes: [String] = [
      "title",
      "overview",
      "genres"
  ]
  client.index("movies").updateSearchableAttributes(searchableAttributes) { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client
      .index('movies')
      .updateSearchableAttributes(['title', 'overview', 'genres']);
  ```
</CodeGroup>

### Customizing attributes to search on at search time

By default, all queries search through all attributes in the `searchableAttributes` list. Use [the `attributesToSearchOn` search parameter](/reference/api/search#customize-attributes-to-search-on-at-search-time) to restrict specific queries to a subset of your index's `searchableAttributes`.

## Data storing

All fields are stored in the database. **This behavior cannot be changed**.

Thus, even if a field is missing from both the `displayedAttributes` list and the `searchableAttributes` list, **it is still stored in the database** and can be added to either or both lists at any time.