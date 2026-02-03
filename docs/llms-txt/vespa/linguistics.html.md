# Source: https://docs.vespa.ai/en/linguistics/linguistics.html.md

# Linguistics in Vespa

 

Vespa uses a _linguistics_ module to process text in queries and documents during indexing and searching. The goal of linguistic processing is to increase _recall_ (how many documents are matched) without hurting _precision_ (the relevance of the documents matched) too much. It consists of such operations as:

- tokenizing text into chunks of known types such as words and punctuation.
- normalizing accents.
- finding the base form of words (stemming or lemmatization).

Linguistic processing is run when writing documents, and when querying:

 ![Overview: linguistic processing in Vespa](/assets/img/vespa-overview-linguistics.svg)

The processing is run on [string](../reference/schemas/schemas.html#string) fields with `index` indexing mode. Overview:

1. When writing documents, string fields with `indexing: index` are by default processed. A field's language will configure this processing. A document/fields can have the language set explicitly, if not, it is [detected](#field-language-detection). 
2. The field's content is processed (e.g., tokenized, normalized, stemmed, etc.), and the resulting terms are added to the index. 
 **Note:** The language for the field is not persisted on the content node, just the processed terms themselves
3. A query is also processed in a similar fashion. Typically through the same [linguistics profile](../reference/schemas/schemas.html#linguistics) as the field content, producing the same terms from the same text. The language of query strings is [detected](#query-language-detection) unless specified using [model.locale](../reference/api/query.html#model.locale) or [annotations](../reference/querying/yql.html#annotations) like `language`. 
 **Note:** This is a very common query problem - it is hard to detect language precisely from short strings.
4. The processed query is evaluated on the content nodes, and will only work as expected if both documents and queries produce the same terms. 

These operations can be turned on or off per field in the [schema](../basics/schemas.html). See [implicitTransforms](../reference/querying/yql.html#implicittransforms) for how to enable/disable transforms per query term.

## Linguistics implementations

Vespa comes with two linguistics variants out of the box: [OpenNLP](linguistics-opennlp.html) and [Lucene](lucene-linguistics.html). Check out the respective pages for more information on how to configure them.

You can also implement a custom [Linguistics](linguistics-custom.html) component.

The default linguistics variant is [OpenNLP](linguistics-opennlp.html), but for the rest of this page we'll go through common options, such as language handling, inherited by all implementations.

## Language handling

Vespa does _not_ know the language of a document - this applies:

1. The indexing processor is instructed on a per-field level what language to use when calling the underlying linguistics library
2. The query processor is instructed on a per-query level what language to use

If no language is explicitly set in a document or a query, Vespa will run its configured language detector (by default, [OpenNLP language detection](linguistics-opennlp.html#language-detection)) on the available text (the full content of a document field, or the full `query=` parameter value).

A document that contains the exact same word as a query might not be recall-able if the language of the document field is detected differently from the query. Unless the query has explicitly declared a [language](../reference/api/query.html#model.language), this can occur.

### Indexing with language

The indexing process run by Vespa is a sequential execution of the indexing scripts of each field in the schema, in the declared order. At any point, the script may set the language that will be used for indexing statements for subsequent fields, using [set\_language](../reference/writing/indexing-language.html#set_language). Example:

```
schema doc {
    document doc {
        field language type string {
            indexing: set_language
        }
        field title type string {
            indexing: index
        }
    }
}
```

If a language has not been set when tokenization of a field is run, the language is determined by[language detection](#field-language-detection).

If all documents have the same language, the language can be hardcoded it the schema in this way:

```
schema doc {

    field language type string {
        indexing: "en" | set_language
    }

    document doc {
    ...
```

If the same document contains fields in multiple languages, set\_language can be invoked multiple times, e.g.:

```
schema doc {
    document doc {
        field language_title1 type string {
            indexing: set_language
        }
        field title1 type string {
            indexing: index
        }
        field language_title2 type string {
            indexing: set_language
        }
        field title2 type string {
            indexing: index
        }
    }
}
```

Or, if fixed per field, use multiple indexing statements in each field:

```
schema doc {
    document doc {
        field my_english_field type string {
            indexing {
                "en" | set_language;
                index;
            }
        }
        field my_spanish_field type string {
            indexing {
                "es" | set_language;
                index;
            }
        }
    }
}
```

### Field language detection

When indexing a document, if a field has unknown language (i.e. not set using `set_language`), language detection is run on the field's content. This means, language detection is per field, not per document.

See [query language detection](#query-language-detection) for detection confidence, fields with little text will default to English.

### Querying with language

The content of an indexed string field is language-agnostic. One must therefore apply a compatible tokenization on the query terms (e.g., stemming for the same language) in order to match the content of that field.

The query parser subscribes to configuration that tells it what fields are indexed strings, and every query term that targets such a field are run through appropriate tokenization. The [language](../reference/api/query.html#model.language) query parameter controls the language state of these calls.

Because an index may simultaneously contain terms in any number of languages, one can have stemmed variants of one language match the stemmed variants of another. To work around this, store the language of a document in a separate attribute, and apply a filter against that attribute at query-time.

By default, there is no knowledge anywhere that captures what languages are used to generate the content of an index. The language parameter only affects the transformation of query terms that hit tokenized indexes.

### Query language detection

If no [language](../reference/api/query.html#model.language) parameter is used, or the query terms are [annotated](../reference/querying/yql.html#annotations), the language detector is called to process the query string.

Queries are normally short, as a consequence, the detection confidence is low. Example:

```
$ vespa query "select * from music where userInput(@text)" \
  tracelevel=3 text='Eine kleine Nachtmusik' | grep 'Stemming with language'
    "message": "Stemming with language=ENGLISH"

$ vespa query "select * from music where userInput(@text)" \
  tracelevel=3 text='Eine kleine Nachtmusik schnell' | grep 'Stemming with language'
    "message": "Stemming with language=GERMAN"
```

See [#24265](https://github.com/vespa-engine/vespa/issues/24265) for details - in short, with the current 0.02 confidence cutoff, queries with 3 terms or fewer will default to English.

### Multiple languages

Vespa supports having documents in multiple languages in the same schema, but does not out-of-the-box support cross-lingual retrieval (e.g., search using English and retrieve relevant documents written in German). This is because the language of a query is determined by the language of the query string and only one transformation can take place.

Approaches to overcome this limitation include:

1. Use semantic retrieval using a multilingual text embedding model (see [blog post](https://blog.vespa.ai/simplify-search-with-multilingual-embeddings/)) which has been trained on multilingual corpus and can be used to retrieve documents in multiple languages. 
2. Stem and tokenize the query using the relevant languages, build a query tree using [weakAnd](../reference/querying/yql.html#weakand) / [or](../reference/querying/yql.html#or) and using [equiv](../reference/querying/yql.html#equiv) per stem variant. This is easiest done in a custom [Searcher](../applications/searchers.html) as mentioned in [#12154](https://github.com/vespa-engine/vespa/issues/12154). 

Example:

**language=fr:** machine learning =\> machin learn

**language=en:** machine learning =\> machine learn

Using _weakAnd_ here as example as that technique is already mentioned in #12154:

```
select * from sources * where rank( 
    default contains "machine", 
    default contains "learning",
    weakAnd(
      default contains equiv("machin", "machine"), 
      default contains "learn"
    )
)
```

We now retrieve using all possible stems/base forms with _weakAnd_, and use the [rank](../reference/querying/yql.html#rank) operator to pass in the original query form, so that ranking can rank literal matches (original) higher. Benefit of _equiv_ is that it allows multiple term variants to share the same position, so that proximity ranking does not become broken by this approach.

## Linguistics profiles

Linguistics profiles are used to configure linguistics processing for a field in the schema. They are typically used with the [Lucene linguistics implementation](lucene-linguistics.html), but can be used in e.g., [custom linguistics implementations](linguistics-custom.html) as well.

### Symmetrical processing

For example, a definition like this:

```
field title type string {
  indexing: summary | index
  linguistics {
      profile: whitespaceLowercase
  }
}
```

Will look for a profile named `whitespaceLowercase`, which could be defined like this in `services.xml`:

```
```
<item key="profile=whitespaceLowercase;language=en">
    <tokenizer>
      <name>whitespace</name>
    </tokenizer>
    <tokenFilters>
      <item>
        <name>lowercase</name>
      </item>
    </tokenFilters>
  </item>
```
```

Note `language=en` there. It is optional: if it's not set, the profile will be used for all languages. But you can have different definitions for different languages on the same profile (e.g., different stemming).

### Different processing for query strings

For some use cases, you may want to process the query string differently than the document content. Synonyms are a good example. If you expand `dog` to `dog,puppy` at query time, it will match either term in the document anyway - no need to expand it at write-time.

To do this, you'd define a different profile for the query string. Like:

```
```
<item key="profile=whitespaceLowercaseSynonyms;language=en">
    <tokenizer>
      <name>whitespace</name>
    </tokenizer>
    <tokenFilters>
      <item>
        <name>lowercase</name>
      </item>
      <item>
        <name>synonymGraph</name>
        <conf>
          <!--
            Synonyms file should contain something like:
            dog,puppy
          -->
          <item key="synonyms">en/synonyms.txt</item>
        </conf>
      </item>
    </tokenFilters>
  </item>
```
```

Then, in the schema, expand `profile` to `profile.index` and `profile.search`:

```
field title type string {
    indexing: summary | index
    linguistics {
        profile {
            index: whitespaceLowercase
            search: whitespaceLowercaseSynonyms
        }
    }
}
```

At this point, `where synonyms_test contains 'dog'` will match a document containing `puppy`.

### Overriding profile for query strings

At query time, you can force Vespa to use a specific profile to process the query string via [grammar.profile](../reference/querying/yql.html#grammar). This works with [userInput()](../reference/querying/yql.html#userinput). For example, to use the `whitespaceLowercase` profile for the query string:

```
where {defaultIndex:'title', grammar.profile: 'whitespaceLowercase', grammar: 'linguistics'}userInput('dog')
```

 **Note:** You should use grammar=linguistics (like in the example above) with grammar.profile to ensure that there is no additional processing (e.g., tokenization) besides what is already defined in the profile.

## Troubleshooting linguistics processing

If your documents don't match as expected, there are two ways to get more information. First, you can get the tokenized text for a field by using [tokens](../reference/schemas/schemas.html#tokens) in the [document summary](../querying/document-summaries.html). For example, to get the original text and tokens for the `title` field:

```
document-summary debug-text-tokens {
    summary title {}
    summary title_tokens {
        source: title
        tokens
    }
    from-disk
}
```

Then, at query time, you can also get the tokens of the query string by increasing the [trace level](../reference/api/query.html#trace.level):

```
```
{
  "yql": "select * from sources * where title contains \"dog\"",
  "presentation.summary": "debug-text-tokens",
  "model.locale": "en",
  "trace.level": 2
}
```
```

 Copyright © 2026 - [Cookie Preferences](#)

### On this page:

- [Linguistics implementations](#linguistics-implementations)
- [Language handling](#language-handling)
- [Indexing with language](#indexing-with-language)
- [Field language detection](#field-language-detection)
- [Querying with language](#querying-with-language)
- [Query language detection](#query-language-detection)
- [Multiple languages](#multiple-languages)
- [Linguistics profiles](#linguistics-profiles)
- [Symmetrical processing](#symmetrical-processing)
- [Different processing for query strings](#different-processing-for-query-strings)
- [Overriding profile for query strings](#overriding-profile-for-query-strings)
- [Troubleshooting linguistics processing](#troubleshooting-linguistics-processing)

