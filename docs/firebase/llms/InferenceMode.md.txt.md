# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/InferenceMode.md.txt

# InferenceMode

# InferenceMode


```
@PublicPreviewAPI
public final class InferenceMode
```

<br />

*** ** * ** ***

Specifies how the SDK should choose between on-device and in-cloud inference.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/InferenceMode.Companion` |

| ### Public fields |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/InferenceMode` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/InferenceMode.Companion#ONLY_IN_CLOUD()` Only use in-cloud inference. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/InferenceMode` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/InferenceMode.Companion#ONLY_ON_DEVICE()` Only use on-device inference. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/InferenceMode` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/InferenceMode.Companion#PREFER_IN_CLOUD()` Prefer in-cloud inference, but fallback to on-device if cloud is unavailable. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/InferenceMode` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/InferenceMode.Companion#PREFER_ON_DEVICE()` Prefer on-device inference, but fallback to in-cloud if unavailable. |

## Public fields

### ONLY_IN_CLOUD

```
public static final @NonNull InferenceMode ONLY_IN_CLOUD
```

Only use in-cloud inference.

### ONLY_ON_DEVICE

```
public static final @NonNull InferenceMode ONLY_ON_DEVICE
```

Only use on-device inference.

### PREFER_IN_CLOUD

```
public static final @NonNull InferenceMode PREFER_IN_CLOUD
```

Prefer in-cloud inference, but fallback to on-device if cloud is unavailable.

In this mode, the SDK will use in-cloud inference only unless the device is offline, at which point the SDK will fall back to on-device inference.

### PREFER_ON_DEVICE

```
public static final @NonNull InferenceMode PREFER_ON_DEVICE
```

Prefer on-device inference, but fallback to in-cloud if unavailable.

In this mode, the SDK will attempt to use on-device inference first and, if the on-device model is unable to generate an answer, it will retry using the cloud model.