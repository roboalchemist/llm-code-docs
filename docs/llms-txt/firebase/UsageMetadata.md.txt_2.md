# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/UsageMetadata.md.txt

# UsageMetadata

# UsageMetadata


```
public final class UsageMetadata
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Usage metadata about response(s).

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/UsageMetadata#candidatesTokenCount()` Number of tokens in the response(s). |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ModalityTokenCount>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/UsageMetadata#candidatesTokensDetails()` The breakdown, by modality, of how many tokens are consumed by the candidates. |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/UsageMetadata#promptTokenCount()` Number of tokens in the request. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ModalityTokenCount>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/UsageMetadata#promptTokensDetails()` The breakdown, by modality, of how many tokens are consumed by the prompt. |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/UsageMetadata#totalTokenCount()` Total number of tokens. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/UsageMetadata#UsageMetadata(kotlin.Int,kotlin.Int,kotlin.Int,kotlin.collections.List,kotlin.collections.List)( int promptTokenCount, https://developer.android.com/reference/kotlin/java/lang/Integer.html candidatesTokenCount, int totalTokenCount, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ModalityTokenCount> promptTokensDetails, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ModalityTokenCount> candidatesTokensDetails )` |

## Public fields

### candidatesTokenCount

```
public final Integer candidatesTokenCount
```

Number of tokens in the response(s).

### candidatesTokensDetails

```
public final @NonNull List<@NonNull ModalityTokenCount> candidatesTokensDetails
```

The breakdown, by modality, of how many tokens are consumed by the candidates.

### promptTokenCount

```
public final int promptTokenCount
```

Number of tokens in the request.

### promptTokensDetails

```
public final @NonNull List<@NonNull ModalityTokenCount> promptTokensDetails
```

The breakdown, by modality, of how many tokens are consumed by the prompt.

### totalTokenCount

```
public final int totalTokenCount
```

Total number of tokens.

## Public constructors

### UsageMetadata

```
public UsageMetadata(
    int promptTokenCount,
    Integer candidatesTokenCount,
    int totalTokenCount,
    @NonNull List<@NonNull ModalityTokenCount> promptTokensDetails,
    @NonNull List<@NonNull ModalityTokenCount> candidatesTokensDetails
)
```

| Parameters |
|---|---|
| `int promptTokenCount` | Number of tokens in the request. |
| `https://developer.android.com/reference/kotlin/java/lang/Integer.html candidatesTokenCount` | Number of tokens in the response(s). |
| `int totalTokenCount` | Total number of tokens. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ModalityTokenCount> promptTokensDetails` | The breakdown, by modality, of how many tokens are consumed by the prompt. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ModalityTokenCount> candidatesTokensDetails` | The breakdown, by modality, of how many tokens are consumed by the candidates. |