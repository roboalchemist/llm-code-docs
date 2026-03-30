# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect.md.txt

# OnDisconnect

# OnDisconnect


```
class OnDisconnect
```

<br />

*** ** * ** ***

The OnDisconnect class is used to manage operations that will be run on the server when this client disconnects. It can be used to add or remove data based on a client's connection status. It is very useful in applications looking for 'presence' functionality. Instances of this class are obtained by calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#onDisconnect()` on a Firebase Database ref.

## Summary

| ### Public functions |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#cancel()()` Cancel any disconnect operations that are queued up at this location |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#cancel(com.google.firebase.database.DatabaseReference.CompletionListener)(listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener)` Cancel any disconnect operations that are queued up at this location |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#removeValue()()` Remove the value at this location when the client disconnects |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#removeValue(com.google.firebase.database.DatabaseReference.CompletionListener)(listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener?)` Remove the value at this location when the client disconnects |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Ensure the data at this location is set to the specified value when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object,com.google.firebase.database.DatabaseReference.CompletionListener)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener?)` Ensure the data at this location is set to the specified value when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object,java.lang.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?, priority: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object,double)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?, priority: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object,java.util.Map,com.google.firebase.database.DatabaseReference.CompletionListener)( value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?, priority: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html?, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener? )` Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object,java.lang.String,com.google.firebase.database.DatabaseReference.CompletionListener)( value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?, priority: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener? )` Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object,double,com.google.firebase.database.DatabaseReference.CompletionListener)( value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?, priority: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener? )` Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#updateChildren(java.util.Map<java.lang.String,java.lang.Object>)(update: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Ensure the data has the specified child values updated when the client is disconnected |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#updateChildren(java.util.Map<java.lang.String,java.lang.Object>,com.google.firebase.database.DatabaseReference.CompletionListener)( update: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener? )` Ensure the data has the specified child values updated when the client is disconnected |

## Public functions

### cancel

```
fun cancel(): Task<Void!>
```

Cancel any disconnect operations that are queued up at this location

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### cancel

```
fun cancel(listener: DatabaseReference.CompletionListener): Unit
```

Cancel any disconnect operations that are queued up at this location

| Parameters |
|---|---|
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener` | A listener that will be triggered once the server has cancelled the operations |

### removeValue

```
fun removeValue(): Task<Void!>
```

Remove the value at this location when the client disconnects

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### removeValue

```
fun removeValue(listener: DatabaseReference.CompletionListener?): Unit
```

Remove the value at this location when the client disconnects

| Parameters |
|---|---|
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener?` | A listener that will be triggered once the server has queued up the operation |

### setValue

```
fun setValue(value: Any?): Task<Void!>
```

Ensure the data at this location is set to the specified value when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The value to be set when a disconnect occurs or null to delete the existing value |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### setValue

```
fun setValue(value: Any?, listener: DatabaseReference.CompletionListener?): Unit
```

Ensure the data at this location is set to the specified value when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The value to be set when a disconnect occurs or null to delete the existing value |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener?` | A listener that will be triggered once the server has queued up the operation |

### setValue

```
fun setValue(value: Any?, priority: String?): Task<Void!>
```

Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The value to be set when a disconnect occurs or null to delete the existing value |
| `priority: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The priority to be set when a disconnect occurs or null to clear the existing priority |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### setValue

```
fun setValue(value: Any?, priority: Double): Task<Void!>
```

Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The value to be set when a disconnect occurs or null to delete the existing value |
| `priority: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` | The priority to be set when a disconnect occurs |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### setValue

```
fun setValue(
    value: Any?,
    priority: (Mutable)Map?,
    listener: DatabaseReference.CompletionListener?
): Unit
```

Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The value to be set when a disconnect occurs or null to delete the existing value |
| `priority: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html?` | The priority to be set when a disconnect occurs |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener?` | A listener that will be triggered once the server has queued up the operation |

### setValue

```
fun setValue(
    value: Any?,
    priority: String?,
    listener: DatabaseReference.CompletionListener?
): Unit
```

Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The value to be set when a disconnect occurs or null to delete the existing value |
| `priority: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The priority to be set when a disconnect occurs or null to clear the existing priority |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener?` | A listener that will be triggered once the server has queued up the operation |

### setValue

```
fun setValue(
    value: Any?,
    priority: Double,
    listener: DatabaseReference.CompletionListener?
): Unit
```

Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The value to be set when a disconnect occurs or null to delete the existing value |
| `priority: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` | The priority to be set when a disconnect occurs |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener?` | A listener that will be triggered once the server has queued up the operation |

### updateChildren

```
fun updateChildren(update: (Mutable)Map<String!, Any!>): Task<Void!>
```

Ensure the data has the specified child values updated when the client is disconnected

| Parameters |
|---|---|
| `update: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>` | The paths to update, along with their desired values |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### updateChildren

```
fun updateChildren(
    update: (Mutable)Map<String!, Any!>,
    listener: DatabaseReference.CompletionListener?
): Unit
```

Ensure the data has the specified child values updated when the client is disconnected

| Parameters |
|---|---|
| `update: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>` | The paths to update, along with their desired values |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener?` | A listener that will be triggered once the server has queued up the operation |