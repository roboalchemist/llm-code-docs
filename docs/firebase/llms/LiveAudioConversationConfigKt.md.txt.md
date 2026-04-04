# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfigKt.md.txt

# LiveAudioConversationConfigKt

# LiveAudioConversationConfigKt


```
public final class LiveAudioConversationConfigKt
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfigKt#liveAudioConversationConfig(kotlin.Function1)( @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Helper method to construct a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig` in a DSL-like manner. |

## Public methods

### liveAudioConversationConfig

```
public static final @NonNull LiveAudioConversationConfig liveAudioConversationConfig(
    @ExtensionFunctionType @NonNull Function1<@NonNull LiveAudioConversationConfig.Builder, Unit> init
)
```

Helper method to construct a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig` in a DSL-like manner.

Example Usage:

```
liveAudioConversationConfig {
  functionCallHandler = ...
  initializationHandler = ...
  ...
}
```