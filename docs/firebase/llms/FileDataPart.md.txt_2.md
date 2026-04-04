# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FileDataPart.md.txt

# FileDataPart

# FileDataPart


```
public final class FileDataPart implements Part
```

<br />

*** ** * ** ***

Represents file data stored in Cloud Storage for Firebase, referenced by URI.

## Summary

| ### Public fields |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FileDataPart#isThought()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FileDataPart#mimeType()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FileDataPart#uri()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FileDataPart#FileDataPart(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html uri, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html mimeType)` |

## Public fields

### isThought

```
public boolean isThought
```

### mimeType

```
public final @NonNull String mimeType
```

### uri

```
public final @NonNull String uri
```

## Public constructors

### FileDataPart

```
public FileDataPart(@NonNull String uri, @NonNull String mimeType)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html uri` | The `"gs://"`-prefixed URI of the file in Cloud Storage for Firebase, for example, `"gs://bucket-name/path/image.jpg"` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html mimeType` | an IANA standard MIME type. For supported MIME type values see the [Firebase documentation](https://firebase.google.com/docs/vertex-ai/input-file-requirements). |