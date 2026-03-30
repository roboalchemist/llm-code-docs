# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PromptFeedback.md.txt

# PromptFeedback

# PromptFeedback


```
public final class PromptFeedback
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Feedback on the prompt provided in the request.

## Summary

| ### Public fields |
|---|---|
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockReason` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PromptFeedback#blockReason()` The reason that content was blocked, if at all. |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PromptFeedback#blockReasonMessage()` A message describing the reason that content was blocked, if any. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetyRating>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PromptFeedback#safetyRatings()` A list of relevant `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetyRating`. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PromptFeedback#PromptFeedback(com.google.firebase.vertexai.type.BlockReason,kotlin.collections.List,kotlin.String)( https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockReason blockReason, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetyRating> safetyRatings, https://developer.android.com/reference/kotlin/java/lang/String.html blockReasonMessage )` |

## Public fields

### blockReason

```
public final BlockReason blockReason
```

The reason that content was blocked, if at all.

### blockReasonMessage

```
public final String blockReasonMessage
```

A message describing the reason that content was blocked, if any.

### safetyRatings

```
public final @NonNull List<@NonNull SafetyRating> safetyRatings
```

A list of relevant `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetyRating`.

## Public constructors

### PromptFeedback

```
public PromptFeedback(
    BlockReason blockReason,
    @NonNull List<@NonNull SafetyRating> safetyRatings,
    String blockReasonMessage
)
```

| Parameters |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockReason blockReason` | The reason that content was blocked, if at all. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetyRating> safetyRatings` | A list of relevant `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetyRating`. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html blockReasonMessage` | A message describing the reason that content was blocked, if any. |