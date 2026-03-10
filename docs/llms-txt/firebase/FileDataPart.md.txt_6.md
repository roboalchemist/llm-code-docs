# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FileDataPart.md.txt

# FileDataPart

# FileDataPart


```
class FileDataPart : Part
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents file data stored in Cloud Storage for Firebase, referenced by URI.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FileDataPart#FileDataPart(kotlin.String,kotlin.String)(uri: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, mimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FileDataPart#mimeType()` an IANA standard MIME type. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FileDataPart#uri()` The `"gs://"`-prefixed URI of the file in Cloud Storage for Firebase, for example, `"gs://bucket-name/path/image.jpg"` |

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

### mimeType

```
val mimeType: String
```

an IANA standard MIME type. For supported MIME type values see the [Firebase documentation](https://firebase.google.com/docs/vertex-ai/input-file-requirements).

### uri

```
val uri: String
```

The `"gs://"`-prefixed URI of the file in Cloud Storage for Firebase, for example, `"gs://bucket-name/path/image.jpg"`