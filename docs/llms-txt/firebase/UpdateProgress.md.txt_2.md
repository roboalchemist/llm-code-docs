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

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress#getApkBytesDownloaded()()` Returns the number of bytes downloaded so far for an APK. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress#getApkFileTotalBytes()()` Returns the file size of the APK file to download in bytes. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress#getUpdateStatus()()` Returns the current `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus` of the update. |

| ### Extension functions |
|---|---|
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress#(com.google.firebase.appdistribution.UpdateProgress).component1()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress` to provide apkBytesDownloaded. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress#(com.google.firebase.appdistribution.UpdateProgress).component2()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress` to provide apkFileTotalBytes. |
| `operator https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress#(com.google.firebase.appdistribution.UpdateProgress).component3()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress` to provide updateStatus. |

## Public functions

### getApkBytesDownloaded

```
fun getApkBytesDownloaded(): Long
```

Returns the number of bytes downloaded so far for an APK.

the number of bytes downloaded, or -1 if called when updating to an AAB or if no new release is available.

### getApkFileTotalBytes

```
fun getApkFileTotalBytes(): Long
```

Returns the file size of the APK file to download in bytes.

the file size in bytes, or -1 if called when updating to an AAB or if no new release is available.

### getUpdateStatus

```
fun getUpdateStatus(): UpdateStatus
```

Returns the current `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus` of the update.

## Extension functions

### component1

```
operator fun UpdateProgress.component1(): Long
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress` to provide apkBytesDownloaded.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the apkBytesDownloaded of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress` |

### component2

```
operator fun UpdateProgress.component2(): Long
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress` to provide apkFileTotalBytes.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the apkFileTotalBytes of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress` |

### component3

```
operator fun UpdateProgress.component3(): UpdateStatus
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress` to provide updateStatus.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateStatus` | the updateStatus of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/UpdateProgress` |