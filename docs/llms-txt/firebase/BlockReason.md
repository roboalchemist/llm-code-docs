# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/BlockReason.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/PromptFeedback/BlockReason.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/PromptFeedback/BlockReason.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/BlockReason.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockReason.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockReason.md.txt

# BlockReason

# BlockReason


```
class BlockReason
```

<br />

*** ** * ** ***

| **This class is deprecated.**   
| The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Describes why content was blocked.

## Summary

|                                        ### Public companion properties                                         |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [BlockReason](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockReason) | [BLOCKLIST](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockReason.Companion#BLOCKLIST()) Content was blocked for another reason.                                                                                                                  |
| [BlockReason](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockReason) | [OTHER](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockReason.Companion#OTHER()) Content was blocked for another reason.                                                                                                                          |
| [BlockReason](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockReason) | [PROHIBITED_CONTENT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockReason.Companion#PROHIBITED_CONTENT()) Candidates blocked due to the terms which are included from the terminology blocklist.                                                 |
| [BlockReason](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockReason) | [SAFETY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockReason.Companion#SAFETY()) Content was blocked for violating provided [SafetySetting](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetySetting). |
| [BlockReason](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockReason) | [UNKNOWN](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockReason.Companion#UNKNOWN()) A new and not yet supported value.                                                                                                                           |

|                              ### Public properties                               |
|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [name](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockReason#name())       |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)       | [ordinal](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockReason#ordinal()) |

## Public companion properties

### BLOCKLIST

```
valÂ BLOCKLIST:Â BlockReason
```

Content was blocked for another reason.  

### OTHER

```
valÂ OTHER:Â BlockReason
```

Content was blocked for another reason.  

### PROHIBITED_CONTENT

```
valÂ PROHIBITED_CONTENT:Â BlockReason
```

Candidates blocked due to the terms which are included from the terminology blocklist.  

### SAFETY

```
valÂ SAFETY:Â BlockReason
```

Content was blocked for violating provided [SafetySetting](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetySetting).  

### UNKNOWN

```
valÂ UNKNOWN:Â BlockReason
```

A new and not yet supported value.  

## Public properties

### name

```
valÂ name:Â String
```  

### ordinal

```
valÂ ordinal:Â Int
```