# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/WebGroundingChunk.md.txt

# WebGroundingChunk

# WebGroundingChunk


```
public final class WebGroundingChunk
```

<br />

*** ** * ** ***

A grounding chunk from the web.

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/WebGroundingChunk#domain()` The domain of the original URI from which the content was retrieved. |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/WebGroundingChunk#title()` The title of the retrieved web page. |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/WebGroundingChunk#uri()` The URI of the retrieved web page. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/WebGroundingChunk#WebGroundingChunk(kotlin.String,kotlin.String,kotlin.String)(https://developer.android.com/reference/kotlin/java/lang/String.html uri, https://developer.android.com/reference/kotlin/java/lang/String.html title, https://developer.android.com/reference/kotlin/java/lang/String.html domain)` |

## Public fields

### domain

```
public final String domain
```

The domain of the original URI from which the content was retrieved. This is only populated when using the Vertex AI Gemini API.

### title

```
public final String title
```

The title of the retrieved web page.

### uri

```
public final String uri
```

The URI of the retrieved web page.

## Public constructors

### WebGroundingChunk

```
public WebGroundingChunk(String uri, String title, String domain)
```