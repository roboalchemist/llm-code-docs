# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetyRating.md.txt

# SafetyRating

# SafetyRating


```
public final class SafetyRating
```

<br />

*** ** * ** ***

An assessment of the potential harm of some generated content.

The rating will be restricted to a particular `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetyRating#category()`.

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/Boolean.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetyRating#blocked()` Indicates whether the content was blocked due to safety concerns. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmCategory` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetyRating#category()` The category of harm being assessed (for example, Hate speech). |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmProbability` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetyRating#probability()` The likelihood of the content causing harm. |
| `final float` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetyRating#probabilityScore()` A numerical score representing the probability of harm, between `0` and `1`. |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/HarmSeverity` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetyRating#severity()` The severity of the potential harm. |
| `final https://developer.android.com/reference/kotlin/java/lang/Float.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SafetyRating#severityScore()` A numerical score representing the severity of harm. |

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

The category of harm being assessed (for example, Hate speech).

### probability

```
public final @NonNull HarmProbability probability
```

The likelihood of the content causing harm.

### probabilityScore

```
public final float probabilityScore
```

A numerical score representing the probability of harm, between `0` and `1`.

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