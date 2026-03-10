# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineData.md.txt

# InlineData

# InlineData


```
class InlineData
```

<br />

*** ** * ** ***

Represents binary data with an associated MIME type.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineData#InlineData(kotlin.ByteArray,kotlin.String)(data: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html, mimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineData#InlineData(kotlin.ByteArray,kotlin.String,kotlin.String)(data: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html, mimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, displayName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineData#data()` the binary data as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineData#displayName()` the file name |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineData#mimeType()` an IANA standard MIME type. |

## Public constructors

### InlineData

```
InlineData(data: ByteArray, mimeType: String)
```

### InlineData

```
InlineData(data: ByteArray, mimeType: String, displayName: String?)
```

## Public properties

### data

```
val data: ByteArray
```

the binary data as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html`

### displayName

```
val displayName: String?
```

the file name

### mimeType

```
val mimeType: String
```

an IANA standard MIME type.