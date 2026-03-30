# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/MediaData.md.txt

# MediaData

# MediaData


```
@PublicPreviewAPI
public final class MediaData
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents the media data to be sent to the server

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/MediaData#data()` Byte array representing the data to be sent. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/MediaData#mimeType()` an IANA standard MIME type. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/MediaData#MediaData(kotlin.ByteArray,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] data, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html mimeType)` |

## Public fields

### data

```
public final @NonNull byte[] data
```

Byte array representing the data to be sent.

### mimeType

```
public final @NonNull String mimeType
```

an IANA standard MIME type. For supported MIME type values see the [Firebase documentation](https://firebase.google.com/docs/vertex-ai/input-file-requirements).

## Public constructors

### MediaData

```
public MediaData(@NonNull byte[] data, @NonNull String mimeType)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] data` | Byte array representing the data to be sent. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html mimeType` | an IANA standard MIME type. For supported MIME type values see the [Firebase documentation](https://firebase.google.com/docs/vertex-ai/input-file-requirements). |