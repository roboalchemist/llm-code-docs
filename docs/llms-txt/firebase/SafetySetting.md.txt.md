# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetySetting.md.txt

# SafetySetting

# SafetySetting


```
public final class SafetySetting
```

<br />

*** ** * ** ***

A configuration for a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockThreshold` of some `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmCategory` allowed and blocked in responses.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetySetting#SafetySetting(com.google.firebase.ai.type.HarmCategory,com.google.firebase.ai.type.HarmBlockThreshold,com.google.firebase.ai.type.HarmBlockMethod)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmCategory harmCategory, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockThreshold threshold, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockMethod method )` |

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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmCategory harmCategory` | The relevant `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmCategory`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockThreshold threshold` | The threshold form harm allowable. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockMethod method` | Specify if the threshold is used for probability or severity score, if not specified it will default to `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmBlockMethod.Companion#PROBABILITY()`. |