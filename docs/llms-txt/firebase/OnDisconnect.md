# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/OnDisconnect.md.txt

# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/OnDisconnect.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect.md.txt

# OnDisconnect

# OnDisconnect


```
class OnDisconnect
```

<br />

*** ** * ** ***

The OnDisconnect class is used to manage operations that will be run on the server when this client disconnects. It can be used to add or remove data based on a client's connection status. It is very useful in applications looking for 'presence' functionality. Instances of this class are obtained by calling [onDisconnect](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#onDisconnect()) on a Firebase Database ref.

## Summary

|                                                                              ### Public functions                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | [cancel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#cancel())`()` Cancel any disconnect operations that are queued up at this location                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                    | [cancel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#cancel(com.google.firebase.database.DatabaseReference.CompletionListener))`(listener: `[DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener)`)` Cancel any disconnect operations that are queued up at this location                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | [removeValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#removeValue())`()` Remove the value at this location when the client disconnects                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                    | [removeValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#removeValue(com.google.firebase.database.DatabaseReference.CompletionListener))`(listener: `[DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener)`?)` Remove the value at this location when the client disconnects                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | [setValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object))`(value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?)` Ensure the data at this location is set to the specified value when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                    | [setValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object,com.google.firebase.database.DatabaseReference.CompletionListener))`(value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?, listener: `[DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener)`?)` Ensure the data at this location is set to the specified value when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).                                                                                                                                                                                                                                                          |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | [setValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object,java.lang.String))`(value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?, priority: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).                                                                                                                                                                                                                                                                                                                                                                         |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | [setValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object,double))`(value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?, priority: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`)` Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).                                                                                                                                                                                                                                                                                                                                                                                    |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                    | [setValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object,java.util.Map,com.google.firebase.database.DatabaseReference.CompletionListener))`(` ` value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?,` ` priority: (`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`?,` ` listener: `[DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener)`?` `)` Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).       |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                    | [setValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object,java.lang.String,com.google.firebase.database.DatabaseReference.CompletionListener))`(` ` value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?,` ` priority: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?,` ` listener: `[DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener)`?` `)` Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).                                                                                                                |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                    | [setValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#setValue(java.lang.Object,double,com.google.firebase.database.DatabaseReference.CompletionListener))`(` ` value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?,` ` priority: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`,` ` listener: `[DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener)`?` `)` Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues).                                                                                                                           |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | [updateChildren](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#updateChildren(java.util.Map<java.lang.String,java.lang.Object>))`(update: (`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>)` Ensure the data has the specified child values updated when the client is disconnected                                                                                                                                                                                                                                                       |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                    | [updateChildren](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/OnDisconnect#updateChildren(java.util.Map<java.lang.String,java.lang.Object>,com.google.firebase.database.DatabaseReference.CompletionListener))`(` ` update: (`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>,` ` listener: `[DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener)`?` `)` Ensure the data has the specified child values updated when the client is disconnected |

## Public functions

### cancel

```
funÂ cancel():Â Task<Void!>
```

Cancel any disconnect operations that are queued up at this location  

|                                                                                     Returns                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | The [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) for this operation. |

### cancel

```
funÂ cancel(listener:Â DatabaseReference.CompletionListener):Â Unit
```

Cancel any disconnect operations that are queued up at this location  

|                                                                               Parameters                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| `listener: `[DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener) | A listener that will be triggered once the server has cancelled the operations |

### removeValue

```
funÂ removeValue():Â Task<Void!>
```

Remove the value at this location when the client disconnects  

|                                                                                     Returns                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | The [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) for this operation. |

### removeValue

```
funÂ removeValue(listener:Â DatabaseReference.CompletionListener?):Â Unit
```

Remove the value at this location when the client disconnects  

|                                                                                 Parameters                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| `listener: `[DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener)`?` | A listener that will be triggered once the server has queued up the operation |

### setValue

```
funÂ setValue(value:Â Any?):Â Task<Void!>
```

Ensure the data at this location is set to the specified value when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.  

