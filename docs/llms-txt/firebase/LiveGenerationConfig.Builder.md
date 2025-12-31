# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder.md.txt

# LiveGenerationConfig.Builder

# LiveGenerationConfig.Builder


```
class LiveGenerationConfig.Builder
```

<br />

*** ** * ** ***

| **This class is deprecated.**   
| The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Builder for creating a [LiveGenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig).

Mainly intended for Java interop. Kotlin consumers should use [liveGenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/package-summary#liveGenerationConfig(kotlin.Function1)) for a more idiomatic experience.

## Summary

|                                                          ### Public constructors                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------|
| [Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#Builder())`()` |

|                                                               ### Public functions                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [LiveGenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig)                 | [build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#build())`()` Create a new [LiveGenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig) with the attached arguments.                                                 |
| [LiveGenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder) | [setCandidateCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setCandidateCount(kotlin.Int))`(candidateCount: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?)`                                                                                             |
| [LiveGenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder) | [setFrequencyPenalty](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setFrequencyPenalty(kotlin.Float))`(frequencyPenalty: `[Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)`?)`                                                                                 |
| [LiveGenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder) | [setMaxOutputTokens](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setMaxOutputTokens(kotlin.Int))`(maxOutputTokens: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?)`                                                                                          |
| [LiveGenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder) | [setPresencePenalty](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setPresencePenalty(kotlin.Float))`(presencePenalty: `[Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)`?)`                                                                                    |
| [LiveGenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder) | [setResponseModality](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setResponseModality(com.google.firebase.vertexai.type.ResponseModality))`(responseModality: `[ResponseModality](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ResponseModality)`?)` |
| [LiveGenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder) | [setSpeechConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setSpeechConfig(com.google.firebase.vertexai.type.SpeechConfig))`(speechConfig: `[SpeechConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SpeechConfig)`?)`                         |
| [LiveGenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder) | [setTemperature](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setTemperature(kotlin.Float))`(temperature: `[Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)`?)`                                                                                                |
| [LiveGenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder) | [setTopK](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setTopK(kotlin.Int))`(topK: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?)`                                                                                                                           |
| [LiveGenerationConfig.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder) | [setTopP](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setTopP(kotlin.Float))`(topP: `[Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)`?)`                                                                                                                     |

|                                                    ### Public properties                                                    |
|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?`                                               | [candidateCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#candidateCount()) See [LiveGenerationConfig.candidateCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#candidateCount()).        |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)`?`                                           | [frequencyPenalty](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#frequencyPenalty()) See [LiveGenerationConfig.frequencyPenalty](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#frequencyPenalty()) |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?`                                               | [maxOutputTokens](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#maxOutputTokens()) See [LiveGenerationConfig.maxOutputTokens](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#maxOutputTokens()).    |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)`?`                                           | [presencePenalty](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#presencePenalty()) See [LiveGenerationConfig.presencePenalty](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#presencePenalty())     |
| [ResponseModality](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ResponseModality)`?` | [responseModality](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#responseModality()) See [LiveGenerationConfig.responseModality](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#responseModality()) |
| [SpeechConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SpeechConfig)`?`         | [speechConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#speechConfig()) See [LiveGenerationConfig.speechConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#speechConfig())                 |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)`?`                                           | [temperature](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#temperature()) See [LiveGenerationConfig.temperature](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#temperature()).                    |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?`                                               | [topK](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#topK()) See [LiveGenerationConfig.topK](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#topK()).                                                |
| [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html)`?`                                           | [topP](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#topP()) See [LiveGenerationConfig.topP](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#topP()).                                                |

## Public constructors

### Builder

```
Builder()
```  

## Public functions

### build

```
funÂ build():Â LiveGenerationConfig
```

Create a new [LiveGenerationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig) with the attached arguments.  

### setCandidateCount

```
funÂ setCandidateCount(candidateCount:Â Int?):Â LiveGenerationConfig.Builder
```  

### setFrequencyPenalty

```
funÂ setFrequencyPenalty(frequencyPenalty:Â Float?):Â LiveGenerationConfig.Builder
```  

### setMaxOutputTokens

```
funÂ setMaxOutputTokens(maxOutputTokens:Â Int?):Â LiveGenerationConfig.Builder
```  

### setPresencePenalty

```
funÂ setPresencePenalty(presencePenalty:Â Float?):Â LiveGenerationConfig.Builder
```  

### setResponseModality

```
funÂ setResponseModality(responseModality:Â ResponseModality?):Â LiveGenerationConfig.Builder
```  

### setSpeechConfig

```
funÂ setSpeechConfig(speechConfig:Â SpeechConfig?):Â LiveGenerationConfig.Builder
```  

### setTemperature

```
funÂ setTemperature(temperature:Â Float?):Â LiveGenerationConfig.Builder
```  

### setTopK

```
funÂ setTopK(topK:Â Int?):Â LiveGenerationConfig.Builder
```  

### setTopP

```
funÂ setTopP(topP:Â Float?):Â LiveGenerationConfig.Builder
```  

## Public properties

### candidateCount

```
varÂ candidateCount:Â Int?
```

See [LiveGenerationConfig.candidateCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#candidateCount()).  

### frequencyPenalty

```
varÂ frequencyPenalty:Â Float?
```

See [LiveGenerationConfig.frequencyPenalty](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#frequencyPenalty())  

### maxOutputTokens

```
varÂ maxOutputTokens:Â Int?
```

See [LiveGenerationConfig.maxOutputTokens](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#maxOutputTokens()).  

### presencePenalty

```
varÂ presencePenalty:Â Float?
```

See [LiveGenerationConfig.presencePenalty](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#presencePenalty())  

### responseModality

```
varÂ responseModality:Â ResponseModality?
```

See [LiveGenerationConfig.responseModality](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#responseModality())  

### speechConfig

```
varÂ speechConfig:Â SpeechConfig?
```

See [LiveGenerationConfig.speechConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#speechConfig())  

### temperature

```
varÂ temperature:Â Float?
```

See [LiveGenerationConfig.temperature](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#temperature()).  

### topK

```
varÂ topK:Â Int?
```

See [LiveGenerationConfig.topK](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#topK()).  

### topP

```
varÂ topP:Â Float?
```

See [LiveGenerationConfig.topP](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#topP()).