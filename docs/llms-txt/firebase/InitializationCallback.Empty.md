# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback.Empty.md.txt

# InitializationCallback.Empty

public static class **InitializationCallback.Empty** extends Object  
implements [InitializationCallback](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback)\<Object\>  

### Inherited Field Summary

From interface [io.fabric.sdk.android.InitializationCallback](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback)  

|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---|
| public static final [InitializationCallback](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback) | [EMPTY](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback#EMPTY) |   |

### Public Method Summary

|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void | [failure](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback.Empty#failure(java.lang.Exception))(Exception exception) Failed initialization with exception |
| void | [success](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback.Empty#success(java.lang.Object))(Object object)                                               |

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

From interface [io.fabric.sdk.android.InitializationCallback](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback)  

|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract void | [failure](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback#failure(java.lang.Exception))(Exception exception) Failed initialization with exception |
| abstract void | [success](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback#success(T))(Object t) Successful initialization.                                        |

## Public Methods

#### public void
**failure**
(Exception exception)

Failed initialization with exception  

##### Parameters

|-----------|---|
| exception |   |

#### public void
**success**
(Object object)

<br />

##### Parameters

|--------|---|
| object |   |