# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus.md.txt

# DownloadStatus

# DownloadStatus


```
public abstract class DownloadStatus
```

<br />

Known direct subclasses [DownloadStatus.DownloadCompleted](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus.DownloadCompleted), [DownloadStatus.DownloadFailed](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus.DownloadFailed), [DownloadStatus.DownloadInProgress](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus.DownloadInProgress), [DownloadStatus.DownloadStarted](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus.DownloadStarted)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus.DownloadCompleted` | Represents when a download has successfully completed. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus.DownloadFailed` | Represents when a download has failed. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus.DownloadInProgress` | Represents when a download is actively in progress. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus.DownloadStarted` | Represents when a download has just started. |

*** ** * ** ***

An abstract class representing the status of an on-device model download operation.

This class has several concrete subclasses, each representing a specific stage or outcome of the download process.

## Summary

| ### Nested types |
|---|
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus.DownloadCompleted extends https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus` Represents when a download has successfully completed. |
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus.DownloadFailed extends https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus` Represents when a download has failed. |
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus.DownloadInProgress extends https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus` Represents when a download is actively in progress. |
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus.DownloadStarted extends https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus` Represents when a download has just started. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ondevice/DownloadStatus#DownloadStatus()()` |

## Public constructors

### DownloadStatus

```
public DownloadStatus()
```