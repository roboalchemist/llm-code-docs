# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit.md.txt

# ParameterValue.Explicit

public static final class **ParameterValue.Explicit** extends [ParameterValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue)  
Represents an explicit Remote Config parameter value with a value that the
parameter is set to.  

### Public Method Summary

|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean | [equals](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit#equals(java.lang.Object))(Object o)                                                                                                                                                    |
| String  | [getValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit#getValue())() Gets the value of [ParameterValue.Explicit](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit). |
| int     | [hashCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit#hashCode())()                                                                                                                                                                        |

### Inherited Method Summary

From class [com.google.firebase.remoteconfig.ParameterValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue)  

|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [ParameterValue.InAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault) | [inAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue#inAppDefault())() Creates a new [ParameterValue.InAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault) instance.                      |
| static [ParameterValue.Explicit](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit)         | [of](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue#of(java.lang.String))(String value) Creates a new [ParameterValue.Explicit](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit) instance with the given value. |

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

## Public Methods

#### public boolean
**equals**
(Object o)

<br />

#### public String
**getValue**
()

Gets the value of [ParameterValue.Explicit](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit).  

##### Returns

- The value.  

#### public int
**hashCode**
()

<br />