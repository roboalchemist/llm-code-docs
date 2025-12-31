# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter.md.txt

# Parameter

public final class **Parameter** extends Object  
Represents a Remote Config parameter that can be included in a [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template).
At minimum, a default value or a conditional value must be present for the
parameter to have any effect.  

### Public Constructor Summary

|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter#Parameter())() Creates a new [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter). |

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean                                                                                                                                          | [equals](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter#equals(java.lang.Object))(Object o)                                                                                                                                                                                                                                                                                                     |
| Map\<String, [ParameterValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue)\> | [getConditionalValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter#getConditionalValues())() Gets the conditional values of the parameter.                                                                                                                                                                                                                                                   |
| [ParameterValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue)                | [getDefaultValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter#getDefaultValue())() Gets the default value of the parameter.                                                                                                                                                                                                                                                                  |
| String                                                                                                                                           | [getDescription](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter#getDescription())() Gets the description of the parameter.                                                                                                                                                                                                                                                                      |
| [ParameterValueType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValueType)        | [getValueType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter#getValueType())() Gets the data type of the parameter value.                                                                                                                                                                                                                                                                      |
| int                                                                                                                                              | [hashCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter#hashCode())()                                                                                                                                                                                                                                                                                                                         |
| [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter)                          | [setConditionalValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter#setConditionalValues(java.util.Map<java.lang.String, com.google.firebase.remoteconfig.ParameterValue>))(Map\<String, [ParameterValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue)\> conditionalValues) Sets the conditional values of the parameter. |
| [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter)                          | [setDefaultValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter#setDefaultValue(com.google.firebase.remoteconfig.ParameterValue))([ParameterValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue) value) Sets the default value of the parameter.                                                                            |
| [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter)                          | [setDescription](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter#setDescription(java.lang.String))(String description) Sets the description of the parameter.                                                                                                                                                                                                                                    |
| [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter)                          | [setValueType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter#setValueType(com.google.firebase.remoteconfig.ParameterValueType))([ParameterValueType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValueType) valueType) Sets the data type of the parameter value.                                                                |

### Inherited Method Summary

From class java.lang.Object  

|------------------|---------------------------|
| Object           | clone()                   |
| boolean          | equals(Object arg0)       |
| void             | finalize()                |
| final Class\<?\> | getClass()                |
| int              | hashCode()                |
| final void       | notify()                  |
| final void       | notifyAll()               |
| String           | toString()                |
| final void       | wait(long arg0, int arg1) |
| final void       | wait(long arg0)           |
| final void       | wait()                    |

## Public Constructors

#### public
**Parameter**
()

Creates a new [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter).

## Public Methods

#### public boolean
**equals**
(Object o)

<br />

#### public Map\<String, [ParameterValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue)\>
**getConditionalValues**
()

Gets the conditional values of the parameter.
The condition name of the highest priority (the one listed first in the
[Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)'s conditions list) determines the value of this parameter.  

##### Returns

- A non-null map of conditional values.  

#### public [ParameterValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue)
**getDefaultValue**
()

Gets the default value of the parameter.  

##### Returns

- A [ParameterValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue) instance or null.  

#### public String
**getDescription**
()

Gets the description of the parameter.  

##### Returns

- The description of the parameter or null.  

#### public [ParameterValueType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValueType)
**getValueType**
()

Gets the data type of the parameter value.  

##### Returns

- The data type of the parameter value or null.  

#### public int
**hashCode**
()

<br />

#### public [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter)
**setConditionalValues**
(Map\<String, [ParameterValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue)\> conditionalValues)

Sets the conditional values of the parameter.
The condition name of the highest priority (the one listed first in the
[Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)'s conditions list) determines the value of this parameter.  

##### Parameters

| conditionalValues | A non-null map of conditional values. |
|-------------------|---------------------------------------|

##### Returns

- This [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter).  

#### public [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter)
**setDefaultValue**
([ParameterValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue) value)

Sets the default value of the parameter.
This is the value to set the parameter to, when none of the named conditions
evaluate to true.  

##### Parameters

| value | An [ParameterValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue) instance. |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter).  

#### public [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter)
**setDescription**
(String description)

Sets the description of the parameter.
Should not be over 100 characters and may contain any Unicode characters.  

##### Parameters

| description | The description of the parameter. |
|-------------|-----------------------------------|

##### Returns

- This [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter).  

#### public [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter)
**setValueType**
([ParameterValueType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValueType) valueType)

Sets the data type of the parameter value.
Defaults to \`ParameterValueType.STRING\` if unspecified.  

##### Parameters

| valueType | The data type of the parameter value. |
|-----------|---------------------------------------|

##### Returns

- This [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter).