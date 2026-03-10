# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType.md.txt

# FirebaseAnalytics.ConsentType

# FirebaseAnalytics.ConsentType


```
enum FirebaseAnalytics.ConsentType
```

<br />

*** ** * ** ***

The type of consent to set. Supported consent types are `AD_STORAGE`, `
ANALYTICS_STORAGE`, `AD_USER_DATA` and `AD_PERSONALIZATION`. Omitting a type retains its previous status.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_PERSONALIZATION` | Sets consent for personalized advertising. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_STORAGE` | Enables storage (such as device identifiers) related to advertising. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_USER_DATA` | Sets consent for sending user data to Google for advertising purposes. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#ANALYTICS_STORAGE` | Enables storage (such as app identifiers) related to analytics, e.g. visit duration. |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#valueOf(java.lang.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` Returns the enum constant of this type with the specified name. |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### AD_PERSONALIZATION

```
val FirebaseAnalytics.ConsentType.AD_PERSONALIZATION: FirebaseAnalytics.ConsentType
```

Sets consent for personalized advertising.

### AD_STORAGE

```
val FirebaseAnalytics.ConsentType.AD_STORAGE: FirebaseAnalytics.ConsentType
```

Enables storage (such as device identifiers) related to advertising.

### AD_USER_DATA

```
val FirebaseAnalytics.ConsentType.AD_USER_DATA: FirebaseAnalytics.ConsentType
```

Sets consent for sending user data to Google for advertising purposes.

### ANALYTICS_STORAGE

```
val FirebaseAnalytics.ConsentType.ANALYTICS_STORAGE: FirebaseAnalytics.ConsentType
```

Enables storage (such as app identifiers) related to analytics, e.g. visit duration.

## Public functions

### valueOf

```
java-static fun valueOf(name: String!): FirebaseAnalytics.ConsentType!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType!` | the enum constant with the specified name |

| Throws |
|---|---|
| `https://developer.android.com/reference/java/lang/IllegalArgumentException.html` | if this enum type has no constant with the specified name |

### values

```
java-static fun values(): Array<FirebaseAnalytics.ConsentType!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType!>!` | an array containing the constants of this enum type, in the order they're declared |