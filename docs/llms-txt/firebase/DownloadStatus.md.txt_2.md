# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus.md.txt

# DownloadStatus

# DownloadStatus


```
abstract class DownloadStatus
```

<br />

Known direct subclasses [DownloadStatus.DownloadCompleted](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus.DownloadCompleted), [DownloadStatus.DownloadFailed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus.DownloadFailed), [DownloadStatus.DownloadInProgress](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus.DownloadInProgress), [DownloadStatus.DownloadStarted](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus.DownloadStarted)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus.DownloadCompleted` | Represents when a download has successfully completed. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus.DownloadFailed` | Represents when a download has failed. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus.DownloadInProgress` | Represents when a download is actively in progress. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus.DownloadStarted` | Represents when a download has just started. |

*** ** * ** ***

An abstract class representing the status of an on-device model download operation.

This class has several concrete subclasses, each representing a specific stage or outcome of the download process.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus.DownloadCompleted : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus` Represents when a download has successfully completed. |
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus.DownloadFailed : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus` Represents when a download has failed. |
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus.DownloadInProgress : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus` Represents when a download is actively in progress. |
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus.DownloadStarted : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus` Represents when a download has just started. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ondevice/DownloadStatus#DownloadStatus()()` |

## Public constructors

### DownloadStatus

```
DownloadStatus()
```