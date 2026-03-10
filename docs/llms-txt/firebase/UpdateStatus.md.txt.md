# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus.md.txt

# UpdateStatus

# UpdateStatus


```
public enum UpdateStatus
```

<br />

*** ** * ** ***

Enum for possible states during Update, used in `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress`.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus#DOWNLOADED` | The new release was downloaded successfully. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus#DOWNLOADING` | The new release download is in progress. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus#DOWNLOAD_FAILED` | The new release failed to download. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus#INSTALL_CANCELED` | The new release installation was canceled. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus#INSTALL_FAILED` | The new release installation failed. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus#NEW_RELEASE_CHECK_FAILED` | The call to `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution#checkForNewRelease()` failed. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus#NEW_RELEASE_NOT_AVAILABLE` | The tester is currently on the latest release they have access to for the current app. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus#PENDING` | The update is queued but not started. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus#REDIRECTED_TO_PLAY` | The tester was redirected to Play to download an `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/BinaryType#AAB` file. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus#UPDATE_CANCELED` | The tester canceled the update. |

| ### Public methods |
|---|---|
| `static https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus#valueOf(java.lang.String)(https://developer.android.com/reference/kotlin/java/lang/String.html name)` Returns the enum constant of this type with the specified name. |
| `static UpdateStatus[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### DOWNLOADED

```
UpdateStatus UpdateStatus.DOWNLOADED
```

The new release was downloaded successfully.

### DOWNLOADING

```
UpdateStatus UpdateStatus.DOWNLOADING
```

The new release download is in progress.

### DOWNLOAD_FAILED

```
UpdateStatus UpdateStatus.DOWNLOAD_FAILED
```

The new release failed to download.

### INSTALL_CANCELED

```
UpdateStatus UpdateStatus.INSTALL_CANCELED
```

The new release installation was canceled.

### INSTALL_FAILED

```
UpdateStatus UpdateStatus.INSTALL_FAILED
```

The new release installation failed.

### NEW_RELEASE_CHECK_FAILED

```
UpdateStatus UpdateStatus.NEW_RELEASE_CHECK_FAILED
```

The call to `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution#checkForNewRelease()` failed.

### NEW_RELEASE_NOT_AVAILABLE

```
UpdateStatus UpdateStatus.NEW_RELEASE_NOT_AVAILABLE
```

The tester is currently on the latest release they have access to for the current app.

### PENDING

```
UpdateStatus UpdateStatus.PENDING
```

The update is queued but not started.

### REDIRECTED_TO_PLAY

```
UpdateStatus UpdateStatus.REDIRECTED_TO_PLAY
```

The tester was redirected to Play to download an `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/BinaryType#AAB` file.

### UPDATE_CANCELED

```
UpdateStatus UpdateStatus.UPDATE_CANCELED
```

The tester canceled the update.

## Public methods

### valueOf

```
public static UpdateStatus valueOf(String name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus` | the enum constant with the specified name |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
public static UpdateStatus[] values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `UpdateStatus[]` | an array containing the constants of this enum type, in the order they're declared |