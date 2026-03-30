# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType.md.txt

# FirebaseAnalytics.ConsentType

# FirebaseAnalytics.ConsentType


```
public enum FirebaseAnalytics.ConsentType
```

<br />

*** ** * ** ***

The type of consent to set. Supported consent types are `AD_STORAGE`, `
ANALYTICS_STORAGE`, `AD_USER_DATA` and `AD_PERSONALIZATION`. Omitting a type retains its previous status.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_PERSONALIZATION` | Sets consent for personalized advertising. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_STORAGE` | Enables storage (such as device identifiers) related to advertising. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_USER_DATA` | Sets consent for sending user data to Google for advertising purposes. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#ANALYTICS_STORAGE` | Enables storage (such as app identifiers) related to analytics, e.g. visit duration. |

| ### Public methods |
|---|---|
| `static https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#valueOf(java.lang.String)(https://developer.android.com/reference/java/lang/String.html name)` Returns the enum constant of this type with the specified name. |
| `static FirebaseAnalytics.ConsentType[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### AD_PERSONALIZATION

```
FirebaseAnalytics.ConsentType FirebaseAnalytics.ConsentType.AD_PERSONALIZATION
```

Sets consent for personalized advertising.

### AD_STORAGE

```
FirebaseAnalytics.ConsentType FirebaseAnalytics.ConsentType.AD_STORAGE
```

Enables storage (such as device identifiers) related to advertising.

### AD_USER_DATA

```
FirebaseAnalytics.ConsentType FirebaseAnalytics.ConsentType.AD_USER_DATA
```

Sets consent for sending user data to Google for advertising purposes.

### ANALYTICS_STORAGE

```
FirebaseAnalytics.ConsentType FirebaseAnalytics.ConsentType.ANALYTICS_STORAGE
```

Enables storage (such as app identifiers) related to analytics, e.g. visit duration.

## Public methods

### valueOf

```
public static FirebaseAnalytics.ConsentType valueOf(String name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType` | the enum constant with the specified name |

| Throws |
|---|---|
| `https://developer.android.com/reference/java/lang/IllegalArgumentException.html` | if this enum type has no constant with the specified name |

### values

```
public static FirebaseAnalytics.ConsentType[] values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `FirebaseAnalytics.ConsentType[]` | an array containing the constants of this enum type, in the order they're declared |