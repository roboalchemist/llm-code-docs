# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse.md.txt

# CountTokensResponse

# CountTokensResponse


```
public final class CountTokensResponse
```

<br />

*** ** * ** ***

The model's response to a count tokens request.

**Important:** The counters in this class do not include billable image, video or other non-text input. See [Pricing](https://firebase.google.com/docs/ai-logic/pricing) for details.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ModalityTokenCount>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse#promptTokensDetails()` The breakdown, by modality, of how many tokens are consumed by the prompt. |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse#totalBillableCharacters()` **This field is deprecated.** This field is deprecated and will be removed in a future version. |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse#totalTokens()` The total number of tokens in the input given to the model as a prompt. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse#CountTokensResponse(kotlin.Int,kotlin.Int,kotlin.collections.List)( int totalTokens, https://developer.android.com/reference/kotlin/java/lang/Integer.html totalBillableCharacters, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ModalityTokenCount> promptTokensDetails )` |

| ### Public methods |
|---|---|
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse#component1()()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse#component2()()` |
| `final https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ModalityTokenCount>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse#component3()()` |

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

> [!CAUTION]
> **This field is deprecated.**   
> This field is deprecated and will be removed in a future version.

The total number of billable characters in the text input given to the model as a prompt. **Important:** this property does not include billable image, video or other non-text input. See [Pricing](https://firebase.google.com/docs/ai-logic/pricing) for details.

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