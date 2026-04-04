# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress.md.txt

# UpdateProgress

# UpdateProgress


```
public interface UpdateProgress
```

<br />

*** ** * ** ***

Represents a progress update or a final state from updating an app.

## Summary

| ### Public methods |
|---|---|
| `abstract long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress#getApkBytesDownloaded()()` Returns the number of bytes downloaded so far for an APK. |
| `abstract long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress#getApkFileTotalBytes()()` Returns the file size of the APK file to download in bytes. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress#getUpdateStatus()()` Returns the current `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus` of the update. |

| ### Extension functions |
|---|---|
| `default final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionKt.https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress#(com.google.firebase.appdistribution.UpdateProgress).component1()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress` to provide apkBytesDownloaded. |
| `default final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionKt.https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress#(com.google.firebase.appdistribution.UpdateProgress).component2()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress` to provide apkFileTotalBytes. |
| `default final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionKt.https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress#(com.google.firebase.appdistribution.UpdateProgress).component3()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress` to provide updateStatus. |

## Public methods

### getApkBytesDownloaded

```
abstract long getApkBytesDownloaded()
```

Returns the number of bytes downloaded so far for an APK.

the number of bytes downloaded, or -1 if called when updating to an AAB or if no new release is available.

### getApkFileTotalBytes

```
abstract long getApkFileTotalBytes()
```

Returns the file size of the APK file to download in bytes.

the file size in bytes, or -1 if called when updating to an AAB or if no new release is available.

### getUpdateStatus

```
abstract @NonNull UpdateStatus getUpdateStatus()
```

Returns the current `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus` of the update.

## Extension functions

### FirebaseAppDistributionKt.component1

```
default final long FirebaseAppDistributionKt.component1(@NonNull UpdateProgress receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress` to provide apkBytesDownloaded.

| Returns |
|---|---|
| `long` | the apkBytesDownloaded of the `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress` |

### FirebaseAppDistributionKt.component2

```
default final long FirebaseAppDistributionKt.component2(@NonNull UpdateProgress receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress` to provide apkFileTotalBytes.

| Returns |
|---|---|
| `long` | the apkFileTotalBytes of the `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress` |

### FirebaseAppDistributionKt.component3

```
default final @NonNull UpdateStatus FirebaseAppDistributionKt.component3(@NonNull UpdateProgress receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress` to provide updateStatus.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateStatus` | the updateStatus of the `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/UpdateProgress` |