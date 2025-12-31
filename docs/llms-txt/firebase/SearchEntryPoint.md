# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/GroundingMetadata/SearchEntryPoint.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SearchEntryPoint.md.txt

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

|                                                                                                                                                                        ### Public constructors                                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SearchEntryPoint](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SearchEntryPoint#SearchEntryPoint(kotlin.String,kotlin.String))`(renderedContent: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, sdkBlob: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` |

|                                ### Public properties                                |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)    | [renderedContent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SearchEntryPoint#renderedContent()) An HTML/CSS snippet that can be embedded in your app. |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | [sdkBlob](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SearchEntryPoint#sdkBlob()) A blob of data for the client SDK to render the search entry point.   |

## Public constructors

### SearchEntryPoint

```
SearchEntryPoint(renderedContent:Â String,Â sdkBlob:Â String?)
```  

## Public properties

### renderedContent

```
valÂ renderedContent:Â String
```

An HTML/CSS snippet that can be embedded in your app. To ensure proper rendering, it's recommended to display this content within a `WebView`.  

### sdkBlob

```
valÂ sdkBlob:Â String?
```

A blob of data for the client SDK to render the search entry point.