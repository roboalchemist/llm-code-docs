# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/OnDisconnect.md.txt

# OnDisconnect

# OnDisconnect


```
public class OnDisconnect
```

<br />

*** ** * ** ***

The OnDisconnect class is used to manage operations that will be run on the server when this client disconnects. It can be used to add or remove data based on a client's connection status. It is very useful in applications looking for 'presence' functionality. Instances of this class are obtained by calling `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#onDisconnect()` on a Firebase Database ref.

## Summary

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/OnDisconnect#cancel()()` Cancel any disconnect operations that are queued up at this location |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/OnDisconnect#cancel(com.google.firebase.database.DatabaseReference.CompletionListener)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener)` Cancel any disconnect operations that are queued up at this location |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/OnDisconnect#removeValue()()` Remove the value at this location when the client disconnects |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/OnDisconnect#removeValue(com.google.firebase.database.DatabaseReference.CompletionListener)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener)` Remove the value at this location when the client disconnects |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value)` Ensure the data at this location is set to the specified value when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object,com.google.firebase.database.DatabaseReference.CompletionListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener )` Ensure the data at this location is set to the specified value when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object,java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html priority)` Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object,double)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value, double priority)` Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object,java.util.Map,com.google.firebase.database.DatabaseReference.CompletionListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/util/Map.html priority, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener )` Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object,java.lang.String,com.google.firebase.database.DatabaseReference.CompletionListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html priority, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener )` Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object,double,com.google.firebase.database.DatabaseReference.CompletionListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value, double priority, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener )` Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/OnDisconnect#updateChildren(java.util.Map<java.lang.String,java.lang.Object>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html> update)` Ensure the data has the specified child values updated when the client is disconnected |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/OnDisconnect#updateChildren(java.util.Map<java.lang.String,java.lang.Object>,com.google.firebase.database.DatabaseReference.CompletionListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html> update, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener )` Ensure the data has the specified child values updated when the client is disconnected |

## Public methods

### cancel

```
public @NonNull Task<Void> cancel()
```

Cancel any disconnect operations that are queued up at this location

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### cancel

```
public void cancel(@NonNull DatabaseReference.CompletionListener listener)
```

Cancel any disconnect operations that are queued up at this location

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener` | A listener that will be triggered once the server has cancelled the operations |

### removeValue

```
public @NonNull Task<Void> removeValue()
```

Remove the value at this location when the client disconnects

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### removeValue

```
public void removeValue(@Nullable DatabaseReference.CompletionListener listener)
```

Remove the value at this location when the client disconnects

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener` | A listener that will be triggered once the server has queued up the operation |

### setValue

```
public @NonNull Task<Void> setValue(@Nullable Object value)
```

Ensure the data at this location is set to the specified value when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The value to be set when a disconnect occurs or null to delete the existing value |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### setValue

```
public void setValue(
    @Nullable Object value,
    @Nullable DatabaseReference.CompletionListener listener
)
```

Ensure the data at this location is set to the specified value when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The value to be set when a disconnect occurs or null to delete the existing value |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener` | A listener that will be triggered once the server has queued up the operation |

### setValue

```
public @NonNull Task<Void> setValue(@Nullable Object value, @Nullable String priority)
```

Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The value to be set when a disconnect occurs or null to delete the existing value |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html priority` | The priority to be set when a disconnect occurs or null to clear the existing priority |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### setValue

```
public @NonNull Task<Void> setValue(@Nullable Object value, double priority)
```

Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The value to be set when a disconnect occurs or null to delete the existing value |
| `double priority` | The priority to be set when a disconnect occurs |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### setValue

```
public void setValue(
    @Nullable Object value,
    @Nullable Map priority,
    @Nullable DatabaseReference.CompletionListener listener
)
```

Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The value to be set when a disconnect occurs or null to delete the existing value |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/util/Map.html priority` | The priority to be set when a disconnect occurs |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener` | A listener that will be triggered once the server has queued up the operation |

### setValue

```
public void setValue(
    @Nullable Object value,
    @Nullable String priority,
    @Nullable DatabaseReference.CompletionListener listener
)
```

Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The value to be set when a disconnect occurs or null to delete the existing value |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html priority` | The priority to be set when a disconnect occurs or null to clear the existing priority |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener` | A listener that will be triggered once the server has queued up the operation |

### setValue

```
public void setValue(
    @Nullable Object value,
    double priority,
    @Nullable DatabaseReference.CompletionListener listener
)
```

Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The value to be set when a disconnect occurs or null to delete the existing value |
| `double priority` | The priority to be set when a disconnect occurs |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener` | A listener that will be triggered once the server has queued up the operation |

### updateChildren

```
public @NonNull Task<Void> updateChildren(@NonNull Map<String, Object> update)
```

Ensure the data has the specified child values updated when the client is disconnected

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html> update` | The paths to update, along with their desired values |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | The `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` for this operation. |

### updateChildren

```
public void updateChildren(
    @NonNull Map<String, Object> update,
    @Nullable DatabaseReference.CompletionListener listener
)
```

Ensure the data has the specified child values updated when the client is disconnected

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html> update` | The paths to update, along with their desired values |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference.CompletionListener listener` | A listener that will be triggered once the server has queued up the operation |