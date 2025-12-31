# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Priority.md.txt

# Priority

public final enum **Priority** extends Enum\<[Priority](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Priority)\>  
enum to define ordering for PriorityBlockingQueue in [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor)  

### Inherited Method Summary

From class java.lang.Enum  

|----------------------------------|---------------------------------------|
| final Object                     | clone()                               |
| final int                        | compareTo(E arg0)                     |
| int                              | compareTo(Object arg0)                |
| final boolean                    | equals(Object arg0)                   |
| final void                       | finalize()                            |
| final Class\<E\>                 | getDeclaringClass()                   |
| final int                        | hashCode()                            |
| final String                     | name()                                |
| final int                        | ordinal()                             |
| String                           | toString()                            |
| static \<T extends Enum\<T\>\> T | valueOf(Class\<T\> arg0, String arg1) |

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

From interface java.lang.Comparable  

|--------------|-------------------------------------|
| abstract int | compareTo(E extends Enum\<E\> arg0) |

## Enum Values

#### public static final Priority
**HIGH**

<br />

#### public static final Priority
**IMMEDIATE**

<br />

#### public static final Priority
**LOW**

<br />

#### public static final Priority
**NORMAL**

<br />