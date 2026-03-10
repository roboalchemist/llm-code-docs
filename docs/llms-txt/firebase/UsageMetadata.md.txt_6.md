# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata.md.txt

# UsageMetadata

# UsageMetadata


```
class UsageMetadata
```

<br />

*** ** * ** ***

Usage metadata about response(s).

## Summary

| ### Public constructors |
|---|
| `[UsageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#UsageMetadata(kotlin.Int,kotlin.Int,kotlin.Int,kotlin.collections.List,kotlin.collections.List,kotlin.Int))( promptTokenCount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, candidatesTokenCount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?, totalTokenCount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, promptTokensDetails: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ModalityTokenCount>, candidatesTokensDetails: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ModalityTokenCount>, thoughtsTokenCount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html )` **This function is deprecated.** Not intended for public use |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ModalityTokenCount>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#cacheTokensDetails()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#cachedContentTokenCount()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#candidatesTokenCount()` Number of tokens in the response(s). |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ModalityTokenCount>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#candidatesTokensDetails()` The breakdown, by modality, of how many tokens are consumed by the candidates. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#promptTokenCount()` Number of tokens in the request. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ModalityTokenCount>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#promptTokensDetails()` The breakdown, by modality, of how many tokens are consumed by the prompt. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#thoughtsTokenCount()` The number of tokens used by the model's internal "thinking" process. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#toolUsePromptTokenCount()` The number of tokens used by tools. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ModalityTokenCount>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#toolUsePromptTokensDetails()` The breakdown, by modality, of how many tokens are consumed by tools. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#totalTokenCount()` Total number of tokens. |

## Public constructors

### UsageMetadata

```
[UsageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#UsageMetadata(kotlin.Int,kotlin.Int,kotlin.Int,kotlin.collections.List,kotlin.collections.List,kotlin.Int))(
    promptTokenCount: Int,
    candidatesTokenCount: Int?,
    totalTokenCount: Int,
    promptTokensDetails: List<ModalityTokenCount>,
    candidatesTokensDetails: List<ModalityTokenCount>,
    thoughtsTokenCount: Int
)
```

> [!CAUTION]
> **This function is deprecated.**   
> Not intended for public use

## Public properties

### cacheTokensDetails

```
val cacheTokensDetails: List<ModalityTokenCount>
```

### cachedContentTokenCount

```
val cachedContentTokenCount: Int
```

### candidatesTokenCount

```
val candidatesTokenCount: Int?
```

Number of tokens in the response(s).

### candidatesTokensDetails

```
val candidatesTokensDetails: List<ModalityTokenCount>
```

The breakdown, by modality, of how many tokens are consumed by the candidates.

### promptTokenCount

```
val promptTokenCount: Int
```

Number of tokens in the request.

### promptTokensDetails

```
val promptTokensDetails: List<ModalityTokenCount>
```

The breakdown, by modality, of how many tokens are consumed by the prompt.

### thoughtsTokenCount

```
val thoughtsTokenCount: Int
```

The number of tokens used by the model's internal "thinking" process.

### toolUsePromptTokenCount

```
val toolUsePromptTokenCount: Int
```

The number of tokens used by tools.

### toolUsePromptTokensDetails

```
val toolUsePromptTokensDetails: List<ModalityTokenCount>
```

The breakdown, by modality, of how many tokens are consumed by tools.

### totalTokenCount

```
val totalTokenCount: Int
```

Total number of tokens.