# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SearchEntryPoint.md.txt

# SearchEntryPoint

# SearchEntryPoint


```
class SearchEntryPoint
```

<br />

*** ** * ** ***

Represents a Google Search entry point.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SearchEntryPoint#SearchEntryPoint(kotlin.String,kotlin.String)(renderedContent: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, sdkBlob: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SearchEntryPoint#renderedContent()` An HTML/CSS snippet that can be embedded in your app. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SearchEntryPoint#sdkBlob()` A blob of data for the client SDK to render the search entry point. |

## Public constructors

### SearchEntryPoint

```
SearchEntryPoint(renderedContent: String, sdkBlob: String?)
```

## Public properties

### renderedContent

```
val renderedContent: String
```

An HTML/CSS snippet that can be embedded in your app. To ensure proper rendering, it's recommended to display this content within a `WebView`.

### sdkBlob

```
val sdkBlob: String?
```

A blob of data for the client SDK to render the search entry point.