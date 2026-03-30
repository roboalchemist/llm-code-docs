# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/PromptFeedback.md.txt

# PromptFeedback

# PromptFeedback


```
class PromptFeedback
```

<br />

*** ** * ** ***

Feedback on the prompt provided in the request.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/PromptFeedback#PromptFeedback(com.google.firebase.ai.type.BlockReason,kotlin.collections.List,kotlin.String)( blockReason: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/BlockReason?, safetyRatings: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating>, blockReasonMessage: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? )` |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/BlockReason?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/PromptFeedback#blockReason()` The reason that content was blocked, if at all. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/PromptFeedback#blockReasonMessage()` A message describing the reason that content was blocked, if any. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/PromptFeedback#safetyRatings()` A list of relevant `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating`. |

## Public constructors

### PromptFeedback

```
PromptFeedback(
    blockReason: BlockReason?,
    safetyRatings: List<SafetyRating>,
    blockReasonMessage: String?
)
```

| Parameters |
|---|---|
| `blockReason: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/BlockReason?` | The reason that content was blocked, if at all. |
| `safetyRatings: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating>` | A list of relevant `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating`. |
| `blockReasonMessage: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | A message describing the reason that content was blocked, if any. |

## Public properties

### blockReason

```
val blockReason: BlockReason?
```

The reason that content was blocked, if at all.

### blockReasonMessage

```
val blockReasonMessage: String?
```

A message describing the reason that content was blocked, if any.

### safetyRatings

```
val safetyRatings: List<SafetyRating>
```

A list of relevant `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating`.