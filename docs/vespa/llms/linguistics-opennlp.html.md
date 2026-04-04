# Source: https://docs.vespa.ai/en/linguistics/linguistics-opennlp.html.md

# OpenNLP Linguistics

 

The default Vespa linguistics implementation uses [OpenNLP](https://opennlp.apache.org/). The Apache OpenNLP language detection is also used, by default, even if you're using a different implementation. See [Language handling](linguistics.html#language-handling) for more information. OpenNLP has support for 103 languages.

## OpenNLP language detection

The OpenNLP language detector gives a prediction with a confidence; with confidence typically increasing with more input. The threshold for using the prediction can be configured with a number typically from 1.0 (wild guess) to 6.0 (confident guess), with 2.0 as the default:

```
<container id="..." version="1.0">
    ...
    <config name="ai.vespa.opennlp.open-nlp">
      <detectConfidenceThreshold>4.2</detectConfidenceThreshold>
    </config>
```

## Default languages

OpenNLP tokenization and stemming supports these languages:

- Arabic (ar)
- Catalan (ca)
- Danish (da)
- Dutch (nl)
- English (en)
- Finnish (fi)
- French (fr)
- German (de)
- Greek (el)
- Hungarian (hu)
- Indonesian (id)
- Irish (ga)
- Italian (it)
- Norwegian (no)
- Portuguese (pt)
- Romanian (ro)
- Russian (ru)
- Spanish (es)
- Swedish (sv)
- Turkish (tr)

Other languages will use a fallback to English _en_.

English uses a simpler stemmer (kStem) by default, which produces fewer stems and therefore lower recall. To use OpenNlp stemming (Snowball) also for English add this config to your \<container\> element(s):

```
<container id="..." version="1.0">
    ...
    <config name="ai.vespa.opennlp.open-nlp">
      <snowballStemmingForEnglish>true</snowballStemmingForEnglish>
    </config>
```

See _Tokens_ [OpenNLP models](https://opennlp.apache.org/models.html) and [text matching](../querying/text-matching.html) for examples and how to experiment with linguistics.

If you need support for more languages, you can consider replacing the default OpenNLP based linguistic integration with the [Lucene Linguistics](lucene-linguistics.html) implementation which supports more languages.

### Chinese

The default linguistics implementation does not segment Chinese into tokens, but this can be turned on by config:

```
<container id="..." version="1.0">
    ...
    <config name="ai.vespa.opennlp.open-nlp">
      <cjk>true</cjk>
      <createCjkGrams>true</createCjkGrams>
    </config>
```

The createCjkGrams adds substrings of segments longer than 2 characters, which may increase recall.

## Tokenization

Tokenization removes any non-word characters, and splits the string into _tokens_ on each word boundary. In addition, CJK tokens are split using a _segmentation_ algorithm. The resulting tokens are then searchable in the index.

Also see [N-gram matching](../reference/schemas/schemas.html#gram).

## Normalization

An example normalization is à ⇒ a. Normalizing will cause accents and similar decorations which are often misspelled to be normalized the same way both in documents and queries.

Vespa uses [java.text.Normalizer](https://docs.oracle.com/javase/7/docs/api/java/text/Normalizer.html)to normalize text, see[SimpleTransformer.java](https://github.com/vespa-engine/vespa/blob/master/linguistics/src/main/java/com/yahoo/language/simple/SimpleTransformer.java). Normalization preserves case.

Refer to the [nfkc](../reference/querying/yql.html#nfkc) query term annotation. Also see the YQL [accentDrop](../reference/querying/yql.html#accentdrop) annotation.

## Stemming

Stemming means _translate a word to its base form_(singular forms for nouns, infinitive for verbs), using a [stemmer](https://en.wikipedia.org/wiki/Stemming). Use of stemming increases search recall, because the searcher is usually interested in documents containing query words regardless of the word form used. Stemming in Vespa is symmetric, i.e. words are converted to stems both when indexing and searching.

Examples of this is when text is indexed, the stemmer will convert the noun _reports_ (plural) to _report_, and the latter will be stored in the index. Likewise, before searching, _reports_ will be stemmed to _report_. Another example is that _am_, _are_ and _was_will be stemmed to _be_ both in queries and indexes.

When [bolding](../reference/schemas/schemas.html#bolding) is enabled, all forms of the query term will be bolded. I.e. when searching for _reports_, both _report_, _reported_ and _reports_ will be bolded.

See the [stem](../reference/querying/yql.html#stem) query term annotation.

### Theory

From a matching point of view, stemming takes all possible token strings and maps them into equivalence classes. So in the example above, the set of tokens { _report_, _reports_, _reported_ } are in an equivalence class. To represent the class, the linguistics library should pick the best element in the class. At query time, the text typed by a user will be tokenized, and then each token should be mapped to the most likely equivalence class, again represented by the shortest element that belongs to the class.

While the theory sounds pretty simple, in practice it is not always possible to figure out which equivalence class a token should belong to. A typical example is the string _number_. In most cases we would guess this to mean a numerical entity of some kind, and the equivalence class would be { _number_, _numbers_ } - but it could also be a verb, with a different equivalence class { _number_, _numbered_, _numbering_ }. These are of course closely related, and in practice they will be merged, so we'll have a slightly larger equivalence class { _number_, _numbers_, _numbered_, _numbering_ } and be happy with that. However, in a sentence such as _my legs keep getting number every day_, the _number_ token clearly does not have the semantics of a numerical entity, but should be in the equivalence class { _numb_, _number_, _numbest_, _numbness_ } instead. But blindly assigning _number_ to the equivalence class _numb_ is clearly not right, since the _more numb_ meaning is much less likely than the _numerical entity_ meaning.

The approach currently taken by the low-level linguistics library will often lead to problems in the _number_-like cases as described above. To give better recall, Vespa has implemented a _multiple_ stemming option.

### Configuration

By default, all words are stemmed to their _best_ form. Refer to the [stemming reference](../reference/schemas/schemas.html#stemming) for other stemming types. To change type, add:

```
stemming: [stemming-type]
```

Stemming can be set either for a field, a fieldset or as a default for all fields. Example: Disable stemming for the field _title_:

```
field title type string {
    indexing: summary | index
    stemming: none
}
```

See [andSegmenting](../reference/querying/yql.html#andsegmenting) for how to control re-segmenting when stemming.

 Copyright © 2026 - [Cookie Preferences](#)

### On this page:

- [OpenNLP language detection](#language-detection)
- [Default languages](#default-languages)
- [Chinese](#chinese)
- [Tokenization](#tokenization)
- [Normalization](#normalization)
- [Stemming](#stemming)
- [Theory](#theory)
- [Configuration](#configuration)

