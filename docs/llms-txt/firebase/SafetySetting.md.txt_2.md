# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetySetting.md.txt

# SafetySetting

# SafetySetting


```
public final class SafetySetting
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

A configuration for a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmBlockThreshold` of some `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmCategory` allowed and blocked in responses.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetySetting#SafetySetting(com.google.firebase.vertexai.type.HarmCategory,com.google.firebase.vertexai.type.HarmBlockThreshold,com.google.firebase.vertexai.type.HarmBlockMethod)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmCategory harmCategory, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmBlockThreshold threshold, https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmBlockMethod method )` |

## Public constructors

### SafetySetting

```
public SafetySetting(
    @NonNull HarmCategory harmCategory,
    @NonNull HarmBlockThreshold threshold,
    HarmBlockMethod method
)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmCategory harmCategory` | The relevant `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmCategory`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmBlockThreshold threshold` | The threshold form harm allowable. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmBlockMethod method` | Specify if the threshold is used for probability or severity score, if not specified it will default to `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmBlockMethod.Companion#PROBABILITY()`. |