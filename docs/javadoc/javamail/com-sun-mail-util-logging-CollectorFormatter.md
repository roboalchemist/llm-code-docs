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

## Class CollectorFormatter

- java.lang.Object

- 

  - java.util.logging.Formatter

  - 

    - com.sun.mail.util.logging.CollectorFormatter

- 

---

```
public class CollectorFormatter
extends Formatter
```

A LogRecord formatter that takes a sequence of LogRecords and combines them
 into a single summary result. Formating of the head, LogRecord, and tail are
 delegated to the wrapped formatter.

 

 By default each CollectorFormatter is initialized using the
 following LogManager configuration properties where
 <formatter-name> refers to the fully qualified class name or
 the fully qualified derived class name of the formatter.  If properties are
 not defined, or contain invalid values, then the specified default values are
 used.
 

 
  - <formatter-name>.comparator name of a
 Comparator class used to choose the collected
 LogRecord. If a comparator is specified then the max
 LogRecord is chosen. If comparator is set to the string literal
 null, then the last record is chosen. (defaults to
 SeverityComparator)

 
  - <formatter-name>.comparator.reverse a boolean
 true to collect the min LogRecord or false to
 collect the max LogRecord. (defaults to false)

 
  - <formatter-name>.format the
 MessageFormat string used to format the
 collected summary statistics. The arguments are explained in detail in the
 getTail documentation.
 (defaults to {0}{1}{2}{4,choice,-1#|0#|0<... {4,number,integer}
 more}\n)

 
  - <formatter-name>.formatter name of a Formatter class used
 to format the collected LogRecord. (defaults to CompactFormatter)

 

Since:
JavaMail 1.5.2
Author:
Jason Mehrens

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`CollectorFormatter()`
Creates the formatter using the LogManager defaults.

`CollectorFormatter(String format)`
Creates the formatter using the given format.

`CollectorFormatter(String format,
                  Formatter f,
                  Comparator<? super LogRecord> c)`
Creates the formatter using the given values.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`protected LogRecord`
`apply(LogRecord t,
     LogRecord u)`
Used to choose the collected LogRecord.

`protected String`
`finish(String s)`
Applied to the head, format, and tail returned by the target formatter.

`String`
`format(LogRecord record)`
Accumulates log records which will be used to produce the final output.

`String`
`getTail(Handler h)`
Formats the collected LogRecord and summary statistics.

`String`
`toString()`
Formats the collected LogRecord and summary statistics.

    - 

### Methods inherited from class java.util.logging.Formatter

`formatMessage, getHead`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### CollectorFormatter

```
public CollectorFormatter()
```

Creates the formatter using the LogManager defaults.

Throws:
`SecurityException` - if a security manager exists and the caller
 does not have LoggingPermission("control").
`UndeclaredThrowableException` - if there are problems loading from
 the LogManager.

    - 

#### CollectorFormatter

```
public CollectorFormatter(String format)
```

Creates the formatter using the given format.

Parameters:
`format` - the message format or null to use the LogManager default.
Throws:
`SecurityException` - if a security manager exists and the caller
 does not have LoggingPermission("control").
`UndeclaredThrowableException` - if there are problems loading from
 the LogManager.

    - 

#### CollectorFormatter

```
public CollectorFormatter(String format,
                          Formatter f,
                          Comparator<? super LogRecord> c)
```

Creates the formatter using the given values.

Parameters:
`format` - the format string or null to use the LogManager default.
`f` - the formatter used on the collected log record or null to
 specify no formatter.
`c` - the comparator used to determine which log record to format or
 null to specify no comparator.
Throws:
`SecurityException` - if a security manager exists and the caller
 does not have LoggingPermission("control").
`UndeclaredThrowableException` - if there are problems loading from
 the LogManager.

  - 

### Method Detail

    - 

#### format

```
public String format(LogRecord record)
```

Accumulates log records which will be used to produce the final output.
 The output is generated using the `getTail(java.util.logging.Handler)` method which also
 resets this formatter back to its original state.

Specified by:
`format` in class `Formatter`
Parameters:
`record` - the record to store.
Returns:
an empty string.
Throws:
`NullPointerException` - if the given record is null.

    - 

#### getTail

```
public String getTail(Handler h)
```

