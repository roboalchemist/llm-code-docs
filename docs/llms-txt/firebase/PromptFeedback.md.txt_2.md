# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PromptFeedback.md.txt

# PromptFeedback

# PromptFeedback


```
public final class PromptFeedback
```

<br />

*** ** * ** ***

Feedback on the prompt provided in the request.

## Summary

| ### Public fields |
|---|---|
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/BlockReason` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PromptFeedback#blockReason()` The reason that content was blocked, if at all. |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PromptFeedback#blockReasonMessage()` A message describing the reason that content was blocked, if any. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetyRating>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PromptFeedback#safetyRatings()` A list of relevant `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetyRating`. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PromptFeedback#PromptFeedback(com.google.firebase.ai.type.BlockReason,kotlin.collections.List,kotlin.String)( https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/BlockReason blockReason, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetyRating> safetyRatings, https://developer.android.com/reference/kotlin/java/lang/String.html blockReasonMessage )` |

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

A list of relevant `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetyRating`.

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
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/BlockReason blockReason` | The reason that content was blocked, if at all. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetyRating> safetyRatings` | A list of relevant `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetyRating`. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html blockReasonMessage` | A message describing the reason that content was blocked, if any. |