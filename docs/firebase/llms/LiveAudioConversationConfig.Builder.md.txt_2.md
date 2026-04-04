# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder.md.txt

# LiveAudioConversationConfig.Builder

# LiveAudioConversationConfig.Builder


```
class LiveAudioConversationConfig.Builder
```

<br />

*** ** * ** ***

Builder for creating a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig`.

Mainly intended for Java interop. Kotlin consumers should use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/package-summary#liveAudioConversationConfig(kotlin.Function1)` for a more idiomatic experience.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#Builder()()` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#build()()` Create a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig` with the attached arguments. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#setEnableInterruptions(kotlin.Boolean)(enableInterruptions: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#setFunctionCallHandler(kotlin.Function1)( functionCallHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)? )` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#setGoAwayHandler(kotlin.Function1)(goAwayHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerGoAway) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#setInitializationHandler(kotlin.Function2)( initializationHandler: ((https://developer.android.com/reference/kotlin/android/media/AudioRecord.Builder.html, https://developer.android.com/reference/kotlin/android/media/AudioTrack.Builder.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)? )` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#setTranscriptHandler(kotlin.Function2)( transcriptHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)? )` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#enableInterruptions()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig#enableInterruptions()`. |
| `((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#functionCallHandler()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig#functionCallHandler()`. |
| `((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerGoAway) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#goAwayHandler()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig#goAwayHandler()`. |
| `((https://developer.android.com/reference/kotlin/android/media/AudioRecord.Builder.html, https://developer.android.com/reference/kotlin/android/media/AudioTrack.Builder.html) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#initializationHandler()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig#initializationHandler()`. |
| `((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#transcriptHandler()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig#transcriptHandler()`. |

## Public constructors

### Builder

```
Builder()
```

## Public functions

### build

```
fun build(): LiveAudioConversationConfig
```

Create a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig` with the attached arguments.

### setEnableInterruptions

```
fun setEnableInterruptions(enableInterruptions: Boolean): LiveAudioConversationConfig.Builder
```

### setFunctionCallHandler

```
fun setFunctionCallHandler(
    functionCallHandler: ((FunctionCallPart) -> FunctionResponsePart)?
): LiveAudioConversationConfig.Builder
```

### setGoAwayHandler

```
fun setGoAwayHandler(goAwayHandler: ((LiveServerGoAway) -> Unit)?): LiveAudioConversationConfig.Builder
```

### setInitializationHandler

```
fun setInitializationHandler(
    initializationHandler: ((AudioRecord.Builder, AudioTrack.Builder) -> Unit)?
): LiveAudioConversationConfig.Builder
```

### setTranscriptHandler

```
fun setTranscriptHandler(
    transcriptHandler: ((Transcription?, Transcription?) -> Unit)?
): LiveAudioConversationConfig.Builder
```

## Public properties

### enableInterruptions

```
var enableInterruptions: Boolean
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig#enableInterruptions()`.

### functionCallHandler

```
var functionCallHandler: ((FunctionCallPart) -> FunctionResponsePart)?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig#functionCallHandler()`.

### goAwayHandler

```
var goAwayHandler: ((LiveServerGoAway) -> Unit)?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig#goAwayHandler()`.

### initializationHandler

```
var initializationHandler: ((AudioRecord.Builder, AudioTrack.Builder) -> Unit)?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig#initializationHandler()`.

### transcriptHandler

```
var transcriptHandler: ((Transcription?, Transcription?) -> Unit)?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig#transcriptHandler()`.