# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/WebGroundingChunk.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/GroundingMetadata/WebGroundingChunk.md.txt

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

|                                                                                                                                                                                                                        ### Public constructors                                                                                                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [WebGroundingChunk](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/WebGroundingChunk#WebGroundingChunk(kotlin.String,kotlin.String,kotlin.String))`(uri: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?, title: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?, domain: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` |

|                                ### Public properties                                |
|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | [domain](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/WebGroundingChunk#domain()) The domain of the original URI from which the content was retrieved. |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | [title](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/WebGroundingChunk#title()) The title of the retrieved web page.                                   |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | [uri](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/WebGroundingChunk#uri()) The URI of the retrieved web page.                                         |

## Public constructors

### WebGroundingChunk

```
WebGroundingChunk(uri:Â String?,Â title:Â String?,Â domain:Â String?)
```  

## Public properties

### domain

```
valÂ domain:Â String?
```

The domain of the original URI from which the content was retrieved. This is only populated when using the Vertex AI Gemini API.  

### title

```
valÂ title:Â String?
```

The title of the retrieved web page.  

### uri

```
valÂ uri:Â String?
```

The URI of the retrieved web page.