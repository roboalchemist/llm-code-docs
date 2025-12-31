# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetySetting.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetySetting.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetySetting.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetySetting.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SafetySetting.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetySetting.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SafetySetting.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetySetting.md.txt

# SafetySetting

# SafetySetting


```
class SafetySetting
```

<br />

*** ** * ** ***

A configuration for a [HarmBlockThreshold](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold) of some [HarmCategory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmCategory) allowed and blocked in responses.

## Summary

|                                                                                                                                                                                                                                                                                                                           ### Public constructors                                                                                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SafetySetting](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetySetting#SafetySetting(com.google.firebase.ai.type.HarmCategory,com.google.firebase.ai.type.HarmBlockThreshold,com.google.firebase.ai.type.HarmBlockMethod))`(` ` harmCategory: `[HarmCategory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmCategory)`,` ` threshold: `[HarmBlockThreshold](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold)`,` ` method: `[HarmBlockMethod](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockMethod)`?` `)` |

## Public constructors

### SafetySetting

```
SafetySetting(
Â Â Â Â harmCategory:Â HarmCategory,
Â Â Â Â threshold:Â HarmBlockThreshold,
Â Â Â Â method:Â HarmBlockMethod? = null
)
```  

|                                                              Parameters                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `harmCategory: `[HarmCategory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmCategory)           | The relevant [HarmCategory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmCategory).                                                                                                                                      |
| `threshold: `[HarmBlockThreshold](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold)  | The threshold form harm allowable.                                                                                                                                                                                                                            |
| `method: `[HarmBlockMethod](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockMethod)`? = null` | Specify if the threshold is used for probability or severity score, if not specified it will default to [HarmBlockMethod.PROBABILITY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockMethod.Companion#PROBABILITY()). |