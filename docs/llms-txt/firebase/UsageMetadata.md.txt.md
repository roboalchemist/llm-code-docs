# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/UsageMetadata.md.txt

# UsageMetadata

# UsageMetadata


```
public final class UsageMetadata
```

<br />

*** ** * ** ***

Usage metadata about response(s).

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ModalityTokenCount>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/UsageMetadata#cacheTokensDetails()` |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/UsageMetadata#cachedContentTokenCount()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/UsageMetadata#candidatesTokenCount()` Number of tokens in the response(s). |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ModalityTokenCount>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/UsageMetadata#candidatesTokensDetails()` The breakdown, by modality, of how many tokens are consumed by the candidates. |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/UsageMetadata#promptTokenCount()` Number of tokens in the request. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ModalityTokenCount>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/UsageMetadata#promptTokensDetails()` The breakdown, by modality, of how many tokens are consumed by the prompt. |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/UsageMetadata#thoughtsTokenCount()` The number of tokens used by the model's internal "thinking" process. |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/UsageMetadata#toolUsePromptTokenCount()` The number of tokens used by tools. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ModalityTokenCount>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/UsageMetadata#toolUsePromptTokensDetails()` The breakdown, by modality, of how many tokens are consumed by tools. |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/UsageMetadata#totalTokenCount()` Total number of tokens. |

| ### Public constructors |
|---|
| `[UsageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/UsageMetadata#UsageMetadata(kotlin.Int,kotlin.Int,kotlin.Int,kotlin.collections.List,kotlin.collections.List,kotlin.Int))( int promptTokenCount, https://developer.android.com/reference/kotlin/java/lang/Integer.html candidatesTokenCount, int totalTokenCount, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ModalityTokenCount> promptTokensDetails, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ModalityTokenCount> candidatesTokensDetails, int thoughtsTokenCount )` **This method is deprecated.** Not intended for public use |

## Public fields

### cacheTokensDetails

```
public final @NonNull List<@NonNull ModalityTokenCount> cacheTokensDetails
```

### cachedContentTokenCount

```
public final int cachedContentTokenCount
```

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

### thoughtsTokenCount

```
public final int thoughtsTokenCount
```

The number of tokens used by the model's internal "thinking" process.

### toolUsePromptTokenCount

```
public final int toolUsePromptTokenCount
```

The number of tokens used by tools.

### toolUsePromptTokensDetails

```
public final @NonNull List<@NonNull ModalityTokenCount> toolUsePromptTokensDetails
```

The breakdown, by modality, of how many tokens are consumed by tools.

### totalTokenCount

```
public final int totalTokenCount
```

Total number of tokens.

## Public constructors

### UsageMetadata

```
public [UsageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/UsageMetadata#UsageMetadata(kotlin.Int,kotlin.Int,kotlin.Int,kotlin.collections.List,kotlin.collections.List,kotlin.Int))(
    int promptTokenCount,
    Integer candidatesTokenCount,
    int totalTokenCount,
    @NonNull List<@NonNull ModalityTokenCount> promptTokensDetails,
    @NonNull List<@NonNull ModalityTokenCount> candidatesTokensDetails,
    int thoughtsTokenCount
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Not intended for public use