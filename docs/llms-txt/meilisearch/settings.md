# Settings
Source: https://www.meilisearch.com/docs/reference/api/settings

The /settings route allows you to customize search settings for the given index.

Use the `/settings` route to customize search settings for a given index. You can either modify all index settings at once using the [update settings endpoint](#update-settings), or use a child route to configure a single setting.

For a conceptual overview of index settings, refer to the [indexes explanation](/learn/getting_started/indexes#index-settings). To learn more about the basics of index configuration, refer to the [index configuration tutorial](/learn/configuration/configuring_index_settings_api).

## Settings interface

[Meilisearch Cloud](https://meilisearch.com/cloud) offers a [user-friendly graphical interface for managing index settings](/learn/configuration/configuring_index_settings) in addition to the `/settings` route. The Cloud interface offers more immediate and visible feedback, and is helpful for tweaking relevancy when used in conjunction with the [search preview](/learn/getting_started/search_preview).

## Settings object

By default, the settings object looks like this. All fields are modifiable.

```json theme={null}
{
  "displayedAttributes": [
    "*"
  ],
  "searchableAttributes": [
    "*"
  ],
  "filterableAttributes": [],
  "sortableAttributes": [],
  "rankingRules":
  [
    "words",
    "typo",
    "proximity",
    "attribute",
    "sort",
    "exactness"
  ],
  "stopWords": [],
  "nonSeparatorTokens": [],
  "separatorTokens": [],
  "dictionary": [],
  "synonyms": {},
  "distinctAttribute": null,
  "typoTolerance": {
    "enabled": true,
    "minWordSizeForTypos": {
      "oneTypo": 5,
      "twoTypos": 9
    },
    "disableOnWords": [],
    "disableOnAttributes": []
  },
  "faceting": {
    "maxValuesPerFacet": 100
  },
  "pagination": {
    "maxTotalHits": 1000
  },
  "proximityPrecision": "byWord",
  "facetSearch": true,
  "prefixSearch": "indexingTime",
  "searchCutoffMs": null,
  "embedders": {},
  "chat": {},
  "vectorStore": "stable"
}
```

## All settings

This route allows you to retrieve, configure, or reset all of an index's settings at once.

### Get settings

<RouteHighlighter method="GET" />

Get the settings of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/movies/settings'
  ```

  ```javascript JS theme={null}
  client.index('movies').getSettings()
  ```

  ```python Python theme={null}
  client.index('movies').get_settings()
  ```

  ```php PHP theme={null}
  $client->index('movies')->getSettings();
  ```

  ```java Java theme={null}
  client.index("movies").getSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('movies').settings
  ```

  ```go Go theme={null}
  client.Index("movies").GetSettings()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").GetSettingsAsync();
  ```

  ```rust Rust theme={null}
  let settings: Settings = client
    .index("movies")
    .get_settings()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").getSettings { (result) in
      switch result {
      case .success(let setting):
          print(setting)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').getSettings();
  ```
</CodeGroup>

##### Response: `200 Ok`

```json theme={null}
{
  "displayedAttributes": [
    "*"
  ],
  "searchableAttributes": [
    "*"
  ],
  "filterableAttributes": [],
  "sortableAttributes": [],
  "rankingRules":
  [
    "words",
    "typo",
    "proximity",
    "attribute",
    "sort",
    "exactness"
  ],
  "stopWords": [],
  "nonSeparatorTokens": [],
  "separatorTokens": [],
  "dictionary": [],
  "synonyms": {},
  "distinctAttribute": null,
  "typoTolerance": {
    "enabled": true,
    "minWordSizeForTypos": {
      "oneTypo": 5,
      "twoTypos": 9
    },
    "disableOnWords": [],
    "disableOnAttributes": []
  },
  "faceting": {
    "maxValuesPerFacet": 100
  },
  "pagination": {
    "maxTotalHits": 1000
  },
  "proximityPrecision": "byWord",
  "facetSearch": true,
  "prefixSearch": "indexingTime",
  "searchCutoffMs": null,
  "embedders": {},
  "chat": {},
  "vectorStore": "stable"
}
```

### Update settings

<RouteHighlighter method="PATCH" />

Update the settings of an index.

Passing `null` to an index setting will reset it to its default value.

Updates in the settings route are **partial**. This means that any parameters not provided in the body will be left unchanged.

If the provided index does not exist, it will be created.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

| Name                                                                                       | Type                        | Default value                                                                                         | Description                                                                      |
| :----------------------------------------------------------------------------------------- | :-------------------------- | :---------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------- |
| **[`dictionary`](#dictionary)**                                                            | Array of strings            | Empty                                                                                                 | List of strings Meilisearch should parse as a single term                        |
| **[`displayedAttributes`](#displayed-attributes)**                                         | Array of strings            | All attributes: `["*"]`                                                                               | Fields displayed in the returned documents                                       |
| **[`distinctAttribute`](#distinct-attribute)**                                             | String                      | `null`                                                                                                | Search returns documents with distinct (different) values of the given field     |
| **[`faceting`](#faceting)**                                                                | Object                      | [Default object](#faceting-object)                                                                    | Faceting settings                                                                |
| **[`filterableAttributes`](#filterable-attributes)**                                       | Array of strings or objects | Empty                                                                                                 | Attributes to use as filters and facets                                          |
| **[`pagination`](#pagination)**                                                            | Object                      | [Default object](#pagination-object)                                                                  | Pagination settings                                                              |
| **[`proximityPrecision`](#proximity-precision)**                                           | String                      | `"byWord"`                                                                                            | Precision level when calculating the proximity ranking rule                      |
| **[`facetSearch`](#facet-search)**                                                         | Boolean                     | `true`                                                                                                | Enable or disable [facet search](/reference/api/facet_search) functionality      |
| **[`prefixSearch`](#prefix-search)**                                                       | String                      | `"indexingTime"`                                                                                      | When Meilisearch should return results only matching the beginning of query      |
| **[`rankingRules`](#ranking-rules)**                                                       | Array of strings            | `["words",`<br />`"typo",`<br />`"proximity",`<br />`"attribute",`<br />`"sort",`<br />`"exactness"]` | List of ranking rules in order of importance                                     |
| **[`searchableAttributes`](#searchable-attributes)**                                       | Array of strings            | All attributes: `["*"]`                                                                               | Fields in which to search for matching query words sorted by order of importance |
| **[`searchCutoffMs`](#search-cutoff)**                                                     | Integer                     | `null`, or 1500ms                                                                                     | Maximum duration of a search query                                               |
| **[`separatorTokens`](#separator-tokens)**                                                 | Array of strings            | Empty                                                                                                 | List of characters delimiting where one term begins and ends                     |
| **[`nonSeparatorTokens`](#non-separator-tokens)**                                          | Array of strings            | Empty                                                                                                 | List of characters not delimiting where one term begins and ends                 |
| **[`sortableAttributes`](#sortable-attributes)**                                           | Array of strings            | Empty                                                                                                 | Attributes to use when sorting search results                                    |
| **[`stopWords`](#stop-words)**                                                             | Array of strings            | Empty                                                                                                 | List of words ignored by Meilisearch when present in search queries              |
| **[`synonyms`](#synonyms)**                                                                | Object                      | Empty                                                                                                 | List of associated words treated similarly                                       |
| **[`typoTolerance`](#typo-tolerance)**                                                     | Object                      | [Default object](#typo-tolerance-object)                                                              | Typo tolerance settings                                                          |
| **[`embedders`](#embedders)**                                                              | Object of objects           | [Default object](#embedders-object)                                                                   | Embedder required for performing meaning-based search queries                    |
| **[`chat`](#conversation)** <NoticeTag type="experimental" label="experimental" />         | Object                      | [Default object](#chat-object)                                                                        | Chat settings for performing conversation-based queries                          |
| **[`vector-store`](#vector-store)** <NoticeTag type="experimental" label="experimental" /> | String                      | `"stable"`                                                                                            | Vector store used for AI-powered search                                          |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PATCH 'MEILISEARCH_URL/indexes/movies/settings' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "rankingRules": [
        "words",
        "typo",
        "proximity",
        "attribute",
        "sort",
        "exactness",
        "release_date:desc",
        "rank:desc"
      ],
      "distinctAttribute": "movie_id",
      "searchableAttributes": [
        "title",
        "overview",
        "genres"
      ],
      "displayedAttributes": [
        "title",
        "overview",
        "genres",
        "release_date"
      ],
      "stopWords": [
        "the",
        "a",
        "an"
      ],
      "sortableAttributes": [
        "title",
        "release_date"
      ],
      "synonyms": {
        "wolverine": [
          "xmen",
          "logan"
      ],
        "logan": ["wolverine"]
      },
      "typoTolerance": {
        "minWordSizeForTypos": {
          "oneTypo": 8,
          "twoTypos": 10
        },
        "disableOnAttributes": ["title"]
      },
      "pagination": {
        "maxTotalHits": 5000
      },
      "faceting": {
        "maxValuesPerFacet": 200
      },
      "searchCutoffMs": 150
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').updateSettings({
      rankingRules: [
          'words',
          'typo',
          'proximity',
          'attribute',
          'sort',
          'exactness',
          'release_date:desc',
          'rank:desc'
      ],
      distinctAttribute: 'movie_id',
      searchableAttributes: [
          'title',
          'overview',
          'genres'
      ],
      displayedAttributes: [
          'title',
          'overview',
          'genres',
          'release_date'
      ],
      stopWords: [
          'the',
          'a',
          'an'
      ],
      sortableAttributes: [
        'title',
        'release_date'
      ],
      synonyms: {
          'wolverine': ['xmen', 'logan'],
          'logan': ['wolverine']
      },
      typoTolerance: {
          'minWordSizeForTypos': {
              'oneTypo': 8,
              'twoTypos': 10
          },
          'disableOnAttributes': [
              'title'
          ]
      },
      pagination: {
          maxTotalHits: 5000
      },
      faceting: {
          maxValuesPerFacet: 200
      },
      searchCutoffMs: 150
  })
  ```

  ```python Python theme={null}
  client.index('movies').update_settings({
    'rankingRules': [
      'words',
      'typo',
      'proximity',
      'attribute',
      'sort',
      'exactness',
      'release_date:desc',
      'rank:desc'
    ],
    'distinctAttribute': 'movie_id',
    'searchableAttributes': [
      'title',
      'overview',
      'genres'
    ],
    'displayedAttributes': [
      'title',
      'overview',
      'genres',
      'release_date'
    ],
    'sortableAttributes': [
      'title',
      'release_date'
    ],
    'stopWords': [
      'the',
      'a',
      'an'
    ],
    'synonyms': {
      'wolverine': ['xmen', 'logan'],
      'logan': ['wolverine']
    },
    'typoTolerance': {
      'minWordSizeForTypos': {
          'oneTypo': 8,
          'twoTypos': 10
      },
      'disableOnAttributes': ['title']
    },
    'pagination': {
      'maxTotalHits': 5000
    },
    'faceting': {
      'maxValuesPerFacet': 200
    },
    'searchCutoffMs': 150
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->updateSettings([
    'rankingRules' => [
      'words',
      'typo',
      'proximity',
      'attribute',
      'sort',
      'exactness',
      'release_date:desc',
      'rank:desc'
    ],
    'distinctAttribute' => 'movie_id',
    'searchableAttributes' => [
      'title',
      'overview',
      'genres'
    ],
    'displayedAttributes' => [
      'title',
      'overview',
      'genres',
      'release_date'
    ],
    'stopWords' => [
      'the',
      'a',
      'an'
    ],
    'sortableAttributes' => [
      'title',
      'release_date'
    ],
    'synonyms' => [
      'wolverine' => ['xmen', 'logan'],
      'logan' => ['wolverine']
    ],
    'typoTolerance' => [
        'minWordSizeForTypos' => [
          'oneTypo' => 8,
          'twoTypos' => 10
        ],
        'disableOnAttributes' => ['title']
    ],
    'pagination' => [
      'maxTotalHits' => 5000
    ],
    'faceting' => [
      'maxValuesPerFacet' => 200
    ],
    'searchCutoffMs' => 150
  ]);
  ```

  ```java Java theme={null}
  Settings settings = new Settings();
  settings.setRankingRules(
    new String[] {
        "words",
        "typo",
        "proximity",
        "attribute",
        "sort",
        "exactness",
        "release_date:desc",
        "rank:desc"
    });
  settings.setDistinctAttribute("movie_id");
  settings.setSearchableAttributes(
    new String[] {
      "title",
      "overview",
      "genres"
    });
  settings.setDisplayedAttributes(
    new String[] {
      "title",
      "overview",
      "genres",
      "release_date"
    });
  settings.setStopWords(
    new String[] {
      "the",
      "a",
      "an"
    });
  settings.setSortableAttributes(
    new String[] {
      "title",
      "release_date"
    });

  HashMap<String, String[]> synonyms = new HashMap<String, String[]>();
  synonyms.put("wolverine", new String[] {"xmen", "logan"});
  synonyms.put("logan", new String[] {"wolverine"});
  settings.setSynonyms(synonyms);

  HashMap<String, Integer> minWordSizeTypos =
    new HashMap<String, Integer>() {
      {
        put("oneTypo", 8);
        put("twoTypos", 10);
      }
    };
  TypoTolerance typoTolerance = new TypoTolerance();
  typoTolerance.setMinWordSizeForTypos(minWordSizeTypos);
  settings.setTypoTolerance(typoTolerance);
  settings.setSearchCutoffMs(150);
  client.index("movies").updateSettings(settings);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').update_settings({
    ranking_rules: [
      'words',
      'typo',
      'proximity',
      'attribute',
      'sort',
      'exactness',
      'release_date:desc',
      'rank:desc'
    ],
    distinct_attribute: 'movie_id',
    searchable_attributes: [
      'title',
      'overview',
      'genres'
    ],
    displayed_attributes: [
      'title',
      'overview',
      'genres',
      'release_date'
    ],
    stop_words: [
      'the',
      'a',
      'an'
    ],
    sortable_attributes: [
      'title',
      'release_date'
    ],
    synonyms: {
      wolverine: ['xmen', 'logan'],
      logan: ['wolverine']
    },
    pagination: {
      max_total_hits: 5000
    },
    faceting: {
      max_values_per_facet: 200
    },
    search_cutoff_ms: 150
  })
  ```

  ```go Go theme={null}
  distinctAttribute := "movie_id"
  settings := meilisearch.Settings{
    RankingRules: []string{
      "words",
      "typo",
      "proximity",
      "attribute",
      "sort",
      "exactness",
      "release_date:desc",
      "rank:desc",
    },
    DistinctAttribute: &distinctAttribute,
    SearchableAttributes: []string{
      "title",
      "overview",
      "genres",
    },
    DisplayedAttributes: []string{
      "title",
      "overview",
      "genres",
      "release_date",
    },
    StopWords: []string{
      "the",
      "a",
      "an",
    },
    SortableAttributes: []string{
      "title",
      "release_date",
    },
    Synonyms: map[string][]string{
      "wolverine": []string{"xmen", "logan"},
      "logan":     []string{"wolverine"},
    },
    TypoTolerance: &meilisearch.TypoTolerance{
      MinWordSizeForTypos: meilisearch.MinWordSizeForTypos{
        OneTypo:  8,
        TwoTypos: 10,
      },
      DisableOnAttributes: []string{"title"},
    },
    Pagination: &meilisearch.Pagination{
      MaxTotalHits: 5000,
    },
    Faceting: &meilisearch.Faceting{
      MaxValuesPerFacet: 200,
    },
    SearchCutoffMs: 150,
  }
  client.Index("movies").UpdateSettings(&settings)
  ```

  ```csharp C# theme={null}
  Settings newSettings = new Settings
  {
    RankingRules = new string[]
    {
      "words",
      "typo",
      "proximity",
      "attribute",
      "sort",
      "exactness",
      "release_date:desc",
      "rank:desc"
    },
    DistinctAttribute = "movie_id",
    SearchableAttributes = new string[] { "title", "overview", "genres" },
    DisplayedAttributes = new string[] { "title", "overview", "genres", "release_date" },
    SortableAttributes = new string[] { "title", "release_date" },
    StopWords = new string[] { "the", "a", "an" },
    Synonyms = new Dictionary<string, IEnumerable<string>>
    {
        { "wolverine", new string[] { "xmen", "logan" } },
        { "logan", new string[] { "wolverine" } },
    },
    FilterableAttributes = new string[] { },
    TypoTolerance = new TypoTolerance
    {
        DisableOnAttributes = new string[] { "title" },
        MinWordSizeForTypos = new TypoTolerance.TypoSize
        {
            OneTypo = 8,
            TwoTypos = 10
        }
    },
    SearchCutoffMs = 150
  };
  TaskInfo task = await client.Index("movies").UpdateSettingsAsync(newFilters);
  ```

  ```rust Rust theme={null}
  let mut synonyms = std::collections::HashMap::new();
  synonyms.insert(String::from("wolverine"), vec!["xmen", "logan"]);
  synonyms.insert(String::from("logan"), vec!["wolverine"]);

  let min_word_size_for_typos = MinWordSizeForTypos {
    one_typo: Some(4),
    two_typos; Some(12)
  }
  let typo_tolerance = TypoToleranceSettings {
    enabled: Some(true),
    disable_on_attributes: Some(vec!["title".to_string()]),
    disable_on_words: Some(vec![])
    min_word_size_for_typos: Some(min_word_size_for_typos),
  };

  let settings = Settings::new()
    .with_ranking_rules([
      "words",
      "typo",
      "proximity",
      "attribute",
      "sort",
      "exactness",
      "release_date:desc",
      "rank:desc"
    ])
    .with_distinct_attribute(Some("movie_id"))
    .with_searchable_attributes([
      "title",
      "overview",
      "genres"
    ])
    .with_displayed_attributes([
      "title",
      "overview",
      "genres",
      "release_date"
    ])
    .with_stop_words([
      "the",
      "a",
      "an"
    ])
    .with_sortable_attributes([
      "title",
      "release_date"
    ])
    .with_synonyms(synonyms)
    .with_typo_tolerance(typo_tolerance)
    .with_search_cutoff(150);

  let task: TaskInfo = client
    .index("movies")
    .set_settings(&settings)
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let settings = Setting(rankingRules: [
      "words",
      "typo",
      "proximity",
      "attribute",
      "sort",
      "exactness",
      "release_date:desc",
      "rank:desc"
  ], searchableAttributes: [
      "title",
      "overview",
      "genres"
  ], displayedAttributes: [
      "title",
      "overview",
      "genres",
      "release_date"
  ], stopWords: [
      "the",
      "a",
      "an"
  ], synonyms: [
      "wolverine": ["xmen", "logan"],
      "logan": ["wolverine"]
  ], distinctAttribute: "movie_id",
  sortableAttributes: [
      "title",
      "release_date"
  ])
  client.index("movies").updateSettings(settings) { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').updateSettings(
        IndexSettings(
          rankingRules: [
            'words',
            'typo',
            'proximity',
            'attribute',
            'sort',
            'exactness',
            'release_date:desc',
            'rank:desc'
          ],
          distinctAttribute: 'movie_id',
          searchableAttributes: ['title', 'overview', 'genres'],
          displayedAttributes: [
            'title',
            'overview',
            'genres',
            'release_date'
          ],
          stopWords: ['the', 'a', 'an'],
          sortableAttributes: ['title', 'release_date'],
          synonyms: {
            'wolverine': ['xmen', 'logan'],
            'logan': ['wolverine'],
          },
        ),
      );
  ```
</CodeGroup>

<Warning>
  If Meilisearch encounters an error when updating any of the settings in a request, it immediately stops processing the request and returns an error message. In this case, the database settings remain unchanged. The returned error message will only address the first error encountered.
</Warning>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset settings

<RouteHighlighter method="DELETE" />

Reset all the settings of an index to their [default value](#settings-object).

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/movies/settings'
  ```

  ```javascript JS theme={null}
  client.index('movies').resetSettings()
  ```

  ```python Python theme={null}
  client.index('movies').reset_settings()
  ```

  ```php PHP theme={null}
  $client->index('movies')->resetSettings();
  ```

  ```java Java theme={null}
  client.index("movies").resetSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('movies').reset_settings
  ```

  ```go Go theme={null}
  client.Index("movies").ResetSettings()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").ResetSettingsAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("movies")
    .reset_settings()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").resetSettings { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').resetSettings();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Dictionary

Allows users to instruct Meilisearch to consider groups of strings as a single term by adding a supplementary dictionary of user-defined terms.

This is particularly useful when working with datasets containing many domain-specific words, and in languages where words are not separated by whitespace such as Japanese.

Custom dictionaries are also useful in a few use-cases for space-separated languages, such as datasets with names such as `"J. R. R. Tolkien"` and `"W. E. B. Du Bois"`.

<Tip>
  User-defined dictionaries can be used together with synonyms. It can be useful to configure Meilisearch so different spellings of an author's initials return the same results:

  ```json theme={null}
  "dictionary": ["W. E. B.", "W.E.B."],
  "synonyms": {
    "W. E. B.": ["W.E.B."],
    "W.E.B.": ["W. E. B."]
  }
  ```
</Tip>

### Get dictionary

<RouteHighlighter method="GET" />

Get an index's user-defined dictionary.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/books/settings/dictionary'
  ```

  ```javascript JS theme={null}
  client.index('books').getDictionary()
  ```

  ```python Python theme={null}
  client.index('books').get_dictionary()
  ```

  ```php PHP theme={null}
  $client->index('books')->getDictionary();
  ```

  ```java Java theme={null}
  client.index("books").getDictionarySettings();
  ```

  ```ruby Ruby theme={null}
  client.index('books').dictionary
  ```

  ```go Go theme={null}
  client.Index("books").GetDictionary()
  ```

  ```csharp C# theme={null}
  var indexDictionary = await client.Index("books").GetDictionaryAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index('books')
    .get_dictionary()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("books").getDictionary { result in
    // handle result
  }
  ```
</CodeGroup>

##### Response: `200 OK`

```json theme={null}
[]
```

### Update dictionary

<RouteHighlighter method="PUT" />

Update an index's user-defined dictionary.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```json theme={null}
["J. R. R.", "W. E. B."]
```

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/books/settings/dictionary' \
    -H 'Content-Type: application/json' \
    --data-binary '[
      "J. R. R.",
      "W. E. B."
    ]'
  ```

  ```javascript JS theme={null}
  client.index('books').updateDictionary(['J. R. R.', 'W. E. B.'])
  ```

  ```python Python theme={null}
  client.index('books').update_dictionary(["J. R. R.", "W. E. B."])
  ```

  ```php PHP theme={null}
  $client->index('books')->updateDictionary(['J. R. R.', 'W. E. B.']);
  ```

  ```java Java theme={null}
  client.index("books").updateDictionarySettings(new String[] {"J. R. R.", "W. E. B."});
  ```

  ```ruby Ruby theme={null}
  client.index('books').update_dictionary(['J. R. R.', 'W. E. B.'])
  ```

  ```go Go theme={null}
  client.Index("books").UpdateDictionary([]string{
    "J. R. R.",
    "W. E. B.",
  })
  ```

  ```csharp C# theme={null}
  var newDictionary = new string[] { "J. R. R.", "W. E. B." };
  await client.Index("books").UpdateDictionaryAsync(newDictionary);
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index('books')
    .set_dictionary(['J. R. R.', 'W. E. B.'])
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("books").updateDictionary(["J. R. R.", "W. E. B."]) { result in
    // handle result
  }
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "books",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2023-09-11T15:39:06.073314Z"
}
```

Use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset dictionary

<RouteHighlighter method="DELETE" />

Reset an index's dictionary to its default value, `[]`.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/books/settings/dictionary'
  ```

  ```javascript JS theme={null}
  client.index('books').resetDictionary()
  ```

  ```python Python theme={null}
  client.index('books').reset_dictionary()
  ```

  ```php PHP theme={null}
  $client->index('books')->resetDictionary();
  ```

  ```java Java theme={null}
  client.index("books").resetDictionarySettings();
  ```

  ```ruby Ruby theme={null}
  client.index('books').reset_dictionary
  ```

  ```go Go theme={null}
  client.Index("books").ResetDictionary()
  ```

  ```csharp C# theme={null}
  await client.Index("books").ResetDictionaryAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index('books')
    .reset_dictionary()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("books").resetDictionary { result in
    // handle result
  }
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "books",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2022-04-14T20:53:32.863107Z"
}
```

Use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Displayed attributes

The attributes added to the `displayedAttributes` list appear in search results. `displayedAttributes` only affects the search endpoints. It has no impact on the [get documents with POST](/reference/api/documents#get-documents-with-post) and [get documents with GET](/reference/api/documents#get-documents-with-get) endpoints.

By default, the `displayedAttributes` array is equal to all fields in your dataset. This behavior is represented by the value `["*"]`.

[To learn more about displayed attributes, refer to our dedicated guide.](/learn/relevancy/displayed_searchable_attributes#displayed-fields)

### Get displayed attributes

<RouteHighlighter method="GET" />

Get the displayed attributes of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/movies/settings/displayed-attributes'
  ```

  ```javascript JS theme={null}
  client.index('movies').getDisplayedAttributes()
  ```

  ```python Python theme={null}
  client.index('movies').get_displayed_attributes()
  ```

  ```php PHP theme={null}
  $client->index('movies')->getDisplayedAttributes();
  ```

  ```java Java theme={null}
  client.index("movies").getDisplayedAttributesSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('movies').get_displayed_attributes
  ```

  ```go Go theme={null}
  client.Index("movies").GetDisplayedAttributes()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").GetDisplayedAttributesAsync();
  ```

  ```rust Rust theme={null}
  let displayed_attributes: Vec<String> = client
    .index("movies")
    .get_displayed_attributes()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").getDisplayedAttributes { (result) in
      switch result {
      case .success(let displayedAttributes):
          print(displayedAttributes)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').getDisplayedAttributes();
  ```
</CodeGroup>

##### Response: `200 Ok`

```json theme={null}
[
  "title",
  "overview",
  "genres",
  "release_date.year"
]
```

### Update displayed attributes

<RouteHighlighter method="PUT" />

Update the displayed attributes of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```
[<String>, <String>, …]
```

An array of strings. Each string should be an attribute that exists in the selected index.

If an attribute contains an object, you can use dot notation to specify one or more of its keys, for example, `"displayedAttributes": ["release_date.year"]`.

<Warning>
  If the field does not exist, no error will be thrown.
</Warning>

#### Example

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
    'release_date'
  ])
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
  client.index("movies").updateDisplayedAttributesSettings(new String[]
  {
    "title",
    "overview",
    "genres",
    "release_date"
  });
  ```

  ```ruby Ruby theme={null}
  client.index('movies').update_displayed_attributes([
    'title',
    'overview',
    'genres',
    'release_date'
  ])
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
  let displayedAttributes: [String] = ["title", "overview", "genres", "release_date"]
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

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset displayed attributes

<RouteHighlighter method="DELETE" />

Reset the displayed attributes of the index to the default value.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/movies/settings/displayed-attributes'
  ```

  ```javascript JS theme={null}
  client.index('movies').resetDisplayedAttributes()
  ```

  ```python Python theme={null}
  client.index('movies').reset_displayed_attributes()
  ```

  ```php PHP theme={null}
  $client->index('movies')->resetDisplayedAttributes();
  ```

  ```java Java theme={null}
  client.index("movies").resetDisplayedAttributesSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('movies').reset_displayed_attributes
  ```

  ```go Go theme={null}
  client.Index("movies").ResetDisplayedAttributes()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").ResetDisplayedAttributesAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("movies")
    .reset_displayed_attributes()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").resetDisplayedAttributes { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').resetDisplayedAttributes();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Distinct attribute

The distinct attribute is a field whose value will always be unique in the returned documents.

<Warning>
  Updating distinct attributes will re-index all documents in the index, which can take some time. We recommend updating your index settings first and then adding documents as this reduces RAM consumption.
</Warning>

[To learn more about the distinct attribute, refer to our dedicated guide.](/learn/relevancy/distinct_attribute)

### Get distinct attribute

<RouteHighlighter method="GET" />

Get the distinct attribute of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/shoes/settings/distinct-attribute'
  ```

  ```javascript JS theme={null}
  client.index('shoes').getDistinctAttribute()
  ```

  ```python Python theme={null}
  client.index('shoes').get_distinct_attribute()
  ```

  ```php PHP theme={null}
  $client->index('shoes')->getDistinctAttribute();
  ```

  ```java Java theme={null}
  client.index("shoes").getDistinctAttributeSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('shoes').distinct_attribute
  ```

  ```go Go theme={null}
  client.Index("shoes").GetDistinctAttribute()
  ```

  ```csharp C# theme={null}
  string result = await client.Index("shoes").GetDistinctAttributeAsync();
  ```

  ```rust Rust theme={null}
  let distinct_attribute: Option<String> = client
    .index("shoes")
    .get_distinct_attribute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("shoes").getDistinctAttribute { (result) in
      switch result {
      case .success(let distinctAttribute):
          print(distinctAttribute)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('shoes').getDistinctAttribute();
  ```
</CodeGroup>

##### Response: `200 Ok`

```json theme={null}
"skuid"
```

### Update distinct attribute

<RouteHighlighter method="PUT" />

Update the distinct attribute field of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```
<String>
```

A string. The string should be an attribute that exists in the selected index.

If an attribute contains an object, you can use dot notation to set one or more of its keys as a value for this setting, for example, `"distinctAttribute": "product.skuid"`.

<Warning>
  If the field does not exist, no error will be thrown.
</Warning>

[To learn more about the distinct attribute, refer to our dedicated guide.](/learn/relevancy/distinct_attribute)

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/shoes/settings/distinct-attribute' \
    -H 'Content-Type: application/json' \
    --data-binary '"skuid"'
  ```

  ```javascript JS theme={null}
  client.index('shoes').updateDistinctAttribute('skuid')
  ```

  ```python Python theme={null}
  client.index('shoes').update_distinct_attribute('skuid')
  ```

  ```php PHP theme={null}
  $client->index('shoes')->updateDistinctAttribute('skuid');
  ```

  ```java Java theme={null}
  client.index("shoes").updateDistinctAttributeSettings("skuid");
  ```

  ```ruby Ruby theme={null}
  client.index('shoes').update_distinct_attribute('skuid')
  ```

  ```go Go theme={null}
  client.Index("shoes").UpdateDistinctAttribute("skuid")
  ```

  ```csharp C# theme={null}
  TaskInfo result = await client.Index("shoes").UpdateDistinctAttributeAsync("skuid");
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("shoes")
    .set_distinct_attribute("skuid")
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("shoes").updateDistinctAttribute("skuid") { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('shoes').updateDistinctAttribute('skuid');
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset distinct attribute

<RouteHighlighter method="DELETE" />

Reset the distinct attribute of an index to its default value.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/shoes/settings/distinct-attribute'
  ```

  ```javascript JS theme={null}
  client.index('shoes').resetDistinctAttribute()
  ```

  ```python Python theme={null}
  client.index('shoes').reset_distinct_attribute()
  ```

  ```php PHP theme={null}
  $client->index('shoes')->resetDistinctAttribute();
  ```

  ```java Java theme={null}
  client.index("shoes").resetDistinctAttributeSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('shoes').reset_distinct_attribute
  ```

  ```go Go theme={null}
  client.Index("shoes").ResetDistinctAttribute()
  ```

  ```csharp C# theme={null}
  TaskInfo result = await client.Index("shoes").ResetDistinctAttributeAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("shoes")
    .reset_distinct_attribute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("shoes").resetDistinctAttribute { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('shoes').resetDistinctAttribute();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Faceting

With Meilisearch, you can create [faceted search interfaces](/learn/filtering_and_sorting/search_with_facet_filters). This setting allows you to:

* Define the maximum number of values returned by the `facets` search parameter
* Sort facet values by value count or alphanumeric order

[To learn more about faceting, refer to our dedicated guide.](/learn/filtering_and_sorting/search_with_facet_filters)

### Faceting object

| Name                    | Type    | Default value                                                                | Description                                                                                                  |
| :---------------------- | :------ | :--------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| **`maxValuesPerFacet`** | Integer | `100`                                                                        | Maximum number of facet values returned for each facet. Values are sorted in ascending lexicographical order |
| **`sortFacetValuesBy`** | Object  | All facet values are sorted in ascending alphanumeric order (`"*": "alpha"`) | Customize facet order to sort by descending value count (`count`) or ascending alphanumeric order (`alpha`)  |

### Get faceting settings

<RouteHighlighter method="GET" />

Get the faceting settings of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/books/settings/faceting'
  ```

  ```javascript JS theme={null}
  client.index('books').getFaceting()
  ```

  ```python Python theme={null}
  client.index('books').get_faceting_settings()
  ```

  ```php PHP theme={null}
  $client->index('books')->getFaceting();
  ```

  ```java Java theme={null}
  client.index("books").getFacetingSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('books').faceting
  ```

  ```go Go theme={null}
  client.Index("books").GetFaceting()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").GetFacetingAsync();
  ```

  ```rust Rust theme={null}
  let faceting: FacetingSettings = client
    .index("books")
    .get_faceting()
    .await
    .unwrap();
  ```

  ```dart Dart theme={null}
  await client.index('movies').getFaceting();
  ```
</CodeGroup>

##### Response: `200 OK`

```json theme={null}
{
  "maxValuesPerFacet": 100,
  "sortFacetValuesBy": {
    "*": "alpha"
  }
}
```

### Update faceting settings

<RouteHighlighter method="PATCH" />

Partially update the faceting settings for an index. Any parameters not provided in the body will be left unchanged.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```
{
  "maxValuesPerFacet": <Integer>,
  "sortFacetValuesBy": {
      <String>: "count",
      <String>: "alpha"
  }
}
```

| Name                    | Type    | Default value                                                                | Description                                                                                                  |
| :---------------------- | :------ | :--------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| **`maxValuesPerFacet`** | Integer | `100`                                                                        | Maximum number of facet values returned for each facet. Values are sorted in ascending lexicographical order |
| **`sortFacetValuesBy`** | Object  | All facet values are sorted in ascending alphanumeric order (`"*": "alpha"`) | Customize facet order to sort by descending value count(`count`) or ascending alphanumeric order (`alpha`)   |

Suppose a query's search results contain a total of three values for a `colors` facet: `blue`, `green`, and `red`. If you set `maxValuesPerFacet` to `2`, Meilisearch will only return `blue` and `green` in the response body's `facetDistribution` object.

<Note>
  Setting `maxValuesPerFacet` to a high value might negatively impact performance.
</Note>

#### Example

The following code sample sets `maxValuesPerFacet` to `2`, sorts the `genres` facet by descending count, and all other facets in ascending alphanumeric order:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PATCH 'MEILISEARCH_URL/indexes/books/settings/faceting' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "maxValuesPerFacet": 2,
      "sortFacetValuesBy": {
        "*": "alpha",
        "genres": "count"
      }
    }'
  ```

  ```javascript JS theme={null}
  client.index('books').updateFaceting({
    maxValuesPerFacet: 2
    sortFacetValuesBy: {
      '*': 'alpha',
      genres: 'count'
    }
  })
  ```

  ```python Python theme={null}
  params = {
    'maxValuesPerFacet': 2,
    'sortFacetValuesBy': {
        '*': 'count',
        'genres': 'count'
      }
  }
  client.index('books').update_faceting_settings(params)
  ```

  ```php PHP theme={null}
  $client->index('books')->updateFaceting([
    'maxValuesPerFacet' => 2,
    'sortFacetValuesBy' => ['*' => 'alpha', 'genres' => 'count']
  ]);
  ```

  ```java Java theme={null}
  Faceting newFaceting = new Faceting();
  newFaceting.setMaxValuesPerFacet(2);
  HashMap<String, FacetSortValue> facetSortValues = new HashMap<>();
  facetSortValues.put("*", FacetSortValue.ALPHA);
  facetSortValues.put("genres", FacetSortValue.COUNT);
  newFaceting.setSortFacetValuesBy(facetSortValues);
  client.index("books").updateFacetingSettings(newFaceting);
  ```

  ```ruby Ruby theme={null}
  client.index('books').update_faceting({
    max_values_per_facet: 2,
    sort_facet_values_by: {
      '*': 'alpha',
      genres: 'count'
    }
  })
  ```

  ```go Go theme={null}
  client.Index("books").UpdateFaceting(&meilisearch.Faceting{
      MaxValuesPerFacet: 2,
      SortFacetValuesBy: {
         "*":      SortFacetTypeAlpha,
         "genres": SortFacetTypeCount,
      }
  })
  ```

  ```csharp C# theme={null}
  var faceting = new Faceting
  {
      MaxValuesPerFacet = 2,
      SortFacetValuesBy = new Dictionary<string, SortFacetValuesByType>
      {
          ["*"] = SortFacetValuesByType.Alpha,
          ["genres"] = SortFacetValuesByType.Count
      }
  };
  await client.Index("books").UpdateFacetingAsync(faceting);
  ```

  ```rust Rust theme={null}
  let mut facet_sort_setting = BTreeMap::new();
  facet_sort_setting.insert(String::from("*"), FacetSortValue::Alpha);
  facet_sort_setting.insert(String::from("genres"), FacetSortValue::Count);
  let mut faceting = FacetingSettings {
    max_values_per_facet: 2,
    sort_facet_values_by: Some(facet_sort_setting),
  };

  let task: TaskInfo = client
    .index("books")
    .set_faceting(&faceting)
    .await
    .unwrap();
  ```

  ```dart Dart theme={null}
  await client.index('books').updateFaceting(Faceting(
          maxValuesPerFacet: 2,
          sortFacetValuesBy: {
            '*': FacetingSortTypes.alpha,
            'genres': FacetingSortTypes.count
          }));
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "books",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2022-04-14T20:56:44.991039Z"
}
```

You can use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset faceting settings

Reset an index's faceting settings to their [default value](#faceting-object). Setting `sortFacetValuesBy` to `null`(`--data-binary '{ "sortFacetValuesBy": null }'`), will restore it to the default value (`"*": "alpha"`).

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/books/settings/faceting'
  ```

  ```javascript JS theme={null}
  client.index('books').resetFaceting()
  ```

  ```python Python theme={null}
  client.index('books').reset_faceting_settings()
  ```

  ```php PHP theme={null}
  $client->index('books')->resetFaceting();
  ```

  ```java Java theme={null}
  client.index("books").resetFacetingSettings();
  ```

  ```ruby Ruby theme={null}
  index('books').reset_faceting
  ```

  ```go Go theme={null}
  client.Index("books").ResetFaceting()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").ResetFacetingAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("books")
    .reset_faceting()
    .await
    .unwrap();
  ```

  ```dart Dart theme={null}
  await client.index('movies').resetFaceting();
  ```
</CodeGroup>

##### Response: `200 OK`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "books",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2022-04-14T20:53:32.863107Z"
}
```

You can use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Filterable attributes

Attributes in the `filterableAttributes` list can be used as [filters](/learn/filtering_and_sorting/filter_search_results) or [facets](/learn/filtering_and_sorting/search_with_facet_filters).

<Warning>
  Updating filterable attributes will re-index all documents in the index, which can take some time. To reduce RAM consumption, first update your index settings and then add documents.
</Warning>

### Filterable attribute object

`filterableAttributes` may be an array of either strings or filterable attribute objects.

Filterable attribute objects must contain the following fields:

| Name                    | Type             | Default value                                                              | Description                                                        |
| ----------------------- | ---------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **`attributePatterns`** | Array of strings | `[]`                                                                       | A list of strings indicating filterable fields                     |
| **`features`**          | Object           | `{"facetSearch": false, "filter": {"equality": true, "comparison": false}` | A list outlining filter types enabled for the specified attributes |

#### `attributePatterns`

Attribute patterns may begin or end with a \* wildcard to match multiple fields: `customer_*`, `attribute*`.

#### `features`

`features` allows you to decide which filter features are allowed for the specified attributes. It accepts the following fields:

* `facetSearch`: Whether facet search should be enabled for the specified attributes. Boolean, defaults to `false`
* `filter`: A list outlining the filter types for the specified attributes. Must be an object and accepts the following fields:
  * `equality`: Enables `=`, `!=`, `IN`, `EXISTS`, `IS NULL`, `IS EMPTY`, `NOT`, `AND`, and `OR`. Boolean, defaults to `true`
  * `comparison`: Enables `>`, `>=`, `<`, `<=`, `TO`, `EXISTS`, `IS NULL`, `IS EMPTY`, `NOT`, `AND`, and `OR`. Boolean, defaults to `false`

Calculating `comparison` filters is a resource-intensive operation. Disabling them may lead to better search and indexing performance. `equality` filters use fewer resources and have limited impact on performance.

<Warning>
  #### Filterable attributes and reserved attributes

  Use the simple string syntax to match reserved attributes. Reserved Meilisearch fields are always prefixed with an underscore (`_`), such as `_geo` and `_vector`.

  If set as a filterable attribute, reserved attributes ignore the `features` field and automatically activate all search features. Reserved fields will not be matched by wildcard `attributePatterns` such as `_*`.
</Warning>

### Get filterable attributes

<RouteHighlighter method="GET" />

Get the filterable attributes for an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/movies/settings/filterable-attributes'
  ```

  ```javascript JS theme={null}
  client.index('movies').getFilterableAttributes()
  ```

  ```python Python theme={null}
  client.index('movies').get_filterable_attributes()
  ```

  ```php PHP theme={null}
  $client->index('movies')->getFilterableAttributes();
  ```

  ```java Java theme={null}
  client.index("movies").getFilterableAttributesSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('movies').filterable_attributes
  ```

  ```go Go theme={null}
  client.Index("movies").GetFilterableAttributes()
  ```

  ```csharp C# theme={null}
  IEnumerable<string> attributes = await client.Index("movies").GetFilterableAttributesAsync();
  ```

  ```rust Rust theme={null}
  let filterable_attributes: Vec<String> = client
    .index("movies")
    .get_filterable_attributes()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").getFilterableAttributes { (result) in
      switch result {
      case .success(let attributes):
          print(attributes)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').getFilterableAttributes();
  ```
</CodeGroup>

##### Response: `200 Ok`

```json theme={null}
[
  "genres",
  "director",
  "release_date.year"
]
```

### Update filterable attributes

<RouteHighlighter method="PUT" />

Update an index's filterable attributes list.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```
[<String>, <String>, …]
```

An array of strings containing the attributes that can be used as filters at query time. All filter types are enabled for the specified attributes when using the array of strings format.

You may also use an array of objects:

```
[
  {
    "attributePatterns": [<String>, <String>, …],
    "features": {
      "facetSearch": <Boolean>,
      "filter": {
        "equality": <Boolean>,
        "comparison": <Boolean>
      }
    }
  }
]
```

If the specified field does not exist, Meilisearch will silently ignore it.

If an attribute contains an object, you can use dot notation to set one or more of its keys as a value for this setting: `"filterableAttributes": ["release_date.year"]` or `"attributePatterns": ["release_date.year"]`.

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/movies/settings/filterable-attributes' \
    -H 'Content-Type: application/json' \
    --data-binary '[
      "genres",
      "director",
      {
        "attributePatterns": ["*_ratings"],
        "features": {
          "facetSearch": false,
          "filter": {
            "equality": true,
            "comparison": false
          }
        }
      }
    ]'
  ```

  ```javascript JS theme={null}
  client.index('movies')
    .updateFilterableAttributes([
      "genres",
      {
        attributePatterns: ["genre"],
        features: {
          facetSearch: true,
          filter: { equality: true, comparison: false },
        },
      }
    ])
  ```

  ```python Python theme={null}
  client.index('movies').update_filterable_attributes([
    'genres',
    'director'
  ])
  ```

  ```php PHP theme={null}
  $client->index('movies')->updateFilterableAttributes([
    'author',
    [
        'attributePatterns' => ['genres'],
        'features' => [
            'facetSearch' => true,
            'filter' => [
                'equality' => true,
                'comparison' => false,
            ],
        ],
    ],
  ]);
  ```

  ```java Java theme={null}
  Settings settings = new Settings();
  settings.setFilterableAttributes(new String[] {"genres", "director"});
  client.index("movies").updateSettings(settings);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').update_filterable_attributes([
    'genres',
    'director'
  ])
  ```

  ```go Go theme={null}
  filterableAttributes := []interface{}{
    "genres",
    "director",
    AttributeRule{
      AttributePatterns: []string{"tag"}
      Features: AttributeFeatures{
        FacetSearch: false,
        Filter: FilterFeatures{
          Equality:   true,
          Comparison: false,
        }
      }
    },
    map[string]interface{}{
      "attributePatterns": []interface{}{"year"}
      "features": map[string]interface{}{
        "facetSearch": false,
        "filter": map[string]interface{}{
          "equality":   true,
          "comparison": true,
        }
      }
    }
  }
  client.Index("movies").UpdateFilterableAttributes(&filterableAttributes)
  ```

  ```csharp C# theme={null}
  List<string> attributes = new() { "genres", "director" };
  TaskInfo result = await client.Index("movies").UpdateFilterableAttributesAsync(attributes);
  ```

  ```rust Rust theme={null}
  use meilisearch_sdk::settings::{
    FilterableAttribute,
    FilterableAttributesSettings,
    FilterFeatures,
    FilterFeatureModes,
  };

  // Mixed legacy + new syntax
  let filterable_attributes: Vec<FilterableAttribute> = vec![
    // legacy: plain attribute name
    "author".into(),
    // new syntax: settings object
    FilterableAttribute::Settings(FilterableAttributesSettings {
      attribute_patterns: vec!["genre".to_string()],
      features: FilterFeatures {
        facet_search: true,
        filter: FilterFeatureModes { equality: true, comparison: false },
      },
    }),
  ];

  let task: TaskInfo = client
    .index("movies")
    .set_filterable_attributes_advanced(filterable_attributes)
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").updateFilterableAttributes(["genre", "director"]) { (result) in
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
      .updateFilterableAttributes(['genres', 'director']);
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset filterable attributes

<RouteHighlighter method="DELETE" />

Reset an index's filterable attributes list back to its default value.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/movies/settings/filterable-attributes'
  ```

  ```javascript JS theme={null}
  client.index('movies').resetFilterableAttributes()
  ```

  ```python Python theme={null}
  client.index('movies').reset_filterable_attributes()
  ```

  ```php PHP theme={null}
  $client->index('movies')->resetFilterableAttributes();
  ```

  ```java Java theme={null}
  client.index("movies").resetFilterableAttributesSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('movies').reset_filterable_attributes
  ```

  ```go Go theme={null}
  client.Index("movies").ResetFilterableAttributes()
  ```

  ```csharp C# theme={null}
  TaskInfo result = await client.Index("movies").ResetFilterableAttributesAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("movies")
    .reset_filterable_attributes()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").resetFilterableAttributes { (result) in
      switch result {
      case .success(let attributes):
          print(attributes)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').resetFilterableAttributes();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Localized attributes

By default, Meilisearch auto-detects the languages used in your documents. This setting allows you to explicitly define which languages are present in a dataset, and in which fields.

Localized attributes affect `searchableAttributes`, `filterableAttributes`, and `sortableAttributes`.

Configuring multiple languages for a single index may negatively impact performance.

<Note>
  [`locales`](/reference/api/search#query-locales) and `localizedAttributes` have the same goal: explicitly state the language used in a search when Meilisearch's language auto-detection is not working as expected.

  If you believe Meilisearch is detecting incorrect languages because of the query text, explicitly set the search language with `locales`.

  If you believe Meilisearch is detecting incorrect languages because of document, explicitly set the document language at the index level with `localizedAttributes`.

  For full control over the way Meilisearch detects languages during indexing and at search time, set both `locales` and `localizedAttributes`.
</Note>

### Localized attributes object

`localizedAttributes` must be an array of locale objects. Its default value is `[]`.

Locale objects must have the following fields:

| Name                    | Type             | Default value | Description                                                                   |
| :---------------------- | :--------------- | :------------ | :---------------------------------------------------------------------------- |
| **`locales`**           | Array of strings | `[]`          | A list of strings indicating one or more ISO-639 locales                      |
| **`attributePatterns`** | Array of strings | `[]`          | A list of strings indicating which fields correspond to the specified locales |

#### `locales`

Meilisearch supports the following [ISO-639-3](https://iso639-3.sil.org/) three-letter `locales`: `epo`, `eng`, `rus`, `cmn`, `spa`, `por`, `ita`, `ben`, `fra`, `deu`, `ukr`, `kat`, `ara`, `hin`, `jpn`, `heb`, `yid`, `pol`, `amh`, `jav`, `kor`, `nob`, `dan`, `swe`, `fin`, `tur`, `nld`, `hun`, `ces`, `ell`, `bul`, `bel`, `mar`, `kan`, `ron`, `slv`, `hrv`, `srp`, `mkd`, `lit`, `lav`, `est`, `tam`, `vie`, `urd`, `tha`, `guj`, `uzb`, `pan`, `aze`, `ind`, `tel`, `pes`, `mal`, `ori`, `mya`, `nep`, `sin`, `khm`, `tuk`, `aka`, `zul`, `sna`, `afr`, `lat`, `slk`, `cat`, `tgl`, `hye`.

You may alternatively use [ISO-639-1 two-letter equivalents](https://iso639-3.sil.org/code_tables/639/data) to the supported `locales`.

You may also assign an empty array to `locales`. In this case, Meilisearch will auto-detect the language of the associated `attributePatterns`.

#### `attributePatterns`

Attribute patterns may begin or end with a `*` wildcard to match multiple fields: `en_*`, `*-ar`.

You may also set `attributePatterns` to `*`, in which case Meilisearch will treat all fields as if they were in the associated locale.

### Get localized attributes settings

<RouteHighlighter method="GET" />

Get the localized attributes settings of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/INDEX_NAME/settings/localized-attributes'
  ```

  ```javascript JS theme={null}
  client.index('INDEX_NAME').getLocalizedAttributes()
  ```

  ```python Python theme={null}
  client.index('INDEX_NAME').get_localized_attributes()
  ```

  ```php PHP theme={null}
  $client->index('INDEX_NAME')->getLocalizedAttributes();
  ```

  ```java Java theme={null}
  client.index("INDEX_NAME").getLocalizedAttributesSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('INDEX_NAME').localized_attributes
  ```

  ```go Go theme={null}
  client.index("INDEX_NAME").GetLocalizedAttributes()
  ```

  ```rust Rust theme={null}
  let localized_attributes: Option<Vec<LocalizedAttributes>> = client
    .index("books")
    .get_localized_attributes()
    .await
    .unwrap();
  ```
</CodeGroup>

##### Response: `200 OK`

```json theme={null}
[
  {"locales": ["jpn"], "attributePatterns": ["*_ja"]}
]
```

### Update localized attribute settings

<RouteHighlighter method="PUT" />

Update the localized attributes settings of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```
[
  {
   "locales": [<String>, …],
   "attributePatterns": [<String>, …],
  }
]
```

| Name                      | Type             | Default value | Description                                                |
| :------------------------ | :--------------- | :------------ | :--------------------------------------------------------- |
| **`localizedAttributes`** | Array of objects | `[]`          | Explicitly set specific locales for one or more attributes |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/INDEX_NAME/settings/localized-attributes' \
    -H 'Content-Type: application/json' \
    --data-binary '[
      {"locales": ["jpn"], "attributePatterns": ["*_ja"]}
    ]'
  ```

  ```javascript JS theme={null}
  client.index('INDEX_NAME').updateLocalizedAttributes([
    { attributePatterns: ['*_ja'], locales: ['jpn'] },
  ])
  ```

  ```python Python theme={null}
  client.index('INDEX_NAME').update_localized_attributes([
    {'attribute_patterns': ['*_ja'], 'locales': ['jpn']}
  ])
  ```

  ```php PHP theme={null}
  $client->index('INDEX_NAME')->updateLocalizedAttributes([
    'locales' => ['jpn'],
    'attributePatterns' => ['*_ja']
  ]);
  ```

  ```java Java theme={null}
  LocalizedAttribute attribute = new LocalizedAttribute();
  attribute.setAttributePatterns(new String[] {"jpn"});
  attribute.setLocales(new String[] {"*_ja"});

  client.index("INDEX_NAME").updateLocalizedAttributesSettings(
    new LocalizedAttributes[] {attribute}
  );
  ```

  ```ruby Ruby theme={null}
  client.index('INDEX_NAME').update_localized_attributes([
    { attribute_patterns: ['*_ja'], locales: ['jpn'] },
  ])
  ```

  ```go Go theme={null}
  client.index("INDEX_NAME").UpdateLocalizedAttributes([]*LocalizedAttributes{
      { AttributePatterns: ["*_ja"], Locales: ["jpn"] },
  })
  ```

  ```rust Rust theme={null}
  let localized_attributes = vec![LocalizedAttributes {
      locales: vec!["jpn".to_string()],
      attribute_patterns: vec!["*_ja".to_string()],
  }];
  let task: TaskInfo = client
    .index("books")
    .set_localized_attributes(&localizced_attributes)
    .await
    .unwrap();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "INDEX_NAME",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2022-04-14T20:56:44.991039Z"
}
```

You can use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset localized attributes settings

<RouteHighlighter method="DELETE" />

Reset an index's localized attributes to their [default value](#localized-attributes-object).

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/INDEX_NAME/settings/localized-attributes'
  ```

  ```javascript JS theme={null}
  client.index('INDEX_NAME').resetLocalizedAttributes()
  ```

  ```python Python theme={null}
  client.index('INDEX_NAME').reset_localized_attributes()
  ```

  ```php PHP theme={null}
  $client->index('INDEX_NAME')->resetLocalizedAttributes();
  ```

  ```java Java theme={null}
  client.index("INDEX_NAME").resetLocalizedAttributesSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('INDEX_NAME').reset_localized_attributes
  ```

  ```go Go theme={null}
  client.index("INDEX_NAME").ResetLocalizedAttributes()
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("books")
    .reset_localized_attributes()
    .await
    .unwrap();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "INDEX_NAME",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2022-04-14T20:53:32.863107Z"
}
```

You can use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Pagination

To protect your database from malicious scraping, Meilisearch has a default limit of 1000 results per search. This setting allows you to configure the maximum number of results returned per search.

`maxTotalHits` takes priority over search parameters such as `limit`, `offset`, `hitsPerPage`, and `page`.

For example, if you set `maxTotalHits` to 100, you will not be able to access search results beyond 100 no matter the value configured for `offset`.

[To learn more about paginating search results with Meilisearch, refer to our dedicated guide.](/guides/front_end/pagination)

### Pagination object

| Name               | Type    | Default value | Description                                                 |
| :----------------- | :------ | :------------ | :---------------------------------------------------------- |
| **`maxTotalHits`** | Integer | `1000`        | The maximum number of search results Meilisearch can return |

<Danger>
  Setting `maxTotalHits` to a value higher than the default will negatively impact search performance. Setting `maxTotalHits` to values over `20000` may result in queries taking seconds to complete.
</Danger>

### Get pagination settings

<RouteHighlighter method="GET" />

Get the pagination settings of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/books/settings/pagination'
  ```

  ```javascript JS theme={null}
  client.index('books').getPagination()
  ```

  ```python Python theme={null}
  client.index('books').get_pagination_settings()
  ```

  ```php PHP theme={null}
  $client->index('books')->getPagination();
  ```

  ```java Java theme={null}
  client.index("books").getPaginationSettings();
  ```

  ```ruby Ruby theme={null}
  index('books').pagination
  ```

  ```go Go theme={null}
  client.Index("books").GetPagination()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").GetPaginationAsync();
  ```

  ```rust Rust theme={null}
  let pagination: PaginationSetting = client
    .index("books")
    .get_pagination()
    .await
    .unwrap();
  ```

  ```dart Dart theme={null}
  await client.index('movies').getPagination();
  ```
</CodeGroup>

##### Response: `200 OK`

```json theme={null}
{
  "maxTotalHits": 1000
}
```

### Update pagination settings

<RouteHighlighter method="PATCH" />

Partially update the pagination settings for an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```
{maxTotalHits: <Integer>}
```

| Name               | Type    | Default value | Description                                                 |
| :----------------- | :------ | :------------ | :---------------------------------------------------------- |
| **`maxTotalHits`** | Integer | `1000`        | The maximum number of search results Meilisearch can return |

<Danger>
  Setting `maxTotalHits` to a value higher than the default will negatively impact search performance. Setting `maxTotalHits` to values over `20000` may result in queries taking seconds to complete.
</Danger>

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PATCH 'MEILISEARCH_URL/indexes/books/settings/pagination' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "maxTotalHits": 100
    }'
  ```

  ```javascript JS theme={null}
  client.index('books').updateSettings({ pagination: { maxTotalHits: 100 }})
  ```

  ```python Python theme={null}
  client.index('books').update_pagination_settings({'maxTotalHits': 100})
  ```

  ```php PHP theme={null}
  $client->index('books')->updateSettings([
    'pagination' => [
      'maxTotalHits' => 100
    ]
  ]);
  ```

  ```java Java theme={null}
  Pagination newPagination = new Pagination();
  newPagination.setMaxTotalHits(100);
  client.index("books").updatePaginationSettings(newPagination);
  ```

  ```ruby Ruby theme={null}
  index('books').update_pagination({ max_total_hits: 100 })
  ```

  ```go Go theme={null}
  client.Index("books").UpdatePagination(&meilisearch.Pagination{
      MaxTotalHits: 100,
  })
  ```

  ```csharp C# theme={null}
  var pagination = new Pagination {
    MaxTotalHits = 20
  };
  await client.Index("movies").UpdatePaginationAsync(pagination);
  ```

  ```rust Rust theme={null}
  let pagination = PaginationSetting {max_total_hits:100};

  let task: TaskInfo = client
    .index("books")
    .set_pagination(pagination)
    .await
    .unwrap();
  ```

  ```dart Dart theme={null}
  await client
      .index('books')
      .updatePagination(Pagination(maxTotalHits: 100));
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "books",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2022-04-14T20:56:44.991039Z"
}
```

You can use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset pagination settings

Reset an index's pagination settings to their [default value](#pagination-object).

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/books/settings/pagination'
  ```

  ```javascript JS theme={null}
  client.index('books').resetPagination()
  ```

  ```python Python theme={null}
  client.index('books').reset_pagination_settings()
  ```

  ```php PHP theme={null}
  $client->index('books')->resetPagination();
  ```

  ```java Java theme={null}
  client.index("books").resetPaginationSettings();
  ```

  ```ruby Ruby theme={null}
  index('books').reset_pagination
  ```

  ```go Go theme={null}
  client.Index("books").ResetPagination()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").ResetPaginationAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("books")
    .reset_pagination()
    .await
    .unwrap();
  ```

  ```dart Dart theme={null}
  await client.index('movies').resetPagination();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "books",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2022-04-14T20:53:32.863107Z"
}
```

You can use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Proximity precision

Calculating the distance between words is a resource-intensive operation. Lowering the precision of this operation may significantly improve performance and will have little impact on result relevancy in most use-cases. Meilisearch uses word distance when [ranking results according to proximity](/learn/relevancy/ranking_rules#3-proximity) and when users perform [phrase searches](/reference/api/search#phrase-search).

`proximityPrecision` accepts one of the following string values:

* `"byWord"`: calculate the precise distance between query terms. Higher precision, but may lead to longer indexing time. This is the default setting
* `"byAttribute"`: determine if multiple query terms are present in the same attribute. Lower precision, but shorter indexing time

### Get proximity precision settings

<RouteHighlighter method="GET" />

Get the proximity precision settings of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/books/settings/proximity-precision'
  ```

  ```javascript JS theme={null}
  client.index('books').getProximityPrecision()
  ```

  ```python Python theme={null}
  client.index('books').get_proximity_precision()
  ```

  ```php PHP theme={null}
  $client->index('books')->getProximityPrecision();
  ```

  ```java Java theme={null}
  client.index("books").getProximityPrecisionSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('books').proximity_precision
  ```

  ```go Go theme={null}
  client.Index("books").GetProximityPrecision()
  ```

  ```csharp C# theme={null}
  await client.Index("books").GetProximityPrecisionAsync();
  ```

  ```rust Rust theme={null}
  let proximity_precision: String = client
    .index("books")
    .get_proximity_precision()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let precisionValue = try await self.client.index("books").getProximityPrecision()
  ```
