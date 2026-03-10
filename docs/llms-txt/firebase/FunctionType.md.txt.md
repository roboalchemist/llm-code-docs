# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionType.md.txt

# FunctionType

# FunctionType


```
public final class FunctionType<T extends Object>
```

<br />

*** ** * ** ***

Represents and passes the type information for an automated function call.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionType.Companion` |

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionType#name()` : the enum name of the type |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<https://developer.android.com/reference/kotlin/java/lang/String.html, T>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionType#parse()` : the deserialization function |

| ### Public constructors |
|---|
| `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionType#FunctionType(kotlin.String,kotlin.Function1)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<https://developer.android.com/reference/kotlin/java/lang/String.html, T> parse )` |

## Public fields

### name

```
public final @NonNull String name
```

: the enum name of the type

### parse

```
public final @NonNull Function1<String, T> parse
```

: the deserialization function

## Public constructors

### FunctionType

```
public <T extends Object> FunctionType(
    @NonNull String name,
    @NonNull Function1<String, T> parse
)
```