# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SearchEntryPoint.md.txt

# SearchEntryPoint

# SearchEntryPoint


```
public final class SearchEntryPoint
```

<br />

*** ** * ** ***

Represents a Google Search entry point.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SearchEntryPoint#renderedContent()` An HTML/CSS snippet that can be embedded in your app. |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SearchEntryPoint#sdkBlob()` A blob of data for the client SDK to render the search entry point. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SearchEntryPoint#SearchEntryPoint(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html renderedContent, https://developer.android.com/reference/kotlin/java/lang/String.html sdkBlob)` |

## Public fields

### renderedContent

```
public final @NonNull String renderedContent
```

An HTML/CSS snippet that can be embedded in your app. To ensure proper rendering, it's recommended to display this content within a `WebView`.

### sdkBlob

```
public final String sdkBlob
```

A blob of data for the client SDK to render the search entry point.

## Public constructors

### SearchEntryPoint

```
public SearchEntryPoint(@NonNull String renderedContent, String sdkBlob)
```