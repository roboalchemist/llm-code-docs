# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerateContentResponse/UsageMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/GenerateContentResponse/UsageMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/UsageMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/UsageMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/UsageMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata.md.txt

# UsageMetadata


```
class UsageMetadata
```

<br />

*** ** * ** ***

Usage metadata about response(s).

## Summary

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ### Public constructors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ~~[UsageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#UsageMetadata(kotlin.Int,kotlin.Int,kotlin.Int,kotlin.collections.List,kotlin.collections.List,kotlin.Int))~~`(` ` promptTokenCount: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`,` ` candidatesTokenCount: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?,` ` totalTokenCount: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`,` ` promptTokensDetails: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[ModalityTokenCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ModalityTokenCount)`>,` ` candidatesTokensDetails: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[ModalityTokenCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ModalityTokenCount)`>,` ` thoughtsTokenCount: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) `)` **This function is deprecated.** Not intended for public use |

|                                                                                                ### Public properties                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?`                                                                                                                                        | [candidatesTokenCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#candidatesTokenCount()) Number of tokens in the response(s).                                                 |
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[ModalityTokenCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ModalityTokenCount)`>` | [candidatesTokensDetails](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#candidatesTokensDetails()) The breakdown, by modality, of how many tokens are consumed by the candidates. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                                                           | [promptTokenCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#promptTokenCount()) Number of tokens in the request.                                                             |
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[ModalityTokenCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ModalityTokenCount)`>` | [promptTokensDetails](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#promptTokensDetails()) The breakdown, by modality, of how many tokens are consumed by the prompt.             |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                                                           | [thoughtsTokenCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#thoughtsTokenCount()) The number of tokens used by the model's internal "thinking" process.                    |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                                                           | [toolUsePromptTokenCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#toolUsePromptTokenCount()) The number of tokens used by tools.                                            |
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[ModalityTokenCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ModalityTokenCount)`>` | [toolUsePromptTokensDetails](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#toolUsePromptTokensDetails()) The breakdown, by modality, of how many tokens are consumed by tools.    |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                                                           | [totalTokenCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#totalTokenCount()) Total number of tokens.                                                                        |

## Public constructors

### UsageMetadata

```
[UsageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/UsageMetadata#UsageMetadata(kotlin.Int,kotlin.Int,kotlin.Int,kotlin.collections.List,kotlin.collections.List,kotlin.Int))(
Â Â Â Â promptTokenCount:Â Int,
Â Â Â Â candidatesTokenCount:Â Int?,
Â Â Â Â totalTokenCount:Â Int,
Â Â Â Â promptTokensDetails:Â List<ModalityTokenCount>,
Â Â Â Â candidatesTokensDetails:Â List<ModalityTokenCount>,
Â Â Â Â thoughtsTokenCount:Â Int
)
```
| **This function is deprecated.**   
Not intended for public use  

## Public properties

### candidatesTokenCount

```
valÂ candidatesTokenCount:Â Int?
```

Number of tokens in the response(s).  

### candidatesTokensDetails

```
valÂ candidatesTokensDetails:Â List<ModalityTokenCount>
```

The breakdown, by modality, of how many tokens are consumed by the candidates.  

### promptTokenCount

```
valÂ promptTokenCount:Â Int
```

Number of tokens in the request.  

### promptTokensDetails

```
valÂ promptTokensDetails:Â List<ModalityTokenCount>
```

The breakdown, by modality, of how many tokens are consumed by the prompt.  

### thoughtsTokenCount

```
valÂ thoughtsTokenCount:Â Int
```

The number of tokens used by the model's internal "thinking" process.  

### toolUsePromptTokenCount

```
valÂ toolUsePromptTokenCount:Â Int
```

The number of tokens used by tools.  

### toolUsePromptTokensDetails

```
valÂ toolUsePromptTokensDetails:Â List<ModalityTokenCount>
```

The breakdown, by modality, of how many tokens are consumed by tools.  

### totalTokenCount

```
valÂ totalTokenCount:Â Int
```

Total number of tokens.