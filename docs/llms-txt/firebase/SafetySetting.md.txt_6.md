# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetySetting.md.txt

# SafetySetting

# SafetySetting


```
class SafetySetting
```

<br />

*** ** * ** ***

A configuration for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold` of some `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmCategory` allowed and blocked in responses.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SafetySetting#SafetySetting(com.google.firebase.ai.type.HarmCategory,com.google.firebase.ai.type.HarmBlockThreshold,com.google.firebase.ai.type.HarmBlockMethod)( harmCategory: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmCategory, threshold: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold, method: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockMethod? )` |

## Public constructors

### SafetySetting

```
SafetySetting(
    harmCategory: HarmCategory,
    threshold: HarmBlockThreshold,
    method: HarmBlockMethod? = null
)
```

| Parameters |
|---|---|
| `harmCategory: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmCategory` | The relevant `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmCategory`. |
| `threshold: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockThreshold` | The threshold form harm allowable. |
| `method: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockMethod? = null` | Specify if the threshold is used for probability or severity score, if not specified it will default to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/HarmBlockMethod.Companion#PROBABILITY()`. |