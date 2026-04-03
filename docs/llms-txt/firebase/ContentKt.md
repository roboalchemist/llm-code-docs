# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ContentKt.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ContentKt.md.txt

# ContentKt

# ContentKt


```
public final class ContentKt
```

<br />

*** ** * ** ***

## Summary

|                                                                                               ### Public methods                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Content](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content) | [content](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ContentKt#content(kotlin.String,kotlin.Function1))`(` ` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` role,` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Content.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content.Builder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)` Function to build a new [Content](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content) instances in a DSL-like manner. |

## Public methods

### content

```
publicÂ staticÂ finalÂ @NonNull ContentÂ content(
Â Â Â Â StringÂ role,
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull Content.Builder,Â Unit>Â init
)
```

Function to build a new [Content](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content) instances in a DSL-like manner.

Contains a collection of text, image, and binary parts.

Example usage:  

```text
content("user") {
  text("Example string")
)
```