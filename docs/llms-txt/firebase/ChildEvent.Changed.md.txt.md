# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/ChildEvent.Changed.md.txt

# ChildEvent.Changed

# ChildEvent.Changed


```
public final data class ChildEvent.Changed extends ChildEvent
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.database.ktx.ChildEvent](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/ChildEvent) ||
|   | ↳ | [com.google.firebase.database.ktx.ChildEvent.Changed](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/ChildEvent.Changed) |

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Emitted when the data at a child location has changed.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/ChildEvent.Changed#previousChildName()` The key name of sibling location ordered before the child. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/ChildEvent.Changed#snapshot()` An immutable snapshot of the data at the new data at the child location |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/database/ktx/ChildEvent.Changed#Changed(com.google.firebase.database.DataSnapshot,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot snapshot, https://developer.android.com/reference/kotlin/java/lang/String.html previousChildName)` |

## Public fields

### previousChildName

```
public final String previousChildName
```

The key name of sibling location ordered before the child. This will

```
    be null for the first child node of a location.
```

### snapshot

```
public final @NonNull DataSnapshot snapshot
```

An immutable snapshot of the data at the new data at the child location

## Public constructors

### Changed

```
public Changed(@NonNull DataSnapshot snapshot, String previousChildName)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot snapshot` | An immutable snapshot of the data at the new data at the child location |
| `https://developer.android.com/reference/kotlin/java/lang/String.html previousChildName` | The key name of sibling location ordered before the child. This will ``` be null for the first child node of a location. ``` |