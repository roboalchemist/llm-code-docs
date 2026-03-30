# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Tool.md.txt

# Tool

# Tool


```
public final class Tool
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Contains a set of function declarations that the model has access to. These can be used to gather information, or complete tasks

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Tool.Companion` |

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