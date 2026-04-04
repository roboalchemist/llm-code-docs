# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger.md.txt

# Logger

public interface **Logger**

|---|---|---|
| Known Indirect Subclasses [DefaultLogger](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/DefaultLogger), [SilentLogger](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/SilentLogger) |---|---| | [DefaultLogger](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/DefaultLogger) | Default logger that logs to android.util.Log. | | [SilentLogger](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/SilentLogger) | Silent logger that does nothing. | |||

Interface to support custom logger.

### Public Method Summary

|---|---|
| abstract void | [d](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#d(java.lang.String, java.lang.String, java.lang.Throwable))(String tag, String text, Throwable throwable) |
| abstract void | [d](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#d(java.lang.String, java.lang.String))(String tag, String text) |
| abstract void | [e](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#e(java.lang.String, java.lang.String))(String tag, String text) |
| abstract void | [e](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#e(java.lang.String, java.lang.String, java.lang.Throwable))(String tag, String text, Throwable throwable) |
| abstract int | [getLogLevel](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#getLogLevel())() |
| abstract void | [i](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#i(java.lang.String, java.lang.String, java.lang.Throwable))(String tag, String text, Throwable throwable) |
| abstract void | [i](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#i(java.lang.String, java.lang.String))(String tag, String text) |
| abstract boolean | [isLoggable](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#isLoggable(java.lang.String, int))(String tag, int level) |
| abstract void | [log](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#log(int, java.lang.String, java.lang.String, boolean))(int priority, String tag, String msg, boolean forceLog) |
| abstract void | [log](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#log(int, java.lang.String, java.lang.String))(int priority, String tag, String msg) |
| abstract void | [setLogLevel](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#setLogLevel(int))(int logLevel) |
| abstract void | [v](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#v(java.lang.String, java.lang.String))(String tag, String text) |
| abstract void | [v](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#v(java.lang.String, java.lang.String, java.lang.Throwable))(String tag, String text, Throwable throwable) |
| abstract void | [w](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#w(java.lang.String, java.lang.String, java.lang.Throwable))(String tag, String text, Throwable throwable) |
| abstract void | [w](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger#w(java.lang.String, java.lang.String))(String tag, String text) |

## Public Methods

#### public abstract void
**d**
(String tag, String text, Throwable throwable)

<br />

##### Parameters

|---|---|
| tag |   |
| text |   |
| throwable |   |

#### public abstract void
**d**
(String tag, String text)

<br />

##### Parameters

|---|---|
| tag |   |
| text |   |

#### public abstract void
**e**
(String tag, String text)

<br />

##### Parameters

|---|---|
| tag |   |
| text |   |

#### public abstract void
**e**
(String tag, String text, Throwable throwable)

<br />

##### Parameters

|---|---|
| tag |   |
| text |   |
| throwable |   |

#### public abstract int
**getLogLevel**
()

<br />

#### public abstract void
**i**
(String tag, String text, Throwable throwable)

<br />

##### Parameters

|---|---|
| tag |   |
| text |   |
| throwable |   |

#### public abstract void
**i**
(String tag, String text)

<br />

##### Parameters

|---|---|
| tag |   |
| text |   |

#### public abstract boolean
**isLoggable**
(String tag, int level)

<br />

##### Parameters

|---|---|
| tag |   |
| level |   |

#### public abstract void
**log**
(int priority, String tag, String msg, boolean forceLog)

<br />

##### Parameters

|---|---|
| priority |   |
| tag |   |
| msg |   |
| forceLog |   |

#### public abstract void
**log**
(int priority, String tag, String msg)

<br />

##### Parameters

|---|---|
| priority |   |
| tag |   |
| msg |   |

#### public abstract void
**setLogLevel**
(int logLevel)

<br />

##### Parameters

|---|---|
| logLevel |   |

#### public abstract void
**v**
(String tag, String text)

<br />

##### Parameters

|---|---|
| tag |   |
| text |   |

#### public abstract void
**v**
(String tag, String text, Throwable throwable)

<br />

##### Parameters

|---|---|
| tag |   |
| text |   |
| throwable |   |

#### public abstract void
**w**
(String tag, String text, Throwable throwable)

<br />

##### Parameters

|---|---|
| tag |   |
| text |   |
| throwable |   |

#### public abstract void
**w**
(String tag, String text)

<br />

##### Parameters

|---|---|
| tag |   |
| text |   |