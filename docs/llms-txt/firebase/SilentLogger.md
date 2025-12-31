# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/SilentLogger.md.txt

# SilentLogger

public class **SilentLogger** extends Object  
implements [Logger](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger)  
Silent logger that does nothing.  

### Public Constructor Summary

|---|-------------------------------------------------------------------------------------------------------------------------------|
|   | [SilentLogger](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/SilentLogger#SilentLogger())() |

### Public Method Summary

|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void    | [d](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/SilentLogger#d(java.lang.String, java.lang.String, java.lang.Throwable))(String tag, String text, Throwable throwable)        |
| void    | [d](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/SilentLogger#d(java.lang.String, java.lang.String))(String tag, String text)                                                  |
| void    | [e](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/SilentLogger#e(java.lang.String, java.lang.String))(String tag, String text)                                                  |
| void    | [e](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/SilentLogger#e(java.lang.String, java.lang.String, java.lang.Throwable))(String tag, String text, Throwable throwable)        |
| int     | [getLogLevel](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/SilentLogger#getLogLevel())()                                                                                       |
| void    | [i](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/SilentLogger#i(java.lang.String, java.lang.String, java.lang.Throwable))(String tag, String text, Throwable throwable)        |
| void    | [i](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/SilentLogger#i(java.lang.String, java.lang.String))(String tag, String text)                                                  |
| boolean | [isLoggable](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/SilentLogger#isLoggable(java.lang.String, int))(String tag, int level)                                               |
| void    | [log](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/SilentLogger#log(int, java.lang.String, java.lang.String, boolean))(int priority, String tag, String msg, boolean forceLog) |
| void    | [log](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/SilentLogger#log(int, java.lang.String, java.lang.String))(int priority, String tag, String msg)                            |
| void    | [setLogLevel](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/SilentLogger#setLogLevel(int))(int logLevel)                                                                        |
| void    | [v](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/SilentLogger#v(java.lang.String, java.lang.String))(String tag, String text)                                                  |
| void    | [v](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/SilentLogger#v(java.lang.String, java.lang.String, java.lang.Throwable))(String tag, String text, Throwable throwable)        |
| void    | [w](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/SilentLogger#w(java.lang.String, java.lang.String, java.lang.Throwable))(String tag, String text, Throwable throwable)        |
| void    | [w](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/SilentLogger#w(java.lang.String, java.lang.String))(String tag, String text)                                                  |

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

From interface [io.fabric.sdk.android.Logger](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger)  

|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract void    | [d](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#d(java.lang.String, java.lang.String, java.lang.Throwable))(String tag, String text, Throwable throwable)        |
| abstract void    | [d](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#d(java.lang.String, java.lang.String))(String tag, String text)                                                  |
| abstract void    | [e](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#e(java.lang.String, java.lang.String))(String tag, String text)                                                  |
| abstract void    | [e](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#e(java.lang.String, java.lang.String, java.lang.Throwable))(String tag, String text, Throwable throwable)        |
| abstract int     | [getLogLevel](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#getLogLevel())()                                                                                       |
| abstract void    | [i](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#i(java.lang.String, java.lang.String, java.lang.Throwable))(String tag, String text, Throwable throwable)        |
| abstract void    | [i](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#i(java.lang.String, java.lang.String))(String tag, String text)                                                  |
| abstract boolean | [isLoggable](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#isLoggable(java.lang.String, int))(String tag, int level)                                               |
| abstract void    | [log](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#log(int, java.lang.String, java.lang.String, boolean))(int priority, String tag, String msg, boolean forceLog) |
| abstract void    | [log](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#log(int, java.lang.String, java.lang.String))(int priority, String tag, String msg)                            |
| abstract void    | [setLogLevel](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#setLogLevel(int))(int logLevel)                                                                        |
| abstract void    | [v](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#v(java.lang.String, java.lang.String))(String tag, String text)                                                  |
| abstract void    | [v](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#v(java.lang.String, java.lang.String, java.lang.Throwable))(String tag, String text, Throwable throwable)        |
| abstract void    | [w](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#w(java.lang.String, java.lang.String, java.lang.Throwable))(String tag, String text, Throwable throwable)        |
| abstract void    | [w](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#w(java.lang.String, java.lang.String))(String tag, String text)                                                  |

## Public Constructors

#### public
**SilentLogger**
()

<br />

## Public Methods

#### public void
**d**
(String tag, String text, Throwable throwable)

<br />

##### Parameters

|-----------|---|
| tag       |   |
| text      |   |
| throwable |   |

#### public void
**d**
(String tag, String text)

<br />

##### Parameters

|------|---|
| tag  |   |
| text |   |

#### public void
**e**
(String tag, String text)

<br />

##### Parameters

|------|---|
| tag  |   |
| text |   |

#### public void
**e**
(String tag, String text, Throwable throwable)

<br />

##### Parameters

|-----------|---|
| tag       |   |
| text      |   |
| throwable |   |

#### public int
**getLogLevel**
()

<br />

#### public void
**i**
(String tag, String text, Throwable throwable)

<br />

##### Parameters

|-----------|---|
| tag       |   |
| text      |   |
| throwable |   |

#### public void
**i**
(String tag, String text)

<br />

##### Parameters

|------|---|
| tag  |   |
| text |   |

#### public boolean
**isLoggable**
(String tag, int level)

<br />

##### Parameters

|-------|---|
| tag   |   |
| level |   |

#### public void
**log**
(int priority, String tag, String msg, boolean forceLog)

<br />

##### Parameters

|----------|---|
| priority |   |
| tag      |   |
| msg      |   |
| forceLog |   |

#### public void
**log**
(int priority, String tag, String msg)

<br />

##### Parameters

|----------|---|
| priority |   |
| tag      |   |
| msg      |   |

#### public void
**setLogLevel**
(int logLevel)

<br />

##### Parameters

|----------|---|
| logLevel |   |

#### public void
**v**
(String tag, String text)

<br />

##### Parameters

|------|---|
| tag  |   |
| text |   |

#### public void
**v**
(String tag, String text, Throwable throwable)

<br />

##### Parameters

|-----------|---|
| tag       |   |
| text      |   |
| throwable |   |

#### public void
**w**
(String tag, String text, Throwable throwable)

<br />

##### Parameters

|-----------|---|
| tag       |   |
| text      |   |
| throwable |   |

#### public void
**w**
(String tag, String text)

<br />

##### Parameters

|------|---|
| tag  |   |
| text |   |