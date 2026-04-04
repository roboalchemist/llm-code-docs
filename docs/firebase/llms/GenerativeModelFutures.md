# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/GenerativeModelFutures.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/GenerativeModelFutures.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/GenerativeModelFutures.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures.md.txt

# GenerativeModelFutures

# GenerativeModelFutures


```
abstract class GenerativeModelFutures
```

<br />

*** ** * ** ***

Wrapper class providing Java compatible methods for [GenerativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel).  

|                                                  See also                                                   |
|-------------------------------------------------------------------------------------------------------------|---|
| [GenerativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel) |   |

## Summary

|                                                 ### Public companion functions                                                 |
|--------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GenerativeModelFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures) | [from](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures.Companion#from(com.google.firebase.ai.GenerativeModel))`(model: `[GenerativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel)`)` |

|                                                                                                                           ### Public functions                                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[CountTokensResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse)`>`         | [countTokens](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures#countTokens(com.google.firebase.ai.type.Content,kotlin.Array))`(prompt: `[Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)`, vararg prompts: `[Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)`)` Counts the number of tokens in a prompt using the model's tokenizer.                                                                                                                                                                                                   |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[GenerateContentResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse)`>` | [generateContent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures#generateContent(com.google.firebase.ai.type.Content,kotlin.Array))`(prompt: `[Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)`, vararg prompts: `[Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)`)` Generates new content from the input [Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content) given to the model as a prompt.                                                                                          |
| `abstract `[Publisher](https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher)`<`[GenerateContentResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse)`>`                             | [generateContentStream](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures#generateContentStream(com.google.firebase.ai.type.Content,kotlin.Array))`(prompt: `[Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)`, vararg prompts: `[Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)`)` Generates new content as a stream from the input [Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content) given to the model as a prompt.                                                                  |
| `abstract `[GenerativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel)                                                                                                                                                    | [getGenerativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures#getGenerativeModel())`()` Returns the [GenerativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel) object wrapped by this object.                                                                                                                                                                                                                                                                                                                                                                                 |
| `abstract `[ChatFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures)                                                                                                                                                       | [startChat](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures#startChat())`()` Creates a [ChatFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures) instance which internally tracks the ongoing conversation with the model.                                                                                                                                                                                                                                                                                                                                                             |
| `abstract `[ChatFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures)                                                                                                                                                       | [startChat](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures#startChat(kotlin.collections.List))`(history: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)`>)` Creates a [ChatFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures) instance, initialized using the optionally provided [history](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures#startChat(kotlin.collections.List)). |

## Public companion functions

### from

```
funÂ from(model:Â GenerativeModel):Â GenerativeModelFutures
```  

|                                                            Returns                                                             |
|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GenerativeModelFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures) | a [GenerativeModelFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures) created around the provided [GenerativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel) |

## Public functions

### countTokens

```
abstractÂ funÂ countTokens(prompt:Â Content,Â varargÂ prompts:Â Content):Â ListenableFuture<CountTokensResponse>
```

Counts the number of tokens in a prompt using the model's tokenizer.  

|                                                 Parameters                                                 |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| `prompt: `[Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content) | The input(s) given to the model as a prompt. |

|                                                                                                                        Returns                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[CountTokensResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse)`>` | The [CountTokensResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse) of running the model's tokenizer on the input. |

|                                                                                                 Throws                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| `com.google.firebase.ai.type.FirebaseAIException: `[com.google.firebase.ai.type.FirebaseAIException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException) | if the request failed. |

### generateContent

```
abstractÂ funÂ generateContent(prompt:Â Content,Â varargÂ prompts:Â Content):Â ListenableFuture<GenerateContentResponse>
```

Generates new content from the input [Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content) given to the model as a prompt.  

|                                                 Parameters                                                 |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| `prompt: `[Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content) | The input(s) given to the model as a prompt. |

|                                                                                                                            Returns                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| [ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[GenerateContentResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse)`>` | The content generated by the model. |

|                                                                                                 Throws                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| `com.google.firebase.ai.type.FirebaseAIException: `[com.google.firebase.ai.type.FirebaseAIException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException) | if the request failed. |

### generateContentStream

```
abstractÂ funÂ generateContentStream(prompt:Â Content,Â varargÂ prompts:Â Content):Â Publisher<GenerateContentResponse>
```

Generates new content as a stream from the input [Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content) given to the model as a prompt.  

|                                                 Parameters                                                 |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| `prompt: `[Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content) | The input(s) given to the model as a prompt. |

|                                                                                                              Returns                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Publisher](https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher)`<`[GenerateContentResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse)`>` | A [Publisher](https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher) which will emit responses as they are returned by the model. |

|                                                                                                 Throws                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| `com.google.firebase.ai.type.FirebaseAIException: `[com.google.firebase.ai.type.FirebaseAIException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException) | if the request failed. |

### getGenerativeModel

```
abstractÂ funÂ getGenerativeModel():Â GenerativeModel
```

Returns the [GenerativeModel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel) object wrapped by this object.  

### startChat

```
abstractÂ funÂ startChat():Â ChatFutures
```

Creates a [ChatFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures) instance which internally tracks the ongoing conversation with the model.  

### startChat

```
abstractÂ funÂ startChat(history:Â List<Content>):Â ChatFutures
```

Creates a [ChatFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures) instance, initialized using the optionally provided [history](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures#startChat(kotlin.collections.List)).  

|                                                                                                Parameters                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| `history: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)`>` | A list of previous interactions with the model to use as a starting point |