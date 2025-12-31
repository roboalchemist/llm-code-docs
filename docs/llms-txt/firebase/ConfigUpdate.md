# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate.md.txt

# ConfigUpdate

# ConfigUpdate


```
@AutoValue
public abstract class ConfigUpdate
```

<br />

*** ** * ** ***

Information about the updated config passed to [onUpdate](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdateListener#onUpdate(com.google.firebase.remoteconfig.ConfigUpdate)).

## Summary

|                                                       ### Public constructors                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------|
| [ConfigUpdate](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate#ConfigUpdate())`()` |

|                                                                                                                          ### Public methods                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ConfigUpdate](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate)                                               | [create](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate#create(java.util.Set<java.lang.String>))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Set](https://developer.android.com/reference/kotlin/java/util/Set.html)`<`[String](https://developer.android.com/reference/kotlin/java/lang/String.html)`> updatedKeys)` |
| `abstract @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Set](https://developer.android.com/reference/kotlin/java/util/Set.html)`<`[String](https://developer.android.com/reference/kotlin/java/lang/String.html)`>` | [getUpdatedKeys](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate#getUpdatedKeys())`()` Parameter keys whose values have been updated from the currently activated values.                                                                                                                                                                                                   |

## Public constructors

### ConfigUpdate

```
publicÂ ConfigUpdate()
```  

## Public methods

### create

```
publicÂ staticÂ @NonNull ConfigUpdateÂ create(@NonNull Set<String>Â updatedKeys)
```  

### getUpdatedKeys

```
publicÂ abstractÂ @NonNull Set<String>Â getUpdatedKeys()
```

Parameter keys whose values have been updated from the currently activated values. Includes keys that are added, deleted, and whose value, value source, or metadata has changed.