# Synonyms
Source: https://www.meilisearch.com/docs/learn/relevancy/synonyms

Use Meilisearch synonyms to indicate sets of query terms which should be considered equivalent during search.

If multiple words have an equivalent meaning in your dataset, you can [create a list of synonyms](/reference/api/settings#update-synonyms). This will make your search results more relevant.

Words set as synonyms won't always return the same results. With the default settings, the `movies` dataset should return 547 results for `great` and 66 for `fantastic`. Let's set them as synonyms:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/movies/settings/synonyms' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "great": ["fantastic"], "fantastic": ["great"]
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').updateSynonyms({
    'great': ['fantastic'],
    'fantastic': ['great']
  })
  ```

  ```python Python theme={null}
  client.index('movies').update_synonyms({
    'great': ['fantastic'],
    'fantastic': ['great']
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->updateSynonyms([
    'great' => ['fantastic'],
    'fantastic' => ['great'],
  ]);
  ```

  ```java Java theme={null}
  HashMap<String, String[]> synonyms = new HashMap<String, String[]>();
  synonyms.put("great", new String[] {"fantastic"});
  synonyms.put("fantastic", new String[] {"great"});

  client.index("movies").updateSynonymsSettings(synonyms);
  ```

  ```ruby Ruby theme={null}
  client.index('movies').update_synonyms({
    great: ['fantastic'],
    fantastic: ['great']
  })
  ```

  ```go Go theme={null}
  synonyms := map[string][]string{
    "great":      []string{"fantastic"},
    "fantastic":  []string{"great"},
  }
  client.Index("movies").UpdateSynonyms(&synonyms)
  ```

  ```csharp C# theme={null}
  var synonyms = new Dictionary<string, IEnumerable<string>>
  {
      { "great", new string[] { "fantastic" } },
      { "fantastic", new string[] { "great" } }
  };
  await client.Index("movies").UpdateSynonymsAsync(synonyms);
  ```

  ```rust Rust theme={null}
  let mut synonyms = std::collections::HashMap::new();
  synonyms.insert(String::from("great"), vec![String::from("fantastic")]);
  synonyms.insert(String::from("fantastic"), vec![String::from("great")]);

  let task: TaskInfo = client
    .index("movies")
    .set_synonyms(&synonyms)
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let synonyms: [String: [String]] = [
    "great": ["fantastic"],
    "fantastic": ["great"]
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
    'great': ['fantastic'],
    'fantastic': ['great'],
  });
  ```
</CodeGroup>

With the new settings, searching for `great` returns 595 results and `fantastic` returns 423 results. This is due to various factors like [typos](/learn/relevancy/typo_tolerance_settings#minwordsizefortypos) and [splitting the query](/learn/engine/concat#split-queries) to find relevant documents. The search for `great` will allow only one typo (for example, `create`) and take into account all variations of `great` (for instance, `greatest`) along with `fantastic`.

<Warning>
  The number of search results may vary depending on changes to the `movies` dataset.
</Warning>

## Normalization

All synonyms are **lowercased** and **de-unicoded** during the indexing process.

### Example

Consider a situation where `Résumé` and `CV` are set as synonyms.

```json theme={null}
{
  "Résumé": [
    "CV"
  ],
  "CV": [
    "Résumé"
  ]
}
```

A search for `cv` would return any documents containing `cv` or `CV`, in addition to any that contain `Résumé`, `resumé`, `resume`, etc., unaffected by case or accent marks.

## One-way association

Use this when you want one word to be synonymous with another, but not the other way around.

```
phone => iphone
```

A search for `phone` will return documents containing `iphone` as if they contained the word `phone`.

However, if you search for `iphone`, documents containing `phone` will be ranked lower in the results due to [the typo rule](/learn/relevancy/ranking_rules).

### Example

To create a one-way synonym list, this is the JSON syntax that should be [added to the settings](/reference/api/settings#update-synonyms).

```json theme={null}
{
  "phone": [
    "iphone"
  ]
}
```

## Relevancy

**The exact search query will always take precedence over its synonyms.** The `exactness` ranking rule favors exact words over synonyms when ranking search results.

Taking the following set of search results:

```json theme={null}
[
  {
    "id": 0,
    "title": "Ghouls 'n Ghosts"
  },
  {
    "id": 1,
    "title": "Phoenix Wright: Spirit of Justice"
  }
]
```

If you configure `ghost` as a synonym of `spirit`, queries searching for `spirit` will return document `1` before document `0`.

## Mutual association

By associating one or more synonyms with each other, they will be considered the same in both directions.

```
shoe <=> boot <=> slipper <=> sneakers
```

When a search is done with one of these words, all synonyms will be considered as the same word and will appear in the search results.

### Example

To create a mutual association between four words, this is the JSON syntax that should be [added to the settings](/reference/api/settings#update-synonyms).

```json theme={null}
{
  "shoe": [
    "boot",
    "slipper",
    "sneakers"
  ],
  "boot": [
    "shoe",
    "slipper",
    "sneakers"
  ],
  "slipper": [
    "shoe",
    "boot",
    "sneakers"
  ],
  "sneakers": [
    "shoe",
    "boot",
    "slipper"
  ]
}
```

## Multi-word synonyms

Meilisearch treats multi-word synonyms as [phrases](/reference/api/search#phrase-search).

### Example

Suppose you set `San Francisco` and `SF` as synonyms with a [mutual association](#mutual-association)

```json theme={null}
{
  "san francisco": [
    "sf"
  ],
  "sf": [
    "san francisco"
  ]
}
```

If you input `SF` as a search query, Meilisearch will also return results containing the phrase `San Francisco`. However, depending on the ranking rules, they might be considered less [relevant](/learn/relevancy/relevancy) than those containing `SF`. The reverse is also true: if your query is `San Francisco`, documents containing `San Francisco` may rank higher than those containing `SF`.

## Maximum number of synonyms per term

A single term may have up to 50 synonyms. Meilisearch silently ignores any synonyms beyond this limit. For example, if you configure 51 synonyms for `book`, Meilisearch will only return results containing the term itself and the first 50 synonyms.

If any synonyms for a term contain more than one word, the sum of all words across all synonyms for that term cannot exceed 100 words. Meilisearch silently ignores any synonyms beyond this limit. For example, if you configure 40 synonyms for `computer` in your application, taken together these synonyms must contain fewer than 100 words.