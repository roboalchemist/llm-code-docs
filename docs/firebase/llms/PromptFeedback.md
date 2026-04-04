# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PromptFeedback.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/PromptFeedback.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PromptFeedback.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/PromptFeedback.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/PromptFeedback.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/PromptFeedback.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/PromptFeedback.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/PromptFeedback.md.txt

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

|                                                                                                                                                                                                                                                                                                                                 ### Public constructors                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PromptFeedback](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/PromptFeedback#PromptFeedback(com.google.firebase.ai.type.BlockReason,kotlin.collections.List,kotlin.String))`(` ` blockReason: `[BlockReason](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/BlockReason)`?,` ` safetyRatings: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[SafetyRating](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating)`>,` ` blockReasonMessage: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` `)` |

|                                                                                          ### Public properties                                                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [BlockReason](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/BlockReason)`?`                                                                                              | [blockReason](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/PromptFeedback#blockReason()) The reason that content was blocked, if at all.                                                                                    |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                                                                                                      | [blockReasonMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/PromptFeedback#blockReasonMessage()) A message describing the reason that content was blocked, if any.                                                    |
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[SafetyRating](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating)`>` | [safetyRatings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/PromptFeedback#safetyRatings()) A list of relevant [SafetyRating](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating). |

## Public constructors

### PromptFeedback

```
PromptFeedback(
Â Â Â Â blockReason:Â BlockReason?,
Â Â Â Â safetyRatings:Â List<SafetyRating>,
Â Â Â Â blockReasonMessage:Â String?
)
```  

|                                                                                                        Parameters                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `blockReason: `[BlockReason](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/BlockReason)`?`                                                                                                | The reason that content was blocked, if at all.                                                                                |
| `safetyRatings: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[SafetyRating](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating)`>` | A list of relevant [SafetyRating](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating). |
| `blockReasonMessage: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                                                                                                 | A message describing the reason that content was blocked, if any.                                                              |

## Public properties

### blockReason

```
valÂ blockReason:Â BlockReason?
```

The reason that content was blocked, if at all.  

### blockReasonMessage

```
valÂ blockReasonMessage:Â String?
```

A message describing the reason that content was blocked, if any.  

### safetyRatings

```
valÂ safetyRatings:Â List<SafetyRating>
```

A list of relevant [SafetyRating](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetyRating).