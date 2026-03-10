# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/TemplateGenerativeModelFutures.md.txt

# TemplateGenerativeModelFutures

# TemplateGenerativeModelFutures


```
public abstract class TemplateGenerativeModelFutures
```

<br />

*** ** * ** ***

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateGenerativeModel`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateGenerativeModel` |   |

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/TemplateGenerativeModelFutures.Companion` |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/TemplateGenerativeModelFutures` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/TemplateGenerativeModelFutures.Companion#from(com.google.firebase.ai.TemplateGenerativeModel)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateGenerativeModel model)` |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/TemplateGenerativeModelFutures#generateContent(kotlin.String,kotlin.collections.Map)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html templateId, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> inputs )` Generates new content using the given templateId with the given inputs. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/TemplateGenerativeModelFutures#generateContentStream(kotlin.String,kotlin.collections.Map)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html templateId, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> inputs )` Generates new content as a stream using the given templateId with the given inputs. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateGenerativeModel` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/TemplateGenerativeModelFutures#getGenerativeModel()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateGenerativeModel` object wrapped by this object. |

## Public methods

### from

```
public static final @NonNull TemplateGenerativeModelFutures from(@NonNull TemplateGenerativeModel model)
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/TemplateGenerativeModelFutures` | a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/TemplateGenerativeModelFutures` created around the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateGenerativeModel` |

### generateContent

```
public abstract @NonNull ListenableFuture<@NonNull GenerateContentResponse> generateContent(
    @NonNull String templateId,
    @NonNull Map<@NonNull String, @NonNull Object> inputs
)
```

Generates new content using the given templateId with the given inputs.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html templateId` | The ID of server prompt template. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> inputs` | the inputs needed to fill in the prompt |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse>` | The content generated by the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException com.google.firebase.ai.type.FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### generateContentStream

```
public abstract @NonNull Publisher<@NonNull GenerateContentResponse> generateContentStream(
    @NonNull String templateId,
    @NonNull Map<@NonNull String, @NonNull Object> inputs
)
```

Generates new content as a stream using the given templateId with the given inputs.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html templateId` | The ID of server prompt template. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> inputs` | the inputs needed to fill in the prompt |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse>` | A `https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher` which will emit responses as they are returned by the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException com.google.firebase.ai.type.FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### getGenerativeModel

```
public abstract @NonNull TemplateGenerativeModel getGenerativeModel()
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/TemplateGenerativeModel` object wrapped by this object.