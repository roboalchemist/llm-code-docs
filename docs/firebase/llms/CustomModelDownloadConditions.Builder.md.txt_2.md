# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder.md.txt

# CustomModelDownloadConditions.Builder

# CustomModelDownloadConditions.Builder


```
class CustomModelDownloadConditions.Builder
```

<br />

*** ** * ** ***

Builder of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions`.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder#Builder()()` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder#build()()` Builds `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresApi.html(value = VERSION_CODES.N) @https://developer.android.com/reference/kotlin/android/annotation/TargetApi.html(value = VERSION_CODES.N) https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder#requireCharging()()` Sets charging as required. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresApi.html(value = VERSION_CODES.N) @https://developer.android.com/reference/kotlin/android/annotation/TargetApi.html(value = VERSION_CODES.N) https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder#requireDeviceIdle()()` Sets device idle as required. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder#requireWifi()()` Sets wifi as required. |

## Public constructors

### Builder

```
Builder()
```

## Public functions

### build

```
fun build(): CustomModelDownloadConditions
```

Builds `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions`.

### requireCharging

```
@RequiresApi(value = VERSION_CODES.N)
@TargetApi(value = VERSION_CODES.N)
fun requireCharging(): CustomModelDownloadConditions.Builder
```

Sets charging as required. Only works on Android N and above.

### requireDeviceIdle

```
@RequiresApi(value = VERSION_CODES.N)
@TargetApi(value = VERSION_CODES.N)
fun requireDeviceIdle(): CustomModelDownloadConditions.Builder
```

Sets device idle as required.

Idle mode is a loose definition provided by the system, which means that the device is not in use, and has not been in use for some time.

Only works on Android N and above.

### requireWifi

```
fun requireWifi(): CustomModelDownloadConditions.Builder
```

Sets wifi as required.