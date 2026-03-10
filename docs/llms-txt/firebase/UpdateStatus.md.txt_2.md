# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus.md.txt

# UpdateStatus

# UpdateStatus


```
enum UpdateStatus
```

<br />

*** ** * ** ***

Enum for possible states during Update, used in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress`.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#DOWNLOADED` | The new release was downloaded successfully. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#DOWNLOADING` | The new release download is in progress. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#DOWNLOAD_FAILED` | The new release failed to download. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#INSTALL_CANCELED` | The new release installation was canceled. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#INSTALL_FAILED` | The new release installation failed. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#NEW_RELEASE_CHECK_FAILED` | The call to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#checkForNewRelease()` failed. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#NEW_RELEASE_NOT_AVAILABLE` | The tester is currently on the latest release they have access to for the current app. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#PENDING` | The update is queued but not started. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#REDIRECTED_TO_PLAY` | The tester was redirected to Play to download an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType#AAB` file. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#UPDATE_CANCELED` | The tester canceled the update. |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#valueOf(java.lang.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` Returns the enum constant of this type with the specified name. |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### DOWNLOADED

```
val UpdateStatus.DOWNLOADED: UpdateStatus
```

The new release was downloaded successfully.

### DOWNLOADING

```
val UpdateStatus.DOWNLOADING: UpdateStatus
```

The new release download is in progress.

### DOWNLOAD_FAILED

```
val UpdateStatus.DOWNLOAD_FAILED: UpdateStatus
```

The new release failed to download.

### INSTALL_CANCELED

```
val UpdateStatus.INSTALL_CANCELED: UpdateStatus
```

The new release installation was canceled.

### INSTALL_FAILED

```
val UpdateStatus.INSTALL_FAILED: UpdateStatus
```

The new release installation failed.

### NEW_RELEASE_CHECK_FAILED

```
val UpdateStatus.NEW_RELEASE_CHECK_FAILED: UpdateStatus
```

The call to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#checkForNewRelease()` failed.

### NEW_RELEASE_NOT_AVAILABLE

```
val UpdateStatus.NEW_RELEASE_NOT_AVAILABLE: UpdateStatus
```

The tester is currently on the latest release they have access to for the current app.

### PENDING

```
val UpdateStatus.PENDING: UpdateStatus
```

The update is queued but not started.

### REDIRECTED_TO_PLAY

```
val UpdateStatus.REDIRECTED_TO_PLAY: UpdateStatus
```

The tester was redirected to Play to download an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType#AAB` file.

### UPDATE_CANCELED

```
val UpdateStatus.UPDATE_CANCELED: UpdateStatus
```

The tester canceled the update.

## Public functions

### valueOf

```
java-static fun valueOf(name: String!): UpdateStatus!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus!` | the enum constant with the specified name |

| Throws |
|---|---|
| `java.lang.IllegalArgumentException: https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html` | if this enum type has no constant with the specified name |

### values

```
java-static fun values(): Array<UpdateStatus!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus!>!` | an array containing the constants of this enum type, in the order they're declared |