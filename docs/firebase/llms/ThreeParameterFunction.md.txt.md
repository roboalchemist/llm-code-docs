# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ThreeParameterFunction.md.txt

# ThreeParameterFunction

# ThreeParameterFunction


```
public final class ThreeParameterFunction<T extends Object, U extends Object, V extends Object> extends FunctionDeclaration
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.vertexai.type.FunctionDeclaration](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclaration) ||
|   | ↳ | [com.google.firebase.vertexai.type.ThreeParameterFunction](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ThreeParameterFunction) |

*** ** * ** ***

A declared three param function, including implementation, that a model can be given access to in order to gain info or complete tasks.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/package-summary#defineFunction(kotlin.String,kotlin.String,kotlin.coroutines.SuspendFunction0)` | for how to create an instance of this class. |

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-suspend-function3/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html U, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html V, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/org/json/JSONObject.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ThreeParameterFunction#function()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ThreeParameterFunction#param1()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html U>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ThreeParameterFunction#param2()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html V>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ThreeParameterFunction#param3()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/org/json/JSONObject.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ThreeParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart part)` Run the attached function with the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ThreeParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart)`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<https://developer.android.com/reference/kotlin/java/lang/Object.html>>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ThreeParameterFunction#getParameters()()` The parameters of the attached function as a list of `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema`. |

| ### Inherited fields |
|---|
| From [com.google.firebase.vertexai.type.FunctionDeclaration](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclaration) |---|---| | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclaration#description()` | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclaration#name()` | |

## Public fields

### function

```
public final @NonNull SuspendFunction3<@NonNull T, @NonNull U, @NonNull V, @NonNull JSONObject> function
```

### param1

```
public final @NonNull Schema<@NonNull T> param1
```

### param2

```
public final @NonNull Schema<@NonNull U> param2
```

### param3

```
public final @NonNull Schema<@NonNull V> param3
```

## Public methods

### execute

```
public @NonNull JSONObject execute(@NonNull FunctionCallPart part)
```

Run the attached function with the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ThreeParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart)`.

### getParameters

```
public @NonNull List<@NonNull Schema<Object>> getParameters()
```

The parameters of the attached function as a list of `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema`.