</CodeGroup>

##### Response: `200 OK`

```
"byWord"
```

### Update proximity precision settings

<RouteHighlighter method="PUT" />

Update the pagination settings for an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```
"byWord"|"byAttribute"
```

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/books/settings/proximity-precision' \
    -H 'Content-Type: application/json' \
    --data-binary '"byAttribute"'
  ```

  ```javascript JS theme={null}
  client.index('books').updateProximityPrecision('byAttribute')
  ```

  ```python Python theme={null}
  client.index('books').update_proximity_precision(ProximityPrecision.BY_ATTRIBUTE)
  ```

  ```php PHP theme={null}
  $client->index('books')->updateProximityPrecision('byAttribute');
  ```

  ```java Java theme={null}
  client.index("books").updateProximityPrecisionSettings("byAttribute");
  ```

  ```ruby Ruby theme={null}
  client.index('books').update_proximity_precision('byAttribute')
  ```

  ```go Go theme={null}
  client.Index("books").UpdateProximityPrecision(ByAttribute)
  ```

  ```csharp C# theme={null}
  await client.Index("books").UpdateProximityPrecisionAsync("byAttribute");
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("books")
    .set_proximity_precision("byAttribute".to_string())
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let task = try await self.client.index("books").updateProximityPrecision(.byWord)
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "books",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2023-04-14T15:50:29.821044Z"
}
```

You can use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset proximity precision settings

<RouteHighlighter method="DELETE" />

Reset an index's proximity precision setting to its default value.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/books/settings/proximity-precision'
  ```

  ```javascript JS theme={null}
  client.index('books').resetProximityPrecision()
  ```

  ```python Python theme={null}
  client.index('books').reset_proximity_precision()
  ```

  ```php PHP theme={null}
  $client->index('books')->resetProximityPrecision();
  ```

  ```java Java theme={null}
  client.index("books").resetProximityPrecisionSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('books').reset_proximity_precision
  ```

  ```go Go theme={null}
  client.Index("books").ResetProximityPrecision()
  ```

  ```csharp C# theme={null}
  await client.Index("books").ResetProximityPrecisionAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("books")
    .reset_proximity_precision()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let task = try await self.client.index("books").resetProximityPrecision()
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "books",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2023-04-14T15:51:47.821044Z"
}
```

