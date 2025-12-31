# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status.md.txt

# FirebaseAppDistributionException.Status

# FirebaseAppDistributionException.Status


```
public enum FirebaseAppDistributionException.Status
```

<br />

*** ** * ** ***

Enum for potential error statuses that caused the [FirebaseAppDistributionException](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException).

## Summary

|                                                                                    ### Enum Values                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [API_DISABLED](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#API_DISABLED)                           | The Firebase App Distribution Tester API is disabled for this project.                |
| [AUTHENTICATION_CANCELED](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#AUTHENTICATION_CANCELED)     | The authentication process was canceled (typically by the tester).                    |
| [AUTHENTICATION_FAILURE](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#AUTHENTICATION_FAILURE)       | The authentication process failed.                                                    |
| [DOWNLOAD_FAILURE](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#DOWNLOAD_FAILURE)                   | The new release failed to download.                                                   |
| [HOST_ACTIVITY_INTERRUPTED](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#HOST_ACTIVITY_INTERRUPTED) | The host activity for a confirmation dialog was destroyed or pushed to the backstack. |
| [INSTALLATION_CANCELED](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#INSTALLATION_CANCELED)         | The installation was canceled (typically by the tester).                              |
| [INSTALLATION_FAILURE](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#INSTALLATION_FAILURE)           | The new release failed to install.                                                    |
| [NETWORK_FAILURE](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#NETWORK_FAILURE)                     | No network was available to make requests, or the request timed out.                  |
| [NOT_IMPLEMENTED](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#NOT_IMPLEMENTED)                     | This API is not implemented.                                                          |
| [UNKNOWN](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#UNKNOWN)                                     | Unknown error or an error from a different error domain.                              |
| [UPDATE_NOT_AVAILABLE](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#UPDATE_NOT_AVAILABLE)           | An update was not available for the current tester and app.                           |

|                                                                                 ### Public methods                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static `[FirebaseAppDistributionException.Status](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status) | [valueOf](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#valueOf(java.lang.String))`(`[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` name)` Returns the enum constant of this type with the specified name. |
| `static FirebaseAppDistributionException.Status[]`                                                                                                                                 | [values](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status#values())`()` Returns an array containing the constants of this enum type, in the order they're declared.                                                                            |

## Enum Values

### API_DISABLED

```
FirebaseAppDistributionException.StatusÂ FirebaseAppDistributionException.Status.API_DISABLED
```

The Firebase App Distribution Tester API is disabled for this project.

Before you use the App Distribution SDK in your app, you must enable the API in the Google Cloud console. For more information, see the [documentation](https://firebase.google.com/docs/app-distribution/set-up-alerts?platform=android). If you enabled this API recently, wait a few minutes for the action to propagate to the App Distribution systems, and retry.  

### AUTHENTICATION_CANCELED

```
FirebaseAppDistributionException.StatusÂ FirebaseAppDistributionException.Status.AUTHENTICATION_CANCELED
```

The authentication process was canceled (typically by the tester).  

### AUTHENTICATION_FAILURE

```
FirebaseAppDistributionException.StatusÂ FirebaseAppDistributionException.Status.AUTHENTICATION_FAILURE
```

The authentication process failed. The tester was either not signed in, does not have access, or something went wrong. Try signing in again by calling [signInTester](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution#signInTester()).  

### DOWNLOAD_FAILURE

```
FirebaseAppDistributionException.StatusÂ FirebaseAppDistributionException.Status.DOWNLOAD_FAILURE
```

The new release failed to download. This was a most likely due to a transient condition and may be corrected by retrying the call to [updateIfNewReleaseAvailable](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution#updateIfNewReleaseAvailable()) or [updateApp](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution#updateApp()).  

### HOST_ACTIVITY_INTERRUPTED

```
FirebaseAppDistributionException.StatusÂ FirebaseAppDistributionException.Status.HOST_ACTIVITY_INTERRUPTED
```

The host activity for a confirmation dialog was destroyed or pushed to the backstack. Try calling [updateIfNewReleaseAvailable](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution#updateIfNewReleaseAvailable()) again.  

### INSTALLATION_CANCELED

```
FirebaseAppDistributionException.StatusÂ FirebaseAppDistributionException.Status.INSTALLATION_CANCELED
```

The installation was canceled (typically by the tester).  

### INSTALLATION_FAILURE

```
FirebaseAppDistributionException.StatusÂ FirebaseAppDistributionException.Status.INSTALLATION_FAILURE
```

The new release failed to install. Verify that the new release has the same signing key as the version running on device.  

### NETWORK_FAILURE

```
FirebaseAppDistributionException.StatusÂ FirebaseAppDistributionException.Status.NETWORK_FAILURE
```

No network was available to make requests, or the request timed out. Check the tester's internet connection and retry the call to [FirebaseAppDistribution](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution).  

### NOT_IMPLEMENTED

```
FirebaseAppDistributionException.StatusÂ FirebaseAppDistributionException.Status.NOT_IMPLEMENTED
```

This API is not implemented.

This build was compiled against the API only. This may be intentional if this variant is intended for use in production. Otherwise you may need to include a dependency on `
com.google.firebase:firebase-appdistribution`.  

### UNKNOWN

```
FirebaseAppDistributionException.StatusÂ FirebaseAppDistributionException.Status.UNKNOWN
```

Unknown error or an error from a different error domain.  

### UPDATE_NOT_AVAILABLE

```
FirebaseAppDistributionException.StatusÂ FirebaseAppDistributionException.Status.UPDATE_NOT_AVAILABLE
```

An update was not available for the current tester and app. Make sure that [checkForNewRelease](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution#checkForNewRelease()) returns with a non-null [AppDistributionRelease](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease) before calling [updateApp](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution#updateApp())  

## Public methods

### valueOf

```
publicÂ staticÂ FirebaseAppDistributionException.StatusÂ valueOf(StringÂ name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)  

|                                                                                  Returns                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| [FirebaseAppDistributionException.Status](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status) | the enum constant with the specified name |

|                                                                              Throws                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [java.lang.IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html)` java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
publicÂ staticÂ FirebaseAppDistributionException.Status[]Â values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.  

|                   Returns                   |
|---------------------------------------------|------------------------------------------------------------------------------------|
| `FirebaseAppDistributionException.Status[]` | an array containing the constants of this enum type, in the order they're declared |