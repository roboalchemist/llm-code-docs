# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.md.txt

# ParameterValue

public abstract class **ParameterValue** extends Object  

|---|---|---|
| Known Direct Subclasses [ParameterValue.Explicit](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit), [ParameterValue.InAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault) |-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------| | [ParameterValue.Explicit](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit)         | Represents an explicit Remote Config parameter value with a value that the parameter is set to. | | [ParameterValue.InAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault) | Represents an in app default parameter value.                                                   | |||

Represents a Remote Config parameter value that can be used in a [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template).  

### Nested Class Summary

|-------|---|---|-------------------------------------------------------------------------------------------------|
| class | [ParameterValue.Explicit](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit) || Represents an explicit Remote Config parameter value with a value that the parameter is set to. |
| class | [ParameterValue.InAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault) || Represents an in app default parameter value.                                                   |

### Public Constructor Summary

|---|------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [ParameterValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue#ParameterValue())() |

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [ParameterValue.InAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault) | [inAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue#inAppDefault())() Creates a new [ParameterValue.InAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault) instance.                      |
| static [ParameterValue.Explicit](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit)         | [of](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue#of(java.lang.String))(String value) Creates a new [ParameterValue.Explicit](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit) instance with the given value. |

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
**ParameterValue**
()

<br />

## Public Methods

#### public static [ParameterValue.InAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault)
**inAppDefault**
()

Creates a new [ParameterValue.InAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault) instance.  

##### Returns

- A [ParameterValue.InAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault) instance.  

#### public static [ParameterValue.Explicit](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit)
**of**
(String value)

Creates a new [ParameterValue.Explicit](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit) instance with the given value.  

##### Parameters

| value | The value of the [ParameterValue.Explicit](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit). |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A [ParameterValue.Explicit](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit) instance.