Package org.apache.commons.validator

# Class Arg

java.lang.Object
org.apache.commons.validator.Arg

All Implemented Interfaces:
`Serializable`, `Cloneable`

---

public class Arg
extends Object
implements Cloneable, Serializable

 A default argument or an argument for a
 specific validator definition (ex: required)
 can be stored to pass into a message as parameters.  This can be used in a
 pluggable validator for constructing locale
 sensitive messages by using `MessageFormat`
 or an equivalent class.  The resource field can be
 used to determine if the value stored in the argument
 is a value to be retrieved from a locale sensitive
 message retrieval system like `java.util.PropertyResourceBundle`.
 The resource field defaults to 'true'.
 
 

Instances of this class are configured with an <arg> xml element.

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

The resource bundle name that this Arg's `key` should be
 resolved in (optional).

`protected String`
`key`

The key or value of the argument.

`protected String`
`name`

The name dependency that this argument goes with (optional).

`protected int`
`position`

This argument's position in the message.

`protected boolean`
`resource`

Whether or not the key is a message resource (optional).

- 

## Constructor Summary

Constructors

Constructor
Description
`Arg()`

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

Gets the resource bundle name.

`String`
`getKey()`

Gets the key/value.

`String`
`getName()`

Gets the name of the dependency.

`int`
`getPosition()`

Gets the replacement position.

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
`setPosition(int position)`

Sets this argument's replacement position.

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
The resource bundle name that this Arg's `key` should be
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

### position

protected int position
This argument's position in the message. Set position=0 to
 make a replacement in this string: "some msg {0}".

Since:
1.1

  - 

### resource

protected boolean resource
Whether or not the key is a message resource (optional).  Defaults to
 true.  If it is 'true', the value will try to be resolved as a message
 resource.

- 

## Constructor Details

  - 

### Arg

public Arg()
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
A copy of this object.

  - 

### getBundle

public String getBundle()
Gets the resource bundle name.

Returns:
the bundle name.
Since:
1.1

  - 

### getKey

public String getKey()
Gets the key/value.

Returns:
the key value.

  - 

### getName

public String getName()
Gets the name of the dependency.

Returns:
the name of the dependency.

  - 

### getPosition

public int getPosition()
Gets the replacement position.

Returns:
This replacement position.

  - 

### isResource

public boolean isResource()
Tests whether or not the key is a resource key or literal value.

Returns:
`true` if key is a resource key.

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
`key` - They to access the argument.

  - 

### setName

public void setName(String name)
Sets the name of the dependency.

Parameters:
`name` - the name of the dependency.

  - 

### setPosition

public void setPosition(int position)
Sets this argument's replacement position.

Parameters:
`position` - set this argument's replacement position.

  - 

### setResource

public void setResource(boolean resource)
Sets whether or not the key is a resource.

Parameters:
`resource` - If true indicates the key is a resource.

  - 

### toString

public String toString()
Returns a string representation of the object.

Overrides:
`toString` in class `Object`
Returns:
a string representation of the object.