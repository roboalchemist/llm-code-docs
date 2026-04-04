# Typo tolerance settings
Source: https://www.meilisearch.com/docs/learn/relevancy/typo_tolerance_settings

This article describes each of the typo tolerance settings.

Typo tolerance helps users find relevant results even when their search queries contain spelling mistakes or typos, for example, typing `phnoe` instead of `phone`. You can [configure the typo tolerance feature for each index](/reference/api/settings#update-typo-tolerance-settings).

## `enabled`

Typo tolerance is enabled by default, but you can disable it if needed:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PATCH 'MEILISEARCH_URL/indexes/movies/settings/typo-tolerance' \
    -H 'Content-Type: application/json' \
    --data-binary '{ "enabled": false }'
  ```

  ```javascript JS theme={null}
  client.index('movies').updateTypoTolerance({
    enabled: false
  })
  ```

  ```python Python theme={null}
  client.index('movies').update_typo_tolerance({
    'enabled': False
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->updateTypoTolerance([
    'enabled' => false
  ]);
  ```

  ```java Java theme={null}
  TypoTolerance typoTolerance = new TypoTolerance();
  typoTolerance.setEnabled(false);
  client.index("movies").updateTypoToleranceSettings(typoTolerance);
  ```

  ```ruby Ruby theme={null}
  index('books').update_typo_tolerance({ enabled: false })
  ```

  ```go Go theme={null}
  client.Index("movies").UpdateTypoTolerance(&meilisearch.TypoTolerance{
    Enabled: false,
  })
  ```

  ```csharp C# theme={null}
  var typoTolerance = new TypoTolerance {
    Enabled = false
  };
  await client.Index("movies").UpdateTypoToleranceAsync(typoTolerance);
  ```

  ```rust Rust theme={null}
  let typo_tolerance = TypoToleranceSettings {
    enabled: Some(false),
    disable_on_attributes: None,
    disable_on_words: None,
    min_word_size_for_typos: None,
  };

  let task: TaskInfo = client
    .index("movies")
    .set_typo_tolerance(&typo_tolerance)
    .await
    .unwrap();
  ```

  ```dart Dart theme={null}
  final toUpdate = TypoTolerance(enabled: false);
  await client.index('movies').updateTypoTolerance(toUpdate);
  ```
</CodeGroup>

With typo tolerance disabled, Meilisearch no longer considers words that are a few characters off from your query terms as matches. For example, a query for `phnoe` will no longer return a document containing the word `phone`.

**In most cases, keeping typo tolerance enabled results in a better search experience.** Massive or multilingual datasets may be exceptions, as typo tolerance can cause false-positive matches in these cases.

## `minWordSizeForTypos`

By default, Meilisearch accepts one typo for query terms containing five or more characters, and up to two typos if the term is at least nine characters long.

If your dataset contains `seven`, searching for `sevem` or `sevan` will match `seven`. But `tow` won't match `two` as it's less than `5` characters.

You can override these default settings using the `minWordSizeForTypos` object. The code sample below sets the minimum word size for one typo to `4` and the minimum word size for two typos to `10`.

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PATCH 'MEILISEARCH_URL/indexes/movies/settings/typo-tolerance' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "minWordSizeForTypos": {
        "oneTypo": 4,
        "twoTypos": 10
      }
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').updateTypoTolerance({
    minWordSizeForTypos: {
      oneTypo: 4,
      twoTypos: 10
    }
  })
  ```

  ```python Python theme={null}
  client.index('movies').update_typo_tolerance({
    'minWordSizeForTypos': {
      'oneTypo': 4,
      'twoTypos': 10
    }
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->updateTypoTolerance([
    'minWordSizeForTypos' => [
      'oneTypo' => 4,
      'twoTypos' => 10
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
  client.index("movies").updateTypoToleranceSettings(typoTolerance);
  ```

  ```ruby Ruby theme={null}
  index('books').update_typo_tolerance({
    min_word_size_for_typos: {
      one_typo: 4,
      two_typos: 10
    }
  })
  ```

  ```go Go theme={null}
  client.Index("movies").UpdateTypoTolerance(&meilisearch.TypoTolerance{
    MinWordSizeForTypos: meilisearch.MinWordSizeForTypos{
      OneTypo: 4,
      TwoTypos: 10,
    },
  })
  ```

  ```csharp C# theme={null}
  var typoTolerance = new TypoTolerance {
    MinWordSizeTypos = new TypoTolerance.TypoSize {
      OneTypo = 4,
      TwoTypos = 10
    }
  };

  await client.Index("movies").UpdateTypoToleranceAsync(typoTolerance);
  ```

  ```rust Rust theme={null}
  let min_word_size_for_typos = MinWordSizeForTypos {
    one_typo: Some(4),
    two_typos: Some(12)
  };
  let typo_tolerance = TypoToleranceSettings {
    enabled: Some(true),
    disable_on_attributes: Some(vec![]),
    disable_on_words: Some(vec!["title".to_string()]),
    min_word_size_for_typos: Some(min_word_size_for_typos),
  };

  let task: TaskInfo = client
    .index("movies")
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
  );
  await client.index('movies').updateTypoTolerance(toUpdate);
  ```
</CodeGroup>

When updating the `minWordSizeForTypos` object, keep in mind that:

* `oneTypo` must be greater than or equal to 0 and less than or equal to `twoTypos`
* `twoTypos` must be greater than or equal to `oneTypo` and less than or equal to `255`

To put it another way: `0 ≤ oneTypo ≤ twoTypos ≤ 255`.

We recommend keeping the value of `oneTypo` between `2` and `8` and the value of `twoTypos` between `4` and `14`. If either value is too low, you may get a large number of false-positive results. On the other hand, if both values are set too high, many search queries may not benefit from typo tolerance.

<Tip>
  **Typo on the first character**\
  Meilisearch considers a typo on a query's first character as two typos.

  **Concatenation**\
  When considering possible candidates for typo tolerance, Meilisearch will concatenate multiple search terms separated by a [space separator](/learn/engine/datatypes#string). This is treated as one typo. For example, a search for `any way` would match documents containing `anyway`.

  For more about typo calculations, [see below](/learn/relevancy/typo_tolerance_calculations).
</Tip>

## `disableOnWords`

You can disable typo tolerance for a list of query terms by adding them to `disableOnWords`. `disableOnWords` is case insensitive.

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PATCH 'MEILISEARCH_URL/indexes/movies/settings/typo-tolerance' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "disableOnWords": [
        "shrek"
      ]
    }'
  ```

  ```javascript JS theme={null}
  client.index('movies').updateTypoTolerance({
    disableOnWords: ['shrek']
  })
  ```

  ```python Python theme={null}
  client.index('movies').update_typo_tolerance({
    'disableOnWords': ['shrek']
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->updateTypoTolerance([
    'disableOnWords' => ['shrek']
  ]);
  ```

  ```java Java theme={null}
  TypoTolerance typoTolerance = new TypoTolerance();
  typoTolerance.setDisableOnWords(new String[] {"shrek"});
  client.index("movies").updateTypoToleranceSettings(typoTolerance);
  ```

  ```ruby Ruby theme={null}
  index('books').update_typo_tolerance({ disable_on_words: ['shrek'] })
  ```

  ```go Go theme={null}
  client.Index("movies").UpdateTypoTolerance(&meilisearch.TypoTolerance{
    DisableOnWords: []string{"shrek"},
  })
  ```

  ```csharp C# theme={null}
  var typoTolerance = new TypoTolerance {
    DisableOnWords = new string[] { "shrek" }
  };
  await client.Index("movies").UpdateTypoToleranceAsync(typoTolerance);
  ```

  ```rust Rust theme={null}
  let min_word_size_for_typos = MinWordSizeForTypos {
    one_typo: Some(5),
    two_typos: Some(12)
  }
  let typo_tolerance = TypoToleranceSettings {
    enabled: Some(true),
    disable_on_attributes: None,
    disable_on_words: Some(vec!["shrek".to_string()]),
    min_word_size_for_typos: Some(min_word_size_for_typos),
  };

  let task: TaskInfo = client
    .index("movies")
    .set_typo_tolerance(&typo_tolerance)
    .await
    .unwrap();
  ```

  ```dart Dart theme={null}
  final toUpdate = TypoTolerance(
    disableOnWords: ['shrek'],
  );
  await client.index('movies').updateTypoTolerance(toUpdate);
  ```
</CodeGroup>

Meilisearch won't apply typo tolerance on the query term `Shrek` or `shrek` at search time to match documents.

## `disableOnAttributes`

You can disable typo tolerance for a specific [document attribute](/learn/getting_started/documents) by adding it to `disableOnAttributes`. The code sample below disables typo tolerance for `title`:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PATCH 'MEILISEARCH_URL/indexes/movies/settings/typo-tolerance' \
    -H 'Content-Type: application/json' \
    --data-binary '{ "disableOnAttributes": ["title"] }'
  ```

  ```javascript JS theme={null}
  client.index('movies').updateTypoTolerance({
    disableOnAttributes: ['title']
  })
  ```

  ```python Python theme={null}
  client.index('movies').update_typo_tolerance({
    'disableOnAttributes': ['title']
  })
  ```

  ```php PHP theme={null}
  $client->index('movies')->updateTypoTolerance([
    'disableOnAttributes' => ['title']
  ]);
  ```

  ```java Java theme={null}
  TypoTolerance typoTolerance = new TypoTolerance();
  typoTolerance.setDisableOnAttributes(new String[] {"title"});
  client.index("movies").updateTypoToleranceSettings(typoTolerance);
  ```

  ```ruby Ruby theme={null}
  index('books').update_typo_tolerance({ disable_on_attributes: ['title'] })
  ```

  ```go Go theme={null}
  client.Index("movies").UpdateTypoTolerance(&meilisearch.TypoTolerance{
    DisableOnAttributes: []string{"title"},
  })
  ```

  ```csharp C# theme={null}
  var typoTolerance = new TypoTolerance {
    DisableOnAttributes = new string[] { "title" }
  };
  await client.Index("movies").UpdateTypoToleranceAsync(typoTolerance);
  ```

  ```rust Rust theme={null}
  let min_word_size_for_typos = MinWordSizeForTypos {
    one_typo: Some(5),
    two_typos: Some(12)
  }
  let typo_tolerance = TypoToleranceSettings {
    enabled: Some(true),
    disable_on_attributes: Some(vec!["title".to_string()]),
    disable_on_words: None,
    min_word_size_for_typos: None,
  };
  let task: TaskInfo = client
    .index("movies")
    .set_typo_tolerance(&typo_tolerance)
    .await
    .unwrap();
  ```

  ```dart Dart theme={null}
  final toUpdate = TypoTolerance(
    disableOnAttributes: ['title'],
  );
  await client.index('movies').updateTypoTolerance(toUpdate);
  ```
</CodeGroup>

With the above settings, matches in the `title` attribute will not tolerate any typos. For example, a search for `beautiful` (9 characters) will not match the movie "Biutiful" starring Javier Bardem. With the default settings, this would be a match.

## `disableOnNumbers`

You can disable typo tolerance for all numeric values across all indexes and search requests by setting `disableOnNumbers` to `true`:

<CodeSamplesTypoToleranceGuide5 />

By default, typo tolerance on numerical values is turned on. This may lead to false positives, such as a search for `2024` matching documents containing `2025` or `2004`.

When `disableOnNumbers` is set to `true`, queries with numbers only return exact matches. Besides reducing the number of false positives, disabling typo tolerance on numbers may also improve indexing performance.