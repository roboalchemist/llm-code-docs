Package org.apache.commons.validator

# Class Msg

java.lang.Object
org.apache.commons.validator.Msg

All Implemented Interfaces:
`Serializable`, `Cloneable`

---

public class Msg
extends Object
implements Cloneable, Serializable
An alternative message can be associated with a `Field`
 and a pluggable validator instead of using the default message
 stored in the `ValidatorAction` (aka pluggable validator).
 Instances of this class are configured with a <msg> xml element.

See Also:

- Serialized Form

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`protected String`
`bundle`

The resource bundle name that this Msg's `key` should be
 resolved in (optional).

`protected String`
`key`

The key or value of the argument.

`protected String`
`name`

The name dependency that this argument goes with (optional).

`protected boolean`
`resource`

Whether or not the key is a message resource (optional).

- 

## Constructor Summary

Constructors

Constructor
Description
`Msg()`

Constructs a new instance.

- 

## Method Summary

Modifier and Type
Method
Description
`Object`
`clone()`

Creates and returns a copy of this object.

`String`
`getBundle()`

Returns the resource bundle name.

`String`
`getKey()`

Gets the key/value.

`String`
`getName()`

Gets the name of the dependency.

`boolean`
`isResource()`

Tests whether or not the key is a resource key or literal value.

`void`
`setBundle(String bundle)`

Sets the resource bundle name.

`void`
`setKey(String key)`

Sets the key/value.

`void`
`setName(String name)`

Sets the name of the dependency.

`void`
`setResource(boolean resource)`

Sets whether or not the key is a resource.

`String`
`toString()`

Returns a string representation of the object.

### Methods inherited from class java.lang.Object

`equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Field Details

  - 

### bundle

protected String bundle
The resource bundle name that this Msg's `key` should be
 resolved in (optional).

Since:
1.1

  - 

### key

protected String key
The key or value of the argument.

  - 

### name

protected String name
The name dependency that this argument goes with (optional).

  - 

### resource

protected boolean resource
Whether or not the key is a message resource (optional).  Defaults to
 true.  If it is 'true', the value will try to be resolved as a message
 resource.

Since:
1.1.4

- 

## Constructor Details

  - 

### Msg

public Msg()
Constructs a new instance.

- 

## Method Details

  - 

### clone

public Object clone()
Creates and returns a copy of this object.

Overrides:
`clone` in class `Object`
Returns:
A copy of the Msg.

  - 

### getBundle

public String getBundle()
Returns the resource bundle name.

Returns:
The bundle name.
Since:
1.1

  - 

### getKey

public String getKey()
Gets the key/value.

Returns:
The message key/value.

  - 

### getName

public String getName()
Gets the name of the dependency.

Returns:
The dependency name.

  - 

### isResource

public boolean isResource()
Tests whether or not the key is a resource key or literal value.

Returns:
`true` if key is a resource key.
Since:
1.1.4

  - 

### setBundle

public void setBundle(String bundle)
Sets the resource bundle name.

Parameters:
`bundle` - The new bundle name.
Since:
1.1

  - 

### setKey

public void setKey(String key)
Sets the key/value.

Parameters:
`key` - The message key/value.

  - 

### setName

public void setName(String name)
Sets the name of the dependency.

Parameters:
`name` - The dependency name.

  - 

### setResource

public void setResource(boolean resource)
Sets whether or not the key is a resource.

Parameters:
`resource` - If true indicates the key is a resource.
Since:
1.1.4

  - 

### toString

public String toString()
Returns a string representation of the object.

Overrides:
`toString` in class `Object`
Returns:
Msg String representation.