You can use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Facet search

Processing filterable attributes for facet search is a resource-intensive operation. This feature is enabled by default, but disabling it may speed up indexing.

`facetSearch` accepts a single Boolean value. If set to `false`, it disables facet search for the whole index. Meilisearch returns an error if you try to access the `/facet-search` endpoint when facet search is disabled.

### Get facet search settings

<RouteHighlighter method="GET" />

Get the facet search settings of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/INDEX_UID/settings/facet-search'
  ```

  ```javascript JS theme={null}
  client.index('INDEX_NAME').getFacetSearch();
  ```

  ```python Python theme={null}
  client.index('books').get_facet_search_settings()
  ```

  ```php PHP theme={null}
  $client->index('INDEX_NAME')->getFacetSearch();
  ```

  ```ruby Ruby theme={null}
  client.index('INDEX_UID').facet_search_setting
  ```

  ```go Go theme={null}
  client.Index("books").GetFacetSearch()
  ```

  ```rust Rust theme={null}
  let facet_search: bool = client
    .index(INDEX_UID)
    .get_facet_search()
    .await
    .unwrap();
  ```
</CodeGroup>

##### Response: `200 OK`

```json theme={null}
true
```

### Update facet search settings

<RouteHighlighter method="PUT" />

Update the facet search settings for an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```
<Boolean>
```

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/INDEX_UID/settings/facet-search' \
    -H 'Content-Type: application/json' \
    --data-binary 'false'
  ```

  ```javascript JS theme={null}
  client.index('INDEX_NAME').updateFacetSearch(false);
  ```

  ```python Python theme={null}
  client.index('books').update_facet_search_settings(False)
  ```

  ```php PHP theme={null}
  $client->index('INDEX_NAME')->updateFacetSearch(false);
  ```

  ```ruby Ruby theme={null}
  client.index('INDEX_UID').update_facet_search_setting(false)
  ```

  ```go Go theme={null}
  client.Index("books").UpdateFacetSearch(false)
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index(INDEX_UID)
    .set_facet_search(false)
    .await
    .unwrap();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "INDEX_UID",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2024-07-19T22:33:18.523881Z"
}
```

