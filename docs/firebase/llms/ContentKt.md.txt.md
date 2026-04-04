# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ContentKt.md.txt

# ContentKt

# ContentKt


```
public final class ContentKt
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ContentKt#content(kotlin.String,kotlin.Function1)( https://developer.android.com/reference/kotlin/java/lang/String.html role, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Function to build a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` instances in a DSL-like manner. |

## Public methods

### content

```
public static final @NonNull Content content(
    String role,
    @ExtensionFunctionType @NonNull Function1<@NonNull Content.Builder, Unit> init
)
```

Function to build a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` instances in a DSL-like manner.

Contains a collection of text, image, and binary parts.

Example usage:

```
content("user") {
  text("Example string")
)
```