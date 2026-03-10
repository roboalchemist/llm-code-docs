# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status.md.txt

# FirebaseAppDistributionException.Status

# FirebaseAppDistributionException.Status


```
public enum FirebaseAppDistributionException.Status
```

<br />

*** ** * ** ***

Enum for potential error statuses that caused the `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException`.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#API_DISABLED` | The Firebase App Distribution Tester API is disabled for this project. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#AUTHENTICATION_CANCELED` | The authentication process was canceled (typically by the tester). |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#AUTHENTICATION_FAILURE` | The authentication process failed. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#DOWNLOAD_FAILURE` | The new release failed to download. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#HOST_ACTIVITY_INTERRUPTED` | The host activity for a confirmation dialog was destroyed or pushed to the backstack. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#INSTALLATION_CANCELED` | The installation was canceled (typically by the tester). |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#INSTALLATION_FAILURE` | The new release failed to install. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#NETWORK_FAILURE` | No network was available to make requests, or the request timed out. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#NOT_IMPLEMENTED` | This API is not implemented. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#UNKNOWN` | Unknown error or an error from a different error domain. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#UPDATE_NOT_AVAILABLE` | An update was not available for the current tester and app. |

| ### Public methods |
|---|---|
| `static https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#valueOf(java.lang.String)(https://developer.android.com/reference/kotlin/java/lang/String.html name)` Returns the enum constant of this type with the specified name. |
| `static FirebaseAppDistributionException.Status[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### API_DISABLED

```
FirebaseAppDistributionException.Status FirebaseAppDistributionException.Status.API_DISABLED
```

The Firebase App Distribution Tester API is disabled for this project.

Before you use the App Distribution SDK in your app, you must enable the API in the Google Cloud console. For more information, see the [documentation](https://firebase.google.com/docs/app-distribution/set-up-alerts?platform=android). If you enabled this API recently, wait a few minutes for the action to propagate to the App Distribution systems, and retry.

### AUTHENTICATION_CANCELED

```
FirebaseAppDistributionException.Status FirebaseAppDistributionException.Status.AUTHENTICATION_CANCELED
```

The authentication process was canceled (typically by the tester).

### AUTHENTICATION_FAILURE

```
FirebaseAppDistributionException.Status FirebaseAppDistributionException.Status.AUTHENTICATION_FAILURE
```

The authentication process failed. The tester was either not signed in, does not have access, or something went wrong. Try signing in again by calling `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution#signInTester()`.

### DOWNLOAD_FAILURE

```
FirebaseAppDistributionException.Status FirebaseAppDistributionException.Status.DOWNLOAD_FAILURE
```

The new release failed to download. This was a most likely due to a transient condition and may be corrected by retrying the call to `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution#updateIfNewReleaseAvailable()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution#updateApp()`.

### HOST_ACTIVITY_INTERRUPTED

```
FirebaseAppDistributionException.Status FirebaseAppDistributionException.Status.HOST_ACTIVITY_INTERRUPTED
```

The host activity for a confirmation dialog was destroyed or pushed to the backstack. Try calling `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution#updateIfNewReleaseAvailable()` again.

### INSTALLATION_CANCELED

```
FirebaseAppDistributionException.Status FirebaseAppDistributionException.Status.INSTALLATION_CANCELED
```

The installation was canceled (typically by the tester).

### INSTALLATION_FAILURE

```
FirebaseAppDistributionException.Status FirebaseAppDistributionException.Status.INSTALLATION_FAILURE
```

The new release failed to install. Verify that the new release has the same signing key as the version running on device.

### NETWORK_FAILURE

```
FirebaseAppDistributionException.Status FirebaseAppDistributionException.Status.NETWORK_FAILURE
```

No network was available to make requests, or the request timed out. Check the tester's internet connection and retry the call to `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution`.

### NOT_IMPLEMENTED

```
FirebaseAppDistributionException.Status FirebaseAppDistributionException.Status.NOT_IMPLEMENTED
```

This API is not implemented.

This build was compiled against the API only. This may be intentional if this variant is intended for use in production. Otherwise you may need to include a dependency on `
com.google.firebase:firebase-appdistribution`.

### UNKNOWN

```
FirebaseAppDistributionException.Status FirebaseAppDistributionException.Status.UNKNOWN
```

Unknown error or an error from a different error domain.

### UPDATE_NOT_AVAILABLE

```
FirebaseAppDistributionException.Status FirebaseAppDistributionException.Status.UPDATE_NOT_AVAILABLE
```

An update was not available for the current tester and app. Make sure that `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution#checkForNewRelease()` returns with a non-null `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease` before calling `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution#updateApp()`

## Public methods

### valueOf

```
public static FirebaseAppDistributionException.Status valueOf(String name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status` | the enum constant with the specified name |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
public static FirebaseAppDistributionException.Status[] values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `FirebaseAppDistributionException.Status[]` | an array containing the constants of this enum type, in the order they're declared |