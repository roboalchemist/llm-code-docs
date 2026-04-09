Package org.apache.commons.validator

# Class ValidatorResources

java.lang.Object
org.apache.commons.validator.ValidatorResources

All Implemented Interfaces:
`Serializable`

---

public class ValidatorResources
extends Object
implements Serializable

 General purpose class for storing `FormSet` objects based
 on their associated `Locale`.  Instances of this class are usually
 configured through a validation.xml file that is parsed in a constructor.
 

 

**Note** - Classes that extend this class
 must be Serializable so that instances may be used in distributable
 application server environments.

 

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
`protected FormSet`
`defaultFormSet`

This is the default `FormSet` (without locale).

`protected static Locale`
`defaultLocale`

The default locale on our server.

`protected org.apache.commons.collections.FastHashMap`
`hActions`

Deprecated.
Subclasses should use getActions() instead.

`protected org.apache.commons.collections.FastHashMap`
`hConstants`

Deprecated.
Subclasses should use getConstants() instead.

`protected org.apache.commons.collections.FastHashMap`
`hFormSets`

Deprecated.
Subclasses should use getFormSets() instead.

- 

## Constructor Summary

Constructors

Constructor
Description
`ValidatorResources()`

Create an empty ValidatorResources object.

`ValidatorResources(InputStream in)`

Create a ValidatorResources object from an InputStream.

`ValidatorResources(InputStream[] streams)`

Create a ValidatorResources object from an InputStream.

`ValidatorResources(String uri)`

Create a ValidatorResources object from an uri

`ValidatorResources(String... uris)`

Create a ValidatorResources object from several uris

`ValidatorResources(URL url)`

Create a ValidatorResources object from a URL.

`ValidatorResources(URL[] urls)`

Create a ValidatorResources object from several URL.

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`addConstant(String name,
 String value)`

Add a global constant to the resource.

`void`
`addFormSet(FormSet fs)`

Add a `FormSet` to this `ValidatorResources`
 object.

`void`
`addValidatorAction(ValidatorAction va)`

Add a `ValidatorAction` to the resource.

`protected String`
`buildKey(FormSet fs)`

Builds a key to store the `FormSet` under based on its
 language, country, and variant values.

`protected Map<String,ValidatorAction>`
`getActions()`

Returns a Map of String ValidatorAction names to their ValidatorAction.

`protected Map<String,String>`
`getConstants()`

Returns a Map of String constant names to their String values.

`Form`
`getForm(String language,
 String country,
 String variant,
 String formKey)`

Gets a `Form` based on the name of the form and the
 `Locale` that most closely matches the `Locale`
 passed in.

`Form`
`getForm(Locale locale,
 String formKey)`

Gets a `Form` based on the name of the form and the
 `Locale` that most closely matches the `Locale`
 passed in.

`protected Map<String,FormSet>`
`getFormSets()`

Returns a Map of String locale keys to Lists of their FormSets.

`ValidatorAction`
`getValidatorAction(String key)`

Gets a `ValidatorAction` based on its name.

`Map<String,ValidatorAction>`
`getValidatorActions()`

Gets an unmodifiable `Map` of the `ValidatorAction`s.

`void`
`process()`

Process the `ValidatorResources` object.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### defaultLocale

protected static Locale defaultLocale
The default locale on our server.

  - 

### hFormSets

@Deprecated
protected org.apache.commons.collections.FastHashMap hFormSets
Deprecated.
Subclasses should use getFormSets() instead.

`Map` of `FormSet`s stored under
 a `Locale` key (expressed as a String).

  - 

### hConstants

@Deprecated
protected org.apache.commons.collections.FastHashMap hConstants
Deprecated.
Subclasses should use getConstants() instead.

`Map` of global constant values with
 the name of the constant as the key.

  - 

### hActions

@Deprecated
protected org.apache.commons.collections.FastHashMap hActions
Deprecated.
Subclasses should use getActions() instead.

`Map` of `ValidatorAction`s with
 the name of the `ValidatorAction` as the key.

  - 

### defaultFormSet

protected FormSet defaultFormSet
This is the default `FormSet` (without locale). (We probably don't need
 the defaultLocale anymore.)

- 

## Constructor Details

  - 

### ValidatorResources

public ValidatorResources()
Create an empty ValidatorResources object.

  - 

### ValidatorResources

public ValidatorResources(InputStream in)
                   throws IOException,
SAXException
Create a ValidatorResources object from an InputStream.

Parameters:
`in` - InputStream to a validation.xml configuration file.  It's the client's
 responsibility to close this stream.
Throws:
`SAXException` - if the validation XML files are not valid or well-formed.
`IOException` - if an I/O error occurs processing the XML files
Since:
1.1

  - 

### ValidatorResources

public ValidatorResources(InputStream[] streams)
                   throws IOException,
SAXException
Create a ValidatorResources object from an InputStream.

Parameters:
`streams` - An array of InputStreams to several validation.xml
 configuration files that will be read in order and merged into this object.
 It's the client's responsibility to close these streams.
