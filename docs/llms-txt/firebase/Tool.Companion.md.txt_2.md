# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Tool.Companion.md.txt

# Tool.Companion

# Tool.Companion


```
public static class Tool.Companion
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Tool` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Tool.Companion#functionDeclarations(kotlin.collections.List)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclaration> functionDeclarations )` Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Tool` instance that provides the model with access to the `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Tool.Companion#functionDeclarations(kotlin.collections.List)`. |

## Public methods

### functionDeclarations

```
public static final @NonNull Tool functionDeclarations(
    @NonNull List<@NonNull FunctionDeclaration> functionDeclarations
)
```

Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Tool` instance that provides the model with access to the `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Tool.Companion#functionDeclarations(kotlin.collections.List)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclaration> functionDeclarations` | The list of functions that this tool allows the model access to. |