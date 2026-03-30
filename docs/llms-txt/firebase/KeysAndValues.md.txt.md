# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues.md.txt

# KeysAndValues

public class **KeysAndValues** extends Object  
Represents data stored in context passed to server-side Remote Config.

### Nested Class Summary

|---|---|---|---|
| class | [KeysAndValues.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues.Builder) || Builder class for KeysAndValues using which values will be assigned to private variables. |

### Public Method Summary

|---|---|
| boolean | [containsKey](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues#containsKey(java.lang.String))(String key) Checks whether a key is present in the context. |
| String | [get](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues#get(java.lang.String))(String key) Gets the value of the data stored in context. |

### Inherited Method Summary

From class java.lang.Object

|---|---|
| Object | clone() |
| boolean | equals(Object arg0) |
| void | finalize() |
| final Class\<?\> | getClass() |
| int | hashCode() |
| final void | notify() |
| final void | notifyAll() |
| String | toString() |
| final void | wait(long arg0, int arg1) |
| final void | wait(long arg0) |
| final void | wait() |

## Public Methods

#### public boolean
**containsKey**
(String key)

Checks whether a key is present in the context.

##### Parameters

| key | The key for data stored in context. |
|---|---|

##### Returns

- Boolean representing whether the key passed is present in context.

#### public String
**get**
(String key)

Gets the value of the data stored in context.

##### Parameters

| key | The key for data stored in context. |
|---|---|

##### Returns

- Value assigned to the key in context.