Use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset facet search settings

<RouteHighlighter method="DELETE" />

Reset an index's facet search to its default settings.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/INDEX_UID/settings/facet-search'
  ```

  ```javascript JS theme={null}
  client.index('INDEX_NAME').resetFacetSearch();
  ```

  ```python Python theme={null}
  client.index('books').reset_facet_search_settings()
  ```

  ```php PHP theme={null}
  $client->index('INDEX_NAME')->resetFacetSearch();
  ```

  ```ruby Ruby theme={null}
  client.index('INDEX_UID').reset_facet_search_setting
  ```

  ```go Go theme={null}
  client.Index("books").ResetFacetSearch()
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index(INDEX_UID)
    .reset_facet_search()
    .await
    .unwrap();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "INDEX_UID",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2024-07-19T22:35:33.723983Z"
}
```

Use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Prefix search

Prefix search is the process through which Meilisearch matches documents that begin with a specific query term, instead of only exact matches. This is a resource-intensive operation that happens during indexing by default.

Use `prefixSearch` to change how prefix search works. It accepts one of the following strings:

* `"indexingTime"`: calculate prefix search during indexing. This is the default behavior
* `"disabled"`: do not calculate prefix search. May speed up indexing, but will severely impact search result relevancy

### Get prefix search settings

<RouteHighlighter method="GET" />

Get the prefix search settings of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/INDEX_UID/settings/prefix-search'
  ```

  ```javascript JS theme={null}
  client.index('INDEX_NAME').getPrefixSearch();
  ```

  ```python Python theme={null}
  client.index('books').get_prefix_search()
  ```

  ```php PHP theme={null}
  $client->index('INDEX_NAME')->getPrefixSearch();
  ```

  ```ruby Ruby theme={null}
  client.index('INDEX_UID').prefix_search
  ```

  ```go Go theme={null}
  client.Index("books").GetPrefixSearch()
  ```

  ```rust Rust theme={null}
  let prefix_search: PrefixSearchSettings = client
    .index(INDEX_UID)
    .get_prefix_search()
    .await
    .unwrap();
  ```
</CodeGroup>

##### Response: `200 OK`

```json theme={null}
"indexingTime"
```

### Update prefix search settings

<RouteHighlighter method="PUT" />

Update the prefix search settings for an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```
"indexingTime" | "disabled"
```

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/INDEX_UID/settings/prefix-search' \
    -H 'Content-Type: application/json' \
    --data-binary '"disabled"'
  ```

  ```javascript JS theme={null}
  client.index('INDEX_NAME').updatePrefixSearch('disabled');
  ```

  ```python Python theme={null}
  client.index('books').update_prefix_search(PrefixSearch.DISABLED)
  ```

  ```php PHP theme={null}
  $client->index('INDEX_NAME')->updatePrefixSearch('disabled');
  ```

  ```ruby Ruby theme={null}
  client.index('INDEX_UID').update_prefix_search('disabled')
  ```

  ```go Go theme={null}
  client.Index("books").UpdatePrefixSearch("disabled")
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index(INDEX_UID)
    .set_prefix_search(PrefixSearchSettings::Disabled)
    .await
    .unwrap();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "INDEX_UID",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2024-07-19T22:33:18.523881Z"
}
```

Use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset prefix search settings

<RouteHighlighter method="DELETE" />

Reset an index's prefix search to its default settings.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/INDEX_UID/settings/facet-search'
  ```

  ```javascript JS theme={null}
  client.index('INDEX_NAME').resetFacetSearch();
  ```

  ```python Python theme={null}
  client.index('books').reset_facet_search_settings()
  ```

  ```php PHP theme={null}
  $client->index('INDEX_NAME')->resetFacetSearch();
  ```

  ```ruby Ruby theme={null}
  client.index('INDEX_UID').reset_facet_search_setting
  ```

  ```go Go theme={null}
  client.Index("books").ResetFacetSearch()
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index(INDEX_UID)
    .reset_facet_search()
    .await
    .unwrap();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "INDEX_UID",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2024-07-19T22:35:33.723983Z"
}
```

Use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Ranking rules

Ranking rules are built-in rules that rank search results according to certain criteria. They are applied in the same order in which they appear in the `rankingRules` array.

[To learn more about ranking rules, refer to our dedicated guide.](/learn/relevancy/relevancy)

### Ranking rules array

| Name              | Description                                                                     |
| :---------------- | :------------------------------------------------------------------------------ |
| **`"words"`**     | Sorts results by decreasing number of matched query terms                       |
| **`"typo"`**      | Sorts results by increasing number of typos                                     |
| **`"proximity"`** | Sorts results by increasing distance between matched query terms                |
| **`"attribute"`** | Sorts results based on the attribute ranking order                              |
| **`"sort"`**      | Sorts results based on parameters decided at query time                         |
| **`"exactness"`** | Sorts results based on the similarity of the matched words with the query words |

#### Default order

```json theme={null}
[
  "words",
  "typo",
  "proximity",
  "attribute",
  "sort",
  "exactness"
]
```

### Get ranking rules

<RouteHighlighter method="GET" />

