# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineDataPart.md.txt

# InlineDataPart

# InlineDataPart


```
public final class InlineDataPart implements Part
```

<br />

*** ** * ** ***

Represents binary data with an associated MIME type sent to and received from requests.

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineDataPart#displayName()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineDataPart#inlineData()` |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineDataPart#isThought()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineDataPart#mimeType()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineDataPart#InlineDataPart(kotlin.ByteArray,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] inlineData, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html mimeType)` |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineDataPart#InlineDataPart(kotlin.ByteArray,kotlin.String,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] inlineData, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html mimeType, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html displayName )` |

## Public fields

### displayName

```
public final String displayName
```

### inlineData

```
public final @NonNull byte[] inlineData
```

### isThought

```
public boolean isThought
```

### mimeType

```
public final @NonNull String mimeType
```

## Public constructors

### InlineDataPart

```
public InlineDataPart(@NonNull byte[] inlineData, @NonNull String mimeType)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] inlineData` | the binary data as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html mimeType` | an IANA standard MIME type. For supported values, see the [Firebase documentation](https://firebase.google.com/docs/vertex-ai/input-file-requirements). |

### InlineDataPart

```
public InlineDataPart(
    @NonNull byte[] inlineData,
    @NonNull String mimeType,
    @NonNull String displayName
)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] inlineData` | the binary data as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html mimeType` | an IANA standard MIME type. For supported values, see the [Firebase documentation](https://firebase.google.com/docs/vertex-ai/input-file-requirements). |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html displayName` | the name of the file, including the extension |