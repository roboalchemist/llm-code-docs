# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineDataPart.md.txt

# InlineDataPart

# InlineDataPart


```
class InlineDataPart : Part
```

<br />

*** ** * ** ***

Represents binary data with an associated MIME type sent to and received from requests.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineDataPart#InlineDataPart(kotlin.ByteArray,kotlin.String)(inlineData: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html, mimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineDataPart#InlineDataPart(kotlin.ByteArray,kotlin.String,kotlin.String)( inlineData: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html, mimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, displayName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html )` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineDataPart#displayName()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineDataPart#inlineData()` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineDataPart#isThought()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineDataPart#mimeType()` |

## Public constructors

### InlineDataPart

```
InlineDataPart(inlineData: ByteArray, mimeType: String)
```

| Parameters |
|---|---|
| `inlineData: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | the binary data as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` |
| `mimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | an IANA standard MIME type. For supported values, see the [Firebase documentation](https://firebase.google.com/docs/vertex-ai/input-file-requirements). |

### InlineDataPart

```
InlineDataPart(
    inlineData: ByteArray,
    mimeType: String,
    displayName: String
)
```

| Parameters |
|---|---|
| `inlineData: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | the binary data as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` |
| `mimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | an IANA standard MIME type. For supported values, see the [Firebase documentation](https://firebase.google.com/docs/vertex-ai/input-file-requirements). |
| `displayName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the name of the file, including the extension |

## Public properties

### displayName

```
val displayName: String?
```

### inlineData

```
val inlineData: ByteArray
```

### isThought

```
open val isThought: Boolean
```

### mimeType

```
val mimeType: String
```