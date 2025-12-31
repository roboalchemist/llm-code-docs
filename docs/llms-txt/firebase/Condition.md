# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition.md.txt

# Condition

public final class **Condition** extends Object  
Represents a Remote Config condition that can be included in a [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template).
A condition targets a specific group of users. A list of these conditions make up
part of a Remote Config template.  

### Public Constructor Summary

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [Condition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition#Condition(java.lang.String, java.lang.String))(String name, String expression) Creates a new [Condition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition).                                                                                                                                                                            |
|   | [Condition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition#Condition(java.lang.String, java.lang.String, com.google.firebase.remoteconfig.TagColor))(String name, String expression, [TagColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/TagColor) tagColor) Creates a new [Condition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition). |

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean                                                                                                                 | [equals](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition#equals(java.lang.Object))(Object o)                                                                                                                                                                                               |
| String                                                                                                                  | [getExpression](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition#getExpression())() Gets the expression of the condition.                                                                                                                                                                   |
| String                                                                                                                  | [getName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition#getName())() Gets the name of the condition.                                                                                                                                                                                     |
| [TagColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/TagColor)   | [getTagColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition#getTagColor())() Gets the tag color of the condition used for display purposes in the Firebase Console.                                                                                                                      |
| int                                                                                                                     | [hashCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition#hashCode())()                                                                                                                                                                                                                   |
| [Condition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition) | [setExpression](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition#setExpression(java.lang.String))(String expression) Sets the expression of the condition.                                                                                                                                  |
| [Condition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition) | [setName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition#setName(java.lang.String))(String name) Sets the name of the condition.                                                                                                                                                          |
| [Condition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition) | [setTagColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition#setTagColor(com.google.firebase.remoteconfig.TagColor))([TagColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/TagColor) tagColor) Sets the tag color of the condition. |

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
**Condition**
(String name, String expression)

Creates a new [Condition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition).  

##### Parameters

|    name    | A non-null, non-empty, and unique name of this condition. |
| expression |  A non-null and non-empty expression of this condition.   |
|------------|-----------------------------------------------------------|

#### public
**Condition**
(String name, String expression, [TagColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/TagColor) tagColor)

Creates a new [Condition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition).  

##### Parameters

|    name    |                                                                     A non-null, non-empty, and unique name of this condition.                                                                     |
| expression |                                                                      A non-null and non-empty expression of this condition.                                                                       |
|  tagColor  | A color associated with this condition for display purposes in the Firebase Console. Not specifying this value results in the console picking an arbitrary color to associate with the condition. |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Public Methods

#### public boolean
**equals**
(Object o)

<br />

#### public String
**getExpression**
()

Gets the expression of the condition.  

##### Returns

- The expression of the condition.  

#### public String
**getName**
()

Gets the name of the condition.  

##### Returns

- The name of the condition.  

#### public [TagColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/TagColor)
**getTagColor**
()

Gets the tag color of the condition used for display purposes in the Firebase Console.  

##### Returns

- The tag color of the condition.  

#### public int
**hashCode**
()

<br />

#### public [Condition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition)
**setExpression**
(String expression)

Sets the expression of the condition.

See [condition expressions](https://firebase.google.com/docs/remote-config/condition-reference) for the expected syntax of this field.  

##### Parameters

| expression | The logic of this condition. |
|------------|------------------------------|

##### Returns

- This [Condition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition).  

#### public [Condition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition)
**setName**
(String name)

Sets the name of the condition.  

##### Parameters

| name | A non-empty and unique name of this condition. |
|------|------------------------------------------------|

##### Returns

- This [Condition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition).  

#### public [Condition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition)
**setTagColor**
([TagColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/TagColor) tagColor)

Sets the tag color of the condition.

The color associated with this condition for display purposes in the Firebase Console.
Not specifying this value results in the console picking an arbitrary color to associate
with the condition.  

##### Parameters

| tagColor | The tag color of this condition. |
|----------|----------------------------------|

##### Returns

- This [Condition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition).