# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate.md.txt

# ConfigUpdate

# ConfigUpdate


```
@AutoValue
public abstract class ConfigUpdate
```

<br />

*** ** * ** ***

Information about the updated config passed to `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdateListener#onUpdate(com.google.firebase.remoteconfig.ConfigUpdate)`.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate#ConfigUpdate()()` |

| ### Public methods |
|---|---|
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate#create(java.util.Set<java.lang.String>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Set.html<https://developer.android.com/reference/kotlin/java/lang/String.html> updatedKeys)` |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Set.html<https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate#getUpdatedKeys()()` Parameter keys whose values have been updated from the currently activated values. |

## Public constructors

### ConfigUpdate

```
public ConfigUpdate()
```

## Public methods

### create

```
public static @NonNull ConfigUpdate create(@NonNull Set<String> updatedKeys)
```

### getUpdatedKeys

```
public abstract @NonNull Set<String> getUpdatedKeys()
```

Parameter keys whose values have been updated from the currently activated values. Includes keys that are added, deleted, and whose value, value source, or metadata has changed.