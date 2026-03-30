# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart.md.txt

# FunctionResponsePart

# FunctionResponsePart


```
public final class FunctionResponsePart implements Part
```

<br />

*** ** * ** ***

Represents function call output to be returned to the model when it requests a function call.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart.Companion` |

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart#id()` |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart#isThought()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart#name()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart#parts()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-object/index.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart#response()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart#FunctionResponsePart(kotlin.String,kotlinx.serialization.json.JsonObject,kotlin.String,kotlin.collections.List)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-object/index.html response, https://developer.android.com/reference/kotlin/java/lang/String.html id, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part> parts )` |

## Public fields

### id

```
public final String id
```

### isThought

```
public boolean isThought
```

### name

```
public final @NonNull String name
```

### parts

```
public final @NonNull List<@NonNull Part> parts
```

### response

```
public final @NonNull JsonObject response
```

## Public constructors

### FunctionResponsePart

```
public FunctionResponsePart(
    @NonNull String name,
    @NonNull JsonObject response,
    String id,
    @NonNull List<@NonNull Part> parts
)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name` | The name of the called function. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-object/index.html response` | The response produced by the function as a `https://developer.android.com/reference/kotlin/org/json/JSONObject.html`. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html id` | Matching `id` for a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart`, if one was provided. |