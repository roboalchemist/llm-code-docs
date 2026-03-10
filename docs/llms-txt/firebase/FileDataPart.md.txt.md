# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FileDataPart.md.txt

# FileDataPart

# FileDataPart


```
public final class FileDataPart implements Part
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents file data stored in Cloud Storage for Firebase, referenced by URI.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FileDataPart#mimeType()` an IANA standard MIME type. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FileDataPart#uri()` The `"gs://"`-prefixed URI of the file in Cloud Storage for Firebase, for example, `"gs://bucket-name/path/image.jpg"` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FileDataPart#FileDataPart(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html uri, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html mimeType)` |

## Public fields

### mimeType

```
public final @NonNull String mimeType
```

an IANA standard MIME type. For supported MIME type values see the [Firebase documentation](https://firebase.google.com/docs/vertex-ai/input-file-requirements).

### uri

```
public final @NonNull String uri
```

The `"gs://"`-prefixed URI of the file in Cloud Storage for Firebase, for example, `"gs://bucket-name/path/image.jpg"`

## Public constructors

### FileDataPart

```
public FileDataPart(@NonNull String uri, @NonNull String mimeType)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html uri` | The `"gs://"`-prefixed URI of the file in Cloud Storage for Firebase, for example, `"gs://bucket-name/path/image.jpg"` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html mimeType` | an IANA standard MIME type. For supported MIME type values see the [Firebase documentation](https://firebase.google.com/docs/vertex-ai/input-file-requirements). |