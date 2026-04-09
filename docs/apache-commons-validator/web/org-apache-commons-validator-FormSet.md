Package org.apache.commons.validator

# Class FormSet

java.lang.Object
org.apache.commons.validator.FormSet

All Implemented Interfaces:
`Serializable`

---

public class FormSet
extends Object
implements Serializable
Holds a set of `Form`s stored associated with a `Locale`
 based on the country, language, and variant specified. Instances of this
 class are configured with a <formset> xml element.

See Also:

- Serialized Form

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`protected static final int`
`COUNTRY_FORMSET`

This is the type of `FormSet`s where only language and country
 locale are specified.

`protected static final int`
`GLOBAL_FORMSET`

This is the type of `FormSet`s where no locale is specified.

`protected static final int`
`LANGUAGE_FORMSET`

This is the type of `FormSet`s where only language locale is
 specified.

`protected static final int`
`VARIANT_FORMSET`

This is the type of `FormSet`s where full locale has been set.

- 

## Constructor Summary

Constructors

Constructor
Description
`FormSet()`

Constructs a new instance.

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`addConstant(String name,
 String value)`

Add a `Constant` to the locale level.

`void`
`addForm(Form f)`

Add a `Form` to the `FormSet`.

`String`
`displayKey()`

Returns a string representation of the object's key.

`String`
`getCountry()`

Gets the equivalent of the country component of `Locale`.

`Form`
`getForm(String formName)`

Retrieve a `Form` based on the form name.

`Map<String,Form>`
`getForms()`

A `Map` of `Form`s is returned as an unmodifiable
 `Map` with the key based on the form name.

`String`
`getLanguage()`

Gets the equivalent of the language component of `Locale`.

`protected int`
`getType()`

Returns the type of `FormSet`:`GLOBAL_FORMSET`,
 `LANGUAGE_FORMSET`,`COUNTRY_FORMSET` or `VARIANT_FORMSET`.

`String`
`getVariant()`

Gets the equivalent of the variant component of `Locale`.

`protected boolean`
`isMerged()`

Has this formSet been merged?

`boolean`
`isProcessed()`

Whether or not the this `FormSet` was processed for replacing
 variables in strings with their values.

`protected void`
`merge(FormSet depends)`

Merges the given `FormSet` into this one.

`void`
`setCountry(String country)`

Sets the equivalent of the country component of `Locale`.

`void`
`setLanguage(String language)`

Sets the equivalent of the language component of `Locale`.

`void`
`setVariant(String variant)`

Sets the equivalent of the variant component of `Locale`.

`String`
`toString()`

Returns a string representation of the object.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Field Details

  - 

### GLOBAL_FORMSET

protected static final int GLOBAL_FORMSET
This is the type of `FormSet`s where no locale is specified.

See Also:

    - Constant Field Values

  - 

### LANGUAGE_FORMSET

protected static final int LANGUAGE_FORMSET
This is the type of `FormSet`s where only language locale is
 specified.

See Also:

    - Constant Field Values

  - 

### COUNTRY_FORMSET

protected static final int COUNTRY_FORMSET
This is the type of `FormSet`s where only language and country
 locale are specified.

See Also:

    - Constant Field Values

  - 

### VARIANT_FORMSET

protected static final int VARIANT_FORMSET
This is the type of `FormSet`s where full locale has been set.

See Also:

    - Constant Field Values

- 

## Constructor Details

  - 

### FormSet

public FormSet()
Constructs a new instance.

- 

## Method Details

  - 

### addConstant

public void addConstant(String name,
 String value)
Add a `Constant` to the locale level.

Parameters:
`name` - The constant name
`value` - The constant value

  - 

### addForm

public void addForm(Form f)
Add a `Form` to the `FormSet`.

Parameters:
`f` - The form

  - 

### displayKey

public String displayKey()
Returns a string representation of the object's key.

Returns:
A string representation of the key

  - 

### getCountry

public String getCountry()
Gets the equivalent of the country component of `Locale`.

Returns:
The country value

  - 

### getForm

public Form getForm(String formName)
Retrieve a `Form` based on the form name.

Parameters:
`formName` - The form name
Returns:
The form

  - 

### getForms

public Map<String,Form> getForms()
A `Map` of `Form`s is returned as an unmodifiable
 `Map` with the key based on the form name.

Returns:
The forms map

  - 

### getLanguage

public String getLanguage()
Gets the equivalent of the language component of `Locale`.

Returns:
The language value

  - 

### getType

protected int getType()
Returns the type of `FormSet`:`GLOBAL_FORMSET`,
 `LANGUAGE_FORMSET`,`COUNTRY_FORMSET` or `VARIANT_FORMSET`.

Returns:
The type value
Throws:
`NullPointerException` - if there is inconsistency in the locale
      definition (not sure about this)
Since:
1.2.0

  - 

### getVariant

public String getVariant()
Gets the equivalent of the variant component of `Locale`.

Returns:
The variant value

  - 

### isMerged

protected boolean isMerged()
Has this formSet been merged?

Returns:
true if it has been merged
Since:
1.2.0

  - 

### isProcessed

public boolean isProcessed()
Whether or not the this `FormSet` was processed for replacing
 variables in strings with their values.

Returns:
The processed value

  - 

### merge

protected void merge(FormSet depends)
Merges the given `FormSet` into this one. If any of `depends`
 s `Forms` are not in this `FormSet` then, include
 them, else merge both `Forms`. Theoretically we should only
 merge a "parent" formSet.

Parameters:
`depends` - FormSet to be merged
Since:
1.2.0

  - 

### setCountry

public void setCountry(String country)
Sets the equivalent of the country component of `Locale`.

Parameters:
`country` - The new country value

  - 

### setLanguage

public void setLanguage(String language)
Sets the equivalent of the language component of `Locale`.

Parameters:
`language` - The new language value

  - 

### setVariant

public void setVariant(String variant)
Sets the equivalent of the variant component of `Locale`.

Parameters:
`variant` - The new variant value

  - 

### toString

public String toString()
Returns a string representation of the object.

Overrides:
`toString` in class `Object`
Returns:
A string representation