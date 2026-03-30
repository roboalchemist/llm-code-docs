# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart.md.txt

# FunctionResponsePart

# FunctionResponsePart


```
public final class FunctionResponsePart implements Part
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents function call output to be returned to the model when it requests a function call.

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart#id()` Matching `id` for a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart`, if one was provided. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart#name()` The name of the called function. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/kotlinx/serialization/json/JsonObject` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart#response()` The response produced by the function as a `https://developer.android.com/reference/kotlin/org/json/JSONObject.html`. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart#FunctionResponsePart(kotlin.String,kotlinx.serialization.json.JsonObject,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/kotlinx/serialization/json/JsonObject response, https://developer.android.com/reference/kotlin/java/lang/String.html id )` |

## Public fields

### id

```
public final String id
```

Matching `id` for a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart`, if one was provided.

### name

```
public final @NonNull String name
```

The name of the called function.

### response

```
public final @NonNull JsonObject response
```

The response produced by the function as a `https://developer.android.com/reference/kotlin/org/json/JSONObject.html`.

## Public constructors

### FunctionResponsePart

```
public FunctionResponsePart(
    @NonNull String name,
    @NonNull JsonObject response,
    String id
)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name` | The name of the called function. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/kotlinx/serialization/json/JsonObject response` | The response produced by the function as a `https://developer.android.com/reference/kotlin/org/json/JSONObject.html`. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html id` | Matching `id` for a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart`, if one was provided. |