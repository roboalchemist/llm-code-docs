# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/UsageMetadata.md.txt

# UsageMetadata

# UsageMetadata


```
class UsageMetadata
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Usage metadata about response(s).

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/UsageMetadata#UsageMetadata(kotlin.Int,kotlin.Int,kotlin.Int,kotlin.collections.List,kotlin.collections.List)( promptTokenCount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, candidatesTokenCount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?, totalTokenCount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, promptTokensDetails: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ModalityTokenCount>, candidatesTokensDetails: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ModalityTokenCount> )` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/UsageMetadata#candidatesTokenCount()` Number of tokens in the response(s). |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ModalityTokenCount>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/UsageMetadata#candidatesTokensDetails()` The breakdown, by modality, of how many tokens are consumed by the candidates. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/UsageMetadata#promptTokenCount()` Number of tokens in the request. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ModalityTokenCount>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/UsageMetadata#promptTokensDetails()` The breakdown, by modality, of how many tokens are consumed by the prompt. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/UsageMetadata#totalTokenCount()` Total number of tokens. |

## Public constructors

### UsageMetadata

```
UsageMetadata(
    promptTokenCount: Int,
    candidatesTokenCount: Int?,
    totalTokenCount: Int,
    promptTokensDetails: List<ModalityTokenCount>,
    candidatesTokensDetails: List<ModalityTokenCount>
)
```

| Parameters |
|---|---|
| `promptTokenCount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | Number of tokens in the request. |
| `candidatesTokenCount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | Number of tokens in the response(s). |
| `totalTokenCount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | Total number of tokens. |
| `promptTokensDetails: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ModalityTokenCount>` | The breakdown, by modality, of how many tokens are consumed by the prompt. |
| `candidatesTokensDetails: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ModalityTokenCount>` | The breakdown, by modality, of how many tokens are consumed by the candidates. |

## Public properties

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

### totalTokenCount

```
val totalTokenCount: Int
```

Total number of tokens.