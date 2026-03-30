# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Citation.md.txt

# Citation

# Citation


```
public final class Citation
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents a citation of content from an external source within the model's output.

When the language model generates text that includes content from another source, it should provide a citation to properly attribute the original source. This class encapsulates the metadata associated with that citation.

## Summary

| ### Public fields |
|---|---|
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Citation#endIndex()` The (exclusive) ending index within the model output where the cited content ends. |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Citation#license()` The license under which the cited content is distributed under, if available. |
| `final https://developer.android.com/reference/kotlin/java/util/Calendar.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Citation#publicationDate()` The date of publication of the cited source, if available. |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Citation#startIndex()` The (inclusive) starting index within the model output where the cited content begins. |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Citation#title()` The title of the cited source, if available. |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Citation#uri()` The URI of the cited source, if available. |

## Public fields

### endIndex

```
public final int endIndex
```

The (exclusive) ending index within the model output where the cited content ends.

### license

```
public final String license
```

The license under which the cited content is distributed under, if available.

### publicationDate

```
public final Calendar publicationDate
```

The date of publication of the cited source, if available.

### startIndex

```
public final int startIndex
```

The (inclusive) starting index within the model output where the cited content begins.

### title

```
public final String title
```

The title of the cited source, if available.

### uri

```
public final String uri
```

The URI of the cited source, if available.