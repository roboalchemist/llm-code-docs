Package org.apache.commons.validator

# Class Form

java.lang.Object
org.apache.commons.validator.Form

All Implemented Interfaces:
`Serializable`

---

public class Form
extends Object
implements Serializable

 This contains a set of validation rules for a form/JavaBean. The information
 is contained in a list of `Field` objects. Instances of this class
 are configured with a <form> xml element.
 
 

 The use of FastHashMap is deprecated and will be replaced in a future
 release.
 

See Also:

- Serialized Form

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`protected org.apache.commons.collections.FastHashMap`
`hFields`

Deprecated.
Subclasses should use getFieldMap() instead.

`protected String`
`inherit`

The name/key of the form which this form extends from.

`protected List<Field>`
`lFields`

List of `Field`s.

`protected String`
`name`

The name/key the set of validation rules is stored under.

- 

## Constructor Summary

Constructors

Constructor
Description
`Form()`

Constructs a new instance.

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`addField(Field f)`

Add a `Field` to the `Form`.

`boolean`
`containsField(String fieldName)`

Returns true if this Form contains a Field with the given name.

`String`
`getExtends()`

Gets the name/key of the parent set of validation rules.

`Field`
`getField(String fieldName)`

Returns the Field with the given name or null if this Form has no such
 field.

`protected Map<String,Field>`
`getFieldMap()`

Returns a Map of String field keys to Field objects.

`List<Field>`
`getFields()`

A `List` of `Field`s is returned as an unmodifiable
 `List`.

`String`
`getName()`

Gets the name/key of the set of validation rules.

`boolean`
`isExtending()`

Gets extends flag.

`boolean`
`isProcessed()`

Whether or not the this `Form` was processed for replacing
 variables in strings with their values.

`protected void`
`merge(Form depends)`

Merges the given form into this one.

`protected void`
`process(Map<String,String> globalConstants,
 Map<String,String> constants,
 Map<String,Form> forms)`

Processes all of the `Form`'s `Field`s.

`void`
`setExtends(String inherit)`

Sets the name/key of the parent set of validation rules.

`void`
`setName(String name)`

Sets the name/key of the set of validation rules.

`String`
`toString()`

Returns a string representation of the object.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Field Details

  - 

### name

protected String name
The name/key the set of validation rules is stored under.

  - 

### lFields

protected List<Field> lFields
List of `Field`s. Used to maintain the order they were added
 in although individual `Field`s can be retrieved using `Map`
 of `Field`s.

  - 

### hFields

@Deprecated
protected org.apache.commons.collections.FastHashMap hFields
Deprecated.
Subclasses should use getFieldMap() instead.

Map of `Field`s keyed on their property value.

  - 

### inherit

protected String inherit
The name/key of the form which this form extends from.

Since:
1.2.0

- 

## Constructor Details

  - 

### Form

public Form()
Constructs a new instance.

- 

## Method Details

  - 

### addField

public void addField(Field f)
Add a `Field` to the `Form`.

Parameters:
`f` - The field

  - 

### containsField

public boolean containsField(String fieldName)
Returns true if this Form contains a Field with the given name.

Parameters:
`fieldName` - The field name
Returns:
True if this form contains the field by the given name
Since:
1.1

  - 

### getExtends

public String getExtends()
Gets the name/key of the parent set of validation rules.

Returns:
The extends value
Since:
1.2.0

  - 

### getField

public Field getField(String fieldName)
Returns the Field with the given name or null if this Form has no such
 field.

Parameters:
`fieldName` - The field name
Returns:
The field value
Since:
1.1

  - 

### getFieldMap

protected Map<String,Field> getFieldMap()
Returns a Map of String field keys to Field objects.

Returns:
The fieldMap value
Since:
1.2.0

  - 

### getFields

public List<Field> getFields()
A `List` of `Field`s is returned as an unmodifiable
 `List`.

Returns:
The fields value

  - 

### getName

public String getName()
Gets the name/key of the set of validation rules.

Returns:
The name value

  - 

### isExtending

public boolean isExtending()
Gets extends flag.

Returns:
The extending value
Since:
1.2.0

  - 

### isProcessed

public boolean isProcessed()
Whether or not the this `Form` was processed for replacing
 variables in strings with their values.

Returns:
The processed value
Since:
1.2.0

  - 

### merge

protected void merge(Form depends)
Merges the given form into this one. For any field in `depends`
 not present in this form, include it. `depends` has precedence
 in the way the fields are ordered.

Parameters:
`depends` - the form we want to merge
Since:
1.2.0

  - 

### process

protected void process(Map<String,String> globalConstants,
 Map<String,String> constants,
 Map<String,Form> forms)
Processes all of the `Form`'s `Field`s.

Parameters:
`globalConstants` - A map of global constants
`constants` - Local constants
`forms` - Map of forms
Since:
1.2.0

  - 

### setExtends

public void setExtends(String inherit)
Sets the name/key of the parent set of validation rules.

Parameters:
`inherit` - The new extends value
Since:
1.2.0

  - 

### setName

public void setName(String name)
Sets the name/key of the set of validation rules.

Parameters:
`name` - The new name value

  - 

### toString

public String toString()
Returns a string representation of the object.

Overrides:
`toString` in class `Object`
Returns:
string representation