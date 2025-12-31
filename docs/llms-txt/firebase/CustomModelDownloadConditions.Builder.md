# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder.md.txt

# CustomModelDownloadConditions.Builder

# CustomModelDownloadConditions.Builder


```
class CustomModelDownloadConditions.Builder
```

<br />

*** ** * ** ***

Builder of [CustomModelDownloadConditions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions).

## Summary

|                                                                 ### Public constructors                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder#Builder())`()` |

|                                                                          ### Public functions                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CustomModelDownloadConditions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions)                 | [build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder#build())`()` Builds [CustomModelDownloadConditions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions).                                                                                                                                                    |
| [CustomModelDownloadConditions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder) | `@`[RequiresApi](https://developer.android.com/reference/kotlin/androidx/annotation/RequiresApi.html)`(value = VERSION_CODES.N)` `@`[TargetApi](https://developer.android.com/reference/kotlin/android/annotation/TargetApi.html)`(value = VERSION_CODES.N)` [requireCharging](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder#requireCharging())`()` Sets charging as required.        |
| [CustomModelDownloadConditions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder) | `@`[RequiresApi](https://developer.android.com/reference/kotlin/androidx/annotation/RequiresApi.html)`(value = VERSION_CODES.N)` `@`[TargetApi](https://developer.android.com/reference/kotlin/android/annotation/TargetApi.html)`(value = VERSION_CODES.N)` [requireDeviceIdle](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder#requireDeviceIdle())`()` Sets device idle as required. |
| [CustomModelDownloadConditions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder) | [requireWifi](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder#requireWifi())`()` Sets wifi as required.                                                                                                                                                                                                                                                                                 |

## Public constructors

### Builder

```
Builder()
```  

## Public functions

### build

```
funÂ build():Â CustomModelDownloadConditions
```

Builds [CustomModelDownloadConditions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions).  

### requireCharging

```
@RequiresApi(valueÂ =Â VERSION_CODES.N)
@TargetApi(valueÂ =Â VERSION_CODES.N)
funÂ requireCharging():Â CustomModelDownloadConditions.Builder
```

Sets charging as required. Only works on Android N and above.  

### requireDeviceIdle

```
@RequiresApi(valueÂ =Â VERSION_CODES.N)
@TargetApi(valueÂ =Â VERSION_CODES.N)
funÂ requireDeviceIdle():Â CustomModelDownloadConditions.Builder
```

Sets device idle as required.

Idle mode is a loose definition provided by the system, which means that the device is not in use, and has not been in use for some time.

Only works on Android N and above.  

### requireWifi

```
funÂ requireWifi():Â CustomModelDownloadConditions.Builder
```

Sets wifi as required.