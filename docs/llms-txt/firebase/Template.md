# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template.md.txt

# Template

public final class **Template** extends Object  
Represents a Remote Config template.  

### Public Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template#Template(java.lang.String))(String etag) Creates a new [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template). |

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean                                                                                                                                          | [equals](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template#equals(java.lang.Object))(Object o)                                                                                                                                                                                                                                                                                                   |
| static [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)                     | [fromJSON](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template#fromJSON(java.lang.String))(String json) Creates and returns a new Remote Config template from a JSON string.                                                                                                                                                                                                                       |
| List\<[Condition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition)\>                  | [getConditions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template#getConditions())() Gets the list of conditions of the template.                                                                                                                                                                                                                                                                |
| String                                                                                                                                           | [getETag](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template#getETag())() Gets the ETag of the template.                                                                                                                                                                                                                                                                                          |
| Map\<String, [ParameterGroup](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup)\> | [getParameterGroups](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template#getParameterGroups())() Gets the map of parameter groups of the template.                                                                                                                                                                                                                                                 |
| Map\<String, [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter)\>           | [getParameters](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template#getParameters())() Gets the map of parameters of the template.                                                                                                                                                                                                                                                                 |
| [Version](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version)                              | [getVersion](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template#getVersion())() Gets the version information of the template.                                                                                                                                                                                                                                                                     |
| int                                                                                                                                              | [hashCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template#hashCode())()                                                                                                                                                                                                                                                                                                                       |
| [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)                            | [setConditions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template#setConditions(java.util.List<com.google.firebase.remoteconfig.Condition>))(List\<[Condition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition)\> conditions) Sets the list of conditions of the template.                                                            |
| [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)                            | [setParameterGroups](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template#setParameterGroups(java.util.Map<java.lang.String, com.google.firebase.remoteconfig.ParameterGroup>))(Map\<String, [ParameterGroup](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup)\> parameterGroups) Sets the map of parameter groups of the template. |
| [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)                            | [setParameters](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template#setParameters(java.util.Map<java.lang.String, com.google.firebase.remoteconfig.Parameter>))(Map\<String, [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter)\> parameters) Sets the map of parameters of the template.                                     |
| [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)                            | [setVersion](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template#setVersion(com.google.firebase.remoteconfig.Version))([Version](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version) version) Sets the version information of the template.                                                                                                  |
| String                                                                                                                                           | [toJSON](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template#toJSON())() Gets the JSON-serializable representation of this template.                                                                                                                                                                                                                                                               |

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
**Template**
(String etag)

Creates a new [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template).  

##### Parameters

| etag | The ETag of this template. |
|------|----------------------------|

## Public Methods

#### public boolean
**equals**
(Object o)

<br />

#### public static [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)
**fromJSON**
(String json)

Creates and returns a new Remote Config template from a JSON string.
Input JSON string must contain an `etag` property to create a valid template.  

##### Parameters

| json | A non-null JSON string to populate a Remote Config template. |
|------|--------------------------------------------------------------|

##### Returns

- A new [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) instance.  

##### Throws

| [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) | If the input JSON string is not parsable. |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|

#### public List\<[Condition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition)\>
**getConditions**
()

Gets the list of conditions of the template.  

##### Returns

- A non-null list of conditions.  

#### public String
**getETag**
()

Gets the ETag of the template.  

##### Returns

- The ETag of the template.  

#### public Map\<String, [ParameterGroup](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup)\>
**getParameterGroups**
()

Gets the map of parameter groups of the template.  

##### Returns

- A non-null map of parameter group names to their parameter group instances.  

#### public Map\<String, [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter)\>
**getParameters**
()

Gets the map of parameters of the template.  

##### Returns

- A non-null map of parameter keys to their optional default values and optional conditional values.  

#### public [Version](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version)
**getVersion**
()

Gets the version information of the template.  

##### Returns

- The version information of the template.  

#### public int
**hashCode**
()

<br />

#### public [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)
**setConditions**
(List\<[Condition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition)\> conditions)

Sets the list of conditions of the template.  

##### Parameters

| conditions | A non-null list of conditions in descending order by priority. |
|------------|----------------------------------------------------------------|

##### Returns

- This [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) instance.  

#### public [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)
**setParameterGroups**
(Map\<String, [ParameterGroup](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup)\> parameterGroups)

Sets the map of parameter groups of the template.  

##### Parameters

| parameterGroups | A non-null map of parameter group names to their parameter group instances. |
|-----------------|-----------------------------------------------------------------------------|

##### Returns

- This [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) instance.  

#### public [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)
**setParameters**
(Map\<String, [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter)\> parameters)

Sets the map of parameters of the template.  

##### Parameters

| parameters | A non-null map of parameter keys to their optional default values and optional conditional values. |
|------------|----------------------------------------------------------------------------------------------------|

##### Returns

- This [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) instance.  

#### public [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template)
**setVersion**
([Version](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version) version)

Sets the version information of the template.
Only the version's description field can be specified here.  

##### Parameters

| version | A [Version](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version) instance. |
|---------|---------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) instance.  

#### public String
**toJSON**
()

Gets the JSON-serializable representation of this template.  

##### Returns

- A JSON-serializable representation of this [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) instance.