# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerConfig.md.txt

# ServerConfig

public final class **ServerConfig** extends Object  
Represents the configuration produced by evaluating a server template.

### Public Method Summary

|---|---|
| boolean | [getBoolean](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerConfig#getBoolean(java.lang.String))(String key) Gets the value for the given key as a boolean.Convenience method for calling serverConfig.getValue(key).asBoolean(). |
| double | [getDouble](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerConfig#getDouble(java.lang.String))(String key) Gets the value for the given key as double.Convenience method for calling serverConfig.getValue(key).asDouble(). |
| long | [getLong](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerConfig#getLong(java.lang.String))(String key) Gets the value for the given key as long.Convenience method for calling serverConfig.getValue(key).asLong(). |
| String | [getString](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerConfig#getString(java.lang.String))(String key) Gets the value for the given key as a string. |
| [ValueSource](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ValueSource) | [getValueSource](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerConfig#getValueSource(java.lang.String))(String key) Gets the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ValueSource` for the given key. |

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
**getBoolean**
(String key)

Gets the value for the given key as a boolean.Convenience method for calling
serverConfig.getValue(key).asBoolean().

##### Parameters

| key | The name of the parameter. |
|---|---|

##### Returns

- config value for the given key as boolean.

#### public double
**getDouble**
(String key)

Gets the value for the given key as double.Convenience method for calling
serverConfig.getValue(key).asDouble().

##### Parameters

| key | The name of the parameter. |
|---|---|

##### Returns

- config value for the given key as double.

#### public long
**getLong**
(String key)

Gets the value for the given key as long.Convenience method for calling
serverConfig.getValue(key).asLong().

##### Parameters

| key | The name of the parameter. |
|---|---|

##### Returns

- config value for the given key as long.

#### public String
**getString**
(String key)

Gets the value for the given key as a string. Convenience method for calling
serverConfig.getValue(key).asString().

##### Parameters

| key | The name of the parameter. |
|---|---|

##### Returns

- config value for the given key as string.

#### public [ValueSource](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ValueSource)
**getValueSource**
(String key)

Gets the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ValueSource` for the given key.

##### Parameters

| key | The name of the parameter. |
|---|---|

##### Returns

- config value source for the given key.