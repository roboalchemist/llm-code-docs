# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse.md.txt

# CountTokensResponse

# CountTokensResponse


```
public final class CountTokensResponse
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

The model's response to a count tokens request.

**Important:** The counters in this class do not include billable image, video or other non-text input. See [Vertex AI pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing) for details.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ModalityTokenCount>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse#promptTokensDetails()` The breakdown, by modality, of how many tokens are consumed by the prompt. |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse#totalBillableCharacters()` The total number of billable characters in the text input given to the model as a prompt. |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse#totalTokens()` The total number of tokens in the input given to the model as a prompt. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse#CountTokensResponse(kotlin.Int,kotlin.Int,kotlin.collections.List)( int totalTokens, https://developer.android.com/reference/kotlin/java/lang/Integer.html totalBillableCharacters, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ModalityTokenCount> promptTokensDetails )` |

| ### Public methods |
|---|---|
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse#component1()()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse#component2()()` |
| `final https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ModalityTokenCount>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse#component3()()` |

## Public fields

### promptTokensDetails

```
public final @NonNull List<@NonNull ModalityTokenCount> promptTokensDetails
```

The breakdown, by modality, of how many tokens are consumed by the prompt.

### totalBillableCharacters

```
public final Integer totalBillableCharacters
```

The total number of billable characters in the text input given to the model as a prompt. **Important:** this property does not include billable image, video or other non-text input. See [Vertex AI pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing) for details.

### totalTokens

```
public final int totalTokens
```

The total number of tokens in the input given to the model as a prompt.

## Public constructors

### CountTokensResponse

```
public CountTokensResponse(
    int totalTokens,
    Integer totalBillableCharacters,
    @NonNull List<@NonNull ModalityTokenCount> promptTokensDetails
)
```

## Public methods

### component1

```
public final int component1()
```

### component2

```
public final Integer component2()
```

### component3

```
public final List<@NonNull ModalityTokenCount> component3()
```