Package org.apache.commons.validator

# Class Field

java.lang.Object
org.apache.commons.validator.Field

All Implemented Interfaces:
`Serializable`, `Cloneable`

---

public class Field
extends Object
implements Cloneable, Serializable
This contains the list of pluggable validators to run on a field and any
 message information and variables to perform the validations and generate
 error messages.  Instances of this class are configured with a
 <field> xml element.
 

 The use of FastHashMap is deprecated and will be replaced in a future
 release.
 

See Also:

- `Form`

- Serialized Form

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`protected Map<String,Arg>[]`
`args`

Holds Maps of arguments.

`protected boolean`
`clientValidation`

The flag that indicates whether scripting should be generated
 by the client for client-side validation.

`protected String`
`depends`

A comma separated list of validator's this field depends on.

`protected int`
`fieldOrder`

The order of the Field in the Form.

`protected org.apache.commons.collections.FastHashMap`
`hMsgs`

Deprecated.
Subclasses should use getMsgMap() instead.

`protected org.apache.commons.collections.FastHashMap`
`hVars`

Deprecated.
Subclasses should use getVarMap() instead.

`protected String`
`indexedListProperty`

The Field's indexed list property name.

`protected String`
`indexedProperty`

The Field's indexed property name.

`protected String`
`key`

The Field's unique key.

`protected int`
`page`

The Page Number

`protected String`
`property`

The Field's property name.

`protected static final String`
`TOKEN_END`

The end of a token.

`static final String`
`TOKEN_INDEXED`

This indicates an indexed property is being referenced.

`protected static final String`
`TOKEN_START`

The start of a token.

`protected static final String`
`TOKEN_VAR`

A Variable token.

- 

## Constructor Summary

Constructors

Constructor
Description
`Field()`

Constructs a new instance.

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`addArg(Arg arg)`

Add an `Arg` to the replacement argument list.

`void`
`addMsg(Msg msg)`

Add a `Msg` to the `Field`.

`void`
`addVar(String name,
 String value,
 String jsType)`

Add a `Var`, based on the values passed in, to the
 `Field`.

`void`
`addVar(Var v)`

Add a `Var` to the `Field`.

`Object`
`clone()`

Creates and returns a copy of this object.

`void`
`generateKey()`

Generate correct `key` value.

`Arg`
`getArg(int position)`

Gets the default `Arg` object at the given position.

`Arg`
`getArg(String key,
 int position)`

Gets the `Arg` object at the given position.

`Arg[]`
`getArgs(String key)`

Gets the Args for the given validator name.

`List<String>`
`getDependencyList()`

Gets an unmodifiable `List` of the dependencies in the same
 order they were defined in parameter passed to the setDepends() method.

`String`
`getDepends()`

Gets the validation rules for this field as a comma separated list.

`int`
`getFieldOrder()`

Gets the position of the `Field` in the validation list.

`String`
`getIndexedListProperty()`

Gets the indexed property name of the field.

`String`
`getIndexedProperty()`

Gets the indexed property name of the field.

`String`
`getKey()`

Gets a unique key based on the property and indexedProperty fields.

`Msg`
`getMessage(String key)`

Retrieve a message object.

`Map<String,Msg>`
`getMessages()`

The `Field`'s messages are returned as an
 unmodifiable `Map`.

`String`
`getMsg(String key)`

Retrieve a message value.

`protected Map<String,Msg>`
`getMsgMap()`

Returns a Map of String Msg names to Msg objects.

`int`
`getPage()`

Gets the page value that the Field is associated with for
 validation.

`String`
`getProperty()`

Gets the property name of the field.

`Var`
`getVar(String mainKey)`

Retrieve a variable.

`protected Map<String,Var>`
`getVarMap()`

Returns a Map of String Var names to Var objects.

`Map<String,Var>`
`getVars()`

The `Field`'s variables are returned as an
 unmodifiable `Map`.

`String`
`getVarValue(String mainKey)`

Retrieve a variable's value.

`boolean`
`isClientValidation()`

Determines whether client-side scripting should be generated
 for this field.

`boolean`
`isDependency(String validatorName)`

Checks if the validator is listed as a dependency.

`boolean`
`isIndexed()`

If there is a value specified for the indexedProperty field then
 `true` will be returned.

`void`
`setClientValidation(boolean clientValidation)`

Sets the flag that determines whether client-side scripting should
 be generated for this field.

`void`
`setDepends(String depends)`

Sets the validation rules for this field as a comma separated list.

`void`
`setFieldOrder(int fieldOrder)`

Sets the position of the `Field` in the validation list.

`void`
`setIndexedListProperty(String indexedListProperty)`

Sets the indexed property name of the field.

`void`
`setIndexedProperty(String indexedProperty)`

Sets the indexed property name of the field.

`void`
`setKey(String key)`

Sets a unique key for the field.

