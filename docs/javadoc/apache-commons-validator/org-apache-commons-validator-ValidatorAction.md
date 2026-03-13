Package org.apache.commons.validator

# Class ValidatorAction

java.lang.Object
org.apache.commons.validator.ValidatorAction

All Implemented Interfaces:
`Serializable`

---

public class ValidatorAction
extends Object
implements Serializable
Contains the information to dynamically create and run a validation method. This is the class representation of a pluggable validator that can be defined in
 an xml file with the <validator> element.

 **Note**: The validation method is assumed to be thread safe.

See Also:

- Serialized Form

- 

## Constructor Summary

Constructors

Constructor
Description
`ValidatorAction()`

Constructs a new instance.

- 

## Method Summary

Modifier and Type
Method
Description
`String`
`getClassname()`

Gets the class of the validator action.

`List<String>`
`getDependencyList()`

Returns the dependent validator names as an unmodifiable `List`.

`String`
`getDepends()`

Gets the dependencies of the validator action as a comma separated list of validator names.

`String`
`getJavascript()`

Gets the JavaScript equivalent of the Java class and method associated with this action.

`String`
`getJsFunctionName()`

Gets the JavaScript function name.

`String`
`getMethod()`

Gets the name of method being called for the validator action.

`String`
`getMethodParams()`

Gets the method parameters for the method.

`String`
`getMsg()`

Gets the message associated with the validator action.

`String`
`getName()`

Gets the name of the validator action.

`protected void`
`init()`

Initialize based on set.

`boolean`
`isDependency(String validatorName)`

Checks whether or not the value passed in is in the depends field.

`protected void`
`loadJavascriptFunction()`

Load the JavaScript function specified by the given path.

`void`
`setClassname(String className)`

Deprecated.
Use `setClassName(String)`.

`void`
`setClassName(String className)`

Sets the class of the validator action.

`void`
`setDepends(String depends)`

Sets the dependencies of the validator action.

`void`
`setJavascript(String javaScript)`

Sets the JavaScript equivalent of the Java class and method associated with this action.

`void`
`setJsFunction(String jsFunction)`

Sets the fully qualified class path of the JavaScript function.

`void`
`setJsFunctionName(String jsFunctionName)`

Sets the JavaScript function name.

`void`
`setMethod(String method)`

Sets the name of method being called for the validator action.

`void`
`setMethodParams(String methodParams)`

Sets the method parameters for the method.

`void`
`setMsg(String msg)`

Sets the message associated with the validator action.

`void`
`setName(String name)`

Sets the name of the validator action.

`String`
`toString()`

Returns a string representation of the object.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### ValidatorAction

public ValidatorAction()
Constructs a new instance.

- 

## Method Details

  - 

### getClassname

public String getClassname()
Gets the class of the validator action.

Returns:
Class name of the validator Action.

  - 

### getDependencyList

public List<String> getDependencyList()
Returns the dependent validator names as an unmodifiable `List`.

Returns:
List of the validator action's dependents.

  - 

### getDepends

public String getDepends()
Gets the dependencies of the validator action as a comma separated list of validator names.

Returns:
The validator action's dependencies.

  - 

### getJavascript

public String getJavascript()
Gets the JavaScript equivalent of the Java class and method associated with this action.

Returns:
The JavaScript validation.

  - 

### getJsFunctionName

public String getJsFunctionName()
Gets the JavaScript function name. This is optional and can be used instead of validator action name for the name of the JavaScript function/object.

Returns:
The JavaScript function name.

  - 

### getMethod

public String getMethod()
Gets the name of method being called for the validator action.

Returns:
The method name.

  - 

### getMethodParams

public String getMethodParams()
Gets the method parameters for the method.

Returns:
Method's parameters.

  - 

### getMsg

public String getMsg()
Gets the message associated with the validator action.

Returns:
The message for the validator action.

  - 

### getName

public String getName()
Gets the name of the validator action.

Returns:
Validator Action name.

  - 

### init

protected void init()
Initialize based on set.

  - 

### isDependency

public boolean isDependency(String validatorName)
Checks whether or not the value passed in is in the depends field.

Parameters:
`validatorName` - Name of the dependency to check.
Returns:
Whether the named validator is a dependant.

  - 

### loadJavascriptFunction

protected void loadJavascriptFunction()
Load the JavaScript function specified by the given path. For this implementation, the `jsFunction` property should contain a fully qualified
 package and script name, separated by periods, to be loaded from the class loader that created this instance.

 TODO if the path begins with a '/' the path will be interpreted as absolute, and remain unchanged. If this fails then it will attempt to treat the path as
 a file path. It is assumed the script ends with a '.js'.

  - 

### setClassname

@Deprecated
public void setClassname(String className)
Deprecated.
Use `setClassName(String)`.

Sets the class of the validator action.

Parameters:
`className` - Class name of the validator Action.

  - 

### setClassName

public void setClassName(String className)
Sets the class of the validator action.

Parameters:
`className` - Class name of the validator Action.

  - 

### setDepends

public void setDepends(String depends)
Sets the dependencies of the validator action.

Parameters:
`depends` - A comma separated list of validator names.

  - 

### setJavascript

public void setJavascript(String javaScript)
Sets the JavaScript equivalent of the Java class and method associated with this action.

Parameters:
`javaScript` - The JavaScript validation.

  - 

### setJsFunction

public void setJsFunction(String jsFunction)
Sets the fully qualified class path of the JavaScript function.
 

 This is optional and can be used **instead** of the setJavascript(). Attempting to call both `setJsFunction` and
 `setJavascript` will result in an `IllegalStateException` being thrown.
 
 

 If **neither** setJsFunction nor setJavascript is set then validator will attempt to load the default JavaScript definition.
 

 

```

 **Examples**
   If in the validator.xml :
 #1:
      <validator name="tire"
            jsFunction="com.yourcompany.project.tireFuncion">
     Validator will attempt to load com.yourcompany.project.validateTireFunction.js from
     its class path.
 #2:
    <validator name="tire">
      Validator will use the name attribute to try and load
         org.apache.commons.validator.javascript.validateTire.js
      which is the default JavaScript definition.
 
```

Parameters:
`jsFunction` - The JavaScript function's fully qualified class path.

  - 

### setJsFunctionName

public void setJsFunctionName(String jsFunctionName)
Sets the JavaScript function name. This is optional and can be used instead of validator action name for the name of the JavaScript function/object.

Parameters:
`jsFunctionName` - The JavaScript function name.

  - 

### setMethod

public void setMethod(String method)
Sets the name of method being called for the validator action.

Parameters:
`method` - The method name.

  - 

### setMethodParams

public void setMethodParams(String methodParams)
Sets the method parameters for the method.

Parameters:
`methodParams` - A comma separated list of parameters.

  - 

### setMsg

public void setMsg(String msg)
Sets the message associated with the validator action.

Parameters:
`msg` - The message for the validator action.

  - 

### setName

public void setName(String name)
Sets the name of the validator action.

Parameters:
`name` - Validator Action name.

  - 

### toString

public String toString()
Returns a string representation of the object.

Overrides:
`toString` in class `Object`
Returns:
a string representation.