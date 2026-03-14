Package org.apache.commons.validator

# Class Validator

java.lang.Object
org.apache.commons.validator.Validator

All Implemented Interfaces:
`Serializable`

---

public class Validator
extends Object
implements Serializable
Validations are processed by the validate method. An instance of
 `ValidatorResources` is used to define the validators
 (validation methods) and the validation rules for a JavaBean.

See Also:

- Serialized Form

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final String`
`BEAN_PARAM`

Resources key the JavaBean is stored to perform validation on.

`protected ClassLoader`
`classLoader`

Deprecated.
Use `getClassLoader()`, will be private in the next major version.

`static final String`
`FIELD_PARAM`

Resources key the `Field` is stored under.

`protected String`
`fieldName`

Deprecated.
Use `getFieldName()`, will be private in the next major version.

`static final String`
`FORM_PARAM`

Resources key the `Form` is stored under.

`protected String`
`formName`

Deprecated.
Use `getFormName()`, will be private in the next major version.

`static final String`
`LOCALE_PARAM`

Resources key the `Locale` is stored.

`protected boolean`
`onlyReturnErrors`

Deprecated.
Use `getOnlyReturnErrors()`, will be private in the next major version.

`protected int`
`page`

Deprecated.
Use `getPage()`, will be private in the next major version.

`protected Map<String,Object>`
`parameters`

Deprecated.
Use `getParameters()`, will be private in the next major version.

`protected ValidatorResources`
`resources`

Deprecated.
Use `getResources()`, will be private in the next major version.

`protected boolean`
`useContextClassLoader`

Deprecated.
Use `getUseContextClassLoader()`, will be private in the next major version.

`static final String`
`VALIDATOR_ACTION_PARAM`

Resources key the `ValidatorAction` is stored under.

`static final String`
`VALIDATOR_PARAM`

Resources key the `Validator` is stored under.

`static final String`
`VALIDATOR_RESULTS_PARAM`

Resources key the `ValidatorResults` is stored under.

- 

## Constructor Summary

Constructors

Constructor
Description
`Validator(ValidatorResources resources)`

Constructs a `Validator` that will
 use the `ValidatorResources`
 passed in to retrieve pluggable validators
 the different sets of validation rules.

`Validator(ValidatorResources resources,
 String formName)`

Constructs a `Validator` that will
 use the `ValidatorResources`
 passed in to retrieve pluggable validators
 the different sets of validation rules.

`Validator(ValidatorResources resources,
 String formName,
 String fieldName)`

Constructs a `Validator` that will
 use the `ValidatorResources`
 passed in to retrieve pluggable validators
 the different sets of validation rules.

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`clear()`

Clears the form name, resources that were added, and the page that was
 set (if any).

`ClassLoader`
`getClassLoader()`

Gets the class loader to be used for instantiating application objects
 when required.

`String`
`getFieldName()`

Gets the field name.

`String`
`getFormName()`

Gets the form name which is the key to a set of validation rules.

`boolean`
`getOnlyReturnErrors()`

Returns true if the Validator is only returning Fields that fail validation.

`int`
`getPage()`

Gets the page.

`Map<String,Object>`
`getParameters()`

Gets the parameter map.

`Object`
`getParameterValue(String parameterClassName)`

Returns the value of the specified parameter that will be used during the
 processing of validations.

`ValidatorResources`
`getResources()`

Gets the validator resource.

`boolean`
`getUseContextClassLoader()`

Gets the boolean as to whether the context classloader should be used.

`void`
`setClassLoader(ClassLoader classLoader)`

Sets the class loader to be used for instantiating application objects
 when required.

`void`
`setFieldName(String fieldName)`

Sets the name of the field to validate in a form (optional)

`void`
`setFormName(String formName)`

Sets the form name which is the key to a set of validation rules.

`void`
`setOnlyReturnErrors(boolean onlyReturnErrors)`

Configures which Fields the Validator returns from the validate() method.

`void`
`setPage(int page)`

Sets the page.

`void`
`setParameter(String parameterClassName,
 Object parameterValue)`

Sets a parameter of a pluggable validation method.

`void`
`setUseContextClassLoader(boolean useContextClassLoader)`

Sets whether to use the Context ClassLoader (the one found by
 calling `Thread.currentThread().getContextClassLoader()`)
 to resolve/load classes that are defined in various rules.

`ValidatorResults`
`validate()`

Performs validations based on the configured resources.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### BEAN_PARAM

public static final String BEAN_PARAM
Resources key the JavaBean is stored to perform validation on.

See Also:

    - Constant Field Values

  - 

### VALIDATOR_ACTION_PARAM

public static final String VALIDATOR_ACTION_PARAM
Resources key the `ValidatorAction` is stored under.
 This will be automatically passed into a validation method
 with the current `ValidatorAction` if it is
 specified in the method signature.

See Also:

    - Constant Field Values

  - 

### VALIDATOR_RESULTS_PARAM

public static final String VALIDATOR_RESULTS_PARAM
Resources key the `ValidatorResults` is stored under.
 This will be automatically passed into a validation method
 with the current `ValidatorResults` if it is
 specified in the method signature.

See Also:

    - Constant Field Values

  - 

### FORM_PARAM

public static final String FORM_PARAM
Resources key the `Form` is stored under.
 This will be automatically passed into a validation method
 with the current `Form` if it is
 specified in the method signature.

See Also:

    - Constant Field Values

  - 

### FIELD_PARAM

public static final String FIELD_PARAM
Resources key the `Field` is stored under.
 This will be automatically passed into a validation method
 with the current `Field` if it is
 specified in the method signature.

See Also:

    - Constant Field Values

  - 

### VALIDATOR_PARAM

public static final String VALIDATOR_PARAM
Resources key the `Validator` is stored under.
 This will be automatically passed into a validation method
 with the current `Validator` if it is
 specified in the method signature.

See Also:

    - Constant Field Values

  - 

### LOCALE_PARAM

public static final String LOCALE_PARAM
Resources key the `Locale` is stored.
 This will be used to retrieve the appropriate
 `FormSet` and `Form` to be
 processed.

See Also:

    - Constant Field Values

  - 

### resources

@Deprecated
protected ValidatorResources resources
Deprecated.
Use `getResources()`, will be private in the next major version.

The Validator Resources.

  - 

### formName

@Deprecated
protected String formName
Deprecated.
Use `getFormName()`, will be private in the next major version.

The name of the form to validate

  - 

### fieldName

@Deprecated
protected String fieldName
Deprecated.
Use `getFieldName()`, will be private in the next major version.

The name of the field on the form to validate

Since:
1.2.0

  - 

### parameters

@Deprecated
protected Map<String,Object> parameters
Deprecated.
Use `getParameters()`, will be private in the next major version.

Maps validation method parameter class names to the objects to be passed
 into the method.

  - 

### page

@Deprecated
protected int page
Deprecated.
Use `getPage()`, will be private in the next major version.

The current page number to validate.

  - 

### classLoader

@Deprecated
protected transient ClassLoader classLoader
Deprecated.
Use `getClassLoader()`, will be private in the next major version.

The class loader to use for instantiating application objects.
 If not specified, the context class loader, or the class loader
 used to load Digester itself, is used, based on the value of the
 `useContextClassLoader` variable.

  - 

### useContextClassLoader

@Deprecated
protected boolean useContextClassLoader
Deprecated.
Use `getUseContextClassLoader()`, will be private in the next major version.

Whether or not to use the Context ClassLoader when loading classes
 for instantiating new objects.  Default is `false`.

  - 

### onlyReturnErrors

@Deprecated
protected boolean onlyReturnErrors
Deprecated.
Use `getOnlyReturnErrors()`, will be private in the next major version.

Sets this to true to not return Fields that pass validation.  Only return failures.

- 

## Constructor Details

  - 

### Validator

public Validator(ValidatorResources resources)
Constructs a `Validator` that will
 use the `ValidatorResources`
 passed in to retrieve pluggable validators
 the different sets of validation rules.

Parameters:
`resources` - `ValidatorResources` to use during validation.

  - 

### Validator

public Validator(ValidatorResources resources,
 String formName)
Constructs a `Validator` that will
 use the `ValidatorResources`
 passed in to retrieve pluggable validators
 the different sets of validation rules.

Parameters:
`resources` - `ValidatorResources` to use during validation.
`formName` - Key used for retrieving the set of validation rules.

  - 

### Validator

public Validator(ValidatorResources resources,
 String formName,
 String fieldName)
Constructs a `Validator` that will
 use the `ValidatorResources`
 passed in to retrieve pluggable validators
 the different sets of validation rules.

Parameters:
`resources` - `ValidatorResources` to use during validation.
`formName` - Key used for retrieving the set of validation rules.
`fieldName` - Key used for retrieving the set of validation rules for a field
Since:
1.2.0

- 

## Method Details

  - 

### clear

public void clear()
Clears the form name, resources that were added, and the page that was
 set (if any).  This can be called to reinitialize the Validator instance
 so it can be reused.  The form name (key to set of validation rules) and any
 resources needed, like the JavaBean being validated, will need to
 set and/or added to this instance again.  The
 `ValidatorResources` will not be removed since it can be used
 again and is thread safe.

  - 

### getClassLoader

public ClassLoader getClassLoader()
Gets the class loader to be used for instantiating application objects
 when required.  This is determined based upon the following rules:
 

 
    - The class loader set by `setClassLoader()`, if any
 
    - The thread context class loader, if it exists and the
     `useContextClassLoader` property is set to true
 
    - The class loader used to load the Digester class itself.
 

Returns:
the class loader.

  - 

### getFieldName

public String getFieldName()
Gets the field name.

Returns:
the field name.
Since:
1.10.0

  - 

### getFormName

public String getFormName()
Gets the form name which is the key to a set of validation rules.

Returns:
the name of the form.

  - 

### getOnlyReturnErrors

public boolean getOnlyReturnErrors()
Returns true if the Validator is only returning Fields that fail validation.

Returns:
whether only failed fields are returned.

  - 

### getPage

public int getPage()
Gets the page.

 

 This in conjunction with the page property of
 a `Field` can control the processing of fields. If the field's
 page is less than or equal to this page value, it will be processed.
 

Returns:
the page number.

  - 

### getParameters

public Map<String,Object> getParameters()
Gets the parameter map.

Returns:
the parameter map.
Since:
1.10.0

  - 

### getParameterValue

public Object getParameterValue(String parameterClassName)
Returns the value of the specified parameter that will be used during the
 processing of validations.

Parameters:
`parameterClassName` - The full class name of the parameter of the
 validation method that corresponds to the value/instance passed in with it.
Returns:
value of the specified parameter.

  - 

### getResources

public ValidatorResources getResources()
Gets the validator resource.

Returns:
the validator resource.
Since:
1.10.0

  - 

### getUseContextClassLoader

public boolean getUseContextClassLoader()
Gets the boolean as to whether the context classloader should be used.

Returns:
whether the context classloader should be used.

  - 

### setClassLoader

public void setClassLoader(ClassLoader classLoader)
Sets the class loader to be used for instantiating application objects
 when required.

Parameters:
`classLoader` - The new class loader to use, or `null`
  to revert to the standard rules

  - 

### setFieldName

public void setFieldName(String fieldName)
Sets the name of the field to validate in a form (optional)

Parameters:
`fieldName` - The name of the field in a form set
Since:
1.2.0

  - 

### setFormName

public void setFormName(String formName)
Sets the form name which is the key to a set of validation rules.

Parameters:
`formName` - the name of the form.

  - 

### setOnlyReturnErrors

public void setOnlyReturnErrors(boolean onlyReturnErrors)
Configures which Fields the Validator returns from the validate() method.  Set this
 to true to only return Fields that failed validation.  By default, validate() returns
 all fields.

Parameters:
`onlyReturnErrors` - whether only failed fields are returned.

  - 

### setPage

public void setPage(int page)
Sets the page.
 

 This in conjunction with the page property of
 a `Field` can control the processing of fields. If the field's page
 is less than or equal to this page value, it will be processed.
 

Parameters:
`page` - the page number.

  - 

### setParameter

public void setParameter(String parameterClassName,
 Object parameterValue)
Sets a parameter of a pluggable validation method.

Parameters:
`parameterClassName` - The full class name of the parameter of the
 validation method that corresponds to the value/instance passed in with it.
`parameterValue` - The instance that will be passed into the
 validation method.

  - 

### setUseContextClassLoader

public void setUseContextClassLoader(boolean useContextClassLoader)
Sets whether to use the Context ClassLoader (the one found by
 calling `Thread.currentThread().getContextClassLoader()`)
 to resolve/load classes that are defined in various rules.  If not
 using Context ClassLoader, then the class-loading defaults to
 using the calling-class' ClassLoader.

Parameters:
`useContextClassLoader` - determines whether to use Context ClassLoader.

  - 

### validate

public ValidatorResults validate()
                          throws ValidatorException
Performs validations based on the configured resources.

Returns:
The `Map` returned uses the property of the
 `Field` for the key and the value is the number of error the
 field had.
Throws:
`ValidatorException` - If an error occurs during validation