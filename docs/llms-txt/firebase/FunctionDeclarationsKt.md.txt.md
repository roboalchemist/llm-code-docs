# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclarationsKt.md.txt

# FunctionDeclarationsKt

# FunctionDeclarationsKt


```
public final class FunctionDeclarationsKt
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/NoParameterFunction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclarationsKt#defineFunction(kotlin.String,kotlin.String,kotlin.coroutines.SuspendFunction0)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html description, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-suspend-function0/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/org/json/JSONObject.html> function )` Defines a function with zero parameters, including its implementation, that a model can be given access to in order to gain info or complete tasks. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/OneParameterFunction<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclarationsKt#defineFunction(kotlin.String,kotlin.String,com.google.firebase.vertexai.type.Schema,kotlin.coroutines.SuspendFunction1)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html description, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> arg1, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-suspend-function1/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/org/json/JSONObject.html> function )` Defines a function with one parameter, including its implementation, that a model can be given access to in order to gain info or complete tasks. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/TwoParameterFunction<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html U>` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html, U extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclarationsKt#defineFunction(kotlin.String,kotlin.String,com.google.firebase.vertexai.type.Schema,com.google.firebase.vertexai.type.Schema,kotlin.coroutines.SuspendFunction2)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html description, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> arg1, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html U> arg2, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-suspend-function2/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html U, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/org/json/JSONObject.html> function )` Defines a function with two parameters, including its implementation, that a model can be given access to in order to gain info or complete tasks. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ThreeParameterFunction<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html U, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html W>` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html, U extends https://developer.android.com/reference/kotlin/java/lang/Object.html, W extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclarationsKt#defineFunction(kotlin.String,kotlin.String,com.google.firebase.vertexai.type.Schema,com.google.firebase.vertexai.type.Schema,com.google.firebase.vertexai.type.Schema,kotlin.coroutines.SuspendFunction3)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html description, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> arg1, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html U> arg2, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html W> arg3, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-suspend-function3/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html U, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html W, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/org/json/JSONObject.html> function )` Defines a function with three parameters, including its implementation, that a model can be given access to in order to gain info or complete tasks. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FourParameterFunction<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html U, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html W, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Z>` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html, U extends https://developer.android.com/reference/kotlin/java/lang/Object.html, W extends https://developer.android.com/reference/kotlin/java/lang/Object.html, Z extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclarationsKt#defineFunction(kotlin.String,kotlin.String,com.google.firebase.vertexai.type.Schema,com.google.firebase.vertexai.type.Schema,com.google.firebase.vertexai.type.Schema,com.google.firebase.vertexai.type.Schema,kotlin.coroutines.SuspendFunction4)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html description, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> arg1, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html U> arg2, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html W> arg3, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Z> arg4, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-suspend-function4/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html U, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html W, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Z, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/org/json/JSONObject.html> function )` Defines a function with four parameters, including its implementation, that a model can be given access to in order to gain info or complete tasks. |

## Public methods

### defineFunction

```
public static final @NonNull NoParameterFunction defineFunction(
    @NonNull String name,
    @NonNull String description,
    @NonNull SuspendFunction0<@NonNull JSONObject> function
)
```

Defines a function with zero parameters, including its implementation, that a model can be given access to in order to gain info or complete tasks.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name` | The name of the function call, this should be clear and descriptive for the model |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html description` | A description of what the function does and its output. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-suspend-function0/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/org/json/JSONObject.html> function` | the function implementation |

### defineFunction

```
public static final @NonNull OneParameterFunction<@NonNull T> <T extends Object> defineFunction(
    @NonNull String name,
    @NonNull String description,
    @NonNull Schema<@NonNull T> arg1,
    @NonNull SuspendFunction1<@NonNull T, @NonNull JSONObject> function
)
```

Defines a function with one parameter, including its implementation, that a model can be given access to in order to gain info or complete tasks.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name` | The name of the function call, this should be clear and descriptive for the model |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html description` | A description of what the function does and its output. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> arg1` | A description of the first function parameter |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-suspend-function1/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/org/json/JSONObject.html> function` | the function implementation |

### defineFunction

```
public static final @NonNull TwoParameterFunction<@NonNull T, @NonNull U> <T extends Object, U extends Object> defineFunction(
    @NonNull String name,
    @NonNull String description,
    @NonNull Schema<@NonNull T> arg1,
    @NonNull Schema<@NonNull U> arg2,
    @NonNull SuspendFunction2<@NonNull T, @NonNull U, @NonNull JSONObject> function
)
```

Defines a function with two parameters, including its implementation, that a model can be given access to in order to gain info or complete tasks.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name` | The name of the function call, this should be clear and descriptive for the model |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html description` | A description of what the function does and its output. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> arg1` | A description of the first function parameter |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html U> arg2` | A description of the second function parameter |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-suspend-function2/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html U, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/org/json/JSONObject.html> function` | the function implementation |

### defineFunction

```
public static final @NonNull ThreeParameterFunction<@NonNull T, @NonNull U, @NonNull W> <T extends Object, U extends Object, W extends Object> defineFunction(
    @NonNull String name,
    @NonNull String description,
    @NonNull Schema<@NonNull T> arg1,
    @NonNull Schema<@NonNull U> arg2,
    @NonNull Schema<@NonNull W> arg3,
    @NonNull SuspendFunction3<@NonNull T, @NonNull U, @NonNull W, @NonNull JSONObject> function
)
```

Defines a function with three parameters, including its implementation, that a model can be given access to in order to gain info or complete tasks.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name` | The name of the function call, this should be clear and descriptive for the model |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html description` | A description of what the function does and its output. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> arg1` | A description of the first function parameter |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html U> arg2` | A description of the second function parameter |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html W> arg3` | A description of the third function parameter |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-suspend-function3/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html U, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html W, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/org/json/JSONObject.html> function` | the function implementation |

### defineFunction

```
public static final @NonNull FourParameterFunction<@NonNull T, @NonNull U, @NonNull W, @NonNull Z> <T extends Object, U extends Object, W extends Object, Z extends Object> defineFunction(
    @NonNull String name,
    @NonNull String description,
    @NonNull Schema<@NonNull T> arg1,
    @NonNull Schema<@NonNull U> arg2,
    @NonNull Schema<@NonNull W> arg3,
    @NonNull Schema<@NonNull Z> arg4,
    @NonNull SuspendFunction4<@NonNull T, @NonNull U, @NonNull W, @NonNull Z, @NonNull JSONObject> function
)
```

Defines a function with four parameters, including its implementation, that a model can be given access to in order to gain info or complete tasks.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name` | The name of the function call, this should be clear and descriptive for the model |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html description` | A description of what the function does and its output. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> arg1` | A description of the first function parameter |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html U> arg2` | A description of the second function parameter |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html W> arg3` | A description of the third function parameter |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Z> arg4` | A description of the fourth function parameter |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-suspend-function4/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html U, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html W, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Z, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/org/json/JSONObject.html> function` | the function implementation |