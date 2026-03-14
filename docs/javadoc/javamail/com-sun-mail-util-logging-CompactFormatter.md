JavaScript is disabled on your browser.

Skip navigation links

- Overview

- Package

- Class

- Use

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

com.sun.mail.util.logging

## Class CompactFormatter

- java.lang.Object

- 

  - java.util.logging.Formatter

  - 

    - com.sun.mail.util.logging.CompactFormatter

- 

---

```
public class CompactFormatter
extends Formatter
```

A plain text formatter that can produce fixed width output. By default this
 formatter will produce output no greater than 160 characters wide plus the
 separator and newline characters. Only specified fields support an
 alternate fixed width format.
 

 By default each CompactFormatter is initialized using the following
 LogManager configuration properties where
 <formatter-name> refers to the fully qualified class name or
 the fully qualified derived class name of the formatter. If properties are
 not defined, or contain invalid values, then the specified default values are
 used.
 

 
  - <formatter-name>.format - the format string used to transform the output. The format string can be
 used to fix the output size. (defaults to %7$#.160s%n)
 

Since:
JavaMail 1.5.2
Author:
Jason Mehrens

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`CompactFormatter()`
Creates an instance with a default format pattern.

`CompactFormatter(String format)`
Creates an instance with the given format pattern.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`protected Throwable`
`apply(Throwable t)`
Chooses a single throwable from the cause chain that will be formatted.

`String`
`format(LogRecord record)`
Format the given log record and returns the formatted string.

`String`
`formatBackTrace(LogRecord record)`
Formats the back trace for the given log record.

`String`
`formatError(LogRecord record)`
Formats the thrown property of a LogRecord as an error message.

`String`
`formatLevel(LogRecord record)`
Formats the level property of the given log record.

`String`
`formatLoggerName(LogRecord record)`
Formats the logger name property of the given log record.

`String`
`formatMessage(LogRecord record)`
Formats message for the log record.

`String`
`formatMessage(Throwable t)`
Formats the message from the thrown property of the log record.

`String`
`formatSource(LogRecord record)`
Formats the source from the given log record.

`Number`
`formatThreadID(LogRecord record)`
Formats the thread id property of the given log record.

`String`
`formatThrown(LogRecord record)`
Formats the thrown property of a LogRecord.

`protected boolean`
`ignore(StackTraceElement s)`
Determines if a stack frame should be ignored as the cause of an error.

`protected String`
`toAlternate(String s)`
Defines the alternate format.

    - 

### Methods inherited from class java.util.logging.Formatter

`getHead, getTail`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### CompactFormatter

```
public CompactFormatter()
```

Creates an instance with a default format pattern.

    - 

#### CompactFormatter

```
public CompactFormatter(String format)
```

Creates an instance with the given format pattern.

Parameters:
`format` - the pattern or null to use
 the LogManager default. The arguments are described in the
 format method.

  - 

### Method Detail

    - 

#### format

```
public String format(LogRecord record)
```

Format the given log record and returns the formatted string. The
 java.util argument indexes are assigned to the following properties:

 

 
      - `format` - the java.util.Formatter format string specified in the
 <formatter-name>.format property or the format that was given when
 this formatter was created.
 
      - `date` - if the log record supports nanoseconds then a
 ZonedDateTime object representing the event time of the log record in the
 system time zone. Otherwise, a Date object representing
 event time of the log record.
 
      - `source` - a string representing the caller, if available;
 otherwise, the logger's name.
 
      - `logger` - the logger's
 simple
 name.
 
      - `level` - the
 log level.
 
      - `message` - the formatted log message returned from the
 formatMessage(LogRecord) method.
 
      - `thrown` - a string representing the
 throwable associated with the log record
 and a relevant stack trace element if available; otherwise, an empty
 string is used.
 
      - `message|thrown` The message and the thrown properties joined
 as one parameter. This parameter supports
 alternate form.
 
      - `thrown|message` The thrown and message properties joined as
 one parameter. This parameter supports
 alternate form.
 
      - `sequence` the
 sequence number if the given
 log record.
 
      - `thread id` the thread id
 of the given log record. By default this is formatted as a `long`
 by an unsigned conversion.
 
      - `error` the throwable
 simple class name and
 error message without any stack
 trace.
 
      - `message|error` The message and error properties joined as one
 parameter. This parameter supports
 alternate form.
 
      - `error|message` The error and message properties joined as one
 parameter. This parameter supports
 alternate form.
 
      - `backtrace` only the
 stack trace of the given
 throwable.
 
      - `bundlename` the resource bundle
 name of the given log
 record.
 
      - `key` the raw message
 before localization or formatting.
 

 

 Some example formats:

 

 
      - `com.sun.mail.util.logging.CompactFormatter.format=%7$#.160s%n`
 

 This prints only 160 characters of the message|thrown (`7$`) using
 the alternate form. The
 separator is not included as part of the total width.
 

```

 Encoding failed.|NullPointerException: null String.getBytes(:913)
 
```

 
      - `com.sun.mail.util.logging.CompactFormatter.format=%7$#.20s%n`
 

 This prints only 20 characters of the message|thrown (`7$`) using
 the alternate form. This will
 perform a weighted truncation of both the message and thrown properties
 of the log record. The separator is not included as part of the total
 width.
 

```

 Encoding|NullPointerE
 
```

 
      - `com.sun.mail.util.logging.CompactFormatter.format=%1$tc %2$s%n%4$s: %5$s%6$s%n`
 

 This prints the timestamp (`1$`) and the source (`2$`) on the
 first line. The second line is the log level (`4$`), log message
 (`5$`), and the throwable with a relevant stack trace element
 (`6$`) if one is available.
 

```

 Fri Nov 20 07:29:24 CST 2009 MyClass fatal
 SEVERE: Encoding failed.NullPointerException: null String.getBytes(:913)
 
```

 
      - `com.sun.mail.util.logging.CompactFormatter.format=%4$s: %12$#.160s%n`
 

 This prints the log level (`4$`) and only 160 characters of the
 message|error (`12$`) using the alternate form.
 

```

 SEVERE: Unable to send notification.|SocketException: Permission denied: connect
 
```

 
      - `com.sun.mail.util.logging.CompactFormatter.format=[%9$d][%1$tT][%10$d][%2$s] %5$s%n%6$s%n`
 

 This prints the sequence (`9$`), event time (`1$`) as 24 hour
 time, thread id (`10$`), source (`2$`), log message
 (`5$`), and the throwable with back trace (`6$`).
 

```

 [125][14:11:42][38][MyClass fatal] Unable to send notification.
 SocketException: Permission denied: connect SMTPTransport.openServer(:1949)
 
```

 

Specified by:
`format` in class `Formatter`
Parameters:
`record` - the log record to format.
Returns:
the formatted record.
Throws:
`NullPointerException` - if the given record is null.

    - 

#### formatMessage

```
public String formatMessage(LogRecord record)
```

Formats message for the log record. This method removes any fully
 qualified throwable class names from the message.

Overrides:
`formatMessage` in class `Formatter`
Parameters:
`record` - the log record.
Returns:
the formatted message string.

    - 

#### formatMessage

```
public String formatMessage(Throwable t)
```

Formats the message from the thrown property of the log record. This
 method replaces fully qualified throwable class names from the message
 cause chain with simple class names.

Parameters:
`t` - the throwable to format or null.
Returns:
the empty string if null was given or the formatted message
 string from the throwable which may be null.

    - 

#### formatLevel

```
public String formatLevel(LogRecord record)
```

Formats the level property of the given log record.

Parameters:
`record` - the record.
Returns:
the formatted logger name.
Throws:
`NullPointerException` - if the given record is null.

    - 

#### formatSource

```
public String formatSource(LogRecord record)
```

Formats the source from the given log record.

Parameters:
`record` - the record.
Returns:
the formatted source of the log record.
Throws:
`NullPointerException` - if the given record is null.

    - 

#### formatLoggerName

```
public String formatLoggerName(LogRecord record)
```

Formats the logger name property of the given log record.

Parameters:
`record` - the record.
Returns:
the formatted logger name.
Throws:
`NullPointerException` - if the given record is null.

    - 

#### formatThreadID

```
public Number formatThreadID(LogRecord record)
```

Formats the thread id property of the given log record. By default this
 is formatted as a `long` by an unsigned conversion.

Parameters:
`record` - the record.
Returns:
the formatted thread id as a number.
Throws:
`NullPointerException` - if the given record is null.
Since:
JavaMail 1.5.4

    - 

#### formatThrown

```
public String formatThrown(LogRecord record)
```

Formats the thrown property of a LogRecord. The returned string will
 contain a throwable message with a back trace.

Parameters:
`record` - the record.
Returns:
empty string if nothing was thrown or formatted string.
Throws:
`NullPointerException` - if the given record is null.
See Also:
`apply(java.lang.Throwable)`, 
`formatBackTrace(java.util.logging.LogRecord)`

    - 

#### formatError

```
public String formatError(LogRecord record)
```

Formats the thrown property of a LogRecord as an error message. The
 returned string will not contain a back trace.

Parameters:
`record` - the record.
Returns:
empty string if nothing was thrown or formatted string.
Throws:
`NullPointerException` - if the given record is null.
Since:
JavaMail 1.5.4
See Also:
`Throwable.toString()`, 
`apply(java.lang.Throwable)`, 
`formatMessage(java.lang.Throwable)`

    - 

#### formatBackTrace

```
public String formatBackTrace(LogRecord record)
```

Formats the back trace for the given log record.

Parameters:
`record` - the log record to format.
Returns:
the formatted back trace.
Throws:
`NullPointerException` - if the given record is null.
See Also:
`apply(java.lang.Throwable)`, 
`formatThrown(java.util.logging.LogRecord)`, 
`ignore(java.lang.StackTraceElement)`

    - 

#### apply

```
protected Throwable apply(Throwable t)
```

Chooses a single throwable from the cause chain that will be formatted.
 This implementation chooses the throwable that best describes the chain.
 Subclasses can override this method to choose an alternate throwable for
 formatting.

Parameters:
`t` - the throwable from the log record.
Returns:
the chosen throwable or null only if the given argument is null.
See Also:
`formatThrown(java.util.logging.LogRecord)`

    - 

#### ignore

```
protected boolean ignore(StackTraceElement s)
```

Determines if a stack frame should be ignored as the cause of an error.

Parameters:
`s` - the stack trace element.
Returns:
true if this frame should be ignored.
See Also:
`formatThrown(java.util.logging.LogRecord)`

    - 

#### toAlternate

```
protected String toAlternate(String s)
```

Defines the alternate format. This implementation removes all control
 characters from the given string.

Parameters:
`s` - any string or null.
Returns:
null if the argument was null otherwise, an alternate string.

Skip navigation links

- Overview

- Package

- Class

- Use

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

Copyright © 2018 Oracle. All rights reserved.