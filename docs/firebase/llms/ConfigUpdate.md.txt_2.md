# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate.md.txt

# ConfigUpdate

# ConfigUpdate


```
@AutoValue
abstract class ConfigUpdate
```

<br />

*** ** * ** ***

Information about the updated config passed to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListener#onUpdate(com.google.firebase.remoteconfig.ConfigUpdate)`.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate#ConfigUpdate()()` |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate#create(java.util.Set<java.lang.String>)(updatedKeys: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>)` |
| `abstract (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate#getUpdatedKeys()()` Parameter keys whose values have been updated from the currently activated values. |

## Public constructors

### ConfigUpdate

```
ConfigUpdate()
```

## Public functions

### create

```
java-static fun create(updatedKeys: (Mutable)Set<String!>): ConfigUpdate
```

### getUpdatedKeys

```
abstract fun getUpdatedKeys(): (Mutable)Set<String!>
```

Parameter keys whose values have been updated from the currently activated values. Includes keys that are added, deleted, and whose value, value source, or metadata has changed.