# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/PromptFeedback.md.txt

# PromptFeedback

# PromptFeedback


```
class PromptFeedback
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Feedback on the prompt provided in the request.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/PromptFeedback#PromptFeedback(com.google.firebase.vertexai.type.BlockReason,kotlin.collections.List,kotlin.String)( blockReason: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockReason?, safetyRatings: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetyRating>, blockReasonMessage: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? )` |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockReason?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/PromptFeedback#blockReason()` The reason that content was blocked, if at all. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/PromptFeedback#blockReasonMessage()` A message describing the reason that content was blocked, if any. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetyRating>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/PromptFeedback#safetyRatings()` A list of relevant `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetyRating`. |

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
| `blockReason: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockReason?` | The reason that content was blocked, if at all. |
| `safetyRatings: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetyRating>` | A list of relevant `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetyRating`. |
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

A list of relevant `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetyRating`.