Get the ranking rules of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/movies/settings/ranking-rules'
  ```

  ```javascript JS theme={null}
  client.index('movies').getRankingRules()
  ```

  ```python Python theme={null}
  client.index('movies').get_ranking_rules()
  ```

  ```php PHP theme={null}
  $client->index('movies')->getRankingRules();
  ```

  ```java Java theme={null}
  client.index("movies").getRankingRulesSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('movies').ranking_rules
  ```

  ```go Go theme={null}
  client.Index("movies").GetRankingRules()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").GetRankingRulesAsync();
  ```

  ```rust Rust theme={null}
  let ranking_rules: Vec<String> = client
    .index("movies")
    .get_ranking_rules()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").getRankingRules { (result) in
      switch result {
      case .success(let rankingRules):
          print(rankingRules)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').getRankingRules();
  ```
</CodeGroup>

##### Response: `200 Ok`

```json theme={null}
[
  "words",
  "typo",
  "proximity",
  "attribute",
  "sort",
  "exactness",
  "release_date:desc"
]
```

### Update ranking rules

<RouteHighlighter method="PUT" />

Update the ranking rules of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```
[<String>, <String>, …]
```

An array that contains ranking rules in order of importance.

To create a custom ranking rule, give an attribute followed by a colon (`:`) and either `asc` for ascending order or `desc` for descending order.

* To apply an **ascending sort** (results sorted by increasing value): `attribute_name:asc`
* To apply a **descending sort** (results sorted by decreasing value): `attribute_name:desc`

<Warning>
  If some documents do not contain the attribute defined in a custom ranking rule, the application of the ranking rule is undefined and the search results might not be sorted as you expected.

  Make sure that any attribute used in a custom ranking rule is present in all of your documents. For example, if you set the custom ranking rule `desc(year)`, make sure that all your documents contain the attribute `year`.
</Warning>

[To learn more about ranking rules, refer to our dedicated guide.](/learn/relevancy/ranking_rules)

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/movies/settings/ranking-rules' \
    -H 'Content-Type: application/json' \
    --data-binary '[
      "words",
      "typo",
      "proximity",
      "attribute",
      "sort",
      "exactness",
      "release_date:asc",
      "rank:desc"
    ]'
  ```

  ```javascript JS theme={null}
  client.index('movies').updateRankingRules([
      'words',
      'typo',
      'proximity',
      'attribute',
      'sort',
      'exactness',
      'release_date:asc',
      'rank:desc'
  ])
  ```

  ```python Python theme={null}
  client.index('movies').update_ranking_rules([
      'words',
      'typo',
      'proximity',
      'attribute',
      'sort',
      'exactness',
      'release_date:asc',
      'rank:desc'
  ])
  ```

  ```php PHP theme={null}
  $client->index('movies')->updateRankingRules([
    'words',
    'typo',
    'proximity',
    'attribute',
    'sort',
    'exactness',
    'release_date:asc',
    'rank:desc'
  ]);
  ```

  ```java Java theme={null}
  Settings settings = new Settings();
  settings.setRankingRules(new String[]
  {
    "words",
    "typo",
    "proximity",
    "attribute",
    "sort",
    "exactness",
    "release_date:asc",
    "rank:desc"
  });
  client.index("movies").updateSettings(settings);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').update_ranking_rules([
    'words',
    'typo',
    'proximity',
    'attribute',
    'sort',
    'exactness',
    'release_date:asc',
    'rank:desc'
  ])
  ```

  ```go Go theme={null}
  rankingRules := []string{
    "words",
    "typo",
    "proximity",
    "attribute",
    "sort",
    "exactness",
    "release_date:asc",
    "rank:desc",
  }
  client.Index("movies").UpdateRankingRules(&rankingRules)
  ```

  ```csharp C# theme={null}
  await client.Index("movies").UpdateRankingRulesAsync(new[]
  {
      "words",
      "typo",
      "proximity",
      "attribute",
      "sort",
      "exactness",
      "release_date:asc",
      "rank:desc"
  });
  ```

  ```rust Rust theme={null}
  let ranking_rules = [
    "words",
    "typo",
    "proximity",
    "attribute",
    "sort",
    "exactness",
    "release_date:asc",
    "rank:desc",
  ];

  let task: TaskInfo = client
    .index("movies")
    .set_ranking_rules(&ranking_rules)
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let rankingRules: [String] = [
      "words",
      "typo",
      "proximity",
      "attribute",
      "sort",
      "exactness",
      "release_date:asc",
      "rank:desc"
  ]
  client.index("movies").updateRankingRules(rankingRules) { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').updateRankingRules([
    'words',
    'typo',
    'proximity',
    'attribute',
    'sort',
    'exactness',
    'release_date:asc',
    'rank:desc',
  ]);
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset ranking rules

<RouteHighlighter method="DELETE" />

Reset the ranking rules of an index to their [default value](#default-order).

<Tip>
  Resetting ranking rules is not the same as removing them. To remove a ranking rule, use the [update ranking rules endpoint](#update-ranking-rules).
</Tip>

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/movies/settings/ranking-rules'
  ```

  ```javascript JS theme={null}
  client.index('movies').resetRankingRules()
  ```

  ```python Python theme={null}
  client.index('movies').reset_ranking_rules()
  ```

  ```php PHP theme={null}
  $client->index('movies')->resetRankingRules();
  ```

  ```java Java theme={null}
  client.index("movies").resetRankingRulesSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('movies').reset_ranking_rules
  ```

  ```go Go theme={null}
  client.Index("movies").ResetRankingRules()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").ResetRankingRulesAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("movies")
    .reset_ranking_rules()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").resetRankingRules { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').resetRankingRules();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Searchable attributes

The values associated with attributes in the `searchableAttributes` list are searched for matching query words. The order of the list also determines the [attribute ranking order](/learn/relevancy/attribute_ranking_order).

By default, the `searchableAttributes` array is equal to all fields in your dataset. This behavior is represented by the value `["*"]`.

<Warning>
  Updating searchable attributes will re-index all documents in the index, which can take some time. We recommend updating your index settings first and then adding documents as this reduces RAM consumption.
</Warning>

[To learn more about searchable attributes, refer to our dedicated guide.](/learn/relevancy/displayed_searchable_attributes#searchable-fields)

### Get searchable attributes

<RouteHighlighter method="GET" />

Get the searchable attributes of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/movies/settings/searchable-attributes'
  ```

  ```javascript JS theme={null}
  client.index('movies').getSearchableAttributes()
  ```

  ```python Python theme={null}
  client.index('movies').get_searchable_attributes()
  ```

  ```php PHP theme={null}
  $client->index('movies')->getSearchableAttributes();
  ```

  ```java Java theme={null}
  client.index("movies").getSearchableAttributesSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('movies').searchable_attributes
  ```

  ```go Go theme={null}
  client.Index("movies").GetSearchableAttributes()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").GetSearchableAttributesAsync();
  ```

  ```rust Rust theme={null}
  let searchable_attributes: Vec<String> = client
    .index("movies")
    .get_searchable_attributes()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").getSearchableAttributes { (result) in
      switch result {
      case .success(let searchableAttributes):
          print(searchableAttributes)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').getSearchableAttributes();
  ```
</CodeGroup>

##### Response: `200 Ok`

```json theme={null}
[
  "title",
  "overview",
  "genres",
  "release_date.year"
]
```

### Update searchable attributes

<RouteHighlighter method="PUT" />

Update the searchable attributes of an index.

<Warning>
  Due to an implementation bug, manually updating `searchableAttributes` will change the displayed order of document fields in the JSON response. This behavior is inconsistent and will be fixed in a future release.
</Warning>

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```
[<String>, <String>, …]
```

An array of strings. Each string should be an attribute that exists in the selected index. The array should be given in [order of importance](/learn/relevancy/attribute_ranking_order): from the most important attribute to the least important attribute.

If an attribute contains an object, you can use dot notation to set one or more of its keys as a value for this setting: `"searchableAttributes": ["release_date.year"]`.

<Warning>
  If the field does not exist, no error will be thrown.
</Warning>

[To learn more about searchable attributes, refer to our dedicated guide.](/learn/relevancy/displayed_searchable_attributes#searchable-fields)

#### Example

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
    'genres'
  ])
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
  client.index("movies").updateSearchableAttributesSettings(new String[]
  {
    "title",
    "overview",
    "genres"
  });
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
  await client.Index("movies").UpdateSearchableAttributesAsync(new[] {"title", "overview", "genres"});
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
  let searchableAttributes: [String] = ["title", "overview", "genres"]
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

In this example, a document with a match in `title` will be more relevant than another document with a match in `overview`.

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset searchable attributes

<RouteHighlighter method="DELETE" />

Reset the searchable attributes of the index to the default value.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/movies/settings/searchable-attributes'
  ```

  ```javascript JS theme={null}
  client.index('movies').resetSearchableAttributes()
  ```

  ```python Python theme={null}
  client.index('movies').reset_searchable_attributes()
  ```

  ```php PHP theme={null}
  $client->index('movies')->resetSearchableAttributes();
  ```

  ```java Java theme={null}
  client.index("movies").resetSearchableAttributesSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('movies').reset_searchable_attributes
  ```

  ```go Go theme={null}
  client.Index("movies").ResetSearchableAttributes()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").ResetSearchableAttributesAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("movies")
    .reset_searchable_attributes()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").resetSearchableAttributes { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').resetSearchableAttributes();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Search cutoff

Configure the maximum duration of a search query. If a search operation reaches the cutoff, Meilisearch immediately interrupts it and returns all computed results.

By default, Meilisearch interrupts searches after 1500 milliseconds.

### Get search cutoff

<RouteHighlighter method="GET" />

Get an index's search cutoff value.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/movies/settings/search-cutoff-ms'
  ```

  ```javascript JS theme={null}
  client.index('movies').getSearchCutoffMs()
  ```

  ```python Python theme={null}
  client.index('movies').get_search_cutoff_ms()
  ```

  ```php PHP theme={null}
  $client->index('movies')->getSearchCutoffMs();
  ```

  ```java Java theme={null}
  client.index("movies").getSearchCutoffMsSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search_cutoff_ms
  ```

  ```go Go theme={null}
  client.Index("movies").GetSearchCutoffMs()
  ```

  ```csharp C# theme={null}
  var searchCutoff = await client.Index("movies").GetSearchCutoffMsAsync();
  ```

  ```rust Rust theme={null}
  let search_cutoff_ms: String = client
    .index("movies")
    .get_search_cutoff_ms()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let precisionValue = try await self.client.index("books").getSearchCutoffMs()
  ```
</CodeGroup>

##### Response: `200 Ok`

```json theme={null}
null
```

### Update search cutoff

<RouteHighlighter method="PUT" />

Update an index's search cutoff value.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```
150
```

A single integer indicating the cutoff value in milliseconds.

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/movies/settings/search-cutoff-ms' \
    -H 'Content-Type: application/json' \
    --data-binary '150'
  ```

  ```javascript JS theme={null}
  client.index('movies').updateSearchCutoffMs(150)
  ```

  ```python Python theme={null}
  client.index('movies').update_search_cutoff_ms(150)
  ```

  ```php PHP theme={null}
  $client->index('movies')->updateSearchCutoffMs(150);
  ```

  ```java Java theme={null}
  client.index("movies").updateSearchCutoffMsSettings(150);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').update_search_cutoff_ms(150)
  ```

  ```go Go theme={null}
  client.Index("movies").UpdateSearchCutoffMs(150)
  ```

  ```csharp C# theme={null}
  await client.Index("movies").UpdateSearchCutoffMsAsync(150);
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("movies")
    .set_search_cutoff_ms(Some(150))
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let task = try await self.client.index("books").updateSearchCutoffMs(150)
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2023-03-21T06:33:41.000000Z"
}
```

Use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset search cutoff

<RouteHighlighter method="DELETE" />

Reset an index's search cutoff value to its default value, `null`. This translates to a cutoff of 1500ms.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/movies/settings/search-cutoff-ms'
  ```

  ```javascript JS theme={null}
  client.index('movies').resetSearchCutoffMs()
  ```

  ```python Python theme={null}
  client.index('movies').reset_search_cutoff_ms()
  ```

  ```php PHP theme={null}
  $client->index('movies')->resetSearchCutoffMs();
  ```

  ```java Java theme={null}
  client.index("movies").resetSearchCutoffMsSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('movies').reset_search_cutoff_ms
  ```

  ```go Go theme={null}
  client.Index("books").ResetSearchCutoffMs()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").ResetSearchCutoffMsAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("movies")
    .reset_search_cutoff_ms()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let task = try await self.client.index("books").resetSearchCutoffMs()
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2023-03-21T07:05:16.000000Z"
}
```

## Separator tokens

Configure strings as custom separator tokens indicating where a word ends and begins.

Tokens in the `separatorTokens` list are added on top of [Meilisearch's default list of separators](/learn/engine/datatypes#string). To remove separators from the default list, use [the `nonSeparatorTokens` setting](#non-separator-tokens).

### Get separator tokens

<RouteHighlighter method="GET" />

Get an index's list of custom separator tokens.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/articles/settings/separator-tokens'
  ```

  ```javascript JS theme={null}
  client.index('books').getSeparatorTokens()
  ```

  ```python Python theme={null}
  client.index('articles').get_separator_tokens()
  ```

  ```php PHP theme={null}
  $client->index('articles')->getSeparatorTokens();
  ```

  ```java Java theme={null}
  client.index("articles").getSeparatorTokensSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('articles').separator_tokens
  ```

  ```go Go theme={null}
  client.Index("articles").GetSeparatorTokens()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").GetSeparatorTokensAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index('articles')
    .get_separator_tokens()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("books").getSeparatorTokens { result in
    // handle result
  }
  ```

  ```dart Dart theme={null}
  await client.index('articles').getSeparatorTokens();
  ```
</CodeGroup>

##### Response: `200 Ok`

```json theme={null}
[]
```

### Update separator tokens

<RouteHighlighter method="PUT" />

Update an index's list of custom separator tokens.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```
["|", "&hellip;"]
```

An array of strings, with each string indicating a word separator.

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/articles/settings/separator-tokens' \
    -H 'Content-Type: application/json'  \
    --data-binary '["|", "&hellip;"]'
  ```

  ```javascript JS theme={null}
  client.index('books').updateSeparatorTokens(['|', '&hellip;'])
  ```

  ```python Python theme={null}
  client.index('articles').update_separator_tokens(["|", "&hellip;"])
  ```

  ```php PHP theme={null}
  $client->index('articles')->updateSeparatorTokens(['|', '&hellip;']);
  ```

  ```java Java theme={null}
  String[] newSeparatorTokens = { "|", "&hellip;" };
  client.index("articles").updateSeparatorTokensSettings(newSeparatorTokens);
  ```

  ```ruby Ruby theme={null}
  client.index('articles').update_separator_tokens(['|', '&hellip;'])
  ```

  ```go Go theme={null}
  client.Index("articles").UpdateSeparatorTokens([]string{
    "|",
    "&hellip;",
  })
  ```

  ```csharp C# theme={null}
  await client.Index("movies").UpdateSeparatorTokensAsync(new[] { "|", "&hellip;" });
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index('articles')
    .set_separator_tokens(&vec!['|'.to_string(), '&hellip;'.to_string()])
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("books").updateSeparatorTokens(["|", "&hellip;"]) { result in
    // handle result
  }
  ```

  ```dart Dart theme={null}
  await client.index('articles').updateSeparatorTokens(["|", "&hellip;"]);
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

Use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset separator tokens

<RouteHighlighter method="DELETE" />

Reset an index's list of custom separator tokens to its default value, `[]`.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/articles/settings/separator-tokens'
  ```

  ```javascript JS theme={null}
  client.index('books').resetSeparatorTokens()
  ```

  ```python Python theme={null}
  client.index('articles').reset_separator_tokens()
  ```

  ```php PHP theme={null}
  $client->index('articles')->resetSeparatorTokens();
  ```

  ```java Java theme={null}
  client.index("articles").resetSeparatorTokensSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('articles').reset_separator_tokens
  ```

  ```go Go theme={null}
  client.Index("articles").ResetSeparatorTokens()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").ResetSeparatorTokensAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index('articles')
    .reset_separator_tokens()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("books").resetSeparatorTokens { result in
    // handle result
  }
  ```

  ```dart Dart theme={null}
  await client.index('articles').resetSeparatorTokens();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

Use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Non-separator tokens

Remove tokens from Meilisearch's default [list of word separators](/learn/engine/datatypes#string).

### Get non-separator tokens

<RouteHighlighter method="GET" />

Get an index's list of non-separator tokens.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/articles/settings/non-separator-tokens'
  ```

  ```javascript JS theme={null}
  client.index('books').getNonSeparatorTokens()
  ```

  ```python Python theme={null}
  client.index('articles').get_non_separator_tokens()
  ```

  ```php PHP theme={null}
  $client->index('articles')->getNonSeparatorTokens();
  ```

  ```java Java theme={null}
  client.index("articles").getNonSeparatorTokensSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('articles').non_separator_tokens
  ```

  ```go Go theme={null}
  client.Index("articles").GetNonSeparatorTokens()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").GetNonSeparatorTokensAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index('articles')
    .get_non_separator_tokens()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("books").getNonSeparatorTokens { result in
    // handle result
  }
  ```

  ```dart Dart theme={null}
  await client.index('articles').getNonSeparatorTokens();
  ```
</CodeGroup>

##### Response: `200 Ok`

```json theme={null}
[]
```

### Update non-separator tokens

