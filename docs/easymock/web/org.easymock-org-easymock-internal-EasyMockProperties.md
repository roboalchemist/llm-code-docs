Module org.easymock
Package org.easymock.internal

## Class EasyMockProperties

- java.lang.Object

- 

  - org.easymock.internal.EasyMockProperties

- 

---

```
public final class EasyMockProperties
extends Object
```

Contains properties used by EasyMock to change its default behavior. The
 loading order is (any step being able to overload the properties of the
 previous step):
 

 
  - easymock.properties in classpath default package
 
  - explicit call to setProperty
 

Author:
Henri Tremblay

- 

  - 

### Method Summary

All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`static EasyMockProperties`
`getInstance()`
 

`String`
`getProperty​(String key)`

Searches for the property with the specified key.

`String`
`getProperty​(String key,
           String defaultValue)`

Searches for the property with the specified key.

`String`
`setProperty​(String key,
           String value)`

Add a value referenced by the provided key.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Method Detail

    - 

#### getInstance

```
public static EasyMockProperties getInstance()
```

    - 

#### getProperty

```
public String getProperty​(String key,
                          String defaultValue)
```

Searches for the property with the specified key. If the key is not
 found, return the default value.

Parameters:
`key` - key leading to the property
`defaultValue` - the value to be returned if the key isn't found
Returns:
the value found for the key or the default value

    - 

#### getProperty

```
public String getProperty​(String key)
```

Searches for the property with the specified key. Return null if the key
 is not found.

Parameters:
`key` - key leading to the property
Returns:
the value found for the key or null

    - 

#### setProperty

```
public String setProperty​(String key,
                          String value)
```

Add a value referenced by the provided key. A null value will remove the
 key

Parameters:
`key` - the key of the new property
`value` - the value corresponding to `key`.
Returns:
the property previous value