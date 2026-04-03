# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask.Status.md.txt

# AsyncTask.Status

public static final enum **AsyncTask.Status** extends Enum\<[AsyncTask.Status](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask.Status)\>  
Indicates the current status of the task. Each status will be set only once
during the lifetime of a task.  

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

#### public static final AsyncTask.Status
**FINISHED**

Indicates that [onPostExecute(Result)](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/AsyncTask#onPostExecute(Result)) has finished.  

#### public static final AsyncTask.Status
**PENDING**

Indicates that the task has not been executed yet.  

#### public static final AsyncTask.Status
**RUNNING**

Indicates that the task is running.