<RouteHighlighter method="PUT" />

Update an index's list of non-separator tokens.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```
["@", "#"]
```

An array of strings, with each string indicating a token present in [list of word separators](/learn/engine/datatypes#string).

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/articles/settings/non-separator-tokens' \
    -H 'Content-Type: application/json'  \
    --data-binary '["@", "#"]'
  ```

  ```javascript JS theme={null}
  client.index('books').updateNonSeparatorTokens(['@', '#'])
  ```

  ```python Python theme={null}
  client.index('articles').update_non_separator_tokens(["@", "#"])
  ```

  ```php PHP theme={null}
  $client->index('articles')->updateNonSeparatorTokens(['@', '#']);
  ```

  ```java Java theme={null}
  String[] newSeparatorTokens = { "@", "#" };
  client.index("articles").updateNonSeparatorTokensSettings(newSeparatorTokens);
  ```

  ```ruby Ruby theme={null}
  client.index('articles').update_non_separator_tokens(['@', '#'])
  ```

  ```go Go theme={null}
  client.Index("articles").UpdateNonSeparatorTokens([]string{
    "@",
    "#",
  })
  ```

  ```csharp C# theme={null}
  await client.Index("movies").UpdateNonSeparatorTokensAsync(new[] { "@", "#" });
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index('articles')
    .set_non_separator_tokens(&vec!['@'.to_string(), '#'.to_string()])
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("books").updateNonSeparatorTokens(["@", "#"]) { result in
    // handle result
  }
  ```

  ```dart Dart theme={null}
  await client.index('articles').updateNonSeparatorTokens(["@", "#"]);
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

Use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset non-separator tokens

<RouteHighlighter method="DELETE" />

Reset an index's list of non-separator tokens to its default value, `[]`.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/articles/settings/separator-tokens'
  ```

  ```javascript JS theme={null}
  client.index('books').resetSeparatorTokens()
  ```

  ```python Python theme={null}
  client.index('articles').reset_separator_tokens()
  ```

  ```php PHP theme={null}
  $client->index('articles')->resetSeparatorTokens();
  ```

  ```java Java theme={null}
  client.index("articles").resetSeparatorTokensSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('articles').reset_separator_tokens
  ```

  ```go Go theme={null}
  client.Index("articles").ResetSeparatorTokens()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").ResetSeparatorTokensAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index('articles')
    .reset_separator_tokens()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("books").resetSeparatorTokens { result in
    // handle result
  }
  ```

  ```dart Dart theme={null}
  await client.index('articles').resetSeparatorTokens();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

Use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Sortable attributes

Attributes that can be used when sorting search results using the [`sort` search parameter](/reference/api/search#sort).

<Warning>
  Updating sortable attributes will re-index all documents in the index, which can take some time. We recommend updating your index settings first and then adding documents as this reduces RAM consumption.
</Warning>

[To learn more about sortable attributes, refer to our dedicated guide.](/learn/filtering_and_sorting/sort_search_results)

### Get sortable attributes

<RouteHighlighter method="GET" />

Get the sortable attributes of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/books/settings/sortable-attributes'
  ```

  ```javascript JS theme={null}
  client.index('books').getSortableAttributes()
  ```

  ```python Python theme={null}
  client.index('books').get_sortable_attributes()
  ```

  ```php PHP theme={null}
  $client->index('books')->getSortableAttributes();
  ```

  ```java Java theme={null}
  client.index("books").getSortableAttributesSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('books').sortable_attributes
  ```

  ```go Go theme={null}
  client.Index("books").GetSortableAttributes()
  ```

  ```csharp C# theme={null}
  await client.Index("books").GetSortableAttributesAsync();
  ```

  ```rust Rust theme={null}
  let sortable_attributes: Vec<String> = client
    .index("books")
    .get_sortable_attributes()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("books").getSortableAttributes { (result: Result<Searchable<Book>, Swift.Error>) in
    switch result {
    case .success(let attributes):
      print(attributes)
    case .failure(let error):
      print(error)
    }
  }
  ```

  ```dart Dart theme={null}
  await client.index('books').getSortableAttributes();
  ```
</CodeGroup>

##### Response: `200 Ok`

```json theme={null}
[
  "price",
  "author.surname"
]
```

### Update sortable attributes

<RouteHighlighter method="PUT" />

Update an index's sortable attributes list.

[You can read more about sorting at query time on our dedicated guide.](/learn/filtering_and_sorting/sort_search_results)

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```
[<String>, <String>, …]
```

An array of strings. Each string should be an attribute that exists in the selected index.

If an attribute contains an object, you can use dot notation to set one or more of its keys as a value for this setting: `"sortableAttributes": ["author.surname"]`.

<Warning>
  If the field does not exist, no error will be thrown.
</Warning>

[To learn more about sortable attributes, refer to our dedicated guide.](/learn/filtering_and_sorting/sort_search_results)

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/books/settings/sortable-attributes' \
    -H 'Content-Type: application/json' \
    --data-binary '[
      "price",
      "author"
    ]'
  ```

  ```javascript JS theme={null}
  client.index('books')
    .updateSortableAttributes([
      'price',
      'author'
    ])
  ```

  ```python Python theme={null}
  client.index('books').update_sortable_attributes([
    'price',
    'author'
  ])
  ```

  ```php PHP theme={null}
  $client->index('books')->updateSortableAttributes([
    'price',
    'author'
  ]);
  ```

  ```java Java theme={null}
  client.index("books").updateSortableAttributesSettings(new String[] {"price", "author"});
  ```

  ```ruby Ruby theme={null}
  client.index('books').update_sortable_attributes([
    'price',
    'author'
  ])
  ```

  ```go Go theme={null}
  sortableAttributes := []string{
    "price",
    "author",
  }
  client.Index("books").UpdateSortableAttributes(&sortableAttributes)
  ```

  ```csharp C# theme={null}
  await client.Index("books").UpdateSortableAttributesAsync(new [] { "price", "author" });
  ```

  ```rust Rust theme={null}
  let sortable_attributes = [
    "price",
    "author"
  ];

  let task: TaskInfo = client
    .index("books")
    .set_sortable_attributes(&sortable_attributes)
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("books").updateSortableAttributes(["price", "author"]) { (result) in
    switch result {
    case .success(let task):
      print(task)
    case .failure(let error):
      print(error)
    }
  }
  ```

  ```dart Dart theme={null}
  await client.index('books').updateSortableAttributes(['price', 'author']);
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset sortable attributes

<RouteHighlighter method="DELETE" />

Reset an index's sortable attributes list back to its default value.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/books/settings/sortable-attributes'
  ```

  ```javascript JS theme={null}
  client.index('books').resetSortableAttributes()
  ```

  ```python Python theme={null}
  client.index('books').reset_sortable_attributes()
  ```

  ```php PHP theme={null}
  $client->index('books')->resetSortableAttributes();
  ```

  ```java Java theme={null}
  client.index("books").resetSortableAttributesSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('books').reset_sortable_attributes
  ```

  ```go Go theme={null}
  client.Index("books").ResetSortableAttributes()
  ```

  ```csharp C# theme={null}
  await client.Index("books").ResetSortableAttributesAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("books")
    .reset_sortable_attributes()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("books").resetSortableAttributes() { (result) in
    switch result {
    case .success(let attributes):
      print(attributes)
    case .failure(let error):
      print(error)
    }
  }
  ```

  ```dart Dart theme={null}
  await client.index('books').resetSortableAttributes();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Stop words

Words added to the `stopWords` list are ignored in future search queries.

<Warning>
  Updating stop words will re-index all documents in the index, which can take some time. We recommend updating your index settings first and then adding documents as this reduces RAM consumption.
</Warning>

<Tip>
  Stop words are strongly related to the language used in your dataset. For example, most datasets containing English documents will have countless occurrences of `the` and `of`. Italian datasets, instead, will benefit from ignoring words like `a`, `la`, or `il`.

  [This open-source project on GitHub](https://github.com/stopwords-iso/stopwords-iso) offers lists of possible stop words in different languages. Note that, depending on your dataset and use case, you will need to tweak these lists for optimal results.
</Tip>

### Get stop words

<RouteHighlighter method="GET" />

Get the stop words list of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/movies/settings/stop-words'
  ```

  ```javascript JS theme={null}
  client.index('movies').getStopWords()
  ```

  ```python Python theme={null}
  client.index('movies').get_stop_words()
  ```

  ```php PHP theme={null}
  $client->index('movies')->getStopWords();
  ```

  ```java Java theme={null}
  client.index("movies").getStopWordsSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('movies').stop_words
  ```

  ```go Go theme={null}
  client.Index("movies").GetStopWords()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").GetStopWordsAsync();
  ```

  ```rust Rust theme={null}
  let stop_words: Vec<String> = client
    .index("movies")
    .get_stop_words()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").getStopWords { (result) in
      switch result {
      case .success(let stopWords):
          print(stopWords)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').getStopWords();
  ```
</CodeGroup>

##### Response: `200 Ok`

```json theme={null}
[
  "of",
  "the",
  "to"
]
```

### Update stop words

<RouteHighlighter method="PUT" />

Update the list of stop words of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```
[<String>, <String>, …]
```

An array of strings. Each string should be a single word.

If a list of stop words already exists, it will be overwritten (*replaced*).

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/movies/settings/stop-words' \
    -H 'Content-Type: application/json' \
    --data-binary '[
      "the",
      "of",
      "to"
    ]'
  ```

  ```javascript JS theme={null}
  client.index('movies').updateStopWords(['of', 'the', 'to'])
  ```

  ```python Python theme={null}
  client.index('movies').update_stop_words(['of', 'the', 'to'])
  ```

  ```php PHP theme={null}
  $client->index('movies')->updateStopWords(['the', 'of', 'to']);
  ```

  ```java Java theme={null}
  client.index("movies").updateStopWordsSettings(new String[] {"of", "the", "to"});
  ```

  ```ruby Ruby theme={null}
  client.index('movies').update_stop_words(['of', 'the', 'to'])
  ```

  ```go Go theme={null}
  stopWords := []string{"of", "the", "to"}
  client.Index("movies").UpdateStopWords(&stopWords)
  ```

  ```csharp C# theme={null}
  await client.Index("movies").UpdateStopWordsAsync(new[] {"of", "the", "to"});
  ```

  ```rust Rust theme={null}
  let stop_words = ["of", "the", "to"];
  let task: TaskInfo = client
    .index("movies")
    .set_stop_words(&stop_words)
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let stopWords: [String] = ["of", "the", "to"]
  client.index("movies").updateStopWords(stopWords) { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').updateStopWords(['of', 'the', 'to']);
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset stop words

<RouteHighlighter method="DELETE" />

Reset the list of stop words of an index to its default value.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/movies/settings/stop-words'
  ```

  ```javascript JS theme={null}
  client.index('movies').resetStopWords()
  ```

  ```python Python theme={null}
  client.index('movies').reset_stop_words()
  ```

  ```php PHP theme={null}
  $client->index('movies')->resetStopWords();
  ```

  ```java Java theme={null}
  client.index("movies").resetStopWordsSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('movies').reset_stop_words
  ```

  ```go Go theme={null}
  client.Index("movies").ResetStopWords()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").ResetStopWordsAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("movies")
    .reset_stop_words()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").resetStopWords { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').resetStopWords();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Synonyms

The `synonyms` object contains words and their respective synonyms. A synonym in Meilisearch is considered equal to its associated word for the purposes of calculating search results.

[To learn more about synonyms, refer to our dedicated guide.](/learn/relevancy/synonyms)

### Get synonyms

<RouteHighlighter method="GET" />

Get the list of synonyms of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/movies/settings/synonyms'
  ```

  ```javascript JS theme={null}
  client.index('movies').getSynonyms()
  ```

  ```python Python theme={null}
  client.index('movies').get_synonyms()
  ```

  ```php PHP theme={null}
  $client->index('movies')->getSynonyms();
  ```

  ```java Java theme={null}
  client.index("movies").getSynonymsSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('movies').synonyms
  ```

  ```go Go theme={null}
  client.Index("movies").GetSynonyms()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").GetSynonymsAsync();
  ```

  ```rust Rust theme={null}
  let synonyms: HashMap<String, Vec<String>> = client
    .index("movies")
    .get_synonyms()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").getSynonyms { (result) in
      switch result {
      case .success(let synonyms):
          print(synonyms)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').getSynonyms();
  ```
</CodeGroup>

##### Response: `200 OK`

```json theme={null}
{
  "wolverine": [
    "xmen",
    "logan"
  ],
  "logan": [
    "wolverine",
    "xmen"
  ],
  "wow": [
    "world of warcraft"
  ]
}
```

### Update synonyms

<RouteHighlighter method="PUT" />

Update the list of synonyms of an index. Synonyms are [normalized](/learn/relevancy/synonyms#normalization).

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```
{
  <String>: [<String>, <String>, …],
  …
}
```

An object that contains all synonyms and their associated words. Add the associated words in an array to set a synonym for a word.

[To learn more about synonyms, refer to our dedicated guide.](/learn/relevancy/synonyms)

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/movies/settings/synonyms' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "wolverine": [
        "xmen",
        "logan"
      ],
      "logan": [
        "wolverine",
        "xmen"
      ],
      "wow": ["world of warcraft"]
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').updateSynonyms({
    wolverine: ['xmen', 'logan'],
    logan: ['wolverine', 'xmen'],
    wow: ['world of warcraft']
  })
  ```

  ```python Python theme={null}
  client.index('movies').update_synonyms({
    'wolverine': ['xmen', 'logan'],
    'logan': ['wolverine', 'xmen'],
    'wow': ['world of warcraft']
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->updateSynonyms([
    'wolverine' => ['xmen', 'logan'],
    'logan' => ['wolverine', 'xmen'],
    'wow' => ['world of warcraft']
  ]);
  ```

  ```java Java theme={null}
  HashMap<String, String[]> synonyms = new HashMap<String, String[]>();
  synonyms.put("wolverine", new String[] {"xmen", "logan"});
  synonyms.put("logan", new String[] {"wolverine"});
  client.index("movies").updateSynonymsSettings(synonyms);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').update_synonyms({
    wolverine: ['xmen', 'logan'],
    logan: ['wolverine', 'xmen'],
    wow: ['world of warcraft']
  })
  ```

  ```go Go theme={null}
  synonyms := map[string][]string{
    "wolverine": []string{"xmen", "logan"},
    "logan":     []string{"wolverine", "xmen"},
    "wow":       []string{"world of warcraft"},
  }
  client.Index("movies").UpdateSynonyms(&synonyms)
  ```

  ```csharp C# theme={null}
  var synonyms = new Dictionary<string, IEnumerable<string>>
  {
      { "wolverine", new string[] { "xmen", "logan" } },
      { "logan", new string[] { "wolverine", "xmen" } },
      { "wow", new string[] { "world of warcraft" } }
  };
  await client.Index("movies").UpdateSynonymsAsync(synonyms);
  ```

  ```rust Rust theme={null}
  let mut synonyms = std::collections::HashMap::new();
  synonyms.insert(String::from("wolverine"), vec![String::from("xmen"), String::from("logan")]);
  synonyms.insert(String::from("logan"), vec![String::from("xmen"), String::from("wolverine")]);
  synonyms.insert(String::from("wow"), vec![String::from("world of warcraft")]);

  let task: TaskInfo = client
    .index("movies")
    .set_synonyms(&synonyms)
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let synonyms: [String: [String]] = [
      "wolverine": ["xmen", "logan"],
      "logan": ["wolverine", "xmen"],
      "wow": ["world of warcraft"]
  ]
  client.index("movies").updateSynonyms(synonyms) { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').updateSynonyms({
    'wolverine': ['xmen', 'logan'],
    'logan': ['wolverine', 'xmen'],
    'wow': ['world of warcraft'],
  });
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset synonyms

<RouteHighlighter method="DELETE" />

Reset the list of synonyms of an index to its default value.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/movies/settings/synonyms'
  ```

  ```javascript JS theme={null}
  client.index('movies').resetSynonyms()
  ```

  ```python Python theme={null}
  client.index('movies').reset_synonyms()
  ```

  ```php PHP theme={null}
  $client->index('movies')->resetSynonyms();
  ```

  ```java Java theme={null}
  client.index("movies").resetSynonymsSettings();
  ```

  ```ruby Ruby theme={null}
  client.index('movies').reset_synonyms
  ```

  ```go Go theme={null}
  client.Index("movies").ResetSynonyms()
  ```

  ```csharp C# theme={null}
  await client.Index("movies").ResetSynonymsAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("movies")
    .reset_synonyms()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").resetSynonyms { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').resetSynonyms();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Typo tolerance

Typo tolerance helps users find relevant results even when their search queries contain spelling mistakes or typos. This setting allows you to configure the minimum word size for typos and disable typo tolerance for specific words or attributes.

[To learn more about typo tolerance, refer to our dedicated guide.](/learn/relevancy/typo_tolerance_settings)

### Typo tolerance object

| Name                               | Type             | Default Value | Description                                                                      |
| :--------------------------------- | :--------------- | :------------ | :------------------------------------------------------------------------------- |
| **`enabled`**                      | Boolean          | `true`        | Whether typo tolerance is enabled or not                                         |
| **`minWordSizeForTypos.oneTypo`**  | Integer          | `5`           | The minimum word size for accepting 1 typo; must be between `0` and `twoTypos`   |
| **`minWordSizeForTypos.twoTypos`** | Integer          | `9`           | The minimum word size for accepting 2 typos; must be between `oneTypo` and `255` |
| **`disableOnWords`**               | Array of strings | Empty         | An array of words for which the typo tolerance feature is disabled               |
| **`disableOnAttributes`**          | Array of strings | Empty         | An array of attributes for which the typo tolerance feature is disabled          |
| **`disableOnNumbers`**             | Boolean          | `false`       | Whether typo tolerance for numbers is disabled or enabled                        |

