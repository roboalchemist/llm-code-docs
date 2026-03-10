# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/WebGroundingChunk.md.txt

# WebGroundingChunk

# WebGroundingChunk


```
class WebGroundingChunk
```

<br />

*** ** * ** ***

A grounding chunk from the web.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/WebGroundingChunk#WebGroundingChunk(kotlin.String,kotlin.String,kotlin.String)(uri: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, domain: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/WebGroundingChunk#domain()` The domain of the original URI from which the content was retrieved. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/WebGroundingChunk#title()` The title of the retrieved web page. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/WebGroundingChunk#uri()` The URI of the retrieved web page. |

## Public constructors

### WebGroundingChunk

```
WebGroundingChunk(uri: String?, title: String?, domain: String?)
```

## Public properties

### domain

```
val domain: String?
```

The domain of the original URI from which the content was retrieved. This is only populated when using the Vertex AI Gemini API.

### title

```
val title: String?
```

The title of the retrieved web page.

### uri

```
val uri: String?
```

The URI of the retrieved web page.