Throws:
`SAXException` - if the validation XML files are not valid or well-formed.
`IOException` - if an I/O error occurs processing the XML files
Since:
1.1

  - 

### ValidatorResources

public ValidatorResources(String uri)
                   throws IOException,
SAXException
Create a ValidatorResources object from an uri

Parameters:
`uri` - The location of a validation.xml configuration file.
Throws:
`SAXException` - if the validation XML files are not valid or well-formed.
`IOException` - if an I/O error occurs processing the XML files
Since:
1.2

  - 

### ValidatorResources

public ValidatorResources(String... uris)
                   throws IOException,
SAXException
Create a ValidatorResources object from several uris

Parameters:
`uris` - An array of uris to several validation.xml
 configuration files that will be read in order and merged into this object.
Throws:
`SAXException` - if the validation XML files are not valid or well-formed.
`IOException` - if an I/O error occurs processing the XML files
Since:
1.2

  - 

### ValidatorResources

public ValidatorResources(URL url)
                   throws IOException,
SAXException
Create a ValidatorResources object from a URL.

Parameters:
`url` - The URL for the validation.xml
 configuration file that will be read into this object.
Throws:
`SAXException` - if the validation XML file are not valid or well-formed.
`IOException` - if an I/O error occurs processing the XML files
Since:
1.3.1

  - 

### ValidatorResources

public ValidatorResources(URL[] urls)
                   throws IOException,
SAXException
Create a ValidatorResources object from several URL.

Parameters:
`urls` - An array of URL to several validation.xml
 configuration files that will be read in order and merged into this object.
Throws:
`SAXException` - if the validation XML files are not valid or well-formed.
`IOException` - if an I/O error occurs processing the XML files
Since:
1.3.1

- 

## Method Details

  - 

### addConstant

public void addConstant(String name,
 String value)
Add a global constant to the resource.

Parameters:
`name` - The constant name.
`value` - The constant value.

  - 

### addFormSet

public void addFormSet(FormSet fs)
Add a `FormSet` to this `ValidatorResources`
 object.  It will be associated with the `Locale` of the
 `FormSet`.

Parameters:
`fs` - The form set to add.
Since:
1.1

  - 

### addValidatorAction

public void addValidatorAction(ValidatorAction va)
Add a `ValidatorAction` to the resource.  It also creates an
 instance of the class based on the `ValidatorAction`s
 class name and retrieves the `Method` instance and sets them
 in the `ValidatorAction`.

Parameters:
`va` - The validator action.

  - 

### buildKey

protected String buildKey(FormSet fs)
Builds a key to store the `FormSet` under based on its
 language, country, and variant values.

Parameters:
`fs` - The Form Set.
Returns:
generated key for a formset.

  - 

### getActions

protected Map<String,ValidatorAction> getActions()
Returns a Map of String ValidatorAction names to their ValidatorAction.

Returns:
Map of Validator Actions
Since:
1.2.0

  - 

### getConstants

protected Map<String,String> getConstants()
Returns a Map of String constant names to their String values.

Returns:
Map of Constants
Since:
1.2.0

  - 

### getForm

public Form getForm(Locale locale,
 String formKey)

Gets a `Form` based on the name of the form and the
 `Locale` that most closely matches the `Locale`
 passed in.  The order of `Locale` matching is:
 

    
    - language + country + variant
    
    - language + country
    
    - language
    
    - default locale
 

Parameters:
`locale` - The Locale.
`formKey` - The key for the Form.
Returns:
The validator Form.
Since:
1.1

  - 

### getForm

public Form getForm(String language,
 String country,
 String variant,
 String formKey)

Gets a `Form` based on the name of the form and the
 `Locale` that most closely matches the `Locale`
 passed in.  The order of `Locale` matching is:
 

    
    - language + country + variant
    
    - language + country
    
    - language
    
    - default locale
 

Parameters:
`language` - The locale's language.
`country` - The locale's country.
`variant` - The locale's language variant.
`formKey` - The key for the Form.
Returns:
The validator Form.
Since:
1.1

  - 

### getFormSets

protected Map<String,FormSet> getFormSets()
Returns a Map of String locale keys to Lists of their FormSets.

Returns:
Map of Form sets
Since:
1.2.0

  - 

### getValidatorAction

public ValidatorAction getValidatorAction(String key)
Gets a `ValidatorAction` based on its name.

Parameters:
`key` - The validator action key.
Returns:
The validator action.

  - 

### getValidatorActions

public Map<String,ValidatorAction> getValidatorActions()
Gets an unmodifiable `Map` of the `ValidatorAction`s.

Returns:
Map of validator actions.

  - 

### process

public void process()
Process the `ValidatorResources` object. Currently, sets the
 `FastHashMap` s to the 'fast' mode and call the processes
 all other resources. **Note **: The framework calls this
 automatically when ValidatorResources is created from an XML file. If you
 create an instance of this class by hand you **must ** call
 this method when finished.