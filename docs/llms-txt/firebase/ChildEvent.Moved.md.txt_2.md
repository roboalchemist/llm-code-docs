# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/ChildEvent.Moved.md.txt

# ChildEvent.Moved

# ChildEvent.Moved


```
public final data class ChildEvent.Moved extends ChildEvent
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.database.ktx.ChildEvent](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/ChildEvent) ||
|   | ↳ | [com.google.firebase.database.ktx.ChildEvent.Moved](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/ChildEvent.Moved) |

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Emitted when a child location's priority changes.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/ChildEvent.Moved#previousChildName()` The key name of the sibling location ordered before the child |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/ChildEvent.Moved#snapshot()` An immutable snapshot of the data at the location that moved. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/ChildEvent.Moved#Moved(com.google.firebase.database.DataSnapshot,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot snapshot, https://developer.android.com/reference/kotlin/java/lang/String.html previousChildName)` |

## Public fields

### previousChildName

```
public final String previousChildName
```

The key name of the sibling location ordered before the child

```
    location. This will be null if this location is ordered first.
```

### snapshot

```
public final @NonNull DataSnapshot snapshot
```

An immutable snapshot of the data at the location that moved.

## Public constructors

### Moved

```
public Moved(@NonNull DataSnapshot snapshot, String previousChildName)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot snapshot` | An immutable snapshot of the data at the location that moved. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html previousChildName` | The key name of the sibling location ordered before the child ``` location. This will be null if this location is ordered first. ``` |