`void`
`setPage(int page)`

Sets the page value that the Field is associated with for
 validation.

`void`
`setProperty(String property)`

Sets the property name of the field.

`String`
`toString()`

Returns a string representation of the object.

`ValidatorResults`
`validate(Map<String,Object> params,
 Map<String,ValidatorAction> actions)`

Run the configured validations on this field.

### Methods inherited from class java.lang.Object

`equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Field Details

  - 

### TOKEN_INDEXED

public static final String TOKEN_INDEXED
This indicates an indexed property is being referenced.

See Also:

    - Constant Field Values

  - 

### TOKEN_START

protected static final String TOKEN_START
The start of a token.

See Also:

    - Constant Field Values

  - 

### TOKEN_END

protected static final String TOKEN_END
The end of a token.

See Also:

    - Constant Field Values

  - 

### TOKEN_VAR

protected static final String TOKEN_VAR
A Variable token.

See Also:

    - Constant Field Values

  - 

### property

protected String property
The Field's property name.

  - 

### indexedProperty

protected String indexedProperty
The Field's indexed property name.

  - 

### indexedListProperty

protected String indexedListProperty
The Field's indexed list property name.

  - 

### key

protected String key
The Field's unique key.

  - 

### depends

protected String depends
A comma separated list of validator's this field depends on.

  - 

### page

protected volatile int page
The Page Number

  - 

### clientValidation

protected volatile boolean clientValidation
The flag that indicates whether scripting should be generated
 by the client for client-side validation.

Since:
1.4

  - 

### fieldOrder

protected volatile int fieldOrder
The order of the Field in the Form.

  - 

### hVars

@Deprecated
protected org.apache.commons.collections.FastHashMap hVars
Deprecated.
Subclasses should use getVarMap() instead.

  - 

### hMsgs

@Deprecated
protected org.apache.commons.collections.FastHashMap hMsgs
Deprecated.
Subclasses should use getMsgMap() instead.

  - 

### args

protected Map<String,Arg>[] args
Holds Maps of arguments.  args[0] returns the Map for the first
 replacement argument.  Start with a 0 length array so that it will
 only grow to the size of the highest argument position.

Since:
1.1

- 

## Constructor Details

  - 

### Field

public Field()
Constructs a new instance.

- 

## Method Details

  - 

### addArg

public void addArg(Arg arg)
Add an `Arg` to the replacement argument list.

Parameters:
`arg` - Validation message's argument.
Since:
1.1

  - 

### addMsg

public void addMsg(Msg msg)
Add a `Msg` to the `Field`.

Parameters:
`msg` - A validation message.

  - 

### addVar

public void addVar(String name,
 String value,
 String jsType)
Add a `Var`, based on the values passed in, to the
 `Field`.

Parameters:
`name` - Name of the validation.
`value` - The Argument's value.
`jsType` - The JavaScript type.

  - 

### addVar

public void addVar(Var v)
Add a `Var` to the `Field`.

Parameters:
`v` - The Validator Argument.

  - 

### clone

public Object clone()
Creates and returns a copy of this object.

Overrides:
`clone` in class `Object`
Returns:
A copy of the Field.

  - 

### generateKey

public void generateKey()
Generate correct `key` value.

  - 

### getArg

public Arg getArg(int position)
Gets the default `Arg` object at the given position.

Parameters:
`position` - Validation message argument's position.
Returns:
The default Arg or null if not found.
Since:
1.1

  - 

### getArg

public Arg getArg(String key,
 int position)
Gets the `Arg` object at the given position.  If the key
 finds a `null` value then the default value will be
 retrieved.

Parameters:
`key` - The name the Arg is stored under.  If not found, the default
 Arg for the given position (if any) will be retrieved.
`position` - The Arg number to find.
Returns:
The Arg with the given name and position or null if not found.
Since:
1.1

  - 

### getArgs

public Arg[] getArgs(String key)
Gets the Args for the given validator name.

Parameters:
`key` - The validator's args to retrieve.
Returns:
An Arg[] sorted by the Args' positions (for example, the Arg at index 0
 has a position of 0).
Since:
1.1.1

  - 

### getDependencyList

public List<String> getDependencyList()
Gets an unmodifiable `List` of the dependencies in the same
 order they were defined in parameter passed to the setDepends() method.

Returns:
A list of the Field's dependencies.

  - 

### getDepends

public String getDepends()
Gets the validation rules for this field as a comma separated list.

Returns:
A comma separated list of validator names.

  - 

### getFieldOrder

public int getFieldOrder()
Gets the position of the `Field` in the validation list.

Returns:
The field position.

  - 

### getIndexedListProperty

public String getIndexedListProperty()
Gets the indexed property name of the field.  This
 is the method name that will return an array or a
 `Collection` used to retrieve the
 list and then loop through the list performing the specified
 validations.

Returns:
The field's indexed List property name.

  - 

### getIndexedProperty

public String getIndexedProperty()
Gets the indexed property name of the field.  This
 is the method name that can take an `int` as
 a parameter for indexed property value retrieval.

Returns:
The field's indexed property name.

  - 

### getKey

public String getKey()
Gets a unique key based on the property and indexedProperty fields.

Returns:
a unique key for the field.

  - 

### getMessage

public Msg getMessage(String key)
Retrieve a message object.

Parameters:
`key` - Validation key.
Returns:
A validation message for a specified validator.
Since:
1.1.4

  - 

### getMessages

public Map<String,Msg> getMessages()
The `Field`'s messages are returned as an
 unmodifiable `Map`.

Returns:
Map of validation messages for the field.
Since:
1.1.4

  - 

### getMsg

public String getMsg(String key)
Retrieve a message value.

Parameters:
`key` - Validation key.
Returns:
A validation message for a specified validator.

  - 

### getMsgMap

protected Map<String,Msg> getMsgMap()
Returns a Map of String Msg names to Msg objects.

Returns:
A Map of the Field's messages.
Since:
1.2.0

  - 

### getPage

public int getPage()
Gets the page value that the Field is associated with for
 validation.

Returns:
The page number.

  - 

### getProperty

public String getProperty()
Gets the property name of the field.

Returns:
The field's property name.

  - 

### getVar

public Var getVar(String mainKey)
Retrieve a variable.

Parameters:
`mainKey` - The Variable's key
Returns:
the Variable

  - 

### getVarMap

protected Map<String,Var> getVarMap()
Returns a Map of String Var names to Var objects.

Returns:
A Map of the Field's variables.
Since:
1.2.0

  - 

### getVars

public Map<String,Var> getVars()
The `Field`'s variables are returned as an
 unmodifiable `Map`.

Returns:
the Map of Variable's for a Field.

  - 

### getVarValue

public String getVarValue(String mainKey)
Retrieve a variable's value.

Parameters:
`mainKey` - The Variable's key
Returns:
the Variable's value

  - 

### isClientValidation

public boolean isClientValidation()
Determines whether client-side scripting should be generated
 for this field. The default is `true`

Returns:
`true` for scripting; otherwise false
Since:
1.4
See Also:

    - `setClientValidation(boolean)`

  - 

### isDependency

public boolean isDependency(String validatorName)
Checks if the validator is listed as a dependency.

Parameters:
`validatorName` - Name of the validator to check.
Returns:
Whether the field is dependant on a validator.

  - 

### isIndexed

public boolean isIndexed()
If there is a value specified for the indexedProperty field then
 `true` will be returned.  Otherwise, it will be
 `false`.

Returns:
Whether the Field is indexed.

  - 

### setClientValidation

public void setClientValidation(boolean clientValidation)
Sets the flag that determines whether client-side scripting should
 be generated for this field.

Parameters:
`clientValidation` - the scripting flag
Since:
1.4
See Also:

    - `isClientValidation()`

  - 

### setDepends

public void setDepends(String depends)
Sets the validation rules for this field as a comma separated list.

Parameters:
`depends` - A comma separated list of validator names.

  - 

### setFieldOrder

public void setFieldOrder(int fieldOrder)
Sets the position of the `Field` in the validation list.

Parameters:
`fieldOrder` - The field position.

  - 

### setIndexedListProperty

public void setIndexedListProperty(String indexedListProperty)
Sets the indexed property name of the field.

Parameters:
`indexedListProperty` - The field's indexed List property name.

  - 

### setIndexedProperty

public void setIndexedProperty(String indexedProperty)
Sets the indexed property name of the field.

Parameters:
`indexedProperty` - The field's indexed property name.

  - 

### setKey

public void setKey(String key)
Sets a unique key for the field.  This can be used to change
 the key temporarily to have a unique key for an indexed field.

Parameters:
`key` - a unique key for the field

  - 

### setPage

public void setPage(int page)
Sets the page value that the Field is associated with for
 validation.

Parameters:
`page` - The page number.

  - 

### setProperty

public void setProperty(String property)
Sets the property name of the field.

Parameters:
`property` - The field's property name.

  - 

### toString

public String toString()
Returns a string representation of the object.

Overrides:
`toString` in class `Object`
Returns:
A string representation of the object.

  - 

### validate

public ValidatorResults validate(Map<String,Object> params,
 Map<String,ValidatorAction> actions)
                          throws ValidatorException
Run the configured validations on this field.  Run all validations
 in the depends clause over each item in turn, returning when the first
 one fails.

Parameters:
`params` - A Map of parameter class names to parameter values to pass
 into validation methods.
`actions` - A Map of validator names to ValidatorAction objects.
Returns:
A ValidatorResults object containing validation messages for
 this field.
Throws:
`ValidatorException` - If an error occurs during validation.