Package com.github.javafaker

## Class DateAndTime

- java.lang.Object

- 

  - com.github.javafaker.DateAndTime

- 

---

```
public class DateAndTime
extends java.lang.Object
```

A generator of random dates.

Author:
pmiklos

- 

  - 

### Constructor Summary

Constructors 

Modifier
Constructor
Description

`protected `
`DateAndTime​(Faker faker)`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`java.util.Date`
`between​(java.util.Date from,
       java.util.Date to)`

Generates a random date between two dates.

`java.util.Date`
`birthday()`

Generates a random birthday between 65 and 18 years ago.

`java.util.Date`
`birthday​(int minAge,
        int maxAge)`

Generates a random birthday between two ages.

`java.util.Date`
`future​(int atMost,
      int minimum,
      java.util.concurrent.TimeUnit unit)`

Generates a future date from now, with a minimum time.

`java.util.Date`
`future​(int atMost,
      java.util.concurrent.TimeUnit unit)`

Generates a future date from now.

`java.util.Date`
`future​(int atMost,
      java.util.concurrent.TimeUnit unit,
      java.util.Date referenceDate)`

Generates a future date relative to the `referenceDate`.

`java.util.Date`
`past​(int atMost,
    int minimum,
    java.util.concurrent.TimeUnit unit)`

Generates a past date from now, with a minimum time.

`java.util.Date`
`past​(int atMost,
    java.util.concurrent.TimeUnit unit)`

Generates a past date from now.

`java.util.Date`
`past​(int atMost,
    java.util.concurrent.TimeUnit unit,
    java.util.Date referenceDate)`

Generates a past date relative to the `referenceDate`.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### DateAndTime

```
protected DateAndTime​(Faker faker)
```

  - 

### Method Detail

    - 

#### future

```
public java.util.Date future​(int atMost,
                             java.util.concurrent.TimeUnit unit)
```

Generates a future date from now. Note that there is a 1 second slack to avoid generating a past date.

Parameters:
`atMost` - at most this amount of time ahead from now exclusive.
`unit` - the time unit.
Returns:
a future date from now.

    - 

#### future

```
public java.util.Date future​(int atMost,
                             int minimum,
                             java.util.concurrent.TimeUnit unit)
```

Generates a future date from now, with a minimum time.

Parameters:
`atMost` - at most this amount of time ahead from now exclusive.
`minimum` - the minimum amount of time in the future from now.
`unit` - the time unit.
Returns:
a future date from now.

    - 

#### future

```
public java.util.Date future​(int atMost,
                             java.util.concurrent.TimeUnit unit,
                             java.util.Date referenceDate)
```

Generates a future date relative to the `referenceDate`.

Parameters:
`atMost` - at most this amount of time ahead to the `referenceDate` exclusive.
`unit` - the time unit.
`referenceDate` - the future date relative to this date.
Returns:
a future date relative to `referenceDate`.

    - 

#### past

```
public java.util.Date past​(int atMost,
                           java.util.concurrent.TimeUnit unit)
```

Generates a past date from now. Note that there is a 1 second slack added.

Parameters:
`atMost` - at most this amount of time earlier from now exclusive.
`unit` - the time unit.
Returns:
a past date from now.

    - 

#### past

```
public java.util.Date past​(int atMost,
                           int minimum,
                           java.util.concurrent.TimeUnit unit)
```

Generates a past date from now, with a minimum time.

Parameters:
`atMost` - at most this amount of time earlier from now exclusive.
`minimum` - the minimum amount of time in the past from now.
`unit` - the time unit.
Returns:
a past date from now.

    - 

#### past

```
public java.util.Date past​(int atMost,
                           java.util.concurrent.TimeUnit unit,
                           java.util.Date referenceDate)
```

Generates a past date relative to the `referenceDate`.

Parameters:
`atMost` - at most this amount of time past to the `referenceDate` exclusive.
`unit` - the time unit.
`referenceDate` - the past date relative to this date.
Returns:
a past date relative to `referenceDate`.

    - 

#### between

```
public java.util.Date between​(java.util.Date from,
                              java.util.Date to)
                       throws java.lang.IllegalArgumentException
```

Generates a random date between two dates.

Parameters:
`from` - the lower bound inclusive
`to` - the upper bound exclusive
Returns:
a random date between `from` and `to`.
Throws:
`java.lang.IllegalArgumentException` - if the `to` date represents an earlier date than `from` date.

    - 

#### birthday

```
public java.util.Date birthday()
```

Generates a random birthday between 65 and 18 years ago.

Returns:
a random birthday between 65 and 18 years ago.

    - 

#### birthday

```
public java.util.Date birthday​(int minAge,
                               int maxAge)
```

Generates a random birthday between two ages.

Parameters:
`minAge` - the minimal age
`maxAge` - the maximal age
Returns:
a random birthday between `minAge` and `maxAge` years ago.
Throws:
`java.lang.IllegalArgumentException` - if the `maxAge` is lower than `minAge`.