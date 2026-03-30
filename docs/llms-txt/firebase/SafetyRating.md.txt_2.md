# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetyRating.md.txt

# SafetyRating

# SafetyRating


```
public final class SafetyRating
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

An assessment of the potential harm of some generated content.

The rating will be restricted to a particular `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetyRating#category()`.

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/Boolean.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetyRating#blocked()` Indicates whether the content was blocked due to safety concerns. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmCategory` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetyRating#category()` The category of harm being assessed (e.g., Hate speech). |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmProbability` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetyRating#probability()` The likelihood of the content causing harm. |
| `final float` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetyRating#probabilityScore()` A numerical score representing the probability of harm, between 0 and |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmSeverity` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetyRating#severity()` The severity of the potential harm. |
| `final https://developer.android.com/reference/kotlin/java/lang/Float.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetyRating#severityScore()` A numerical score representing the severity of harm. |

## Public fields

### blocked

```
public final Boolean blocked
```

Indicates whether the content was blocked due to safety concerns.

### category

```
public final @NonNull HarmCategory category
```

The category of harm being assessed (e.g., Hate speech).

### probability

```
public final @NonNull HarmProbability probability
```

The likelihood of the content causing harm.

### probabilityScore

```
public final float probabilityScore
```

A numerical score representing the probability of harm, between 0 and

1. 

### severity

```
public final HarmSeverity severity
```

The severity of the potential harm.

### severityScore

```
public final Float severityScore
```

A numerical score representing the severity of harm.