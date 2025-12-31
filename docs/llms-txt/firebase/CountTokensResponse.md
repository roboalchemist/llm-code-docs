# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/CountTokensResponse.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/CountTokensResponse.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/CountTokensResponse.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/CountTokensResponse.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse.md.txt

# CountTokensResponse

# CountTokensResponse


```
class CountTokensResponse
```

<br />

*** ** * ** ***

| **This class is deprecated.**   
| The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

The model's response to a count tokens request.

**Important:** The counters in this class do not include billable image, video or other non-text input. See [Vertex AI pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing) for details.

## Summary

|                                                                                                                                                                                                                                                                                                                       ### Public constructors                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CountTokensResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse#CountTokensResponse(kotlin.Int,kotlin.Int,kotlin.collections.List))`(` ` totalTokens: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`,` ` totalBillableCharacters: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?,` ` promptTokensDetails: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[ModalityTokenCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ModalityTokenCount)`>` `)` |

|                                                                                                          ### Public functions                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| `operator `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                                                                  | [component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse#component1())`()` |
| `operator `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?`                                                                                                                                               | [component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse#component2())`()` |
| `operator `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[ModalityTokenCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ModalityTokenCount)`>?` | [component3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse#component3())`()` |

|                                                                                                   ### Public properties                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[ModalityTokenCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ModalityTokenCount)`>` | [promptTokensDetails](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse#promptTokensDetails()) The breakdown, by modality, of how many tokens are consumed by the prompt.                        |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?`                                                                                                                                              | [totalBillableCharacters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse#totalBillableCharacters()) The total number of billable characters in the text input given to the model as a prompt. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                                                                 | [totalTokens](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse#totalTokens()) The total number of tokens in the input given to the model as a prompt.                                           |

## Public constructors

### CountTokensResponse

```
CountTokensResponse(
Â Â Â Â totalTokens:Â Int,
Â Â Â Â totalBillableCharacters:Â Int? = null,
Â Â Â Â promptTokensDetails:Â List<ModalityTokenCount> = emptyList()
)
```  

## Public functions

### component1

```
operatorÂ funÂ component1():Â Int
```  

### component2

```
operatorÂ funÂ component2():Â Int?
```  

### component3

```
operatorÂ funÂ component3():Â List<ModalityTokenCount>?
```  

## Public properties

### promptTokensDetails

```
valÂ promptTokensDetails:Â List<ModalityTokenCount>
```

The breakdown, by modality, of how many tokens are consumed by the prompt.  

### totalBillableCharacters

```
valÂ totalBillableCharacters:Â Int?
```

The total number of billable characters in the text input given to the model as a prompt. **Important:** this property does not include billable image, video or other non-text input. See [Vertex AI pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing) for details.  

### totalTokens

```
valÂ totalTokens:Â Int
```

The total number of tokens in the input given to the model as a prompt.