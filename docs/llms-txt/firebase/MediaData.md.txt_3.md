# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/MediaData.md.txt

# MediaData

# MediaData


```
@PublicPreviewAPI
class MediaData
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> Use \`InlineData\` instead

Represents the media data to be sent to the server

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/MediaData#MediaData(kotlin.ByteArray,kotlin.String)(data: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html, mimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/MediaData#data()` Byte array representing the data to be sent. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/MediaData#mimeType()` an IANA standard MIME type. |

## Public constructors

### MediaData

```
MediaData(data: ByteArray, mimeType: String)
```

| Parameters |
|---|---|
| `data: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | Byte array representing the data to be sent. |
| `mimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | an IANA standard MIME type. For supported MIME type values see the [Firebase documentation](https://firebase.google.com/docs/vertex-ai/input-file-requirements). |

## Public properties

### data

```
val data: ByteArray
```

Byte array representing the data to be sent.

### mimeType

```
val mimeType: String
```

an IANA standard MIME type. For supported MIME type values see the [Firebase documentation](https://firebase.google.com/docs/vertex-ai/input-file-requirements).