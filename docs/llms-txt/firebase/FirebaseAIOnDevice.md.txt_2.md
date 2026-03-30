# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/FirebaseAIOnDevice.md.txt

# FirebaseAIOnDevice

# FirebaseAIOnDevice


```
object FirebaseAIOnDevice
```

<br />

*** ** * ** ***

Entry point for Firebase AI On-Device functionality.

*Note:* This class **does not** provides any inference-related functionality for the on-device AI model.

## Summary

| ### Public functions |
|---|---|
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/OnDeviceModelStatus` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/FirebaseAIOnDevice#checkStatus()()` Checks the current status / availability of the on-device AI model. |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/FirebaseAIOnDevice#download()()` Initiates the download of the on-device AI model. |

## Public functions

### checkStatus

```
suspend fun checkStatus(): OnDeviceModelStatus
```

Checks the current status / availability of the on-device AI model.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/OnDeviceModelStatus` | An `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/OnDeviceModelStatus` object indicating the current state of the model. |

### download

```
fun download(): Flow<DownloadStatus>
```

Initiates the download of the on-device AI model.

This method returns a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` that emits `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus` updates as the download progresses. Consumers should collect the flow to start the download process, and optionally process any updates on the download state, progress, and completion or failure.

| Returns |
|---|---|
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus>` | A `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus` objects representing the download lifecycle. |