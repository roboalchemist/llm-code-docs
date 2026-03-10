# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ExecutableCodePart.md.txt

# ExecutableCodePart

# ExecutableCodePart


```
public final class ExecutableCodePart implements Part
```

<br />

*** ** * ** ***

Represents the code that was executed by the model.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ExecutableCodePart#code()` The source code to be executed. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ExecutableCodePart#isThought()` Indicates whether the response is a thought. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ExecutableCodePart#language()` The programming language of the code. |

| ### Public constructors |
|---|
| `[ExecutableCodePart](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ExecutableCodePart#ExecutableCodePart(kotlin.String,kotlin.String))(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html language, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html code)` **This method is deprecated.** Part of the model response. |

## Public fields

### code

```
public final @NonNull String code
```

The source code to be executed.

### isThought

```
public boolean isThought
```

Indicates whether the response is a thought.

### language

```
public final @NonNull String language
```

The programming language of the code.

## Public constructors

### ExecutableCodePart

```
public [ExecutableCodePart](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ExecutableCodePart#ExecutableCodePart(kotlin.String,kotlin.String))(@NonNull String language, @NonNull String code)
```

> [!CAUTION]
> **This method is deprecated.**   
> Part of the model response. Do not instantiate directly.