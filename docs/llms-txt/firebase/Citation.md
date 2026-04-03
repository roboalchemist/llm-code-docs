# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/Citation.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Citation.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Citation.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Citation.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Citation.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Citation.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Citation.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Citation.md.txt

# Citation

# Citation


```
class Citation
```

<br />

*** ** * ** ***

| **This class is deprecated.**   
| The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents a citation of content from an external source within the model's output.

When the language model generates text that includes content from another source, it should provide a citation to properly attribute the original source. This class encapsulates the metadata associated with that citation.

## Summary

|                                 ### Public properties                                 |
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)            | [endIndex](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Citation#endIndex()) The (exclusive) ending index within the model output where the cited content ends.         |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`   | [license](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Citation#license()) The license under which the cited content is distributed under, if available.                |
| [Calendar](https://developer.android.com/reference/kotlin/java/util/Calendar.html)`?` | [publicationDate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Citation#publicationDate()) The date of publication of the cited source, if available.                   |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)            | [startIndex](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Citation#startIndex()) The (inclusive) starting index within the model output where the cited content begins. |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`   | [title](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Citation#title()) The title of the cited source, if available.                                                     |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`   | [uri](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Citation#uri()) The URI of the cited source, if available.                                                           |

## Public properties

### endIndex

```
valÂ endIndex:Â Int
```

The (exclusive) ending index within the model output where the cited content ends.  

### license

```
valÂ license:Â String?
```

The license under which the cited content is distributed under, if available.  

### publicationDate

```
valÂ publicationDate:Â Calendar?
```

The date of publication of the cited source, if available.  

### startIndex

```
valÂ startIndex:Â Int
```

The (inclusive) starting index within the model output where the cited content begins.  

### title

```
valÂ title:Â String?
```

The title of the cited source, if available.  

### uri

```
valÂ uri:Â String?
```

The URI of the cited source, if available.