# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Citation.md.txt

# Citation

# Citation


```
class Citation
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents a citation of content from an external source within the model's output.

When the language model generates text that includes content from another source, it should provide a citation to properly attribute the original source. This class encapsulates the metadata associated with that citation.

## Summary

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Citation#endIndex()` The (exclusive) ending index within the model output where the cited content ends. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Citation#license()` The license under which the cited content is distributed under, if available. |
| `https://developer.android.com/reference/kotlin/java/util/Calendar.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Citation#publicationDate()` The date of publication of the cited source, if available. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Citation#startIndex()` The (inclusive) starting index within the model output where the cited content begins. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Citation#title()` The title of the cited source, if available. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Citation#uri()` The URI of the cited source, if available. |

## Public properties

### endIndex

```
val endIndex: Int
```

The (exclusive) ending index within the model output where the cited content ends.

### license

```
val license: String?
```

The license under which the cited content is distributed under, if available.

### publicationDate

```
val publicationDate: Calendar?
```

The date of publication of the cited source, if available.

### startIndex

```
val startIndex: Int
```

The (inclusive) starting index within the model output where the cited content begins.

### title

```
val title: String?
```

The title of the cited source, if available.

### uri

```
val uri: String?
```

The URI of the cited source, if available.