# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.md.txt

# CustomModelDownloadConditions

# CustomModelDownloadConditions


```
public class CustomModelDownloadConditions
```

<br />

*** ** * ** ***

Conditions to allow download of custom models.

## Summary

| ### Nested types |
|---|
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder` Builder of `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions`. |

| ### Public fields |
|---|---|
| `final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions#isChargingRequired()` |
| `final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions#isDeviceIdleRequired()` |
| `final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions#isWifiRequired()` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions#equals(java.lang.Object)(https://developer.android.com/reference/kotlin/java/lang/Object.html o)` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions#hashCode()()` |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions#isChargingRequired()()` |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions#isDeviceIdleRequired()()` |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions#isWifiRequired()()` |

## Public fields

### isChargingRequired

```
public final boolean isChargingRequired
```

### isDeviceIdleRequired

```
public final boolean isDeviceIdleRequired
```

### isWifiRequired

```
public final boolean isWifiRequired
```

## Public methods

### equals

```
public boolean equals(Object o)
```

### hashCode

```
public int hashCode()
```

### isChargingRequired

```
public boolean isChargingRequired()
```

| Returns |
|---|---|
| `boolean` | True if charging is required for download. |

### isDeviceIdleRequired

```
public boolean isDeviceIdleRequired()
```

| Returns |
|---|---|
| `boolean` | True if device idle is required for download. |

### isWifiRequired

```
public boolean isWifiRequired()
```

| Returns |
|---|---|
| `boolean` | True if wifi is required for download. |