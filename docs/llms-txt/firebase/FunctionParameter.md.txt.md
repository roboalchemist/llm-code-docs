# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionParameter.md.txt

# FunctionParameter

# FunctionParameter


```
public final class FunctionParameter<T extends Object>
```

<br />

*** ** * ** ***

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionParameter#description()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionParameter#name()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionType<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionParameter#type()` |

| ### Public constructors |
|---|
| `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionParameter#FunctionParameter(kotlin.String,kotlin.String,com.google.firebase.vertexai.type.FunctionType)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html description, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionType<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> type )` |

## Public fields

### description

```
public final @NonNull String description
```

### name

```
public final @NonNull String name
```

### type

```
public final @NonNull FunctionType<@NonNull T> type
```

## Public constructors

### FunctionParameter

```
public <T extends Object> FunctionParameter(
    @NonNull String name,
    @NonNull String description,
    @NonNull FunctionType<@NonNull T> type
)
```