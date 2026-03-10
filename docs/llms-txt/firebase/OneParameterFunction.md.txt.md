# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/OneParameterFunction.md.txt

# OneParameterFunction

# OneParameterFunction


```
public final class OneParameterFunction<T extends Object> extends FunctionDeclaration
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.vertexai.type.FunctionDeclaration](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclaration) ||
|   | ↳ | [com.google.firebase.vertexai.type.OneParameterFunction](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/OneParameterFunction) |

*** ** * ** ***

A declared one param function, including implementation, that a model can be given access to in order to gain info or complete tasks.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/package-summary#defineFunction(kotlin.String,kotlin.String,kotlin.coroutines.SuspendFunction0)` | for how to create an instance of this class. |

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-suspend-function1/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/org/json/JSONObject.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/OneParameterFunction#function()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/OneParameterFunction#param()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/org/json/JSONObject.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/OneParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart part)` Run the attached function with the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/OneParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart)`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/OneParameterFunction#getParameters()()` The parameters of the attached function as a list of `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema`. |

| ### Inherited fields |
|---|
| From [com.google.firebase.vertexai.type.FunctionDeclaration](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclaration) |---|---| | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclaration#description()` | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclaration#name()` | |

## Public fields

### function

```
public final @NonNull SuspendFunction1<@NonNull T, @NonNull JSONObject> function
```

### param

```
public final @NonNull Schema<@NonNull T> param
```

## Public methods

### execute

```
public @NonNull JSONObject execute(@NonNull FunctionCallPart part)
```

Run the attached function with the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/OneParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart)`.

### getParameters

```
public @NonNull List<@NonNull Schema<@NonNull T>> getParameters()
```

The parameters of the attached function as a list of `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema`.