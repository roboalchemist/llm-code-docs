Package org.apache.commons.validator

# Class Var

java.lang.Object
org.apache.commons.validator.Var

All Implemented Interfaces:
`Serializable`, `Cloneable`

---

public class Var
extends Object
implements Cloneable, Serializable
A variable that can be associated with a `Field` for
 passing in information to a pluggable validator.  Instances of this class are
 configured with a <var> xml element.

See Also:

- Serialized Form

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final String`
`JSTYPE_INT`

Int Constant for JavaScript type.

`static final String`
`JSTYPE_REGEXP`

Regular Expression Constant for JavaScript type.

`static final String`
`JSTYPE_STRING`

String Constant for JavaScript type.

- 

## Constructor Summary

Constructors

Constructor
Description
`Var()`

Constructs a new instance.

`Var(String name,
 String value,
 String jsType)`

Constructs a variable with a specified name, value
 and JavaScript type.

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
`getJsType()`

Gets the JavaScript type of the variable.

`String`
`getName()`

Gets the name of the variable.

`String`
`getValue()`

Gets the value of the variable.

`boolean`
`isResource()`

Tests whether or not the value is a resource key or literal value.

`void`
`setBundle(String bundle)`

Sets the resource bundle name.

`void`
`setJsType(String jsType)`

Sets the JavaScript type of the variable.

`void`
`setName(String name)`

Sets the name of the variable.

`void`
`setResource(boolean resource)`

Sets whether or not the value is a resource.

`void`
`setValue(String value)`

Sets the value of the variable.

`String`
`toString()`

Returns a string representation of the object.

### Methods inherited from class java.lang.Object

`equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Field Details

  - 

### JSTYPE_INT

public static final String JSTYPE_INT
Int Constant for JavaScript type.  This can be used
 when auto-generating JavaScript.

See Also:

    - Constant Field Values

  - 

### JSTYPE_STRING

public static final String JSTYPE_STRING
String Constant for JavaScript type.  This can be used
 when auto-generating JavaScript.

See Also:

    - Constant Field Values

  - 

### JSTYPE_REGEXP

public static final String JSTYPE_REGEXP
Regular Expression Constant for JavaScript type.  This can be used
 when auto-generating JavaScript.

See Also:

    - Constant Field Values

- 

## Constructor Details

  - 

### Var

public Var()
Constructs a new instance.

  - 

### Var

public Var(String name,
 String value,
 String jsType)
Constructs a variable with a specified name, value
 and JavaScript type.

Parameters:
`name` - Variable name.
`value` - Variable value.
`jsType` - Variable JavaScript type.

- 

## Method Details

  - 

### clone

public Object clone()
Creates and returns a copy of this object.

Overrides:
`clone` in class `Object`
Returns:
A copy of the variable.

  - 

### getBundle

public String getBundle()
Returns the resource bundle name.

Returns:
The bundle name.
Since:
1.2.0

  - 

### getJsType

public String getJsType()
Gets the JavaScript type of the variable.

Returns:
The JavaScript type of the variable.

  - 

### getName

public String getName()
Gets the name of the variable.

Returns:
The name of the variable.

  - 

### getValue

public String getValue()
Gets the value of the variable.

Returns:
The value of the variable.

  - 

### isResource

public boolean isResource()
Tests whether or not the value is a resource key or literal value.

Returns:
`true` if value is a resource key.
Since:
1.2.0

  - 

### setBundle

public void setBundle(String bundle)
Sets the resource bundle name.

Parameters:
`bundle` - The new bundle name.
Since:
1.2.0

  - 

### setJsType

public void setJsType(String jsType)
Sets the JavaScript type of the variable.

Parameters:
`jsType` - The JavaScript type of the variable.

  - 

### setName

public void setName(String name)
Sets the name of the variable.

Parameters:
`name` - The name of the variable.

  - 

### setResource

public void setResource(boolean resource)
Sets whether or not the value is a resource.

Parameters:
`resource` - If true indicates the value is a resource.
Since:
1.2.0

  - 

### setValue

public void setValue(String value)
Sets the value of the variable.

Parameters:
`value` - The value of the variable.

  - 

### toString

public String toString()
Returns a string representation of the object.

Overrides:
`toString` in class `Object`
Returns:
A string representation of the variable.