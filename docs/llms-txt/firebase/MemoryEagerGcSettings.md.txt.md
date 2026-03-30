# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryEagerGcSettings.md.txt

# MemoryEagerGcSettings

# MemoryEagerGcSettings


```
public final class MemoryEagerGcSettings implements MemoryGarbageCollectorSettings
```

<br />

*** ** * ** ***

Configures the SDK to use an eager garbage collector for memory cache. The eager garbage collector will attempt to remove any documents from SDK's memory cache as soon as it is no longer used.

This is the default garbage collector unless specified explicitly otherwise.

To use, create an instance using `MemoryEagerGcSettings#newBuilder().build()`, then set the instance to `MemoryCacheSettings.Builder#setGcSettings`, and use the built `
MemoryCacheSettings` instance to configure the Firestore SDK.

## Summary

| ### Nested types |
|---|
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryEagerGcSettings.Builder` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryEagerGcSettings#equals(java.lang.Object)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html obj)` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryEagerGcSettings#hashCode()()` |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryEagerGcSettings.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryEagerGcSettings#newBuilder()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryEagerGcSettings#toString()()` |

## Public methods

### equals

```
public boolean equals(@Nullable Object obj)
```

### hashCode

```
public int hashCode()
```

### newBuilder

```
public static @NonNull MemoryEagerGcSettings.Builder newBuilder()
```

### toString

```
public @NonNull String toString()
```