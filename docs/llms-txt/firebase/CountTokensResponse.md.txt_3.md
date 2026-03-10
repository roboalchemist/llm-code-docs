# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse.md.txt

# CountTokensResponse

# CountTokensResponse


```
class CountTokensResponse
```

<br />

*** ** * ** ***

The model's response to a count tokens request.

**Important:** The counters in this class do not include billable image, video or other non-text input. See [Pricing](https://firebase.google.com/docs/ai-logic/pricing) for details.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse#CountTokensResponse(kotlin.Int,kotlin.Int,kotlin.collections.List)( totalTokens: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, totalBillableCharacters: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?, promptTokensDetails: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ModalityTokenCount> )` |

| ### Public functions |
|---|---|
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse#component1()()` |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse#component2()()` |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ModalityTokenCount>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse#component3()()` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ModalityTokenCount>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse#promptTokensDetails()` The breakdown, by modality, of how many tokens are consumed by the prompt. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse#totalBillableCharacters()` **This property is deprecated.** This field is deprecated and will be removed in a future version. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse#totalTokens()` The total number of tokens in the input given to the model as a prompt. |

## Public constructors

### CountTokensResponse

```
CountTokensResponse(
    totalTokens: Int,
    totalBillableCharacters: Int? = null,
    promptTokensDetails: List<ModalityTokenCount> = emptyList()
)
```

## Public functions

### component1

```
operator fun component1(): Int
```

### component2

```
operator fun component2(): Int?
```

### component3

```
operator fun component3(): List<ModalityTokenCount>?
```

## Public properties

### promptTokensDetails

```
val promptTokensDetails: List<ModalityTokenCount>
```

The breakdown, by modality, of how many tokens are consumed by the prompt.

### totalBillableCharacters

```
val totalBillableCharacters: Int?
```

> [!CAUTION]
> **This property is deprecated.**   
> This field is deprecated and will be removed in a future version.

The total number of billable characters in the text input given to the model as a prompt. **Important:** this property does not include billable image, video or other non-text input. See [Pricing](https://firebase.google.com/docs/ai-logic/pricing) for details.

### totalTokens

```
val totalTokens: Int
```

The total number of tokens in the input given to the model as a prompt.