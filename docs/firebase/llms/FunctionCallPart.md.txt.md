# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart.md.txt

# FunctionCallPart

# FunctionCallPart


```
public final class FunctionCallPart implements Part
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents function call name and params received from requests.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/kotlinx/serialization/json/JsonElement>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart#args()` the function parameters and values as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart#id()` Unique id of the function call. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart#name()` the name of the function to call |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart#FunctionCallPart(kotlin.String,kotlin.collections.Map,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/kotlinx/serialization/json/JsonElement> args, https://developer.android.com/reference/kotlin/java/lang/String.html id )` |

## Public fields

### args

```
public final @NonNull Map<@NonNull String, @NonNull JsonElement> args
```

the function parameters and values as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html`

### id

```
public final String id
```

Unique id of the function call. If present, the returned `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart` should have a matching `id` field.

### name

```
public final @NonNull String name
```

the name of the function to call

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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/kotlinx/serialization/json/JsonElement> args` | the function parameters and values as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html` |
| `https://developer.android.com/reference/kotlin/java/lang/String.html id` | Unique id of the function call. If present, the returned `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart` should have a matching `id` field. |