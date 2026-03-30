# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetySetting.md.txt

# SafetySetting

# SafetySetting


```
class SafetySetting
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

A configuration for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmBlockThreshold` of some `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory` allowed and blocked in responses.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetySetting#SafetySetting(com.google.firebase.vertexai.type.HarmCategory,com.google.firebase.vertexai.type.HarmBlockThreshold,com.google.firebase.vertexai.type.HarmBlockMethod)( harmCategory: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory, threshold: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmBlockThreshold, method: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmBlockMethod? )` |

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
| `harmCategory: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory` | The relevant `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory`. |
| `threshold: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmBlockThreshold` | The threshold form harm allowable. |
| `method: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmBlockMethod? = null` | Specify if the threshold is used for probability or severity score, if not specified it will default to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmBlockMethod.Companion#PROBABILITY()`. |