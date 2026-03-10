# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse.md.txt

# CountTokensResponse

# CountTokensResponse


```
class CountTokensResponse
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

The model's response to a count tokens request.

**Important:** The counters in this class do not include billable image, video or other non-text input. See [Vertex AI pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing) for details.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse#CountTokensResponse(kotlin.Int,kotlin.Int,kotlin.collections.List)( totalTokens: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, totalBillableCharacters: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?, promptTokensDetails: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ModalityTokenCount> )` |

| ### Public functions |
|---|---|
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse#component1()()` |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse#component2()()` |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ModalityTokenCount>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse#component3()()` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ModalityTokenCount>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse#promptTokensDetails()` The breakdown, by modality, of how many tokens are consumed by the prompt. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse#totalBillableCharacters()` The total number of billable characters in the text input given to the model as a prompt. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse#totalTokens()` The total number of tokens in the input given to the model as a prompt. |

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

The total number of billable characters in the text input given to the model as a prompt. **Important:** this property does not include billable image, video or other non-text input. See [Vertex AI pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing) for details.

### totalTokens

```
val totalTokens: Int
```

The total number of tokens in the input given to the model as a prompt.