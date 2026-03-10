# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus.md.txt

# FirebaseAnalytics.ConsentStatus

# FirebaseAnalytics.ConsentStatus


```
public enum FirebaseAnalytics.ConsentStatus
```

<br />

*** ** * ** ***

The status value of the consent type. Supported statuses are `GRANTED` and `
DENIED`.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#DENIED` | Consent status indicating consent is denied. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#GRANTED` | Consent status indicating consent is granted. |

| ### Public methods |
|---|---|
| `static https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#valueOf(java.lang.String)(https://developer.android.com/reference/java/lang/String.html name)` Returns the enum constant of this type with the specified name. |
| `static FirebaseAnalytics.ConsentStatus[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### DENIED

```
FirebaseAnalytics.ConsentStatus FirebaseAnalytics.ConsentStatus.DENIED
```

Consent status indicating consent is denied. For an overview of which data is sent when consent is denied, see [SDK behavior with consent mode](https://developers.google.com/tag-platform/security/concepts/consent-mode#tag-behavior).

### GRANTED

```
FirebaseAnalytics.ConsentStatus FirebaseAnalytics.ConsentStatus.GRANTED
```

Consent status indicating consent is granted.

## Public methods

### valueOf

```
public static FirebaseAnalytics.ConsentStatus valueOf(String name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus` | the enum constant with the specified name |

| Throws |
|---|---|
| `https://developer.android.com/reference/java/lang/IllegalArgumentException.html` | if this enum type has no constant with the specified name |

### values

```
public static FirebaseAnalytics.ConsentStatus[] values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `FirebaseAnalytics.ConsentStatus[]` | an array containing the constants of this enum type, in the order they're declared |