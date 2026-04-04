# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder.md.txt

# GenerationConfig.Builder

# GenerationConfig.Builder


```
class GenerationConfig.Builder
```

<br />

*** ** * ** ***

Builder for creating a [GenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig).

Mainly intended for Java interop. Kotlin consumers should use [generationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/package-summary#generationConfig(kotlin.Function1)) for a more idiomatic experience.  

|                                                                       See also                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [generationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/package-summary#generationConfig(kotlin.Function1)) |   |

## Summary

|                                                     ### Public constructors                                                     |
|---------------------------------------------------------------------------------------------------------------------------------|
| [Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#Builder())`()` |

|                                                        ### Public functions                                                        |
|------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig)                 | [build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#build())`()` Create a new [GenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig) with the attached arguments.                                                                                                                                |
| [GenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder) | [setCandidateCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setCandidateCount(kotlin.Int))`(candidateCount: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?)`                                                                                                                                                              |
| [GenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder) | [setFrequencyPenalty](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setFrequencyPenalty(kotlin.Float))`(frequencyPenalty: `[Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)`?)`                                                                                                                                                  |
| [GenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder) | [setMaxOutputTokens](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setMaxOutputTokens(kotlin.Int))`(maxOutputTokens: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?)`                                                                                                                                                           |
| [GenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder) | [setPresencePenalty](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setPresencePenalty(kotlin.Float))`(presencePenalty: `[Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)`?)`                                                                                                                                                     |
| [GenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder) | [setResponseMimeType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setResponseMimeType(kotlin.String))`(responseMimeType: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)`                                                                                                                                               |
| [GenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder) | [setResponseModalities](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setResponseModalities(kotlin.collections.List))`(responseModalities: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[ResponseModality](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ResponseModality)`>?)` |
| [GenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder) | [setResponseSchema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setResponseSchema(com.google.firebase.ai.type.Schema))`(responseSchema: `[Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema)`?)`                                                                                                                  |
| [GenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder) | [setStopSequences](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setStopSequences(kotlin.collections.List))`(stopSequences: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`>?)`                                                  |
| [GenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder) | [setTemperature](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setTemperature(kotlin.Float))`(temperature: `[Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)`?)`                                                                                                                                                                 |
| [GenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder) | [setThinkingConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setThinkingConfig(com.google.firebase.ai.type.ThinkingConfig))`(thinkingConfig: `[ThinkingConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingConfig)`?)`                                                                                          |
| [GenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder) | [setTopK](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setTopK(kotlin.Int))`(topK: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?)`                                                                                                                                                                                            |
| [GenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder) | [setTopP](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setTopP(kotlin.Float))`(topP: `[Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)`?)`                                                                                                                                                                                      |

|                                                                                               ### Public properties                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?`                                                                                                                                     | [candidateCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#candidateCount()) See [GenerationConfig.candidateCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#candidateCount()).                 |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)`?`                                                                                                                                 | [frequencyPenalty](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#frequencyPenalty()) See [GenerationConfig.frequencyPenalty](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#frequencyPenalty())          |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?`                                                                                                                                     | [maxOutputTokens](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#maxOutputTokens()) See [GenerationConfig.maxOutputTokens](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#maxOutputTokens()).             |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)`?`                                                                                                                                 | [presencePenalty](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#presencePenalty()) See [GenerationConfig.presencePenalty](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#presencePenalty())              |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                                                                                                               | [responseMimeType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#responseMimeType()) See [GenerationConfig.responseMimeType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#responseMimeType()).         |
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[ResponseModality](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ResponseModality)`>?` | [responseModalities](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#responseModalities()) See [GenerationConfig.responseModalities](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#responseModalities()). |
| [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema)`?`                                                                                                                 | [responseSchema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#responseSchema()) See [GenerationConfig.responseSchema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#responseSchema()).                 |
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`>?`                                   | [stopSequences](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#stopSequences()) See [GenerationConfig.stopSequences](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#stopSequences()).                     |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)`?`                                                                                                                                 | [temperature](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#temperature()) See [GenerationConfig.temperature](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#temperature()).                             |
| [ThinkingConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingConfig)`?`                                                                                                 | [thinkingConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#thinkingConfig())                                                                                                                                                                         |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?`                                                                                                                                     | [topK](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#topK()) See [GenerationConfig.topK](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#topK()).                                                         |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)`?`                                                                                                                                 | [topP](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#topP()) See [GenerationConfig.topP](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#topP()).                                                         |

## Public constructors

### Builder

```
Builder()
```  

## Public functions

### build

```
funÂ build():Â GenerationConfig
```

Create a new [GenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig) with the attached arguments.  

### setCandidateCount

```
funÂ setCandidateCount(candidateCount:Â Int?):Â GenerationConfig.Builder
```  

### setFrequencyPenalty

```
funÂ setFrequencyPenalty(frequencyPenalty:Â Float?):Â GenerationConfig.Builder
```  

### setMaxOutputTokens

```
funÂ setMaxOutputTokens(maxOutputTokens:Â Int?):Â GenerationConfig.Builder
```  

### setPresencePenalty

```
funÂ setPresencePenalty(presencePenalty:Â Float?):Â GenerationConfig.Builder
```  

### setResponseMimeType

```
funÂ setResponseMimeType(responseMimeType:Â String?):Â GenerationConfig.Builder
```  

### setResponseModalities

```
funÂ setResponseModalities(responseModalities:Â List<ResponseModality>?):Â GenerationConfig.Builder
```  

### setResponseSchema

```
funÂ setResponseSchema(responseSchema:Â Schema?):Â GenerationConfig.Builder
```  

### setStopSequences

```
funÂ setStopSequences(stopSequences:Â List<String>?):Â GenerationConfig.Builder
```  

### setTemperature

```
funÂ setTemperature(temperature:Â Float?):Â GenerationConfig.Builder
```  

### setThinkingConfig

```
funÂ setThinkingConfig(thinkingConfig:Â ThinkingConfig?):Â GenerationConfig.Builder
```  

### setTopK

```
funÂ setTopK(topK:Â Int?):Â GenerationConfig.Builder
```  

### setTopP

```
funÂ setTopP(topP:Â Float?):Â GenerationConfig.Builder
```  

## Public properties

### candidateCount

```
varÂ candidateCount:Â Int?
```

See [GenerationConfig.candidateCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#candidateCount()).  

### frequencyPenalty

```
varÂ frequencyPenalty:Â Float?
```

See [GenerationConfig.frequencyPenalty](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#frequencyPenalty())  

### maxOutputTokens

```
varÂ maxOutputTokens:Â Int?
```

See [GenerationConfig.maxOutputTokens](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#maxOutputTokens()).  

### presencePenalty

```
varÂ presencePenalty:Â Float?
```

See [GenerationConfig.presencePenalty](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#presencePenalty())  

### responseMimeType

```
varÂ responseMimeType:Â String?
```

See [GenerationConfig.responseMimeType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#responseMimeType()).  

### responseModalities

```
varÂ responseModalities:Â List<ResponseModality>?
```

See [GenerationConfig.responseModalities](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#responseModalities()).  

### responseSchema

```
varÂ responseSchema:Â Schema?
```

See [GenerationConfig.responseSchema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#responseSchema()).  

### stopSequences

```
varÂ stopSequences:Â List<String>?
```

See [GenerationConfig.stopSequences](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#stopSequences()).  

### temperature

```
varÂ temperature:Â Float?
```

See [GenerationConfig.temperature](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#temperature()).  

### thinkingConfig

```
varÂ thinkingConfig:Â ThinkingConfig?
```  

### topK

```
varÂ topK:Â Int?
```

See [GenerationConfig.topK](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#topK()).  

### topP

```
varÂ topP:Â Float?
```

See [GenerationConfig.topP](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#topP()).