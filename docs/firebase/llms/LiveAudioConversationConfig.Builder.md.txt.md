# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder.md.txt

# LiveAudioConversationConfig.Builder

# LiveAudioConversationConfig.Builder


```
public final class LiveAudioConversationConfig.Builder
```

<br />

*** ** * ** ***

Builder for creating a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig`.

Mainly intended for Java interop. Kotlin consumers should use `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/package-summary#liveAudioConversationConfig(kotlin.Function1)` for a more idiomatic experience.

## Summary

| ### Public fields |
|---|---|
| `final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#enableInterruptions()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig#enableInterruptions()`. |
| `final Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#functionCallHandler()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig#functionCallHandler()`. |
| `final Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerGoAway, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#goAwayHandler()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig#goAwayHandler()`. |
| `final Function2<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/media/AudioRecord.Builder.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/media/AudioTrack.Builder.html, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#initializationHandler()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig#initializationHandler()`. |
| `final Function2<https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#transcriptHandler()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig#transcriptHandler()`. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#Builder()()` |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#build()()` Create a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig` with the attached arguments. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#setEnableInterruptions(kotlin.Boolean)(boolean enableInterruptions)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#setFunctionCallHandler(kotlin.Function1)( Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionCallHandler )` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#setGoAwayHandler(kotlin.Function1)( Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerGoAway, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> goAwayHandler )` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#setInitializationHandler(kotlin.Function2)( Function2<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/media/AudioRecord.Builder.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/media/AudioTrack.Builder.html, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> initializationHandler )` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder#setTranscriptHandler(kotlin.Function2)( Function2<https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> transcriptHandler )` |

## Public fields

### enableInterruptions

```
public final boolean enableInterruptions
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig#enableInterruptions()`.

### functionCallHandler

```
public final Function1<@NonNull FunctionCallPart, @NonNull FunctionResponsePart> functionCallHandler
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig#functionCallHandler()`.

### goAwayHandler

```
public final Function1<@NonNull LiveServerGoAway, Unit> goAwayHandler
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig#goAwayHandler()`.

### initializationHandler

```
public final Function2<@NonNull AudioRecord.Builder, @NonNull AudioTrack.Builder, Unit> initializationHandler
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig#initializationHandler()`.

### transcriptHandler

```
public final Function2<Transcription, Transcription, Unit> transcriptHandler
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig#transcriptHandler()`.

## Public constructors

### Builder

```
public Builder()
```

## Public methods

### build

```
public final @NonNull LiveAudioConversationConfig build()
```

Create a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig` with the attached arguments.

### setEnableInterruptions

```
public final @NonNull LiveAudioConversationConfig.Builder setEnableInterruptions(boolean enableInterruptions)
```

### setFunctionCallHandler

```
public final @NonNull LiveAudioConversationConfig.Builder setFunctionCallHandler(
    Function1<@NonNull FunctionCallPart, @NonNull FunctionResponsePart> functionCallHandler
)
```

### setGoAwayHandler

```
public final @NonNull LiveAudioConversationConfig.Builder setGoAwayHandler(
    Function1<@NonNull LiveServerGoAway, Unit> goAwayHandler
)
```

### setInitializationHandler

```
public final @NonNull LiveAudioConversationConfig.Builder setInitializationHandler(
    Function2<@NonNull AudioRecord.Builder, @NonNull AudioTrack.Builder, Unit> initializationHandler
)
```

### setTranscriptHandler

```
public final @NonNull LiveAudioConversationConfig.Builder setTranscriptHandler(
    Function2<Transcription, Transcription, Unit> transcriptHandler
)
```