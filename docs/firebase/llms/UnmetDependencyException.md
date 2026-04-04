# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/UnmetDependencyException.md.txt

# UnmetDependencyException

public class **UnmetDependencyException** extends RuntimeException  
Used when a dependency is required but not met.  

### Public Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [UnmetDependencyException](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/UnmetDependencyException#UnmetDependencyException())()                                                                               |
|   | [UnmetDependencyException](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/UnmetDependencyException#UnmetDependencyException(java.lang.String))(String detailMessage)                                           |
|   | [UnmetDependencyException](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/UnmetDependencyException#UnmetDependencyException(java.lang.String, java.lang.Throwable))(String detailMessage, Throwable throwable) |
|   | [UnmetDependencyException](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/UnmetDependencyException#UnmetDependencyException(java.lang.Throwable))(Throwable throwable)                                         |

### Inherited Method Summary

From class java.lang.Throwable  

|----------------------------------|-------------------------------------------|
| synchronized final void          | addSuppressed(Throwable arg0)             |
| synchronized Throwable           | fillInStackTrace()                        |
| synchronized Throwable           | getCause()                                |
| String                           | getLocalizedMessage()                     |
| String                           | getMessage()                              |
| StackTraceElement\[\]            | getStackTrace()                           |
| synchronized final Throwable\[\] | getSuppressed()                           |
| synchronized Throwable           | initCause(Throwable arg0)                 |
| void                             | printStackTrace()                         |
| void                             | printStackTrace(PrintWriter arg0)         |
| void                             | printStackTrace(PrintStream arg0)         |
| void                             | setStackTrace(StackTraceElement\[\] arg0) |
| String                           | toString()                                |

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
**UnmetDependencyException**
()

<br />

#### public
**UnmetDependencyException**
(String detailMessage)

<br />

##### Parameters

|---------------|---|
| detailMessage |   |

#### public
**UnmetDependencyException**
(String detailMessage, Throwable throwable)

<br />

##### Parameters

|---------------|---|
| detailMessage |   |
| throwable     |   |

#### public
**UnmetDependencyException**
(Throwable throwable)

<br />

##### Parameters

|-----------|---|
| throwable |   |