Formats the collected LogRecord and summary statistics. The collected
 results are reset after calling this method. The
 java.text argument indexes are assigned
 to the following properties:

 

 
      - `head` the
 head string
 returned from the target formatter and
 finished by this formatter.
 
      - `formatted` the current log record
 formatted by
 the target formatter and finished
 by this formatter.  If the formatter is null then record is formatted by
 this formatter.
 
      - `tail` the
 tail string
 returned from the target formatter and
 finished by this formatter.
 
      - `count` the total number of log records
 consumed by this formatter.
 
      - `remaining` the count minus one.
 
      - `thrown` the total number of log records
 consumed by this formatter with an assigned
 throwable.
 
      - `normal messages` the count minus the thrown.
 
      - `minMillis` the eldest log record
 event time
 consumed by this formatter. If the count is zero
 then this is set to the previous max or approximate start time if there
 was no previous max. By default this parameter is defined as a number.
 The format type and format style rules from the
 MessageFormat should be used to convert this from
 milliseconds to a date or time.
 
      - `maxMillis` the most recent log record
 event time
 consumed by this formatter. If the count is zero
 then this is set to the current time.
 By default this parameter is defined as a number. The format type and
 format style rules from the MessageFormat should be
 used to convert this from milliseconds to a date or time.
 
      - `elapsed` the elapsed time in milliseconds between the
 `maxMillis` and `minMillis`.
 
      - `startTime` the approximate start time in milliseconds.  By
 default this parameter is defined as a number. The format type and format
 style rules from the MessageFormat should be used to
 convert this from milliseconds to a date or time.
 
      - `currentTime` the
 current time in milliseconds.  By
 default this parameter is defined as a number. The format type and format
 style rules from the MessageFormat should be used to
 convert this from milliseconds to a date or time.
 
      - `uptime` the elapsed time in milliseconds between the
 `currentTime` and `startTime`.
 
      - `generation` the number times this method produced output with
 at least one consumed log record.  This can be used
 to track the number of complete reports this formatter has produced.
 

 

 Some example formats:

 

 
      - `com.sun.mail.util.logging.CollectorFormatter.format={0}{1}{2}{4,choice,-1#|0#|0<... {4,number,integer} more}\n`
 

 This prints the head (`{0}`), format (`{1}`), and tail
 (`{2}`) from the target formatter followed by the number of
 remaining (`{4}`) log records consumed by this formatter if there
 are any remaining records.
 

```

 Encoding failed.|NullPointerException: null String.getBytes(:913)... 3 more
 
```

 
      - `com.sun.mail.util.logging.CollectorFormatter.format=These {3} messages occurred between\n{7,date,EEE, MMM dd HH:mm:ss:S ZZZ yyyy} and {8,time,EEE, MMM dd HH:mm:ss:S ZZZ yyyy}\n`
 

 This prints the count (`{3}`) followed by the date and time of the
 eldest log record (`{7}`) and the date and time of the most recent
 log record (`{8}`).
 

```

 These 292 messages occurred between
 Tue, Jul 21 14:11:42:449 -0500 2009 and Fri, Nov 20 07:29:24:0 -0600 2009
 
```

 
      - `com.sun.mail.util.logging.CollectorFormatter.format=These {3} messages occurred between {9,choice,86400000#{7,date} {7,time} and {8,time}|86400000<{7,date} and {8,date}}\n`
 

 This prints the count (`{3}`) and then chooses the format based on
 the elapsed time (`{9}`). If the elapsed time is less than one day
 then the eldest log record (`{7}`) date and time is formatted
 followed by just the time of the most recent log record (`{8}`.
 Otherwise, the just the date of the eldest log record (`{7}`) and
 just the date of most recent log record (`{8}` is formatted.
 

```

 These 73 messages occurred between Jul 21, 2009 2:11:42 PM and 2:13:32 PM

 These 116 messages occurred between Jul 21, 2009 and Aug 20, 2009
 
```

 
      - `com.sun.mail.util.logging.CollectorFormatter.format={13} alert reports since {10,date}.\n`
 

 This prints the generation (`{13}`) followed by the start time
 (`{10}`) formatted as a date.
 

```

 4,320 alert reports since Jul 21, 2012.
 
```

 

Overrides:
`getTail` in class `Formatter`
Parameters:
`h` - the handler or null.
Returns:
the output string.

    - 

#### toString

```
public String toString()
```

Formats the collected LogRecord and summary statistics. The LogRecord and
 summary statistics are not changed by calling this method.

Overrides:
`toString` in class `Object`
Returns:
the current record formatted or the default toString.
See Also:
`getTail(java.util.logging.Handler)`

    - 

#### apply

```
protected LogRecord apply(LogRecord t,
                          LogRecord u)
```

Used to choose the collected LogRecord. This implementation returns the
 greater of two LogRecords.

Parameters:
`t` - the current record.
`u` - the record that could replace the current.
Returns:
the greater of the given log records.
Throws:
`NullPointerException` - may occur if either record is null.

    - 

#### finish

```
protected String finish(String s)
```

Applied to the head, format, and tail returned by the target formatter.
 This implementation trims all input strings.

Parameters:
`s` - the string to transform.
Returns:
the transformed string.
Throws:
`NullPointerException` - if the given string is null.

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