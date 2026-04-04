# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus.md.txt

# UpdateStatus

# UpdateStatus


```
enum UpdateStatus
```

<br />

*** ** * ** ***

Enum for possible states during Update, used in [UpdateProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress).

## Summary

|                                                                      ### Enum Values                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DOWNLOADED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#DOWNLOADED)                               | The new release was downloaded successfully.                                                                                                                                 |
| [DOWNLOADING](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#DOWNLOADING)                             | The new release download is in progress.                                                                                                                                     |
| [DOWNLOAD_FAILED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#DOWNLOAD_FAILED)                     | The new release failed to download.                                                                                                                                          |
| [INSTALL_CANCELED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#INSTALL_CANCELED)                   | The new release installation was canceled.                                                                                                                                   |
| [INSTALL_FAILED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#INSTALL_FAILED)                       | The new release installation failed.                                                                                                                                         |
| [NEW_RELEASE_CHECK_FAILED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#NEW_RELEASE_CHECK_FAILED)   | The call to [checkForNewRelease](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#checkForNewRelease()) failed. |
| [NEW_RELEASE_NOT_AVAILABLE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#NEW_RELEASE_NOT_AVAILABLE) | The tester is currently on the latest release they have access to for the current app.                                                                                       |
| [PENDING](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#PENDING)                                     | The update is queued but not started.                                                                                                                                        |
| [REDIRECTED_TO_PLAY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#REDIRECTED_TO_PLAY)               | The tester was redirected to Play to download an [AAB](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType#AAB) file.           |
| [UPDATE_CANCELED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#UPDATE_CANCELED)                     | The tester canceled the update.                                                                                                                                              |

|                                                                                                  ### Public functions                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[UpdateStatus](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus)`!`                                                                                    | [valueOf](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#valueOf(java.lang.String))`(name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!)` Returns the enum constant of this type with the specified name. |
| `java-static `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[UpdateStatus](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus)`!>!` | [values](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus#values())`()` Returns an array containing the constants of this enum type, in the order they're declared.                                                                                |

## Enum Values

### DOWNLOADED

```
valÂ UpdateStatus.DOWNLOADED:Â UpdateStatus
```

The new release was downloaded successfully.  

### DOWNLOADING

```
valÂ UpdateStatus.DOWNLOADING:Â UpdateStatus
```

The new release download is in progress.  

### DOWNLOAD_FAILED

```
valÂ UpdateStatus.DOWNLOAD_FAILED:Â UpdateStatus
```

The new release failed to download.  

### INSTALL_CANCELED

```
valÂ UpdateStatus.INSTALL_CANCELED:Â UpdateStatus
```

The new release installation was canceled.  

### INSTALL_FAILED

```
valÂ UpdateStatus.INSTALL_FAILED:Â UpdateStatus
```

The new release installation failed.  

### NEW_RELEASE_CHECK_FAILED

```
valÂ UpdateStatus.NEW_RELEASE_CHECK_FAILED:Â UpdateStatus
```

The call to [checkForNewRelease](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#checkForNewRelease()) failed.  

### NEW_RELEASE_NOT_AVAILABLE

```
valÂ UpdateStatus.NEW_RELEASE_NOT_AVAILABLE:Â UpdateStatus
```

The tester is currently on the latest release they have access to for the current app.  

### PENDING

```
valÂ UpdateStatus.PENDING:Â UpdateStatus
```

The update is queued but not started.  

### REDIRECTED_TO_PLAY

```
valÂ UpdateStatus.REDIRECTED_TO_PLAY:Â UpdateStatus
```

The tester was redirected to Play to download an [AAB](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType#AAB) file.  

### UPDATE_CANCELED

```
valÂ UpdateStatus.UPDATE_CANCELED:Â UpdateStatus
```

The tester canceled the update.  

## Public functions

### valueOf

```
java-staticÂ funÂ valueOf(name:Â String!):Â UpdateStatus!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)  

|                                                        Returns                                                        |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| [UpdateStatus](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus)`!` | the enum constant with the specified name |

|                                                                               Throws                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `java.lang.IllegalArgumentException: `[java.lang.IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html) | if this enum type has no constant with the specified name |

### values

```
java-staticÂ funÂ values():Â Array<UpdateStatus!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.  

|                                                                                                 Returns                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[UpdateStatus](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus)`!>!` | an array containing the constants of this enum type, in the order they're declared |