# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues.Builder.md.txt

# KeysAndValues.Builder

public static class **KeysAndValues.Builder** extends Object  
Builder class for KeysAndValues using which values will be assigned to
private variables.

### Public Constructor Summary

|---|---|
|   | [Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues.Builder#Builder())() |

### Public Method Summary

|---|---|
| [KeysAndValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues) | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues.Builder#build())() Creates an instance of KeysAndValues with the values assigned through builder. |
| [KeysAndValues.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues.Builder) | [put](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues.Builder#put(java.lang.String, double))(String key, double value) Adds a context data with double value. |
| [KeysAndValues.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues.Builder) | [put](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues.Builder#put(java.lang.String, long))(String key, long value) Adds a context data with long value. |
| [KeysAndValues.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues.Builder) | [put](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues.Builder#put(java.lang.String, java.lang.String))(String key, String value) Adds a context data with string value. |
| [KeysAndValues.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues.Builder) | [put](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues.Builder#put(java.lang.String, boolean))(String key, boolean value) Adds a context data with boolean value. |

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

## Public Constructors

#### public
**Builder**
()

<br />

## Public Methods

#### public [KeysAndValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues)
**build**
()

Creates an instance of KeysAndValues with the values assigned through
builder.

##### Returns

- instance of KeysAndValues

#### public [KeysAndValues.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues.Builder)
**put**
(String key, double value)

Adds a context data with double value.

##### Parameters

| key | Identifies the value in context. |
| value | Value assigned to the context. |
|---|---|

##### Returns

- Reference to class itself so that more data can be added.

#### public [KeysAndValues.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues.Builder)
**put**
(String key, long value)

Adds a context data with long value.

##### Parameters

| key | Identifies the value in context. |
| value | Value assigned to the context. |
|---|---|

##### Returns

- Reference to class itself so that more data can be added.

#### public [KeysAndValues.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues.Builder)
**put**
(String key, String value)

Adds a context data with string value.

##### Parameters

| key | Identifies the value in context. |
| value | Value assigned to the context. |
|---|---|

##### Returns

- Reference to class itself so that more data can be added.

#### public [KeysAndValues.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues.Builder)
**put**
(String key, boolean value)

Adds a context data with boolean value.

##### Parameters

| key | Identifies the value in context. |
| value | Value assigned to the context. |
|---|---|

##### Returns

- Reference to class itself so that more data can be added.