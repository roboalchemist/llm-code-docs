# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart.md.txt

# FileDataPart

# FileDataPart


```
class FileDataPart : Part
```

<br />

*** ** * ** ***

Represents file data stored in Cloud Storage for Firebase, referenced by URI.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart#FileDataPart(kotlin.String,kotlin.String)(uri: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, mimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |

| ### Public properties |
|---|---|
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart#isThought()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart#mimeType()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FileDataPart#uri()` |

## Public constructors

### FileDataPart

```
FileDataPart(uri: String, mimeType: String)
```

| Parameters |
|---|---|
| `uri: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The `"gs://"`-prefixed URI of the file in Cloud Storage for Firebase, for example, `"gs://bucket-name/path/image.jpg"` |
| `mimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | an IANA standard MIME type. For supported MIME type values see the [Firebase documentation](https://firebase.google.com/docs/vertex-ai/input-file-requirements). |

## Public properties

### isThought

```
open val isThought: Boolean
```

### mimeType

```
val mimeType: String
```

### uri

```
val uri: String
```