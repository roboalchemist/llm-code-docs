# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineData.md.txt

# InlineData

# InlineData


```
public final class InlineData
```

<br />

*** ** * ** ***

Represents binary data with an associated MIME type.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineData#data()` the binary data as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineData#displayName()` the file name |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineData#mimeType()` an IANA standard MIME type. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineData#InlineData(kotlin.ByteArray,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] data, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html mimeType)` |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineData#InlineData(kotlin.ByteArray,kotlin.String,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] data, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html mimeType, https://developer.android.com/reference/kotlin/java/lang/String.html displayName )` |

## Public fields

### data

```
public final @NonNull byte[] data
```

the binary data as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html`

### displayName

```
public final String displayName
```

the file name

### mimeType

```
public final @NonNull String mimeType
```

an IANA standard MIME type.

## Public constructors

### InlineData

```
public InlineData(@NonNull byte[] data, @NonNull String mimeType)
```

### InlineData

```
public InlineData(
    @NonNull byte[] data,
    @NonNull String mimeType,
    String displayName
)
```