### Get typo tolerance settings

<RouteHighlighter method="GET" />

Get the typo tolerance settings of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/books/settings/typo-tolerance'
  ```

  ```javascript JS theme={null}
  client.index('books').getTypoTolerance()
  ```

  ```python Python theme={null}
  client.index('books').get_typo_tolerance()
  ```

  ```php PHP theme={null}
  $client->index('books')->getTypoTolerance();
  ```

  ```java Java theme={null}
  client.index("books").getTypoToleranceSettings();
  ```

  ```ruby Ruby theme={null}
  index('books').typo_tolerance
  ```

  ```go Go theme={null}
  client.Index("books").GetTypoTolerance()
  ```

  ```csharp C# theme={null}
  await client.Index("books").GetTypoToleranceAsync();
  ```

  ```rust Rust theme={null}
  let typo_tolerance: TypoToleranceSettings = client
    .index("books")
    .get_typo_tolerance()
    .await
    .unwrap();
  ```

  ```dart Dart theme={null}
  await client.index('books').getTypoTolerance();
  ```
</CodeGroup>

##### Response: `200 OK`

```json theme={null}
{
  "enabled": true,
  "minWordSizeForTypos": {
    "oneTypo": 5,
    "twoTypos": 9
  },
  "disableOnWords": [],
  "disableOnAttributes": []
}
```

### Update typo tolerance settings

<RouteHighlighter method="PATCH" />

Partially update the typo tolerance settings for an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```
{
  "enabled": <Boolean>,
  "minWordSizeForTypos": {
    "oneTypo": <Integer>,
    "twoTypos": <Integer>
  },
  "disableOnWords": [<String>, <String>, …],
  "disableOnAttributes": [<String>, <String>, …]
  "disableOnNumbers": <Boolean>,
}
```

| Name                               | Type             | Default Value | Description                                                                      |
| :--------------------------------- | :--------------- | :------------ | :------------------------------------------------------------------------------- |
| **`enabled`**                      | Boolean          | `true`        | Whether typo tolerance is enabled or not                                         |
| **`minWordSizeForTypos.oneTypo`**  | Integer          | `5`           | The minimum word size for accepting 1 typo; must be between `0` and `twoTypos`   |
| **`minWordSizeForTypos.twoTypos`** | Integer          | `9`           | The minimum word size for accepting 2 typos; must be between `oneTypo` and `255` |
| **`disableOnWords`**               | Array of strings | Empty         | An array of words for which the typo tolerance feature is disabled               |
| **`disableOnAttributes`**          | Array of strings | Empty         | An array of attributes for which the typo tolerance feature is disabled          |
| **`disableOnNumbers`**             | Boolean          | `false`       | Whether typo tolerance for numbers is disabled or enabled                        |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PATCH 'MEILISEARCH_URL/indexes/books/settings/typo-tolerance' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "minWordSizeForTypos": {
        "oneTypo": 4,
        "twoTypos": 10
      },
      "disableOnAttributes": ["title"]
    }'
  ```

  ```javascript JS theme={null}
  client.index('books').updateTypoTolerance({
    minWordSizeForTypos: {
        oneTypo: 4,
        twoTypos: 10
      },
      disableOnAttributes: [
        'title'
    ]
  })
  ```

  ```python Python theme={null}
  client.index('books').update_typo_tolerance({
    'minWordSizeForTypos': {
        'oneTypo': 4,
        'twoTypos': 10
      },
      'disableOnAttributes': [
         'title'
      ]
  })
  ```

  ```php PHP theme={null}
  $client->index('books')->updateTypoTolerance([
    'minWordSizeForTypos' => [
        'oneTypo' => 4,
        'twoTypos' => 10
      ],
      'disableOnAttributes' => [
        'title'
    ]
  ]);
  ```

  ```java Java theme={null}
  TypoTolerance typoTolerance = new TypoTolerance();
  HashMap<String, Integer> minWordSizeTypos =
          new HashMap<String, Integer>() {
              {
                  put("oneTypo", 4);
                  put("twoTypos", 10);
              }
          };

  typoTolerance.setMinWordSizeForTypos(minWordSizeTypos);
  typoTolerance.setDisableOnAttributes(new String[] {"title"});

  client.index("books").updateTypoToleranceSettings(typoTolerance);
  ```

  ```ruby Ruby theme={null}
  index('books').update_typo_tolerance({
    min_word_size_for_typos: {
      one_typo: 4,
      two_typos: 10
    },
    disable_on_attributes: ['title']
  })
  ```

  ```go Go theme={null}
  client.Index("books").UpdateTypoTolerance(&meilisearch.TypoTolerance{
    MinWordSizeForTypos: meilisearch.MinWordSizeForTypos{
        OneTypo: 4,
        TwoTypos: 10,
      },
      DisableOnAttributes: []string{"title"},
  })
  ```

  ```csharp C# theme={null}
  var typoTolerance = new TypoTolerance {
    DisableOnAttributes = new string[] { "title" },
    MinWordSizeTypos = new TypoTolerance.TypoSize {
        OneTypo = 4,
        TwoTypos = 10
    }
  };

  await client.Index("books").UpdateTypoToleranceAsync(typoTolerance);
  ```

  ```rust Rust theme={null}
  let typo_tolerance = TypoToleranceSettings {
    enabled: Some(false),
    disable_on_attributes: None,
    disable_on_words: None,
    min_word_size_for_typos: None,
  };

  let task: TaskInfo = client
    .index("books")
    .set_typo_tolerance(&typo_tolerance)
    .await
    .unwrap();
  ```

  ```dart Dart theme={null}
  final toUpdate = TypoTolerance(
    minWordSizeForTypos: MinWordSizeForTypos(
      oneTypo: 4,
      twoTypos: 10,
    ),
    disableOnAttributes: ['title'],
  );
  await client.index('books').updateTypoTolerance(toUpdate);
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "books",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2022-04-14T20:56:44.991039Z"
}
```

You can use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset typo tolerance settings

<RouteHighlighter method="DELETE" />

Reset an index's typo tolerance settings to their [default value](#typo-tolerance-object).

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/books/settings/typo-tolerance'
  ```

  ```javascript JS theme={null}
  client.index('books').resetTypoTolerance()
  ```

  ```python Python theme={null}
  client.index('books').reset_typo_tolerance()
  ```

  ```php PHP theme={null}
  $client->index('books')->resetTypoTolerance();
  ```

  ```java Java theme={null}
  client.index("books").resetTypoToleranceSettings();
  ```

  ```ruby Ruby theme={null}
  index('books').reset_typo_tolerance
  ```

  ```go Go theme={null}
  client.Index("books").ResetTypoTolerance()
  ```

  ```csharp C# theme={null}
  await client.Index("books").ResetTypoToleranceAsync();
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index("books")
    .reset_typo_tolerance()
    .await
    .unwrap();
  ```

  ```dart Dart theme={null}
  await client.index('books').resetTypoTolerance();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "books",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2022-04-14T20:53:32.863107Z"
}
```

You can use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Embedders

Embedders translate documents and queries into vector embeddings. You must configure at least one embedder to use AI-powered search.

### Embedders object

The embedders object may contain up to 256 embedder objects. Each embedder object must be assigned a unique name:

```json theme={null}
{
  "default": {
    "source": "huggingFace",
    "model": "BAAI/bge-base-en-v1.5",
    "documentTemplate": "A movie titled '{{doc.title}}' whose description starts with {{doc.overview|truncatewords: 20}}"
  },
  "openai": {
    "source": "openAi",
    "apiKey": "OPENAI_API_KEY",
    "model": "text-embedding-3-small",
    "documentTemplate": "A movie titled {{doc.title}} whose description starts with {{doc.overview|truncatewords: 20}}",
  }
}
```

These embedder objects may contain the following fields:

| Name                           | Type    | Default Value                                                                                                                                   | Description                                                                                                                                                    |
| ------------------------------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`source`**                   | String  | Empty                                                                                                                                           | The third-party tool that will generate embeddings from documents. Must be `openAi`, `huggingFace`, `ollama`, `rest`, or `userProvided`                        |
| **`url`**                      | String  | `http://localhost:11434/api/embeddings`                                                                                                         | The URL Meilisearch contacts when querying the embedder                                                                                                        |
| **`apiKey`**                   | String  | Empty                                                                                                                                           | Authentication token Meilisearch should send with each request to the embedder. If not present, Meilisearch will attempt to read it from environment variables |
| **`model`**                    | String  | Empty                                                                                                                                           | The model your embedder uses when generating vectors                                                                                                           |
| **`documentTemplate`**         | String  | `{% for field in fields %} {% if field.is_searchable and not field.value == nil %}{{ field.name }}: {{ field.value }} {% endif %} {% endfor %}` | Template defining the data Meilisearch sends to the embedder                                                                                                   |
| **`documentTemplateMaxBytes`** | Integer | `400`                                                                                                                                           | Maximum allowed size of rendered document template                                                                                                             |
| **`dimensions`**               | Integer | Empty                                                                                                                                           | Number of dimensions in the chosen model. If not supplied, Meilisearch tries to infer this value                                                               |
| **`revision`**                 | String  | Empty                                                                                                                                           | Model revision hash                                                                                                                                            |
| **`distribution`**             | Object  | Empty                                                                                                                                           | Describes the natural distribution of search results. Must contain two fields, `mean` and `sigma`, each containing a numeric value between `0` and `1`         |
| **`request`**                  | Object  | Empty                                                                                                                                           | A JSON value representing the request Meilisearch makes to the remote embedder                                                                                 |
| **`response`**                 | Object  | Empty                                                                                                                                           | A JSON value representing the response Meilisearch expects from the remote embedder                                                                            |
| **`binaryQuantized`**          | Boolean | Empty                                                                                                                                           | Once set to `true`, irreversibly converts all vector dimensions to 1-bit values                                                                                |
| **`indexingEmbedder`**         | Object  | Empty                                                                                                                                           | Configures embedder to vectorize documents during indexing                                                                                                     |
| **`searchEmbedder`**           | Object  | Empty                                                                                                                                           | Configures embedder to vectorize search queries                                                                                                                |
| **`pooling`**                  | String  | `"useModel"`                                                                                                                                    | Pooling method for Hugging Face embedders                                                                                                                      |
| **`indexingFragments`**        | Object  | Empty                                                                                                                                           | Configures multimodal embedding generation at indexing time                                                                                                    |
| **`searchFragments`**          | Object  | Empty                                                                                                                                           | Configures data handling during multimodal search                                                                                                              |

### Get embedder settings

<RouteHighlighter method="GET" />

Get the embedders configured for an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/INDEX_NAME/settings/embedders'
  ```

  ```ruby Ruby theme={null}
  client.index('INDEX_NAME').embedders
  ```

  ```rust Rust theme={null}
  let embedders = index.get_embedders().await.unwrap();
  ```
</CodeGroup>

##### Response: `200 OK`

```json theme={null}
{
  "default": {
    "source":  "openAi",
    "apiKey": "OPENAI_API_KEY",
    "model": "text-embedding-3-small",
    "documentTemplate": "A movie titled {{doc.title}} whose description starts with {{doc.overview|truncatewords: 20}}",
    "dimensions": 1536
  }
}
```

### Update embedder settings

<RouteHighlighter method="PATCH" />

Partially update the embedder settings for an index. When this setting is updated Meilisearch may reindex all documents and regenerate their embeddings.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```json theme={null}
{
  "default": {
    "source": <String>,
    "url": <String>,
    "apiKey": <String>,
    "model": <String>,
    "documentTemplate": <String>,
    "documentTemplateMaxBytes": <Integer>,
    "dimensions": <Integer>,
    "revision": <String>,
    "distribution": {
      "mean": <Float>,
      "sigma": <Float>
    },
    "request": { … },
    "response": { … },
    "headers": { … },
    "binaryQuantized": <Boolean>,
    "pooling": <String>,
    "indexingEmbedder": { … },
    "searchEmbedder": { … }
  }
}
```

Set an embedder to `null` to remove it from the embedders list.

##### `source`

Use `source` to configure an embedder's source. The source corresponds to a service that generates embeddings from your documents.

Meilisearch supports the following sources:

* `openAi`
* `huggingFace`
* `ollama`
* `rest`
* `userProvided`
* `composite` <NoticeTag type="experimental" label="experimental" />

`rest` is a generic source compatible with any embeddings provider offering a REST API.

Use `userProvided` when you want to generate embeddings manually. In this case, you must include vector data in your documents' `_vectors` field. You must also generate vectors for search queries.

This field is mandatory.

###### Composite embedders <NoticeTag type="experimental" label="experimental" />

Choose `composite` to use one embedder during indexing time, and another embedder at search time. Must be used together with [`indexingEmbedder` and `searchEmbedder`](#indexingembedder-and-searchembedder).

<Note>
  This is an experimental feature. Use the experimental features endpoint to activate it:

  ```sh theme={null}
  curl \
    -X PATCH 'MEILISEARCH_URL/experimental-features/' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "compositeEmbedders": true
    }'
  ```
</Note>

##### `url`

Meilisearch queries `url` to generate vector embeddings for queries and documents. `url` must point to a REST-compatible embedder. You may also use `url` to work with proxies, such as when targeting `openAi` from behind a proxy.

This field is mandatory when using `rest` embedders.

This field is optional when using `ollama` and `openAi` embedders. `ollama` URLs must end with either `/api/embed` or `/api/embeddings`.

This field is incompatible with `huggingFace` and `userProvided` embedders.

##### `apiKey`

Authentication token Meilisearch should send with each request to the embedder. Meilisearch redacts this value when returning embedder settings. Do not use the redacted API key when updating settings.

This field is mandatory if using a protected `rest` embedder.

This field is optional for `openAI` and `ollama` embedders. If you don't specify `apiKey` when using `openAI`, Meilisearch attempts to read it from the `OPENAI_API_KEY` environment variable.

This field is incompatible with `huggingFace` and `userProvided` embedders.

##### `model`

The model your embedder uses when generating vectors. These are the officially supported models Meilisearch supports:

* `openAi`: `text-embedding-3-small`, `text-embedding-3-large`, `openai-text-embedding-ada-002`
* `huggingFace`: `BAAI/bge-base-en-v1.5`

Other models, such as [HuggingFace's BERT models](https://huggingface.co/models?other=bert) and [ModernBERT](https://huggingface.co/models?other=modernbert), as well as some of the models provided by Ollama and REST embedders, may also be compatible with Meilisearch.

This field is mandatory for `Ollama` embedders.

This field is optional for `openAi` and `huggingFace`. By default, Meilisearch uses `text-embedding-3-small` and `BAAI/bge-base-en-v1.5` respectively.

This field is incompatible with `rest` and `userProvided` embedders.

##### `documentTemplate`

`documentTemplate` is a string containing a [Liquid template](https://shopify.github.io/liquid/basics/introduction). When using an embedding generation service such as OpenAI, Meillisearch interpolates the template for each document and sends the resulting text to the embedder. The embedder then generates document vectors based on this text. If used with a custom embedder, Meilisearch will return an error.

You may use the following context values:

* `{{doc.FIELD}}`: `doc` stands for the document itself. `FIELD` must correspond to an attribute present on all documents value will be replaced by the value of that field in the input document
* `{{fields}}`: a list of all the `field`s appearing in any document in the index. Each `field` object in this list has the following properties:
  * `name`: the field's attribute
  * `value`: the field's value
  * `is_searchable`: whether the field is present in the searchable attributes list

If a `field` does not exist in a document, its `value` is `nil`.

For best results, build short templates that only contain highly relevant data. If working with a long field, consider [truncating it](https://shopify.github.io/liquid/filters/truncatewords/). If you do not manually set it, `documentTemplate` will include all searchable and non-null document fields. This may lead to suboptimal performance and relevancy.

This field is incompatible with `userProvided` embedders.

This field is optional but strongly encouraged for all other embedders.

##### `documentTemplateMaxBytes`

The maximum size of a rendered document template. Longer texts are truncated to fit the configured limit.

`documentTemplateMaxBytes` must be an integer. It defaults to `400`.

This field is incompatible with `userProvided` embedders.

This field is optional for all other embedders.

##### `dimensions`

Number of dimensions in the chosen model. If not supplied, Meilisearch tries to infer this value.

In most cases, `dimensions` should be the exact same value of your chosen model. Setting `dimensions` to a value lower than the model may lead to performance improvements and is only supported in the following OpenAI models:

* `openAi`: `text-embedding-3-small`, `text-embedding-3-large`

This field is mandatory for `userProvided` embedders.

This field is optional for `openAi`, `huggingFace`, `ollama`, and `rest` embedders.

##### `revision`

Use this field to use a specific revision of a model.

This field is optional for the `huggingFace` embedder.

This field is incompatible with all other embedders.

##### `request`

`request` must be a JSON object with the same structure and data of the request you must send to your `rest` embedder.

The field containing the input text Meilisearch should send to the embedder must be replaced with `"{{text}}"`:

```json theme={null}
{
  "source": "rest",
  "request": {
    "prompt": "{{text}}"
    …
  },
  …
}
```

If sending multiple documents in a single request, replace the input field with `["{{text}}", "{{..}}"]`:

```json theme={null}
{
  "source": "rest",
  "request": {
    "prompt": ["{{text}}", "{{..}}"]
    …
  },
  …
}
```

This field is mandatory when using the `rest` embedder.

This field is incompatible with all other embedders.

##### `response`

`response` must be a JSON object with the same structure and data of the response you expect to receive from your `rest` embedder.

The field containing the embedding itself must be replaced with `"{{embedding}}"`:

```json theme={null}
{
  "source": "rest",
  "response": {
    "data": "{{embedding}}"
    …
  },
  …
}
```

If a single response includes multiple embeddings, the field containing the embedding itself must be an array with two items. One must declare the location and structure of a single embedding, while the second item should be `"{{..}}"`:

```json theme={null}
{
  "source": "rest",
  "response": {
    "data": [
      {
        "embedding": "{{embedding}}"
      },
      "{{..}}"
    ]
    …
  },
  …
}
```

This field is mandatory when using the `rest` embedder.

This field is incompatible with all other embedders.

##### `distribution`

For mathematical reasons, the `_rankingScore` of semantic search results tend to be closely grouped around an average value that depends on the embedder and model used. This may result in relevant semantic hits being underrepresented and irrelevant semantic hits being overrepresented compared with keyword search hits.

Use `distribution` when configuring an embedder to correct the returned `_rankingScore`s of the semantic hits with an affine transformation:

```sh theme={null}
curl \
  -X PATCH 'MEILISEARCH_URL/indexes/INDEX_NAME/settings' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "embedders": {
      "default": {
        "source":  "huggingFace",
        "model": "MODEL_NAME",
        "distribution": {
          "mean": 0.7,
          "sigma": 0.3
        }
      }
    }
  }'
