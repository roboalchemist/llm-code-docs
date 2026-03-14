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

## Class DurationFilter

- java.lang.Object

- 

  - com.sun.mail.util.logging.DurationFilter

- 

All Implemented Interfaces:
Filter

---

```
public class DurationFilter
extends Object
implements Filter
```

A filter used to limit log records based on a maximum generation rate.

 The duration specified is used to compute the record rate and the amount of
 time the filter will reject records once the rate has been exceeded. Once the
 rate is exceeded records are not allowed until the duration has elapsed.

 

 By default each `DurationFilter` is initialized using the following
 LogManager configuration properties where `<filter-name>` refers to the
 fully qualified class name of the handler. If properties are not defined, or
 contain invalid values, then the specified default values are used.

 

 
  - <filter-name>.records the max number of records per duration.
 A numeric long integer or a multiplication expression can be used as the
 value. (defaults to `1000`)

 
  - <filter-name>.duration the number of milliseconds to suppress
 log records from being published. This is also used as duration to determine
 the log record rate. A numeric long integer or a multiplication expression
 can be used as the value. If the `java.time` package is available then
 an ISO-8601 duration format of `PnDTnHnMn.nS` can be used as the value.
 The suffixes of "D", "H", "M" and "S" are for days, hours, minutes and
 seconds. The suffixes must occur in order. The seconds can be specified with
 a fractional component to declare milliseconds. (defaults to `PT15M`)
 

 

 For example, the settings to limit `MailHandler` with a default
 capacity to only send a maximum of two email messages every six minutes would
 be as follows:
 

```

 
  com.sun.mail.util.logging.MailHandler.filter = com.sun.mail.util.logging.DurationFilter
  com.sun.mail.util.logging.MailHandler.capacity = 1000
  com.sun.mail.util.logging.DurationFilter.records = 2L * 1000L
  com.sun.mail.util.logging.DurationFilter.duration = PT6M
 
 
```

Since:
JavaMail 1.5.5
Author:
Jason Mehrens

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`DurationFilter()`
Creates the filter using the default properties.

`DurationFilter(long records,
              long duration)`
Creates the filter using the given properties.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`protected DurationFilter`
`clone()`
Creates a copy of this filter that retains the filter settings but does
 not include the current filter state.

`boolean`
`equals(Object obj)`
Determines if this filter is equal to another filter.

`int`
`hashCode()`
Returns a hash code value for this filter.

`boolean`
`isIdle()`
Determines if this filter is able to accept the maximum number of log
 records for this instant in time.

`boolean`
`isLoggable()`
Determines if this filter will accept log records for this instant in
 time.

`boolean`
`isLoggable(LogRecord record)`
Check if the given log record should be published.

`String`
`toString()`
Returns a string representation of this filter.

    - 

### Methods inherited from class java.lang.Object

`finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### DurationFilter

```
public DurationFilter()
```

Creates the filter using the default properties.

    - 

#### DurationFilter

```
public DurationFilter(long records,
                      long duration)
```

Creates the filter using the given properties. Default values are used if
 any of the given values are outside the allowed range.

Parameters:
`records` - the number of records per duration.
`duration` - the number of milliseconds to suppress log records from
 being published.

  - 

### Method Detail

    - 

#### equals

```
public boolean equals(Object obj)
```

Determines if this filter is equal to another filter.

Overrides:
`equals` in class `Object`
Parameters:
`obj` - the given object.
Returns:
true if equal otherwise false.

    - 

#### isIdle

```
public boolean isIdle()
```

Determines if this filter is able to accept the maximum number of log
 records for this instant in time. The result is a best-effort estimate
 and should be considered out of date as soon as it is produced. This
 method is designed for use in monitoring the state of this filter.

Returns:
true if the filter is idle; false otherwise.

    - 

#### hashCode

```
public int hashCode()
```

Returns a hash code value for this filter.

Overrides:
`hashCode` in class `Object`
Returns:
hash code for this filter.

    - 

#### isLoggable

```
public boolean isLoggable(LogRecord record)
```

Check if the given log record should be published. This method will
 modify the internal state of this filter.

Specified by:
`isLoggable` in interface `Filter`
Parameters:
`record` - the log record to check.
Returns:
true if allowed; false otherwise.
Throws:
`NullPointerException` - if given record is null.

    - 

#### isLoggable

```
public boolean isLoggable()
```

Determines if this filter will accept log records for this instant in
 time. The result is a best-effort estimate and should be considered out
 of date as soon as it is produced. This method is designed for use in
 monitoring the state of this filter.

Returns:
true if the filter is not saturated; false otherwise.

    - 

#### toString

```
public String toString()
```

Returns a string representation of this filter. The result is a
 best-effort estimate and should be considered out of date as soon as it
 is produced.

Overrides:
`toString` in class `Object`
Returns:
a string representation of this filter.

    - 

#### clone

```
protected DurationFilter clone()
                        throws CloneNotSupportedException
```

Creates a copy of this filter that retains the filter settings but does
 not include the current filter state. The newly create clone acts as if
 it has never seen any records.

Overrides:
`clone` in class `Object`
Returns:
a copy of this filter.
Throws:
`CloneNotSupportedException` - if this filter is not allowed to be
 cloned.

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