|                                       Parameters                                       |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| `value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?` | The value to be set when a disconnect occurs or null to delete the existing value |

|                                                                                     Returns                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | The [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) for this operation. |

### setValue

```
funÂ setValue(value:Â Any?,Â listener:Â DatabaseReference.CompletionListener?):Â Unit
```

Ensure the data at this location is set to the specified value when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.  

|                                                                                 Parameters                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| `value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?`                                                                                     | The value to be set when a disconnect occurs or null to delete the existing value |
| `listener: `[DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener)`?` | A listener that will be triggered once the server has queued up the operation     |

### setValue

```
funÂ setValue(value:Â Any?,Â priority:Â String?):Â Task<Void!>
```

Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.  

|                                           Parameters                                            |
|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| `value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?`          | The value to be set when a disconnect occurs or null to delete the existing value      |
| `priority: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The priority to be set when a disconnect occurs or null to clear the existing priority |

|                                                                                     Returns                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | The [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) for this operation. |

### setValue

```
funÂ setValue(value:Â Any?,Â priority:Â Double):Â Task<Void!>
```

Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| `value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?`       | The value to be set when a disconnect occurs or null to delete the existing value |
| `priority: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html) | The priority to be set when a disconnect occurs                                   |

|                                                                                     Returns                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | The [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) for this operation. |

### setValue

```
funÂ setValue(
Â Â Â Â value:Â Any?,
Â Â Â Â priority:Â (Mutable)Map?,
Â Â Â Â listener:Â DatabaseReference.CompletionListener?
):Â Unit
```

Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.  

|                                                                                                 Parameters                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| `value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?`                                                                                                                      | The value to be set when a disconnect occurs or null to delete the existing value |
| `priority: (`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`?` | The priority to be set when a disconnect occurs                                   |
| `listener: `[DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener)`?`                                  | A listener that will be triggered once the server has queued up the operation     |

### setValue

```
funÂ setValue(
Â Â Â Â value:Â Any?,
Â Â Â Â priority:Â String?,
Â Â Â Â listener:Â DatabaseReference.CompletionListener?
):Â Unit
```

Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.  

|                                                                                 Parameters                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| `value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?`                                                                                     | The value to be set when a disconnect occurs or null to delete the existing value      |
| `priority: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                                                            | The priority to be set when a disconnect occurs or null to clear the existing priority |
| `listener: `[DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener)`?` | A listener that will be triggered once the server has queued up the operation          |

### setValue

```
funÂ setValue(
Â Â Â Â value:Â Any?,
Â Â Â Â priority:Â Double,
Â Â Â Â listener:Â DatabaseReference.CompletionListener?
):Â Unit
```

Ensure the data at this location is set to the specified value and priority when the client is disconnected (due to closing the browser, navigating to a new page, or network issues). This method is especially useful for implementing "presence" systems, where a value should be changed or cleared when a user disconnects so that they appear "offline" to other users.  

|                                                                                 Parameters                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| `value: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?`                                                                                     | The value to be set when a disconnect occurs or null to delete the existing value |
| `priority: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)                                                                               | The priority to be set when a disconnect occurs                                   |
| `listener: `[DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener)`?` | A listener that will be triggered once the server has queued up the operation     |

### updateChildren

```
funÂ updateChildren(update:Â (Mutable)Map<String!,Â Any!>):Â Task<Void!>
```

Ensure the data has the specified child values updated when the client is disconnected  

|                                                                                                                                                                                  Parameters                                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| `update: (`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>` | The paths to update, along with their desired values |

|                                                                                     Returns                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | The [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) for this operation. |

### updateChildren

```
funÂ updateChildren(
Â Â Â Â update:Â (Mutable)Map<String!,Â Any!>,
Â Â Â Â listener:Â DatabaseReference.CompletionListener?
):Â Unit
```

Ensure the data has the specified child values updated when the client is disconnected  

|                                                                                                                                                                                  Parameters                                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| `update: (`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>` | The paths to update, along with their desired values                          |
| `listener: `[DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference.CompletionListener)`?`                                                                                                                                                                                                   | A listener that will be triggered once the server has queued up the operation |