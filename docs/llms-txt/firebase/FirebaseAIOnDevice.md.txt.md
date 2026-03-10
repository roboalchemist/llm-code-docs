# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/FirebaseAIOnDevice.md.txt

# FirebaseAIOnDevice

# FirebaseAIOnDevice


```
public static class FirebaseAIOnDevice
```

<br />

*** ** * ** ***

Entry point for Firebase AI On-Device functionality.

*Note:* This class **does not** provides any inference-related functionality for the on-device AI model.

## Summary

| ### Public fields |
|---|---|
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/FirebaseAIOnDevice` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/FirebaseAIOnDevice#INSTANCE()` |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/OnDeviceModelStatus` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/FirebaseAIOnDevice#checkStatus()()` Checks the current status / availability of the on-device AI model. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/FirebaseAIOnDevice#download()()` Initiates the download of the on-device AI model. |

## Public fields

### INSTANCE

```
public static @NonNull FirebaseAIOnDevice INSTANCE
```

## Public methods

### checkStatus

```
public static final @NonNull OnDeviceModelStatus checkStatus()
```

Checks the current status / availability of the on-device AI model.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/OnDeviceModelStatus` | An `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/OnDeviceModelStatus` object indicating the current state of the model. |

### download

```
public static final @NonNull Flow<@NonNull DownloadStatus> download()
```

Initiates the download of the on-device AI model.

This method returns a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` that emits `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus` updates as the download progresses. Consumers should collect the flow to start the download process, and optionally process any updates on the download state, progress, and completion or failure.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus>` | A `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus` objects representing the download lifecycle. |