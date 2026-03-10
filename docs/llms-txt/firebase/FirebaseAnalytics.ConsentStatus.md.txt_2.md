# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus.md.txt

# FirebaseAnalytics.ConsentStatus

# FirebaseAnalytics.ConsentStatus


```
enum FirebaseAnalytics.ConsentStatus
```

<br />

*** ** * ** ***

The status value of the consent type. Supported statuses are `GRANTED` and `
DENIED`.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#DENIED` | Consent status indicating consent is denied. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#GRANTED` | Consent status indicating consent is granted. |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#valueOf(java.lang.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` Returns the enum constant of this type with the specified name. |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### DENIED

```
val FirebaseAnalytics.ConsentStatus.DENIED: FirebaseAnalytics.ConsentStatus
```

Consent status indicating consent is denied. For an overview of which data is sent when consent is denied, see [SDK behavior with consent mode](https://developers.google.com/tag-platform/security/concepts/consent-mode#tag-behavior).

### GRANTED

```
val FirebaseAnalytics.ConsentStatus.GRANTED: FirebaseAnalytics.ConsentStatus
```

Consent status indicating consent is granted.

## Public functions

### valueOf

```
java-static fun valueOf(name: String!): FirebaseAnalytics.ConsentStatus!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus!` | the enum constant with the specified name |

| Throws |
|---|---|
| `https://developer.android.com/reference/java/lang/IllegalArgumentException.html` | if this enum type has no constant with the specified name |

### values

```
java-static fun values(): Array<FirebaseAnalytics.ConsentStatus!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus!>!` | an array containing the constants of this enum type, in the order they're declared |