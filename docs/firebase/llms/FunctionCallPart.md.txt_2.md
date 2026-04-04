# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart.md.txt

# FunctionCallPart

# FunctionCallPart


```
public final class FunctionCallPart implements Part
```

<br />

*** ** * ** ***

Represents function call name and params received from requests.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-element/index.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart#args()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart#id()` |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart#isThought()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart#name()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart#FunctionCallPart(kotlin.String,kotlin.collections.Map,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-element/index.html> args, https://developer.android.com/reference/kotlin/java/lang/String.html id )` |

## Public fields

### args

```
public final @NonNull Map<@NonNull String, @NonNull JsonElement> args
```

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

## Public constructors

### FunctionCallPart

```
public FunctionCallPart(
    @NonNull String name,
    @NonNull Map<@NonNull String, @NonNull JsonElement> args,
    String id
)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name` | the name of the function to call |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-element/index.html> args` | the function parameters and values as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html` |
| `https://developer.android.com/reference/kotlin/java/lang/String.html id` | Unique id of the function call. If present, the returned `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart` should have a matching `id` field. |