```

Configuring `distribution` requires a certain amount of trial and error, in which you must perform semantic searches and monitor the results. Based on their `rankingScore`s and relevancy, add the observed `mean` and `sigma` values for that index.

`distribution` is an optional field compatible with all embedder sources. It must be an object with two fields:

* `mean`: a number between `0` and `1` indicating the semantic score of "somewhat relevant" hits before using the `distribution` setting
* `sigma`: a number between `0` and `1` indicating the average absolute difference in `_rankingScore`s between "very relevant" hits and "somewhat relevant" hits, and "somewhat relevant" hits and "irrelevant hits".

Changing `distribution` does not trigger a reindexing operation.

##### `headers`

`headers` must be a JSON object whose keys represent the name of additional headers to send in requests to embedders, and whose values represent the value of these additional headers.

By default, Meilisearch sends the following headers with all requests to `rest` embedders:

* `Authorization: Bearer EMBEDDER_API_KEY` (only if `apiKey` was provided)
* `Content-Type: application/json`

If `headers` includes one of these fields, the explicitly declared values take precedence over the defaults.

This field is optional when using the `rest` embedder.

This field is incompatible with all other embedders.

##### `binaryQuantized`

When set to `true`, compresses vectors by representing each dimension with 1-bit values. This reduces the relevancy of semantic search results, but greatly reduces database size.

This option can be useful when working with large Meilisearch projects. Consider activating it if your project contains more than one million documents and uses models with more than 1400 dimensions.

<Warning>
  **Activating `binaryQuantized` is irreversible.** Once enabled, Meilisearch converts all vectors and discards all vector data that does fit within 1-bit. The only way to recover the vectors' original values is to re-vectorize the whole index in a new embedder.
</Warning>

##### `pooling`

Configure how Meilisearch should merge individual tokens into a single embedding.

`pooling` must be one of the following strings:

* `"useModel"`: Meilisearch will fetch the pooling method from the model configuration. Default value for new embedders
* `"forceMean"`: always use mean pooling. Default value for embedders created in Meilisearch \<=v1.13
* `"forceCls"`: always use CLS pooling

If in doubt, use `"useModel"`. `"forceMean"` and `"forceCls"` are compatibility options that might be necessary for certain embedders and models.

`pooling` is optional for embedders with the `huggingFace` source.

`pooling` is invalid for all other embedder sources.

##### `indexingEmbedder` and `searchEmbedder` <NoticeTag type="experimental" label="experimental" />

When using a [composite embedder](#composite-embedders), configure separate embedders Meilisearch should use when vectorizing documents and search queries.

`indexingEmbedder` often benefits from the higher bandwidth and speed of remote providers so it can vectorize large batches of documents quickly. `searchEmbedder` may often benefits from the lower latency of processing queries locally.

Both fields must be an object and accept the same fields as a regular embedder, with the following exceptions:

* `indexingEmbedder` and `searchEmbedder` must use the same model for generating embeddings
* `indexingEmbedder` and `searchEmbedder` must have identical `dimension`s and `pooling` methods
* `source` is mandatory for both `indexingEmbedder` and `searchEmbedder`
* Neither sub-embedder can set `source` to `composite` or `userProvided`
* Neither `binaryQuantized` and `distribution` are valid sub-embedder fields and must always be declared in the main embedder
* `documentTemplate` and `documentTemplateMaxBytes` are invalid fields for `searchEmbedder`
* `documentTemplate` and `documentTemplateMaxBytes` are mandatory for `indexingEmbedder`, if applicable to its source

`indexingEmbedder` and `searchEmbedder` are mandatory when using the `composite` source.

`indexingEmbedder` and `searchEmbedder` are incompatible with all other embedder sources.

##### `indexingFragments` <NoticeTag type="experimental" label="experimental" />

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

`indexingFragments` specifies which fields in your documents should be used to generate multimodal embeddings. It must be an object with the following structure:

```json theme={null}
  "FRAGMENT_NAME": {
    "value": {
      …
    }
  }
```

`FRAGMENT_NAME` can be any valid string. It must contain a single field, `value`. `value` must then follow your chosen model's specifications.

For example, for [VoyageAI's multimodal embedding route](https://docs.voyageai.com/reference/multimodal-embeddings-api), `value` must be an object containing a `content` field. `content` itself must contain an array of objects with a `type` field. Depending on `type`'s value, you must include either `text`, `image_url`, or `image_base64`:

```json theme={null}
{
  "VOYAGE_FRAGMENT_NAME_A": {
    "value": {
      "content": [
        {
          "type": "text",
          "text": "A document called {{doc.title}} that can be described as {{doc.description}}"
        }
      ]
    }
  },
  "VOYAGE_FRAGMENT_NAME_B": {
    "value": {
      "content": [
        {
          "type": "image_url",
          "image_url": "{{doc.image_url}}"
        }
      ]
    }
  },
}
```

Use Liquid templates to interpolate document data into the fragment fields, where `doc` gives you access to all fields within a document.

<Warning>
  If a Liquid template appearing inside of a fragment cannot be rendered, no embedding will be generated for that fragment and that document. If a document has no indexing fragments, it will not be returned in multimodal searches. In most cases, a fragment is not rendered because a field it references is missing in the document.

  This is different from embeddings based on `documentTemplate`, which abort the indexing task if the document template cannot be rendered for a document.

  You can check which documents have embeddings for a given fragment using [vector filters](/learn/filtering_and_sorting/filter_expression_reference#vector-filters).
</Warning>

`indexingFragments` is optional when using the `rest` source.

`indexingFragments` is incompatible with all other embedder sources.

Specifying a `documentTemplate` in an embedder using `indexingFragments` will result in an error.

You must specify at least one valid fragment in `searchFragments` when using `indexingFragments`.

##### `searchFragments` <NoticeTag type="experimental" label="experimental" />

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

`searchFragments` instructs Meilisearch how to parse fields present in a query's [`media` search parameter](/reference/api/search#media). It must be an object following the same structure as the [`indexingFragments`](/reference/api/settings#indexingfragments) object:

```json theme={null}
  "FRAGMENT_NAME": {
    "value": {
      …
    }
  }
```

As with `indexingFragments`, the content of `value` should follow your model's specification.

Use Liquid templates to interpolate search query data into the fragment fields, where `{{media.*}}` gives you access to all [multimodal data received with a query](/reference/api/search#media) and `{{q}}` gives you access to the regular textual query:

```json theme={null}
{
  "SEARCH_FRAGMENT_A": {
    "value": {
      "content": [
        {
          "type": "image_base64",
          "image_base64": "data:{{media.image.mime}};base64,{{media.image.data}}"
        }
      ]
    }
  },
  "SEARCH_FRAGMENT_B": {
    "value": {
      "content": [
        {
          "type": "text",
          "text": "{{q}}"
        }
      ]
    }
  }
}
```

`searchFragments` is optional when using the `rest` source.

`searchFragments` is incompatible with all other embedder sources.

You must specify at least one valid fragment in `indexingFragments` when using `searchFragments`.

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PATCH 'MEILISEARCH_URL/indexes/INDEX_NAME/settings/embedders' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "default": {
        "source":  "openAi",
        "apiKey": "OPEN_AI_API_KEY",
        "model": "text-embedding-3-small",
        "documentTemplate": "A document titled '{{doc.title}}' whose description starts with {{doc.overview|truncatewords: 20}}"
      }
    }'
  ```

  ```javascript JS theme={null}
  client.index('INDEX_NAME').updateEmbedders({
    default: {
      source: 'openAi',
      apiKey: 'OPEN_AI_API_KEY',
      model: 'text-embedding-3-small',
      documentTemplate: 'A document titled '{{doc.title}}' whose description starts with {{doc.overview|truncatewords: 20}}'
    }
  });
  ```

  ```php PHP theme={null}
  $client->updateEmbedders([
    'default' => [
      'source' => 'openAi',
      'apiKey' => 'OPEN_AI_API_KEY',
      'model' => 'text-embedding-3-small',
      'documentTemplate' => 'A document titled '{{doc.title}}' whose description starts with {{doc.overview|truncatewords: 20}}'
    ]
  ]);
  ```

  ```ruby Ruby theme={null}
  client.index('INDEX_NAME').update_embedders(
    default: {
      source:  'openAi',
      api_key: 'OPEN_AI_API_KEY',
      model: 'text-embedding-3-small',
      document_template: "A document titled '{{doc.title}}' whose description starts with {{doc.overview|truncatewords: 20}}"
    }
  )
  ```

  ```rust Rust theme={null}
  let embedders = HashMap::from([(
    String::from("default"),
    Embedder {
      source: EmbedderSource::OpenAi,
      api_key: Some(String::from("OPEN_AI_API_KEY")),
      model: Some(String::from("text-embedding-3-small")),
      document_template: Some(String::from("A document titled '{{doc.title}}' whose description starts with {{doc.overview|truncatewords: 20}}")),
      ..Embedder::default()
    }
  )]);
  let task = index
    .set_embedders(&embedders)
    .await
    .unwrap();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "kitchenware",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2024-05-11T09:33:12.691402Z"
}
```

You can use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset embedder settings

<RouteHighlighter method="DELETE" />

Removes all embedders from your index.

To remove a single embedder, use the [update embedder settings endpoint](#update-embedder-settings) and set the target embedder to `null`.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/INDEX_NAME/settings/embedders'
  ```

  ```ruby Ruby theme={null}
  client.index('INDEX_NAME').reset_embedders
  ```

  ```rust Rust theme={null}
  index.reset_embedders().await.unwrap();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "books",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2022-04-14T20:53:32.863107Z"
}
```

You can use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Chat <NoticeTag type="experimental" label="experimental" />

<Note>
  This is an experimental feature. Use the Meilisearch Cloud UI or the experimental features endpoint to activate it:

  ```sh theme={null}
  curl \
    -X PATCH 'http://localhost:7700/experimental-features/' \
    -H 'Authorization: Bearer MEILISEARCH_API_KEY' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "chatCompletions": true
    }'
  ```
</Note>

The chat settings allow you to configure how your index integrates with Meilisearch's conversational search feature.

### Chat object

```json theme={null}
{
  "description": "A comprehensive movie database containing titles, overviews, genres, and release dates to help users find movies",
  "documentTemplate": "{% for field in fields %}{% if field.is_searchable and field.value != nil %}{{ field.name }}: {{ field.value }}\n{% endif %}{% endfor %}",
  "documentTemplateMaxBytes": 400,
  "searchParameters": {
    "hybrid": { "embedder": "my-embedder" },
    "limit": 20
  }
}
```

The chat object may contain the following fields:

| Name                           | Type    | Default Value                                                                                                                                   | Description                                                                                   |
| ------------------------------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **`description`**              | String  | Empty                                                                                                                                           | The description of the index. Helps the LLM decide which index to use when generating answers |
| **`documentTemplate`**         | String  | `{% for field in fields %} {% if field.is_searchable and not field.value == nil %}{{ field.name }}: {{ field.value }} {% endif %} {% endfor %}` | Template defining the data Meilisearch sends to the LLM                                       |
| **`documentTemplateMaxBytes`** | Integer | 400                                                                                                                                             | Maximum allowed size of rendered document template                                            |
| **`searchParameters`**         | Object  | Empty                                                                                                                                           | The search parameters to use when LLM is performing search requests                           |

### Search parameters object

Must be one of the following [search parameters](/reference/api/search#search-parameters-object):

* **`hybrid`**
* **`limit`**
* **`sort`**
* **`distinct`**
* **`matchingStrategy`**
* **`attributesToSearchOn`**
* **`rankingScoreThreshold`**

### Get index chat settings

<RouteHighlighter method="GET" />

Get the index chat settings configured for an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

```bash theme={null}
curl \
  -X GET 'http://localhost:7700/indexes/movies/settings/chat' \
  -H 'Authorization: Bearer MEILISEARCH_KEY'
```

##### Response: `200 OK`

```json theme={null}
{
  "description": "",
  "documentTemplate": "{% for field in fields %} {% if field.is_searchable and not field.value == nil %}{{ field.name }}: {{ field.value }} {% endif %} {% endfor %}",
  "documentTemplateMaxBytes": 400,
  "searchParameters": {}
}
```

### Update index chat settings

<RouteHighlighter method="PUT" />

Partially update the index chat settings for an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```json theme={null}
{
  "description": <String>,
  "documentTemplate": <String>,
  "documentTemplateMaxBytes": <Integer>,
  "searchParameters": {
    "hybrid": <Object>,
    "limit": <Integer>,
    "sort": [<String>, <String>, … ],
    "distinct": <String>,
    "matchingStrategy": <String>,
    "attributesToSearchOn": [<String>, <String>, … ],
    "rankingScoreThreshold": <Float>,
  }
}
```

#### Example

```bash theme={null}
curl \
  -X PATCH 'http://localhost:7700/indexes/movies/settings/chat' \
  -H 'Authorization: Bearer MEILISEARCH_KEY' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "description": "A comprehensive movie database containing titles, descriptions, genres, and release dates to help users find movies",
    "documentTemplate": "Title: {{ title }}\nDescription: {{ overview }}\nGenres: {{ genres }}\n",
    "documentTemplateMaxBytes": 400,
    "searchParameters": {
      "limit": 20
    }
  }'
```

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2024-05-11T09:33:12.691402Z"
}
```

You can use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

## Vector store <NoticeTag type="experimental" label="experimental" />

<Note>
  This is an experimental feature. On Meilisearch Cloud, contact support to activate it. On OSS, use the experimental features endpoint:

  ```sh theme={null}
  curl \
    -X PATCH 'http://localhost:7700/experimental-features/' \
    -H 'Authorization: Bearer MEILISEARCH_API_KEY' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "vectorStoreSetting": true
    }'
  ```
</Note>

Use `vectorStore` to switch between the `stable` and `experimental` vector store.

The experimental vector store may improve performance in large Meilisearch databases that make heavy use of AI-powered search features.

### Get vector store settings

<RouteHighlighter method="GET" />

Get the vector store of an index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeSamplesGetVectorStoreSettings1 />

##### Response: `200 OK`

```json theme={null}
"stable"
```

### Update vector store settings

<RouteHighlighter method="PATCH" />

Update the vector store of an index.

When switching between vector stores, Meilisearch must convert all vector data for use with the new backend. This operation may take a significant amount of time in existing indexes. If a conversion is taking too long, create a new empty index, set its store to `experimental`, and add your documents.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Body

```
"stable" | "experimental"
```

#### Example

<CodeSamplesUpdateVectorStoreSettings1 />

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "INDEX_UID",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2024-07-19T22:33:18.523881Z"
}
```

Use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).

### Reset vector store settings

<RouteHighlighter method="DELETE" />

Reset an index's vector store to its default settings.

If you had set `vectorStore` to anything other than the default value, resetting triggers a convertion operation. This operation may take a significant amount of time depending on the size of the index.

#### Path parameters

| Name               | Type   | Description                                                              |
| :----------------- | :----- | :----------------------------------------------------------------------- |
| **`index_uid`** \* | String | [`uid`](/learn/getting_started/indexes#index-uid) of the requested index |

#### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X DELETE 'MEILISEARCH_URL/indexes/INDEX_UID/settings/facet-search'
  ```

  ```javascript JS theme={null}
  client.index('INDEX_NAME').resetFacetSearch();
  ```

  ```python Python theme={null}
  client.index('books').reset_facet_search_settings()
  ```

  ```php PHP theme={null}
  $client->index('INDEX_NAME')->resetFacetSearch();
  ```

  ```ruby Ruby theme={null}
  client.index('INDEX_UID').reset_facet_search_setting
  ```

  ```go Go theme={null}
  client.Index("books").ResetFacetSearch()
  ```

  ```rust Rust theme={null}
  let task: TaskInfo = client
    .index(INDEX_UID)
    .reset_facet_search()
    .await
    .unwrap();
  ```
</CodeGroup>

##### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "INDEX_UID",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2024-07-19T22:35:33.723983Z"
}
```

Use the returned `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task).