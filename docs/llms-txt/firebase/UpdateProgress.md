# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress.md.txt

# UpdateProgress

# UpdateProgress


```
interface UpdateProgress
```

<br />

*** ** * ** ***

Represents a progress update or a final state from updating an app.

## Summary

|                                                ### Public functions                                                |
|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)                                       | [getApkBytesDownloaded](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress#getApkBytesDownloaded())`()` Returns the number of bytes downloaded so far for an APK.                                                                                 |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)                                       | [getApkFileTotalBytes](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress#getApkFileTotalBytes())`()` Returns the file size of the APK file to download in bytes.                                                                                 |
| [UpdateStatus](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus) | [getUpdateStatus](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress#getUpdateStatus())`()` Returns the current [UpdateStatus](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus) of the update. |

|                                                    ### Extension functions                                                    |
|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `operator `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)                                       | [UpdateProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress)`.`[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress#(com.google.firebase.appdistribution.UpdateProgress).component1())`()` Destructuring declaration for [UpdateProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress) to provide apkBytesDownloaded. |
| `operator `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)                                       | [UpdateProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress)`.`[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress#(com.google.firebase.appdistribution.UpdateProgress).component2())`()` Destructuring declaration for [UpdateProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress) to provide apkFileTotalBytes.  |
| `operator `[UpdateStatus](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus) | [UpdateProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress)`.`[component3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress#(com.google.firebase.appdistribution.UpdateProgress).component3())`()` Destructuring declaration for [UpdateProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress) to provide updateStatus.       |

## Public functions

### getApkBytesDownloaded

```
funÂ getApkBytesDownloaded():Â Long
```

Returns the number of bytes downloaded so far for an APK.

the number of bytes downloaded, or -1 if called when updating to an AAB or if no new release is available.  

### getApkFileTotalBytes

```
funÂ getApkFileTotalBytes():Â Long
```

Returns the file size of the APK file to download in bytes.

the file size in bytes, or -1 if called when updating to an AAB or if no new release is available.  

### getUpdateStatus

```
funÂ getUpdateStatus():Â UpdateStatus
```

Returns the current [UpdateStatus](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus) of the update.  

## Extension functions

### component1

```
operatorÂ funÂ UpdateProgress.component1():Â Long
```

Destructuring declaration for [UpdateProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress) to provide apkBytesDownloaded.  

|                                   Returns                                    |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | the apkBytesDownloaded of the [UpdateProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress) |

### component2

```
operatorÂ funÂ UpdateProgress.component2():Â Long
```

Destructuring declaration for [UpdateProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress) to provide apkFileTotalBytes.  

|                                   Returns                                    |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | the apkFileTotalBytes of the [UpdateProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress) |

### component3

```
operatorÂ funÂ UpdateProgress.component3():Â UpdateStatus
```

Destructuring declaration for [UpdateProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress) to provide updateStatus.  

|                                                      Returns                                                       |
|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [UpdateStatus](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus) | the updateStatus of the [UpdateProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress) |