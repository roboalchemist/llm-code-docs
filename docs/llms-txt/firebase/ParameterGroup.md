# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup.md.txt

# ParameterGroup

public final class **ParameterGroup** extends Object  
Represents a Remote Config parameter group that can be included in a [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template).
Grouping parameters is only for management purposes and does not affect client-side
fetching of parameter values.  

### Public Constructor Summary

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [ParameterGroup](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup#ParameterGroup())() Creates a new [ParameterGroup](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup). |

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean                                                                                                                                | [equals](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup#equals(java.lang.Object))(Object o)                                                                                                                                                                                                                                                                         |
| String                                                                                                                                 | [getDescription](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup#getDescription())() Gets the description of the parameter group.                                                                                                                                                                                                                                    |
| Map\<String, [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter)\> | [getParameters](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup#getParameters())() Gets the map of parameters that belong to this group.                                                                                                                                                                                                                             |
| int                                                                                                                                    | [hashCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup#hashCode())()                                                                                                                                                                                                                                                                                             |
| [ParameterGroup](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup)      | [setDescription](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup#setDescription(java.lang.String))(String description) Sets the description of the parameter group.                                                                                                                                                                                                  |
| [ParameterGroup](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup)      | [setParameters](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup#setParameters(java.util.Map<java.lang.String, com.google.firebase.remoteconfig.Parameter>))(Map\<String, [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter)\> parameters) Sets the map of parameters that belong to this group. |

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
**ParameterGroup**
()

Creates a new [ParameterGroup](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup).

## Public Methods

#### public boolean
**equals**
(Object o)

<br />

#### public String
**getDescription**
()

Gets the description of the parameter group.  

##### Returns

- The description of the parameter or null.  

#### public Map\<String, [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter)\>
**getParameters**
()

Gets the map of parameters that belong to this group.  

##### Returns

- A non-null map of parameter keys to their optional default values and optional conditional values.  

#### public int
**hashCode**
()

<br />

#### public [ParameterGroup](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup)
**setDescription**
(String description)

Sets the description of the parameter group.
Should not be over 256 characters and may contain any Unicode characters.  

##### Parameters

| description | The description of the parameter group. |
|-------------|-----------------------------------------|

##### Returns

- This [ParameterGroup](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup).  

#### public [ParameterGroup](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup)
**setParameters**
(Map\<String, [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter)\> parameters)

Sets the map of parameters that belong to this group.

A parameter only appears once per Remote Config template.
An ungrouped parameter appears at the top level, whereas a
parameter organized within a group appears within its group's map of parameters.  

##### Parameters

| parameters | A non-null map of parameter keys to their optional default values and optional conditional values. |
|------------|----------------------------------------------------------------------------------------------------|

##### Returns

- This [ParameterGroup](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup) instance.